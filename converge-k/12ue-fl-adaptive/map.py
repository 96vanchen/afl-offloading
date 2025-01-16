

import numpy as np
import math
import copy
import random


class Map(object):
    def __init__(self):
        #################### map ####################
        self.length = 300
        self.high_state = None
        self.a_delay_total = [0.1, 0.1, 0.1, 0.1, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9]
        self.r_false_slot = 40

        #################### UE ####################
        self.M = 12  # number
        self.p_tr_min = 5  # power-min
        self.p_tr_max = 12  # power-max
        self.t_delay_slot = np.zeros(self.M)
        self.t_delay_circle = 0
        # task
        self.t_slot = 100
        self.T = 100
        # self.T = 100
        self.slot_count = 0
        self.loc_ue_list = np.array([[250, 50], [200, 40], [100, 150], [55, 85], [175, 210], [78, 210],
                                     [185, 112], [61, 103], [220, 248], [208, 192],
                                     [119, 238], [223, 76]])
        self.task_data = np.random.randint(0.5 * 1024, 1.5 * 1024 + 1, self.M)
        self.task_CPU = np.random.randint(80, 140 + 1, self.M) / 100
        self.task_delay = np.random.randint(60, 100 + 1, self.M)
        self.v_ue = 0.5
        self.num_ue_0 = round(self.M / 2)

        self.ue_theta = np.zeros(self.M)
        for i in range(self.M):
            if i < self.num_ue_0:
                self.ue_theta[i] = 0
            else:
                self.ue_theta[i] = math.pi / 2

        #################### UAV ####################
        self.N = 2  # number
        self.loc_uav = np.array([[0, 300], [150, 150]])
        self.H = 100
        self.v = 4
        self.r_cover_uav = 80
        self.r_cover_uav_ou = math.sqrt(self.r_cover_uav**2 + self.H**2)
        self.com_UAV = 20

        #################### MBS ####################
        self.BS = 4  # number
        self.loc_bs = np.array([[70, 230], [230, 230], [60, 60], [240, 70]])
        self.r_cover_bs = 120
        self.com_bs = 25
        self.t_wait = np.zeros(self.N + self.BS)

        ##################### communicate model ####################
        self.rou = 1
        self.gain_0_uav = -2
        self.gain_0_bs = -3
        self.d_basic_uav = 3
        self.d_basic_bs = 1
        self.p_path_loss = 3
        self.band = 10 ** 7
        self.noise_power = 4 * 10 ** (-15)

        ##################### Metrics ####################
        self.delay_trans_single_T = np.zeros(self.M)
        self.false_single_T = np.zeros(self.M)

    def map_init_circle(self):
        #################### variables to be updated after one period ####################
        self.slot_count = 0
        self.loc_uav = np.array([[0, 300], [150, 150]])
        self.loc_ue_list = np.array([[250, 50], [200, 40], [100, 150], [55, 85], [175, 210], [78, 210],
                                     [185, 112], [61, 103], [220, 248], [208, 192],
                                     [119, 238], [223, 76]])
        self.t_delay_circle = 0
        self.t_wait = np.zeros(self.N + self.BS)
        self.delay_trans_single_T = np.zeros(self.M)
        self.false_single_T = np.zeros(self.M)
        self.ue_theta = np.zeros(self.M)
        for i in range(self.M):
            if i < self.num_ue_0:
                self.ue_theta[i] = 0
            else:
                self.ue_theta[i] = math.pi / 2

    def map_update_slot(self):
        #################### variables to be updated after one time slot ####################
        # UAV-loc
        if self.slot_count <= 52:
            uav_theta = math.pi / 4
        else:
            uav_theta = math.pi + math.pi / 4
        move_x = self.v * math.cos(uav_theta)
        move_y = self.v * math.sin(uav_theta)
        self.loc_uav[0][0] = self.loc_uav[0][0] + move_x
        self.loc_uav[0][1] = self.loc_uav[0][1] - move_y
        self.loc_uav[1][0] = self.loc_uav[1][0] + move_x
        self.loc_uav[1][1] = self.loc_uav[1][1] - move_y
        # task
        self.task_data = np.random.randint(0.5 * 1024, 1.5 * 1024 + 1, self.M)
        self.task_CPU = np.random.randint(80, 140 + 1, self.M) / 100
        self.task_delay = np.random.randint(60, 100 + 1, self.M)
        # UE-loc
        self.ue_loc_update()

        self.t_wait = self.t_wait - self.t_slot
        for i in range(self.N + self.BS):
            if self.t_wait[i] < 0:
                self.t_wait[i] = 0

    #################### UE-loc ####################
    def ue_loc_update(self):
        for i in range(self.num_ue_0):
            loc_ue_single_save = self.loc_ue_list[i, :].copy()
            loc_ue_single_save[0] = loc_ue_single_save[0] + self.v_ue * math.cos(self.ue_theta[i])
            if loc_ue_single_save[0] <= 0 or loc_ue_single_save[0] >= self.length:
                self.ue_theta[i] = self.ue_theta[i] + math.pi
            self.loc_ue_list[i][0] = self.loc_ue_list[i][0] + self.v_ue * math.cos(self.ue_theta[i])
            self.loc_ue_list[i][1] = self.loc_ue_list[i][1] + self.v_ue * math.sin(self.ue_theta[i])
        for i in range(self.M - self.num_ue_0):
            loc_ue_single_save = self.loc_ue_list[i + self.num_ue_0, :].copy()
            loc_ue_single_save[1] = loc_ue_single_save[1] + self.v_ue * math.sin(self.ue_theta[i + self.num_ue_0])
            if loc_ue_single_save[1] <= 0 or loc_ue_single_save[1] >= self.length:
                self.ue_theta[i + self.num_ue_0] = self.ue_theta[i + self.num_ue_0] + math.pi
            self.loc_ue_list[i + self.num_ue_0][0] = self.loc_ue_list[i + self.num_ue_0][0] \
                                                     + self.v_ue * math.cos(self.ue_theta[i + self.num_ue_0])
            self.loc_ue_list[i + self.num_ue_0][1] = self.loc_ue_list[i + self.num_ue_0][1] \
                                                     + self.v_ue * math.sin(self.ue_theta[i + self.num_ue_0])

    #################### distance ####################
    def com_d_o(self, loc_ue, loc_mec):
        d_k_mec = math.sqrt((loc_ue[0] - loc_mec[0]) ** 2 + (loc_ue[1] - loc_mec[1]) ** 2 + ((0 - loc_mec[2]) ** 2))
        return d_k_mec

    def s_update_single(self, ue_index):
        #################### observation ####################
        d_uav = np.array([])
        for u in range(self.N):
            loc_mec = np.append(self.loc_uav[u], self.H)
            loc_ue = np.append(self.loc_ue_list[ue_index], 0)
            d_k_uav = self.com_d_o(loc_ue, loc_mec)
            d_uav = np.append(d_uav, d_k_uav)
        d_bs = np.array([])
        for u in range(self.BS):
            loc_mec = np.append(self.loc_bs[u], 0)
            loc_ue = np.append(self.loc_ue_list[ue_index], 0)
            d_k_bs = self.com_d_o(loc_ue, loc_mec)
            d_bs = np.append(d_bs, d_k_bs)

        start_state = np.append(self.task_data[ue_index], self.task_CPU[ue_index])
        start_state = np.append(start_state, self.task_delay[ue_index])
        start_state = np.append(start_state, d_uav)
        start_state = np.append(start_state, d_bs)
        start_state = np.append(start_state, self.t_wait)
        return start_state

    def s_norm(self, state):
        #################### state-regularization ####################
        high_state = np.append(1.5 * 1024, 140 / 100)
        high_state = np.append(high_state, 100)
        high_state = np.append(high_state, np.ones(self.N) * math.sqrt(self.length**2*2+self.H**2))
        high_state = np.append(high_state, np.ones(self.BS) * math.sqrt(self.length ** 2 * 2))
        high_state = np.append(high_state, np.ones(self.N + self.BS) * 100 * 3)

        low_state = np.append(0.5 * 1024, 80/100)
        low_state = np.append(low_state, 60)
        low_state = np.append(low_state, np.ones(self.N) * self.H)
        low_state = np.append(low_state, np.zeros(self.BS + self.N + self.BS))

        state_norm = state / (high_state - low_state)
        return state_norm

    def s_real(self, state_norm):
        #################### regularized state is materialized ####################
        high_state = np.append(1.5 * 1024, 140 / 100)
        high_state = np.append(high_state, 100)
        high_state = np.append(high_state, np.ones(self.N) * math.sqrt(self.length**2*2+self.H**2))
        high_state = np.append(high_state, np.ones(self.BS) * math.sqrt(self.length ** 2 * 2))
        high_state = np.append(high_state, np.ones(self.N + self.BS) * 100 * 3)

        low_state = np.append(0.5 * 1024, 80/100)
        low_state = np.append(low_state, 60)
        low_state = np.append(low_state, np.ones(self.N) * self.H)
        low_state = np.append(low_state, np.zeros(self.BS + self.N + self.BS))

        state = state_norm * (high_state - low_state)
        return state

    #################### transmission delay ####################
    def com_rate_trans(self, ue_index, serve_matrix, a_total, start_state_total):
        start_state = start_state_total[ue_index, :]
        a_single = a_total[ue_index, :]
        a_single_offload = a_single[0:self.N + self.BS]
        offload_index = np.argmax(a_single_offload)
        d_k_mec_ou = start_state[3 + offload_index]
        if offload_index < self.N:
            gain_0_mec = self.gain_0_uav
            d_basic_mec = self.d_basic_uav
            r_cover_mec_ou = self.r_cover_uav_ou
        else:
            gain_0_mec = self.gain_0_bs
            d_basic_mec = self.d_basic_bs
            r_cover_mec_ou = self.r_cover_bs
        n_cover = self.num_cover(serve_matrix, offload_index)

        if d_k_mec_ou > r_cover_mec_ou:
            rate_trans_k = 10000
        else:
            gain_k_mec = self.rou * math.sqrt((10 ** gain_0_mec) * ((d_basic_mec / d_k_mec_ou) ** self.p_path_loss))
            channel_inter = self.channel_inter(ue_index, serve_matrix, a_total, start_state_total)
            p_tr = a_total[ue_index][self.N+self.BS]
            rate_trans_k = self.band / n_cover * math.log2(1 + p_tr * gain_k_mec / (self.noise_power+channel_inter))
            rate_trans_k = rate_trans_k / 1024
        return rate_trans_k

    #################### covered number ####################
    def num_cover(self, serve_matrix, mec_index):
        n_cover = sum(serve_matrix[mec_index, :])
        return n_cover

    #################### served matrix ####################
    def serve_matrix(self, a_total, s_total):
        a_total_offload = a_total[:, 0:self.N+self.BS]
        serve_matrix = np.zeros((self.N+self.BS, self.M))
        for i in range(self.M):
            offload_index = np.argmax(a_total_offload[i, :])
            if offload_index < self.N:
                r_cover_mec_ou = self.r_cover_uav_ou
            else:
                r_cover_mec_ou = self.r_cover_bs
            d_k_mec_ou = s_total[i][3+offload_index]
            if d_k_mec_ou <= r_cover_mec_ou:
                serve_matrix[offload_index][i] = 1
        return serve_matrix

    #################### channel disturbance ####################
    def channel_inter(self, ue_index, serve_matrix, a_total, start_state_total):
        offload_index = np.argmax(serve_matrix[:, ue_index])
        if offload_index < self.N:
            gain_0_mec = self.gain_0_uav
            d_basic_mec = self.d_basic_uav
        else:
            gain_0_mec = self.gain_0_bs
            d_basic_mec = self.d_basic_bs
        channel_inter = 0
        for i in range(self.M):
            if i != ue_index and serve_matrix[offload_index][i] == 1:
                d_k_mec_ou = start_state_total[i][3 + offload_index]
                gain_k_mec = self.rou * math.sqrt((10 ** gain_0_mec) * ((d_basic_mec / d_k_mec_ou) ** self.p_path_loss))
                channel_inter = channel_inter + a_total[i][self.N+self.BS]*gain_k_mec
        return channel_inter

    def delay_ue_single(self, a_total, start_state_total, ue_index):
        #################### UE-delay ####################
        serve_matrix = self.serve_matrix(a_total, start_state_total)

        a_single = a_total[ue_index, :]
        start_state = start_state_total[ue_index, :]
        t_data = start_state[0]
        t_cpu = start_state[1]
        t_allow = start_state[2]
        ue_slot_false = 0
        a_single_offload = a_single[0:self.N+self.BS]
        offload_index = np.argmax(a_single_offload)
        if offload_index < self.N:
            f_com = self.com_UAV
        else:
            f_com = self.com_bs
        rate_trans_k = self.com_rate_trans(ue_index, serve_matrix, a_total, start_state_total)  # 传输速率
        delay_trans = t_data / rate_trans_k * 10**3

        delay_exe = t_cpu / f_com * 10**3
        delay_slot_single = delay_trans + delay_exe + self.t_wait[offload_index]
        if delay_slot_single > t_allow:
            delay_slot_single = t_allow
            ue_slot_false = 1
            self.t_wait[offload_index] = self.t_wait[offload_index] + \
                                         max((t_allow - (delay_trans + self.t_wait[offload_index])), 0)
        else:
            self.t_wait[offload_index] = self.t_wait[offload_index] + delay_exe
        return delay_trans, ue_slot_false

    def reward_slot_single(self, a_total_list, s_total_list, agent_id):
        #################### feature reward ####################
        a_total = np.zeros((self.M, self.N + self.BS + 1))
        s_total = np.zeros((self.M, 3+(self.N+self.BS)*2))
        for i in range(self.M):
            a_total[i, :] = a_total_list[i]
            s_total[i, :] = s_total_list[i]
            s_total[i, :] = self.s_real(s_total[i, :])
        a_total = (a_total + 1) / 2
        a_total[:, self.N + self.BS] = a_total[:, self.N + self.BS] * (self.p_tr_max - self.p_tr_min) + self.p_tr_min

        exe_order = np.argsort(self.task_delay)
        delay_trans_sing, false_sing = self.delay_ue_single(a_total, s_total, agent_id)
        reward_single = self.a_delay_total[agent_id] * delay_trans_sing \
                        + (1 - self.a_delay_total[agent_id]) * false_sing * self.r_false_slot
        reward_single = - reward_single / 10
        return reward_single

    def reward_slot(self, a_total_list, s_total_list):
        #################### cooperative reward ####################
        a_total = np.zeros((self.M, self.N + self.BS + 1))
        s_total = np.zeros((self.M, 3+(self.N+self.BS)*2))
        for i in range(self.M):
            a_total[i, :] = a_total_list[i]
            s_total[i, :] = s_total_list[i]
            s_total[i, :] = self.s_real(s_total[i, :])
        a_total = (a_total + 1) / 2
        a_total[:, self.N + self.BS] = a_total[:, self.N + self.BS] * (self.p_tr_max - self.p_tr_min) + self.p_tr_min

        exe_order = np.argsort(self.task_delay)
        reward_re = []
        reward = 0
        for i in range(self.M):
            delay_trans_sing, false_sing = self.delay_ue_single(a_total, s_total, i)
            reward_single = self.a_delay_total[i] * delay_trans_sing \
                            + (1 - self.a_delay_total[i]) * false_sing * self.r_false_slot

            self.delay_trans_single_T[exe_order[i]] = self.delay_trans_single_T[exe_order[i]] + delay_trans_sing
            self.false_single_T[exe_order[i]] = self.false_single_T[exe_order[i]] + false_sing
            reward_re.append(reward_single)
            reward = reward + reward_single
        reward = (- reward/self.M) / 10
        self.slot_count = self.slot_count + 1
        return reward



