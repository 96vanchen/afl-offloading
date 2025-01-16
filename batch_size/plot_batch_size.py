

import numpy as np
from scipy import io
# adaptive fl
ep_reward_list_2 = io.loadmat\
    ('D:/code-all/code_fl_1/upload/batch_size/6ue-fl-adaptive-128/ep_reward_list.mat')
ep_reward_list_2 = ep_reward_list_2['array']
ep_reward_list_3 = io.loadmat\
    ('D:/code-all/code_fl_1/upload/batch_size/6ue-fl-adaptive-256/ep_reward_list.mat')
ep_reward_list_3 = ep_reward_list_3['array']
ep_reward_list_4 = io.loadmat\
    ('D:/code-all/code_fl_1/upload/batch_size/6ue-fl-adaptive-512/ep_reward_list.mat')
ep_reward_list_4 = ep_reward_list_4['array']

reward_mean_2, reward_mean_4 = [], []
for i in range(10000):
    if i == 0 or i % 10 == 0:
        r_mean_2_sum = 0
        r_mean_4_sum = 0
        for j in range(10):
            r_mean_2_sum = r_mean_2_sum + ep_reward_list_2[0][i+j]
            r_mean_4_sum = r_mean_4_sum + ep_reward_list_4[0][i + j]
        r_mean_2_sum = r_mean_2_sum / 10
        r_mean_4_sum = r_mean_4_sum / 10
        for j in range(10):
            reward_mean_2.append(r_mean_2_sum)
            reward_mean_4.append(r_mean_4_sum)
reward_mean_3 = []
for i in range(10000):
    if i == 0 or i % 25 == 0:
        r_mean_3_sum = 0
        for j in range(25):
            r_mean_3_sum = r_mean_3_sum + ep_reward_list_3[0][i + j]
        r_mean_3_sum = r_mean_3_sum / 25
        for j in range(25):
            reward_mean_3.append(r_mean_3_sum)

##### plot
import matplotlib.pyplot as plt
x1 = []
for i in range(10000):
    x1.append(i)
x2 = []
for i in range(10000):
    x2.append(i)
ep_reward_list_2 = ep_reward_list_2.tolist()[0]
ep_reward_list_3 = ep_reward_list_3.tolist()[0]
ep_reward_list_4 = ep_reward_list_4.tolist()[0]

font = {
        'weight': 'normal',
        'size': 16}
plt.rc('font', **font)
plt.plot(x1, ep_reward_list_2, color='mistyrose', alpha=0.6)
plt.plot(x1, ep_reward_list_3, color='lightsteelblue', alpha=0.6)
plt.plot(x1, ep_reward_list_4, color='honeydew', alpha=0.6)
plt.plot(x2, reward_mean_2, label='$G= 128$', color='r')
plt.plot(x2, reward_mean_3, label='$G= 256$', color='b')
plt.plot(x2, reward_mean_4, label='$G= 512$', color='g')
plt.xlabel('Episodes')
plt.ylabel('Average reward')
plt.legend()
plt.tight_layout()
plt.show()
# plt.savefig('batch_size.pdf', dpi=300)  # eps文件，用于LaTeX


