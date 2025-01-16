import numpy as np
from scipy import io

# reward
r_circle_afl_mix_7 = io.loadmat\
    ('D:/code-all/code_fl_1/upload/reward-para/reward-para-mt6/6ue-fl-adaptive-both-7/ep_reward_list.mat')
r_circle_afl_mix_7 = r_circle_afl_mix_7['array']
ep_reward_list_all_mean_7 = r_circle_afl_mix_7.mean(axis=1)
r_circle_afl_last_50_mean_mix_7 = np.mean(ep_reward_list_all_mean_7[-50:])

r_circle_afl_mix_8 = io.loadmat\
    ('D:/code-all/code_fl_1/upload/reward-para/reward-para-mt6/6ue-fl-adaptive-both-8/ep_reward_list.mat')
r_circle_afl_mix_8 = r_circle_afl_mix_8['array']
ep_reward_list_all_mean_8 = r_circle_afl_mix_8.mean(axis=1)
r_circle_afl_last_50_mean_mix_8 = np.mean(ep_reward_list_all_mean_8[-50:])

r_circle_afl_mix_9 = io.loadmat\
    ('D:/code-all/code_fl_1/upload/reward-para/reward-para-mt6/6ue-fl-adaptive-both-9/ep_reward_list.mat')
r_circle_afl_mix_9 = r_circle_afl_mix_9['array']
ep_reward_list_all_mean_9 = r_circle_afl_mix_9.mean(axis=1)
r_circle_afl_last_50_mean_mix_9 = np.mean(ep_reward_list_all_mean_9[-50:])

# delay
t_delay_circle_afl_mix_7 = io.loadmat\
    ('D:/code-all/code_fl_1/upload/reward-para/reward-para-mt6/6ue-fl-adaptive-both-7/delay_T.mat')
t_delay_circle_afl_mix_7 = t_delay_circle_afl_mix_7['array']
t_delay_circle_afl_mix_7 = np.sum(t_delay_circle_afl_mix_7, axis=1)/1000
t_delay_circle_afl_last_50_mean_mix_7 = np.mean(t_delay_circle_afl_mix_7[-50:])

t_delay_circle_afl_mix_8 = io.loadmat\
    ('D:/code-all/code_fl_1/upload/reward-para/reward-para-mt6/6ue-fl-adaptive-both-8/delay_T.mat')
t_delay_circle_afl_mix_8 = t_delay_circle_afl_mix_8['array']
t_delay_circle_afl_mix_8 = np.sum(t_delay_circle_afl_mix_8, axis=1)/1000
t_delay_circle_afl_last_50_mean_mix_8 = np.mean(t_delay_circle_afl_mix_8[-50:])

t_delay_circle_afl_mix_9 = io.loadmat\
    ('D:/code-all/code_fl_1/upload/reward-para/reward-para-mt6/6ue-fl-adaptive-both-9/delay_T.mat')
t_delay_circle_afl_mix_9 = t_delay_circle_afl_mix_9['array']
t_delay_circle_afl_mix_9 = np.sum(t_delay_circle_afl_mix_9, axis=1)/1000
t_delay_circle_afl_last_50_mean_mix_9 = np.mean(t_delay_circle_afl_mix_9[-50:])

# packet
false_circle_afl_mix_7 = io.loadmat\
    ('D:/code-all/code_fl_1/upload/reward-para/reward-para-mt6/6ue-fl-adaptive-both-7/rate_false_T.mat')
false_circle_afl_mix_7 = false_circle_afl_mix_7['array']
false_circle_afl_mean_mix_7 = np.mean(false_circle_afl_mix_7, axis=1)
false_circle_afl_last_50_mean_mix_7 = np.mean(false_circle_afl_mean_mix_7[-50:])

false_circle_afl_mix_8 = io.loadmat\
    ('D:/code-all/code_fl_1/upload/reward-para/reward-para-mt6/6ue-fl-adaptive-both-8/rate_false_T.mat')
false_circle_afl_mix_8 = false_circle_afl_mix_8['array']
false_circle_afl_mean_mix_8 = np.mean(false_circle_afl_mix_8, axis=1)
false_circle_afl_last_50_mean_mix_8 = np.mean(false_circle_afl_mean_mix_8[-50:])

false_circle_afl_mix_9 = io.loadmat\
    ('D:/code-all/code_fl_1/upload/reward-para/reward-para-mt6/6ue-fl-adaptive-both-9/rate_false_T.mat')
false_circle_afl_mix_9 = false_circle_afl_mix_9['array']
false_circle_afl_mean_mix_9 = np.mean(false_circle_afl_mix_9, axis=1)
false_circle_afl_last_50_mean_mix_9 = np.mean(false_circle_afl_mean_mix_9[-50:])
