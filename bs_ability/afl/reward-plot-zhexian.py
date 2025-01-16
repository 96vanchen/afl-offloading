
#  reward
import numpy as np
from scipy import io

# adaptive fl
ep_reward_list_afl_3 = io.loadmat\
    ('D:/code-all/code_fl_1/upload/bs_ability/afl/6ue-fl-adaptive-15/ep_reward_list.mat')
ep_reward_list_afl_3 = ep_reward_list_afl_3['array'][0]
ep_reward_list_afl_6 = io.loadmat\
    ('D:/code-all/code_fl_1/upload/bs_ability/afl/6ue-fl-adaptive-20/ep_reward_list.mat')
ep_reward_list_afl_6 = ep_reward_list_afl_6['array'][0]
ep_reward_list_afl_9 = io.loadmat\
    ('D:/code-all/code_fl_1/upload/bs_ability/afl/6ue-fl-adaptive-25/ep_reward_list.mat')
ep_reward_list_afl_9 = ep_reward_list_afl_9['array'][0]
ep_reward_list_afl_12 = io.loadmat\
    ('D:/code-all/code_fl_1/upload/bs_ability/afl/6ue-fl-adaptive-30/ep_reward_list.mat')
ep_reward_list_afl_12 = ep_reward_list_afl_12['array'][0]
# last 100
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
x_axis_data = [15, 20, 25, 30]

y_axis_data1 = [mean_reward_afl_3, mean_reward_afl_6, mean_reward_afl_9, mean_reward_afl_12]
y_axis_data1 = np.array(y_axis_data1)

# plot
plt.figure(figsize=(10, 6))
plt.plot(x_axis_data, y_axis_data1, 'rs--', alpha=0.5, linewidth=1, label='AFDDPG')

plt.legend(loc='lower left', fontsize=15)

my_x_ticks = np.arange(15, 31, 5)
plt.xticks(my_x_ticks)
plt.tick_params(axis='x', labelsize=15)
plt.tick_params(axis='y', labelsize=15)
plt.xlabel('Number of MTs', fontsize=15)
plt.ylabel('Average reward', fontsize=15)  # accuracy
plt.show()
# plt.savefig('bs_ability_reward.pdf', dpi=300)







