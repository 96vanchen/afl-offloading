import numpy as np
from scipy import io

# delay
t_delay_circle_afl_mix_4 = io.loadmat\
    ('D:/code-all/code_fl_1/upload/reward-para/reward-para-mt3/3ue-fl-adaptive-both-4/delay_T.mat')
t_delay_circle_afl_mix_4 = t_delay_circle_afl_mix_4['array']
t_delay_circle_afl_mix_4 = np.sum(t_delay_circle_afl_mix_4, axis=1)/1000
t_delay_circle_afl_last_50_mean_mix_4 = np.mean(t_delay_circle_afl_mix_4[-100:-50])

t_delay_circle_afl_mix_5 = io.loadmat\
    ('D:/code-all/code_fl_1/upload/reward-para/reward-para-mt3/3ue-fl-adaptive-both-5/delay_T.mat')
t_delay_circle_afl_mix_5 = t_delay_circle_afl_mix_5['array']
t_delay_circle_afl_mix_5 = np.sum(t_delay_circle_afl_mix_5, axis=1)/1000
t_delay_circle_afl_last_50_mean_mix_5 = np.mean(t_delay_circle_afl_mix_5[-100:-50])

t_delay_circle_afl_mix_6 = io.loadmat\
    ('D:/code-all/code_fl_1/upload/reward-para/reward-para-mt3/3ue-fl-adaptive-both-6/delay_T.mat')
t_delay_circle_afl_mix_6 = t_delay_circle_afl_mix_6['array']
t_delay_circle_afl_mix_6 = np.sum(t_delay_circle_afl_mix_6, axis=1)/1000
t_delay_circle_afl_last_50_mean_mix_6 = np.mean(t_delay_circle_afl_mix_6[-100:-50])

# packet
false_circle_afl_mix_4 = io.loadmat\
    ('D:/code-all/code_fl_1/upload/reward-para/reward-para-mt3/3ue-fl-adaptive-both-4/rate_false_T.mat')
false_circle_afl_mix_4 = false_circle_afl_mix_4['array']
false_circle_afl_mean_mix_4 = np.mean(false_circle_afl_mix_4, axis=1)
false_circle_afl_last_50_mean_mix_4 = np.mean(false_circle_afl_mean_mix_4[-100:-50])

false_circle_afl_mix_5 = io.loadmat\
    ('D:/code-all/code_fl_1/upload/reward-para/reward-para-mt3/3ue-fl-adaptive-both-5/rate_false_T.mat')
false_circle_afl_mix_5 = false_circle_afl_mix_5['array']
false_circle_afl_mean_mix_5 = np.mean(false_circle_afl_mix_5, axis=1)
false_circle_afl_last_50_mean_mix_5 = np.mean(false_circle_afl_mean_mix_5[-100:-50])

false_circle_afl_mix_6 = io.loadmat\
    ('D:/code-all/code_fl_1/upload/reward-para/reward-para-mt3/3ue-fl-adaptive-both-6/rate_false_T.mat')
false_circle_afl_mix_6 = false_circle_afl_mix_6['array']
false_circle_afl_mean_mix_6 = np.mean(false_circle_afl_mix_6, axis=1)
false_circle_afl_last_50_mean_mix_6 = np.mean(false_circle_afl_mean_mix_6[-100:-50])
