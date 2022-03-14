import torch
# #方便调试不同的奖励函数
# def reward1(a,b,c,d,e,,,):
#    reward = [这里写奖励函数设计]
#    return
# def reward2(a,b,c,d,e,,,):
#    reward = [这里写奖励函数设计]
#    return
#
# PARAMS_ENV = {
#         'reward_fun':         reward1,
# }
PARAMS_PPO = {
        'n_envs':            6,#同时采样的环境数量
        'active':            torch.nn.PReLU,#激活函数
        'net_pi':            [60,90,90,50],#动作函数网络
        'net_vf':            [60,90,90,50],#值函数网络
        'learning_rate':     0.0003,#学习率
        'n_steps':           100,#每次更新前，每个环境采样的动作数
        'batch_size':        200,#batch数大小。注意n_steps*n_env要是batch_size的倍数
        'n_epochs':          2,#每次使用采样的样本进行2次更新
        'total_timesteps':   3*10**4,#总共学习的步数
        'gamma':             0.99,#折扣率
        'n_eval_episodes':   6#多少个回合测试一次
}
