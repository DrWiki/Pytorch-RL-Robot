import numpy as np
import torch
from stable_baselines3 import PPO
from stable_baselines3.common.env_util import make_vec_env
import random
import argparse
import GymEnv
import os
import Params
def fixed_seed(i):
     random.seed(i)
     os.environ['PYTHONHASHSEED'] = str(i)  # 为了禁止hash随机化，使得实验可复现
     np.random.seed(i)
     torch.manual_seed(i)
     torch.cuda.manual_seed(i)
     torch.cuda.manual_seed_all(i)  # if you are using multi-GPU.
     torch.backends.cudnn.benchmark = False
     torch.backends.cudnn.deterministic = True


if __name__=='__main__':
     parser = argparse.ArgumentParser()
     parser.add_argument("--name", required=True, help="Name of the this train")
     args = parser.parse_args()
     fixed_seed(0)#固定随机种子
     params = Params.PARAMS_PPO
     env = make_vec_env("robot-v0",seed = 0,n_envs=params['n_envs'])#建立环境
     policy_kwargs =(#网络设置
     dict(activation_fn=params['active'],
          net_arch=[dict(pi=params['net_pi'],
          vf=params['net_vf'])]))
     model = PPO(
          "MlpPolicy",#mpl神经网络
          env,
          gamma=params['gamma'],
          learning_rate=params['learning_rate'],
          n_steps=params['n_steps'],
          batch_size=params['batch_size'],
          n_epochs=params['n_epochs'],
          policy_kwargs=policy_kwargs,
          verbose=1,#需要打印训练信息
          tensorboard_log="./tf-logs/")#tensorboard文件存放地址
     model.learn(
          total_timesteps=params['total_timesteps'],
          n_eval_episodes=params['n_eval_episodes'])
     model.save('%s.pkl'%args.name)