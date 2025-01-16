

import numpy as np
from scipy import io

r_afl_mix = io.loadmat\
    ('D:/code-all/code_fl_1/upload/Ablation experiment/3ue-fl-adaptive-both-5/ep_reward_list.mat')
r_afl_mix = r_afl_mix['array']
r_afl_mix = np.mean(r_afl_mix, axis=1)


r_afl_single = io.loadmat\
    ('D:/code-all/code_fl_1/upload/Ablation experiment/3ue-fl-adaptive-single/ep_reward_list.mat')
r_afl_single = r_afl_single['array']
r_afl_single = np.mean(r_afl_single, axis=1)


r_afl_only = io.loadmat\
    ('D:/code-all/code_fl_1/upload/Ablation experiment/3ue-fl-adaptive-only/ep_reward_list.mat')
r_afl_only = r_afl_only['array'][0]




### mean
reward_mean_4, reward_mean_5, reward_mean_6 = [], [], []
for i in range(5000):
    if i == 0 or i % 20 == 0:
        r_mean_4_sum = 0
        r_mean_5_sum = 0
        r_mean_6_sum = 0
        for j in range(20):
            r_mean_4_sum = r_mean_4_sum + r_afl_mix[i + j]
            r_mean_5_sum = r_mean_5_sum + r_afl_single[i + j]
            r_mean_6_sum = r_mean_6_sum + r_afl_only[i + j]
        r_mean_4_sum = r_mean_4_sum / 20
        r_mean_5_sum = r_mean_5_sum / 20
        r_mean_6_sum = r_mean_6_sum / 20
        for j in range(20):
            reward_mean_4.append(r_mean_4_sum)
            reward_mean_5.append(r_mean_5_sum)
            reward_mean_6.append(r_mean_6_sum)

##### plot
import matplotlib.pyplot as plt
x1 = []
for i in range(5000):
    x1.append(i)
x2 = []
for i in range(5000):
    x2.append(i)
ep_reward_list_4 = r_afl_mix.tolist()
ep_reward_list_5 = r_afl_single.tolist()
ep_reward_list_6 = r_afl_only.tolist()


plt.figure()
font = {
        'weight': 'normal',
        'size': 16}
plt.rc('font', **font)
plt.plot(x2, reward_mean_4, label='$AFDDPG$', color='r')
plt.plot(x2, reward_mean_5, label='$AFDDPG\ with\ feature\ reward$', color='b')
plt.plot(x2, reward_mean_6, label='$AFDDPG\ with\ cooperation\ reward$', color='g')
plt.xlabel('Episodes')
plt.ylabel('Reward')
plt.legend()
plt.tight_layout()
plt.show()
# plt.savefig('ablation-reward.pdf', dpi=300)
