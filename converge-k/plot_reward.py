from scipy import io

# data
r_circle_afl_mix_3 = io.loadmat\
    ('D:/code-all/code_fl_1/upload/converge-k/3ue-fl-adaptive/ep_reward_list.mat')
r_circle_afl_mix_3 = r_circle_afl_mix_3['array']
ep_reward_list_all_mean_3 = r_circle_afl_mix_3.mean(axis=1)

r_circle_afl_mix_6 = io.loadmat\
    ('D:/code-all/code_fl_1/upload/converge-k/6ue-fl-adaptive/ep_reward_list.mat')
r_circle_afl_mix_6 = r_circle_afl_mix_6['array']
ep_reward_list_all_mean_6 = r_circle_afl_mix_6[0]

r_circle_afl_mix_9 = io.loadmat\
    ('D:/code-all/code_fl_1/upload/converge-k/9ue-fl-adaptive/ep_reward_list.mat')
r_circle_afl_mix_9 = r_circle_afl_mix_9['array']
ep_reward_list_all_mean_9 = r_circle_afl_mix_9[0]

r_circle_afl_mix_12 = io.loadmat\
    ('D:/code-all/code_fl_1/upload/converge-k/12ue-fl-adaptive/ep_reward_list.mat')
r_circle_afl_mix_12 = r_circle_afl_mix_12['array']
ep_reward_list_all_mean_12 = r_circle_afl_mix_12[0]


### mean
reward_mean_3, reward_mean_6, reward_mean_9, reward_mean_12 = [], [], [], []
for i in range(15000):
    if i == 0 or i % 10 == 0:
        r_mean_3_sum = 0
        r_mean_6_sum = 0
        r_mean_9_sum = 0
        r_mean_12_sum = 0
        for j in range(10):
            r_mean_3_sum = r_mean_3_sum + ep_reward_list_all_mean_3[i + j]
            r_mean_6_sum = r_mean_6_sum + ep_reward_list_all_mean_6[i + j]
            r_mean_9_sum = r_mean_9_sum + ep_reward_list_all_mean_9[i + j]
            r_mean_12_sum = r_mean_12_sum + ep_reward_list_all_mean_12[i + j]
        r_mean_3_sum = r_mean_3_sum / 10
        r_mean_6_sum = r_mean_6_sum / 10
        r_mean_9_sum = r_mean_9_sum / 10
        r_mean_12_sum = r_mean_12_sum / 10
        for j in range(10):
            reward_mean_3.append(r_mean_3_sum)
            reward_mean_6.append(r_mean_6_sum)
            reward_mean_9.append(r_mean_9_sum)
            reward_mean_12.append(r_mean_12_sum)
##### plot
import matplotlib.pyplot as plt
x1 = []
for i in range(15000):
    x1.append(i)
x2 = []
for i in range(15000):
    x2.append(i)
ep_reward_list_3 = ep_reward_list_all_mean_3.tolist()
ep_reward_list_6 = ep_reward_list_all_mean_6.tolist()
ep_reward_list_9 = ep_reward_list_all_mean_9.tolist()
ep_reward_list_12 = ep_reward_list_all_mean_12.tolist()
plt.figure()
font = {
        'weight': 'normal',
        'size': 16}
plt.rc('font', **font)
plt.plot(x2, reward_mean_3, label='$K=3$', color='b')
plt.plot(x2, reward_mean_6, label='$K=6$', color='r')
plt.plot(x2, reward_mean_9, label='$K=9$', color='g')
plt.plot(x2, reward_mean_12, label='$K=12$', color='c')
plt.xlabel('Episodes')
plt.ylabel('Reward')
plt.legend()
plt.tight_layout()
plt.show()
# plt.savefig('converge-k.pdf', dpi=300)

