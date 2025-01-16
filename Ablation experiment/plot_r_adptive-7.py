
import numpy as np
from scipy import io

r_afl_mix = io.loadmat\
    ('D:/code-all/code_fl_1/upload/Ablation experiment/3ue-fl-adaptive-both-5/ep_reward_list.mat')
r_afl_mix = r_afl_mix['array']
r_afl_mix = np.mean(r_afl_mix, axis=1)

r_fl_mix = io.loadmat\
    ('D:/code-all/code_fl_1/upload/Ablation experiment/3ue-fl-adaptive-both-5-7/ep_reward_list.mat')
r_fl_mix = r_fl_mix['array']
r_fl_mix = np.mean(r_fl_mix, axis=1)

### mean
reward_mean_4, reward_mean_5 = [], []
for i in range(5000):
    if i == 0 or i % 20 == 0:
        r_mean_4_sum = 0
        r_mean_5_sum = 0
        for j in range(20):
            r_mean_4_sum = r_mean_4_sum + r_afl_mix[i + j]
            r_mean_5_sum = r_mean_5_sum + r_fl_mix[i + j]
        r_mean_4_sum = r_mean_4_sum / 20
        r_mean_5_sum = r_mean_5_sum / 20
        for j in range(20):
            reward_mean_4.append(r_mean_4_sum)
            reward_mean_5.append(r_mean_5_sum)

##### plot
import matplotlib.pyplot as plt
x1 = []
for i in range(5000):
    x1.append(i)
x2 = []
for i in range(5000):
    x2.append(i)
ep_reward_list_4 = r_afl_mix.tolist()
ep_reward_list_5 = r_fl_mix.tolist()


plt.figure()
font = {
        'weight': 'normal',
        'size': 16}
plt.rc('font', **font)
plt.plot(x2, reward_mean_4, label='$AFDDPG$', color='r')
plt.plot(x2, reward_mean_5, label=r"AFDDPG with $\chi=0.7$", color='b')
plt.xlabel('Episodes')
plt.ylabel('Reward')
plt.legend()
plt.tight_layout()
plt.show()
# plt.savefig('ablation-alu-7.pdf', dpi=300)