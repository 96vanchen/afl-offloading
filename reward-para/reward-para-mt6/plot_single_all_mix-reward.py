from scipy import io

# data
r_circle_afl_mix_7 = io.loadmat\
    ('D:/code-all/code_fl_1/upload/reward-para/reward-para-mt6/6ue-fl-adaptive-both-7/ep_reward_list.mat')
r_circle_afl_mix_7 = r_circle_afl_mix_7['array']
ep_reward_list_all_mean_7 = r_circle_afl_mix_7.mean(axis=1)

r_circle_afl_mix_8 = io.loadmat\
    ('D:/code-all/code_fl_1/upload/reward-para/reward-para-mt6/6ue-fl-adaptive-both-8/ep_reward_list.mat')
r_circle_afl_mix_8 = r_circle_afl_mix_8['array']
ep_reward_list_all_mean_8 = r_circle_afl_mix_8.mean(axis=1)

r_circle_afl_mix_9 = io.loadmat\
    ('D:/code-all/code_fl_1/upload/reward-para/reward-para-mt6/6ue-fl-adaptive-both-9/ep_reward_list.mat')
r_circle_afl_mix_9 = r_circle_afl_mix_9['array']
ep_reward_list_all_mean_9 = r_circle_afl_mix_9.mean(axis=1)



### mean
reward_mean_7, reward_mean_8, reward_mean_9 = [], [], []
for i in range(10000):
    if i == 0 or i % 10 == 0:
        r_mean_7_sum = 0
        r_mean_8_sum = 0
        r_mean_9_sum = 0
        for j in range(10):
            r_mean_7_sum = r_mean_7_sum + ep_reward_list_all_mean_7[i + j]
            r_mean_8_sum = r_mean_8_sum + ep_reward_list_all_mean_8[i + j]
            r_mean_9_sum = r_mean_9_sum + ep_reward_list_all_mean_9[i + j]
        r_mean_7_sum = r_mean_7_sum / 10
        r_mean_8_sum = r_mean_8_sum / 10
        r_mean_9_sum = r_mean_9_sum / 10
        for j in range(10):
            reward_mean_7.append(r_mean_7_sum)
            reward_mean_8.append(r_mean_8_sum)
            reward_mean_9.append(r_mean_9_sum)

##### plot
import matplotlib.pyplot as plt
x1 = []
for i in range(10000):
    x1.append(i)
x2 = []
for i in range(10000):
    x2.append(i)
ep_reward_list_7 = ep_reward_list_all_mean_7.tolist()
ep_reward_list_8 = ep_reward_list_all_mean_8.tolist()
ep_reward_list_9 = ep_reward_list_all_mean_9.tolist()


plt.figure()
font = {
        'weight': 'normal',
        'size': 16}
plt.rc('font', **font)
plt.plot(x2, reward_mean_7, label='$br=7$', color='r')
plt.plot(x2, reward_mean_8, label='$br=8$', color='g')
plt.plot(x2, reward_mean_9, label='$br=9$', color='m')
plt.xlabel('Episodes')
plt.ylabel('Reward')
plt.legend()
plt.tight_layout()
plt.show()
# plt.savefig('r-para-mt6-all.pdf', dpi=300)






