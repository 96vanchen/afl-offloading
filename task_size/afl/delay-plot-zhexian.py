
#  delay
import numpy as np
from scipy import io

# adaptive fl
t_delay_circle_afl_3 = io.loadmat\
    ('D:/code-all/code_fl_1/upload/task_size/afl/6ue-fl-adaptive-06/delay_T.mat')
t_delay_circle_afl_3 = t_delay_circle_afl_3['array']
t_delay_circle_afl_mean_3 = np.sum(t_delay_circle_afl_3, axis=1)
t_delay_circle_afl_6 = io.loadmat\
    ('D:/code-all/code_fl_1/upload/task_size/afl/6ue-fl-adaptive-1/delay_T.mat')
t_delay_circle_afl_6 = t_delay_circle_afl_6['array']
t_delay_circle_afl_mean_6 = np.sum(t_delay_circle_afl_6, axis=1)
t_delay_circle_afl_9 = io.loadmat\
    ('D:/code-all/code_fl_1/upload/task_size/afl/6ue-fl-adaptive-14/delay_T.mat')
t_delay_circle_afl_9 = t_delay_circle_afl_9['array']
t_delay_circle_afl_mean_9 = np.sum(t_delay_circle_afl_9, axis=1)
t_delay_circle_afl_12 = io.loadmat\
    ('D:/code-all/code_fl_1/upload/task_size/afl/6ue-fl-adaptive-18/delay_T.mat')
t_delay_circle_afl_12 = t_delay_circle_afl_12['array']
t_delay_circle_afl_mean_12 = np.sum(t_delay_circle_afl_12, axis=1)

episode = 100
leng_3 = len(t_delay_circle_afl_mean_3)
leng_6 = len(t_delay_circle_afl_mean_6)
leng_9 = len(t_delay_circle_afl_mean_9)
leng_12 = len(t_delay_circle_afl_mean_12)
delay_afl_3, delay_afl_6, delay_afl_9, delay_afl_12 = [], [], [], []
for i in range(episode):
    delay_afl_3.append(t_delay_circle_afl_mean_3[leng_3-i-1])
    delay_afl_6.append(t_delay_circle_afl_mean_6[leng_6 - i-1])
    delay_afl_9.append(t_delay_circle_afl_mean_9[leng_9 - i-1])
    delay_afl_12.append(t_delay_circle_afl_mean_12[leng_12 - i-1])
delay_mean_afl_3 = sum(delay_afl_3)/episode/1000
delay_mean_afl_6 = sum(delay_afl_6)/episode/1000
delay_mean_afl_9 = sum(delay_afl_9)/episode/1000
delay_mean_afl_12 = sum(delay_afl_12)/episode/1000



import matplotlib.pyplot as plt
waters = ('0.6', '0.8', '1.0', '1.2')
y_axis_data1 = [delay_mean_afl_3, delay_mean_afl_6, delay_mean_afl_9, delay_mean_afl_12]

bar_width = 0.1
index_afl = np.arange(len(waters))  # AFL

plt.bar(index_afl, height=y_axis_data1, width=bar_width, color='r', label='AFDDPG')


plt.legend(fontsize=12)
plt.xticks(index_afl + bar_width/2, waters)
plt.tick_params(axis='x', labelsize=15)
plt.tick_params(axis='y', labelsize=15)
plt.xlabel('Data size of tasks (Mb)', fontsize=15)
plt.ylabel('Average delay of MTs in a task cycle (s)', fontsize=15)
plt.show()
# plt.savefig('task_size_delay.pdf', dpi=300)




