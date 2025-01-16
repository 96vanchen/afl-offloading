
#  reward
import numpy as np
from scipy import io

# adaptive fl
ep_reward_list_afl_3 = io.loadmat\
    ('D:/code-all/code_fl_1/upload/task_size/afl/6ue-fl-adaptive-06/ep_reward_list.mat')
ep_reward_list_afl_3 = ep_reward_list_afl_3['array'][0]
ep_reward_list_afl_6 = io.loadmat\
    ('D:/code-all/code_fl_1/upload/task_size/afl/6ue-fl-adaptive-1/ep_reward_list.mat')
ep_reward_list_afl_6 = ep_reward_list_afl_6['array'][0]
ep_reward_list_afl_9 = io.loadmat\
    ('D:/code-all/code_fl_1/upload/task_size/afl/6ue-fl-adaptive-14/ep_reward_list.mat')
ep_reward_list_afl_9 = ep_reward_list_afl_9['array'][0]
ep_reward_list_afl_12 = io.loadmat\
    ('D:/code-all/code_fl_1/upload/task_size/afl/6ue-fl-adaptive-18/ep_reward_list.mat')
ep_reward_list_afl_12 = ep_reward_list_afl_12['array'][0]

episode = 100
leng_3 = len(ep_reward_list_afl_3)
leng_6 = len(ep_reward_list_afl_6)
leng_9 = len(ep_reward_list_afl_9)
leng_12 = len(ep_reward_list_afl_12)
reward_afl_3, reward_afl_6, reward_afl_9, reward_afl_12 = [], [], [], []
for i in range(episode):
    reward_afl_3.append(ep_reward_list_afl_3[leng_3-i-1])
    reward_afl_6.append(ep_reward_list_afl_6[leng_6 - i-1])
    reward_afl_9.append(ep_reward_list_afl_9[leng_9 - i-1])
    reward_afl_12.append(ep_reward_list_afl_12[leng_12 - i-1])
mean_reward_afl_3 = sum(reward_afl_3)/episode
mean_reward_afl_6 = sum(reward_afl_6)/episode
mean_reward_afl_9 = sum(reward_afl_9)/episode
mean_reward_afl_12 = sum(reward_afl_12)/episode


import matplotlib.pyplot as plt
x_axis_data = [0.6, 1, 1.4, 1.8]
y_axis_data1 = [mean_reward_afl_3, mean_reward_afl_6, mean_reward_afl_9, mean_reward_afl_12]

plt.figure(figsize=(10, 7.5))
plt.plot(x_axis_data, y_axis_data1, 'rs--', alpha=0.5, linewidth=2, label='AFDDPG')


plt.legend(loc='lower left', fontsize=15)
plt.tick_params(axis='x', labelsize=16)
plt.tick_params(axis='y', labelsize=16)
plt.xlabel('Data size of tasks (Mb)', fontsize=16)
plt.ylabel('Average reward', fontsize=16)
plt.show()
# plt.savefig('task_size_reward.pdf', dpi=300)







