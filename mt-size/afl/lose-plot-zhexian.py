

import numpy as np
from scipy import io


# adaptive fl
false_circle_afl_3 = io.loadmat\
    ('D:/code-all/code_fl_1/upload/mt-size/afl/3ue-fl-adaptive/rate_false_T.mat')
false_circle_afl_3 = false_circle_afl_3['array']
false_circle_afl_mean_3 = np.sum(false_circle_afl_3, axis=1)
false_circle_afl_mean_3_last = np.mean(false_circle_afl_mean_3[-100:])
false_circle_afl_6 = io.loadmat\
    ('D:/code-all/code_fl_1/upload/mt-size/afl/6ue-fl-adaptive/rate_false_T.mat')
false_circle_afl_6 = false_circle_afl_6['array']
false_circle_afl_mean_6 = np.sum(false_circle_afl_6, axis=1)
false_circle_afl_mean_6_last = np.mean(false_circle_afl_mean_6[-100:])
false_circle_afl_9 = io.loadmat\
    ('D:/code-all/code_fl_1/upload/mt-size/afl/9ue-fl-adaptive/rate_false_T.mat')
false_circle_afl_9 = false_circle_afl_9['array']
false_circle_afl_mean_9 = np.sum(false_circle_afl_9, axis=1)
false_circle_afl_mean_9_last = np.mean(false_circle_afl_mean_9[-100:])
false_circle_afl_12 = io.loadmat\
    ('D:/code-all/code_fl_1/upload/mt-size/afl/12ue-fl-adaptive/rate_false_T.mat')
false_circle_afl_12 = false_circle_afl_12['array']
false_circle_afl_mean_12 = np.sum(false_circle_afl_12, axis=1)
false_circle_afl_mean_12_last = np.mean(false_circle_afl_mean_12[-100:])
false_mean_afl_3 = false_circle_afl_mean_3_last/3 * 100
false_mean_afl_6 = false_circle_afl_mean_6_last/6 * 100
false_mean_afl_9 = false_circle_afl_mean_9_last/9 * 100
false_mean_afl_12 = false_circle_afl_mean_12_last/12 * 100




import matplotlib.pyplot as plt

waters = ('3', '6', '9', '12')
y_axis_data1 = np.round([false_mean_afl_3, false_mean_afl_6, false_mean_afl_9, false_mean_afl_12])


bar_width = 0.17
index_afl = np.arange(len(waters))

plt.bar(index_afl, height=y_axis_data1, width=bar_width, color='r', label='AFDDPG')

plt.legend()
plt.xticks(index_afl + bar_width/2, waters)
plt.xlabel('Number of MTs')
plt.ylabel('Packet loss rate (%)')
plt.show()
# plt.savefig('UE_size_lose.pdf', dpi=300)




