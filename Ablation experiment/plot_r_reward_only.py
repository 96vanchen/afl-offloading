
from scipy import io
ep_reward_list_all = io.loadmat\
    ('D:/code-all/code_fl_1/upload/Ablation experiment/3ue-fl-adaptive-only/ep_reward_list.mat')
ep_reward_list_all = ep_reward_list_all['array'][0]

############## reward ##############
### mean
reward_mean_all = []
for i in range(5000):
    if i == 0 or i % 100 == 0:
        r_mean_all_sum = 0
        for j in range(100):
            r_mean_all_sum = r_mean_all_sum + ep_reward_list_all[i + j]
        r_mean_all_sum = r_mean_all_sum / 100
        for j in range(100):
            reward_mean_all.append(r_mean_all_sum)

##### plot
import matplotlib.pyplot as plt
x1 = []
for i in range(5000):
    x1.append(i)
x2 = []
for i in range(5000):
    x2.append(i)
ep_reward_list_all = ep_reward_list_all.tolist()

plt.figure()
font = {
        'weight': 'normal',
        'size': 16}
plt.rc('font', **font)
plt.plot(x2, reward_mean_all, label='$all\ agents$', color='g')
plt.xlabel('Episodes')
plt.ylabel('Reward')
plt.legend()
plt.ylim(-700, -200)
plt.tight_layout()
plt.show()
# plt.savefig('ablation-reward-only.pdf', dpi=300)