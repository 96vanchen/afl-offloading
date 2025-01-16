
import numpy as np
from scipy import io

ep_reward_list_2 = io.loadmat\
    ('D:/code-all/code_fl_1/upload/chi-bound/6ue-fl-adaptive-0.3/ep_reward_list.mat')
ep_reward_list_2 = ep_reward_list_2['array']
ep_reward_list_5 = io.loadmat\
    ('D:/code-all/code_fl_1/upload/chi-bound/6ue-fl-adaptive-0.5/ep_reward_list.mat')
ep_reward_list_5 = ep_reward_list_5['array']
ep_reward_list_8 = io.loadmat\
    ('D:/code-all/code_fl_1/upload/chi-bound/6ue-fl-adaptive-0.7/ep_reward_list.mat')
ep_reward_list_8 = ep_reward_list_8['array']
ep_reward_list_1 = io.loadmat\
    ('D:/code-all/code_fl_1/upload/chi-bound/6ue-fl-adaptive-1/ep_reward_list.mat')
ep_reward_list_1 = ep_reward_list_1['array']


reward_mean_2, reward_mean_5, reward_mean_1 = [], [], []
for i in range(10000):
    if i == 0 or i % 10 == 0:
        r_mean_2_sum = 0
        r_mean_5_sum = 0
        r_mean_1_sum = 0
        for j in range(10):
            r_mean_2_sum = r_mean_2_sum + ep_reward_list_2[0][i+j]
            r_mean_5_sum = r_mean_5_sum + ep_reward_list_5[0][i + j]
            r_mean_1_sum = r_mean_1_sum + ep_reward_list_1[0][i + j]
        r_mean_2_sum = r_mean_2_sum / 10
        r_mean_5_sum = r_mean_5_sum / 10
        r_mean_1_sum = r_mean_1_sum / 10
        for j in range(10):
            reward_mean_2.append(r_mean_2_sum)
            reward_mean_5.append(r_mean_5_sum)
            reward_mean_1.append(r_mean_1_sum)
reward_mean_8 = []
for i in range(10000):
    if i == 0 or i % 25 == 0:
        r_mean_8_sum = 0
        for j in range(25):
            r_mean_8_sum = r_mean_8_sum + ep_reward_list_8[0][i + j]
        r_mean_8_sum = r_mean_8_sum / 25
        for j in range(25):
            reward_mean_8.append(r_mean_8_sum)

##### plot
import matplotlib.pyplot as plt
x1 = []
for i in range(10000):
    x1.append(i)
x2 = []
for i in range(10000):
    x2.append(i)
ep_reward_list_2 = ep_reward_list_2.tolist()[0]
ep_reward_list_5 = ep_reward_list_5.tolist()[0]
ep_reward_list_8 = ep_reward_list_8.tolist()[0]
ep_reward_list_1 = ep_reward_list_1.tolist()[0]

font = {
        'weight': 'normal',
        'size': 16}
plt.rc('font', **font)
plt.plot(x1, ep_reward_list_2, color='mistyrose', alpha=0.6)
plt.plot(x1, ep_reward_list_5, color='honeydew', alpha=0.6)
plt.plot(x1, ep_reward_list_8, color='lightsteelblue', alpha=0.6)
plt.plot(x1, ep_reward_list_1, color='bisque', alpha=0.6)
plt.plot(x2, reward_mean_2, label='$\u03C7_{min}=0.3$', color='r')
plt.plot(x2, reward_mean_5, label='$\u03C7_{min}=0.5$', color='g')
plt.plot(x2, reward_mean_8, label='$\u03C7_{min}=0.7$', color='b')
plt.plot(x2, reward_mean_1, label='$\u03C7_{min}=1$', color='y')
plt.xlabel('Episodes')
plt.ylabel('Average reward')
plt.legend()
# plt.title('Scatter')
plt.tight_layout()
plt.show()
# plt.savefig('bound.pdf', dpi=300)  # eps文件，用于LaTeX


