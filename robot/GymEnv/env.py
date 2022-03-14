# _*_coding:utf-8-*-
import sys
import gym
from sympy import *
import math
import numpy as np
gym.logger.set_level(40)
# sys.path.append('这里写其上层文件见的绝对路径，如'~/autodl-nas/robot/'')
# import Params
class RobotEnv(gym.Env):
    # 初始化参数
    def __init__(self):
        # 状态空间为18（关节角度）+18（关节角速度）+2（控制方向）+1（控制速度）=39
        self.observation_space = gym.spaces.Box(low=-1, high=1, shape=(39,))
        # 动作空间为18（关节角度）
        self.action_space = gym.spaces.Box(low=-1, high=1, shape=(18,))
        # 附加功能，可选,对应第35行
        # self.reward_fun = Params.PARAMS_ENV['reward_fun']

    # 获取原始数据，并生成状态，同时更新done
    def get_state(self):
        origin_data = [这里写获取数据的函数]
        tmp_data = [将原始数据按照要求组成状态，注意角度\角速度\方向和速度归一化到[-1,-1],速度可以除以系数归一化到0-1]]
        state = np.array(tmp_data).reshape(1,39)
        self.done = True if[写判断终止条件]else False
        return state

    # 根据强化学习输出，发送控制指令，控制机器人运动
    def move(self, action):
                  [这里将动作对应的控制指令发送给仿真环境中的机器人]
        pass

    # 奖励函数
    def get_reward(self):
        reward =  [根据任务需求定义奖励函数,建议三个方面：1、存活时间长短（即能否满足站立并运动的要求）2、方向是否为给定方向3、速度是否为给定速度]
        # reward = self.reward_fun#如果使用这个，就不需要上面个这句，上面这句就可以放到参数文件中进行定义
        return reward

    # 主程序
    def step(self, action):
        # 执行动作
        self.move(action)
        # 获取动作对应奖励
        reward = self.get_reward()
        # 获取下一状态
        state = self.get_state()
        # 返回
        return state, reward, self.done, {}

    # 重置环境
    def reset(self):
                   [初始化机器人]
        # 获得对应状态
        state = self.get_state()
        return state