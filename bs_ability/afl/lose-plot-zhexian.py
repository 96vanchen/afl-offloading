
#  packet
import numpy as np
from scipy import io


false_afl_3 = io.loadmat\
    ('D:/code-all/code_fl_1/upload/bs_ability/afl/6ue-fl-adaptive-15/rate_false_T.mat')
false_afl_3 = false_afl_3['array']
false_circle_afl_mean_3 = np.sum(false_afl_3, axis=1)
false_circle_afl_mean_3_last = np.mean(false_circle_afl_mean_3[-100:])
false_afl_6 = io.loadmat\
    ('D:/code-all/code_fl_1/upload/bs_ability/afl/6ue-fl-adaptive-20/rate_false_T.mat')
false_afl_6 = false_afl_6['array']
false_circle_afl_mean_6 = np.sum(false_afl_6, axis=1)
false_circle_afl_mean_6_last = np.mean(false_circle_afl_mean_6[-100:])
false_afl_9 = io.loadmat\
    ('D:/code-all/code_fl_1/upload/bs_ability/afl/6ue-fl-adaptive-25/rate_false_T.mat')
false_afl_9 = false_afl_9['array']
false_circle_afl_mean_9 = np.sum(false_afl_9, axis=1)
false_circle_afl_mean_9_last = np.mean(false_circle_afl_mean_9[-100:])
false_afl_12 = io.loadmat\
    ('D:/code-all/code_fl_1/upload/bs_ability/afl/6ue-fl-adaptive-30/rate_false_T.mat')
false_afl_12 = false_afl_12['array']
false_circle_afl_mean_12 = np.sum(false_afl_12, axis=1)
false_circle_afl_mean_12_last = np.mean(false_circle_afl_mean_12[-100:])
false_mean_afl_3 = false_circle_afl_mean_3_last/6 * 100
false_mean_afl_6 = false_circle_afl_mean_6_last/6 * 100
false_mean_afl_9 = false_circle_afl_mean_9_last/6 * 100
false_mean_afl_12 = false_circle_afl_mean_12_last/6 * 100



# plot
import matplotlib.pyplot as plt

fenmu = np.array([3, 6, 9, 12])
waters = ('15', '20', '25', '30')

y_axis_data1 = [false_mean_afl_3, false_mean_afl_6, false_mean_afl_9, false_mean_afl_12]

bar_width = 0.1
index_afl = np.arange(len(waters))  # AFL

plt.bar(index_afl, height=y_axis_data1, width=bar_width, color='r', label='AFDDPG')


plt.legend()
plt.tick_params(axis='x', labelsize=15)
plt.tick_params(axis='y', labelsize=15)
plt.xticks(index_afl + bar_width/2, waters)
plt.xlabel('Computing ability of MBSs (GHz)')
plt.ylabel('Packet loss rate (%)')
plt.show()
# plt.savefig('bs_ability_lose.pdf', dpi=300)




