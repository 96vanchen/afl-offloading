
#  reward
import numpy as np
from scipy import io

# adaptive fl
ep_reward_list_afl_3 = io.loadmat\
    ('D:/code-all/code_fl_1/upload/mt-size/afl/3ue-fl-adaptive/ep_reward_list.mat')
ep_reward_list_afl_3 = ep_reward_list_afl_3['array']
ep_reward_list_afl_3 = np.mean(ep_reward_list_afl_3, axis=1)
ep_reward_list_afl_6 = io.loadmat\
    ('D:/code-all/code_fl_1/upload/mt-size/afl/6ue-fl-adaptive/ep_reward_list.mat')
ep_reward_list_afl_6 = ep_reward_list_afl_6['array'][0]
ep_reward_list_afl_9 = io.loadmat\
    ('D:/code-all/code_fl_1/upload/mt-size/afl/9ue-fl-adaptive/ep_reward_list.mat')
ep_reward_list_afl_9 = ep_reward_list_afl_9['array'][0]
ep_reward_list_afl_12 = io.loadmat\
    ('D:/code-all/code_fl_1/upload/mt-size/afl/12ue-fl-adaptive/ep_reward_list.mat')
ep_reward_list_afl_12 = ep_reward_list_afl_12['array'][0]
# 计算最后100次的平均值
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


# plot
import matplotlib.pyplot as plt
x_axis_data = [3, 6, 9, 12]
y_axis_data1 = [mean_reward_afl_3, mean_reward_afl_6, mean_reward_afl_9, mean_reward_afl_12]


plt.plot(x_axis_data, y_axis_data1, 'rs--', alpha=0.5, linewidth=2, label='AFDDPG')


plt.legend()
my_x_ticks = np.arange(3, 13, 3)
plt.xticks(my_x_ticks)
plt.xlabel('Number of MTs')
plt.ylabel('Average reward')  
plt.show()
# plt.savefig('UE_size_reward.pdf', dpi=300)





