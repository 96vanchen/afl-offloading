
from scipy import io
ep_reward_list_all = io.loadmat\
    ('D:/code-all/code_fl_1/upload/Ablation experiment/3ue-fl-adaptive-both-5/ep_reward_list.mat')
ep_reward_list_all = ep_reward_list_all['array']
ep_reward_list_0 = ep_reward_list_all[:, 0]
ep_reward_list_1 = ep_reward_list_all[:, 1]
ep_reward_list_2 = ep_reward_list_all[:, 2]

############## reward ##############
### mean
reward_mean_0, reward_mean_1, reward_mean_2 = [], [], []
for i in range(5000):
    if i == 0 or i % 100 == 0:
        r_mean_0_sum = 0
        r_mean_1_sum = 0
        r_mean_2_sum = 0
        for j in range(100):
            r_mean_0_sum = r_mean_0_sum + ep_reward_list_0[i + j]
            r_mean_1_sum = r_mean_1_sum + ep_reward_list_1[i + j]
            r_mean_2_sum = r_mean_2_sum + ep_reward_list_2[i + j]
        r_mean_0_sum = r_mean_0_sum / 100
        r_mean_1_sum = r_mean_1_sum / 100
        r_mean_2_sum = r_mean_2_sum / 100
        for j in range(100):
            reward_mean_0.append(r_mean_0_sum)
            reward_mean_1.append(r_mean_1_sum)
            reward_mean_2.append(r_mean_2_sum)

##### plot
import matplotlib.pyplot as plt
x1 = []
for i in range(5000):
    x1.append(i)
x2 = []
for i in range(5000):
    x2.append(i)
ep_reward_list_0 = ep_reward_list_0.tolist()
ep_reward_list_1 = ep_reward_list_1.tolist()
ep_reward_list_2 = ep_reward_list_2.tolist()

plt.figure()
font = {
        'weight': 'normal',
        'size': 16}
plt.rc('font', **font)
plt.plot(x2, reward_mean_0, label='$agent 1$', color='r', linestyle=':', linewidth=1.5)
plt.plot(x2, reward_mean_1, label='$agent 2$', color='r', linestyle='--', linewidth=1.5)
plt.plot(x2, reward_mean_2, label='$agent 3$', color='r', marker='o', linewidth=1.5)
plt.xlabel('Episodes')
plt.ylabel('Reward')
plt.legend()
plt.tight_layout()
plt.show()
# plt.savefig('ablation-reward-mix.pdf', dpi=300)