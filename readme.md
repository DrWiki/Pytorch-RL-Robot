# Reinforcement Learning for HexPod Robot

---

### Abstract : 

Currently, most reinforcement learning (RL) algorithms have been designed and evaluated to ameliorae agents' performance in a certain environment. However reseachers evaluated their works commonly in an ideal environment or a simulation software. 

我所了解的大部分强化学习文章中，很少有能既给出仿真验证结果，又给出实物验证结果的。真实的环境往往比理想的环境和仿真环境具有更大的随机性，蕴含着更具有挑战性的难题。这也就意味着，在真实的环境中运行强化学习算法，不仅使我们的最终目标，也是一个创造力源泉。



# Introduction

## 1. GymEnv

the Gym Env actually is an API connecting this project and a particular environment that can be pysical or vitual. This API primarily help us to read the agent's state, write out our control cammonds and get the reward. 





## 2. Agent









## 3. Training





```text
0、
env_test环境为测试环境，测试代码能否正常运行；
env为你的真实环境，需要自己对相应接口函数进行定义。
1、
需要的安装包：
pytorch、stabe_baseline3、gym、numpy、argparse
2、
首先测试env_test环境：         python train.py --name 这里写这次的训练名
3、
搭建自己的环境， 如果有用到提供的模板里的奖励函数指针功能，需要再env中将相应注释解开。
```



