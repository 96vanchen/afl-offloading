from scipy import io

# data
r_circle_afl_mix_4 = io.loadmat\
    ('D:/code-all/code_fl_1/upload/reward-para/reward-para-mt3/3ue-fl-adaptive-both-4/ep_reward_list.mat')
r_circle_afl_mix_4 = r_circle_afl_mix_4['array']
ep_reward_list_all_mean_4 = r_circle_afl_mix_4.mean(axis=1)

r_circle_afl_mix_5 = io.loadmat\
    ('D:/code-all/code_fl_1/upload/reward-para/reward-para-mt3/3ue-fl-adaptive-both-5/ep_reward_list.mat')
r_circle_afl_mix_5 = r_circle_afl_mix_5['array']
ep_reward_list_all_mean_5 = r_circle_afl_mix_5.mean(axis=1)

r_circle_afl_mix_6 = io.loadmat\
    ('D:/code-all/code_fl_1/upload/reward-para/reward-para-mt3/3ue-fl-adaptive-both-6/ep_reward_list.mat')
r_circle_afl_mix_6 = r_circle_afl_mix_6['array']
ep_reward_list_all_mean_6 = r_circle_afl_mix_6.mean(axis=1)


### mean
reward_mean_4, reward_mean_5, reward_mean_6 = [], [], []
for i in range(5000):
    if i == 0 or i % 10 == 0:
        r_mean_4_sum = 0
        r_mean_5_sum = 0
        r_mean_6_sum = 0
        for j in range(10):
            r_mean_4_sum = r_mean_4_sum + ep_reward_list_all_mean_4[i + j]
            r_mean_5_sum = r_mean_5_sum + ep_reward_list_all_mean_5[i + j]
            r_mean_6_sum = r_mean_6_sum + ep_reward_list_all_mean_6[i + j]
        r_mean_4_sum = r_mean_4_sum / 10
        r_mean_5_sum = r_mean_5_sum / 10
        r_mean_6_sum = r_mean_6_sum / 10
        for j in range(10):
            reward_mean_4.append(r_mean_4_sum)
            reward_mean_5.append(r_mean_5_sum)
            reward_mean_6.append(r_mean_6_sum)

##### plot
import matplotlib.pyplot as plt
x1 = []
for i in range(5000):
    x1.append(i)
x2 = []
for i in range(5000):
    x2.append(i)
ep_reward_list_4 = ep_reward_list_all_mean_4.tolist()
ep_reward_list_5 = ep_reward_list_all_mean_5.tolist()
ep_reward_list_6 = ep_reward_list_all_mean_6.tolist()


plt.figure()
font = {
        'weight': 'normal',
        'size': 16}
plt.rc('font', **font)
plt.plot(x2, reward_mean_4, label='$br=4$', color='b')
plt.plot(x2, reward_mean_5, label='$br=5$', color='r')
plt.xlabel('Episodes')
plt.ylabel('Reward')
plt.legend()
plt.tight_layout()
plt.show()
# plt.savefig('r-para-mt3-1.pdf', dpi=300)


plt.figure()
font = {
        'weight': 'normal',
        'size': 16}
plt.rc('font', **font)
plt.plot(x2, reward_mean_5, label='$br=5$', color='r')
plt.plot(x2, reward_mean_6, label='$br=6$', color='g')
plt.xlabel('Episodes')
plt.ylabel('Reward')
plt.legend()
plt.tight_layout()
plt.show()
# plt.savefig('r-para-mt3-2.pdf', dpi=300)

plt.figure()
font = {
        'weight': 'normal',
        'size': 16}
plt.rc('font', **font)
plt.plot(x2, reward_mean_4, label='$br=4$', color='b')
plt.plot(x2, reward_mean_5, label='$br=5$', color='r')
plt.plot(x2, reward_mean_6, label='$br=6$', color='g')
plt.xlabel('Episodes')
plt.ylabel('Reward')
plt.legend()
plt.tight_layout()
plt.show()
# plt.savefig('r-para-mt3-all.pdf', dpi=300)
