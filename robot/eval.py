import gym
import GymEnv
from stable_baselines3 import PPO
from stable_baselines3.common.env_util import make_vec_env
from stable_baselines3.common.evaluation import evaluate_policy
env = gym.make('robot-v0')
model = PPO.load("这里写名字.pkl")# 导入模型

TEST_NUM = 5
score = 0
steps = 0
for i in range(TEST_NUM):
    state = env.reset()
    done = False
    while not done:
        action,_ = model.predict(state,deterministic=True)
        state,reward,done,_ = env.step(action)
        score = score+reward
        steps =steps+1
env.close()
avg_score = score/TEST_NUM
avg_steps = steps/TEST_NUM
print("avg_score=",avg_score)
print("avg_steps=",avg_steps)