
import numpy as np
from scipy import io

# delay
t_afl_mix = io.loadmat\
    ('D:/code-all/code_fl_1/upload/Ablation experiment/3ue-fl-adaptive-both-5/delay_T.mat')
t_afl_mix = t_afl_mix['array']
t_afl_mix = np.sum(t_afl_mix, axis=1)/1000
t_afl_last_50_mean_mix = np.mean(t_afl_mix[-500:])

t_fl_mix = io.loadmat\
    ('D:/code-all/code_fl_1/upload/Ablation experiment/3ue-fl-adaptive-single/delay_T.mat')
t_fl_mix = t_fl_mix['array']
t_fl_mix = np.sum(t_fl_mix, axis=1)/1000
t_fl_last_50_mean_mix = np.mean(t_fl_mix[-500:])

t_afl_single = io.loadmat\
    ('D:/code-all/code_fl_1/upload/Ablation experiment/3ue-fl/delay_T.mat')
t_afl_single = t_afl_single['array']
t_afl_single = np.sum(t_afl_single, axis=1)/1000
t_afl_last_50_mean_single = np.mean(t_afl_single[-500:])

t_afl_only = io.loadmat\
    ('D:/code-all/code_fl_1/upload/Ablation experiment/3ue-fl-adaptive-only/delay_T.mat')
t_afl_only = t_afl_only['array']
t_afl_only = np.sum(t_afl_only, axis=1)/1000
t_afl_last_50_mean_only = np.mean(t_afl_only[-500:])

t_afl_7 = io.loadmat\
    ('D:/code-all/code_fl_1/upload/Ablation experiment/3ue-fl-adaptive-both-5-7/delay_T.mat')
t_afl_7 = t_afl_7['array']
t_afl_7 = np.sum(t_afl_7, axis=1)/1000
t_afl_last_50_mean_7 = np.mean(t_afl_7[-500:])

t_afl_3 = io.loadmat\
    ('D:/code-all/code_fl_1/upload/Ablation experiment/3ue-fl-adaptive-both-5-3/delay_T.mat')
t_afl_3 = t_afl_3['array']
t_afl_3 = np.sum(t_afl_3, axis=1)/1000
t_afl_last_50_mean_3 = np.mean(t_afl_3[-500:])


# packet
false_afl_mix = io.loadmat\
    ('D:/code-all/code_fl_1/upload/Ablation experiment/3ue-fl-adaptive-both-5/rate_false_T.mat')
false_afl_mix = false_afl_mix['array']
false_afl_mix = np.mean(false_afl_mix, axis=1)
false_afl_last_50_mean_mix = np.mean(false_afl_mix[-50:])

false_fl_mix = io.loadmat\
    ('D:/code-all/code_fl_1/upload/Ablation experiment/3ue-fl/rate_false_T.mat')
false_fl_mix = false_fl_mix['array']
false_fl_mix = np.mean(false_fl_mix, axis=1)
false_fl_last_50_mean_mix = np.mean(false_fl_mix[-50:])

false_afl_single = io.loadmat\
    ('D:/code-all/code_fl_1/upload/Ablation experiment/3ue-fl-adaptive-single/rate_false_T.mat')
false_afl_single = false_afl_single['array']
false_afl_single = np.mean(false_afl_single, axis=1)
false_afl_last_50_mean_single = np.mean(false_afl_single[-50:])

false_afl_only = io.loadmat\
    ('D:/code-all/code_fl_1/upload/Ablation experiment/3ue-fl-adaptive-only/rate_false_T.mat')
false_afl_only = false_afl_only['array']
false_afl_only = np.mean(false_afl_only, axis=1)
false_afl_last_50_mean_only = np.mean(false_afl_only[-50:])

false_afl_7 = io.loadmat\
    ('D:/code-all/code_fl_1/upload/Ablation experiment/3ue-fl-adaptive-both-5-7/rate_false_T.mat')
false_afl_7 = false_afl_7['array']
false_afl_7 = np.mean(false_afl_7, axis=1)
false_afl_last_50_mean_7 = np.mean(false_afl_7[-500:])

false_afl_3 = io.loadmat\
    ('D:/code-all/code_fl_1/upload/Ablation experiment/3ue-fl-adaptive-both-5-3/rate_false_T.mat')
false_afl_3 = false_afl_3['array']
false_afl_3 = np.mean(false_afl_3, axis=1)
false_afl_last_50_mean_3 = np.mean(false_afl_3[-500:])
