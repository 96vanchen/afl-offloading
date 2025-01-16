
import numpy as np
from scipy import io

ep_reward_list_50 = io.loadmat\
    ('D:/code-all/code_fl_1/upload/fed_interval/6ue-fl-adaptive-50/ep_reward_list.mat')
ep_reward_list_50 = ep_reward_list_50['array']
ep_reward_list_100 = io.loadmat\
    ('D:/code-all/code_fl_1/upload/fed_interval/6ue-fl-adaptive-100/ep_reward_list.mat')
ep_reward_list_100 = ep_reward_list_100['array']
ep_reward_list_150 = io.loadmat\
    ('D:/code-all/code_fl_1/upload/fed_interval/6ue-fl-adaptive-150/ep_reward_list.mat')
ep_reward_list_150 = ep_reward_list_150['array']


############## reward ##############

reward_mean_50, reward_mean_150 = [], []
for i in range(10000):
    if i == 0 or i % 10 == 0:
        r_mean_50_sum = 0
        r_mean_150_sum = 0
        for j in range(10):
            r_mean_50_sum = r_mean_50_sum + ep_reward_list_50[0][i+j]
            r_mean_150_sum = r_mean_150_sum + ep_reward_list_150[0][i + j]
        r_mean_50_sum = r_mean_50_sum / 10
        r_mean_150_sum = r_mean_150_sum / 10
        for j in range(10):
            reward_mean_50.append(r_mean_50_sum)
            reward_mean_150.append(r_mean_150_sum)
reward_mean_100 = []
for i in range(10000):
    if i == 0 or i % 25 == 0:
        r_mean_100_sum = 0
        for j in range(25):
            r_mean_100_sum = r_mean_100_sum + ep_reward_list_100[0][i + j]
        r_mean_100_sum = r_mean_100_sum / 25
        for j in range(25):
            reward_mean_100.append(r_mean_100_sum)

##### plot
import matplotlib.pyplot as plt
x1 = []
for i in range(10000):
    x1.append(i)
x2 = []
for i in range(10000):
    x2.append(i)
ep_reward_list_50 = ep_reward_list_50.tolist()[0]
ep_reward_list_100 = ep_reward_list_100.tolist()[0]
ep_reward_list_150 = ep_reward_list_150.tolist()[0]

font = {
        'weight': 'normal',
        'size': 16}
plt.rc('font', **font)
plt.plot(x1, ep_reward_list_50, color='mistyrose', alpha=0.6)
plt.plot(x1, ep_reward_list_100, color='lightsteelblue', alpha=0.6)
plt.plot(x1, ep_reward_list_150, color='honeydew', alpha=0.6)
plt.plot(x2, reward_mean_50, label='$E=50$', color='r')
plt.plot(x2, reward_mean_100, label='$E=100$', color='b')
plt.plot(x2, reward_mean_150, label='$E=150$', color='g')
plt.xlabel('Episodes')
plt.ylabel('Average reward')
plt.legend()
# plt.title('Scatter')
plt.tight_layout()
plt.show()
# plt.savefig('fed_interval.pdf', dpi=300)  # eps文件，用于LaTeX

