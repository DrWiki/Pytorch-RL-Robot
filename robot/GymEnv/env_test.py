# _*_coding:utf-8-*-
import sys
import gym
from sympy import *
import math
import numpy as np
gym.logger.set_level(40)
# sys.path.append('~/autodl-nas/robot/')
# import Params
class RobotEnv(gym.Env):
    # 初始化参数
    def __init__(self):
        # 状态空间为18（关节角度）+18（关节角速度）+2（控制方向）+1（控制速度）=39
        self.observation_space = gym.spaces.Box(low=-1, high=1, shape=(39,))
        # 动作空间为18（关节角度）
        self.action_space = gym.spaces.Box(low=-1, high=1, shape=(18,))
        self.t = 1

    # 获取原始数据，并生成状态，同时更新done
    def get_state(self):
        state = np.array(self.observation_space.sample()).reshape(1,39)
        self.t = self.t+1
        self.done = True if self.t==50 else False
        return state

    # 奖励函数
    def get_reward(self):
        if self.t == 10:
            reward =  1
        else:
            reward = 0
        return reward

    # 主程序
    def step(self, action):
        reward = self.get_reward()
        state = self.get_state()
        # print(self.t,self.done,reward)
        return state, reward, self.done, {}

    # 重置环境
    def reset(self):
        self.t = 1
        state = self.get_state()
        return state
if __name__=='__main__':
    U=RobotEnv()
    for i in range(2):
        U.reset()
        while not U.done:
            U.step(0)
