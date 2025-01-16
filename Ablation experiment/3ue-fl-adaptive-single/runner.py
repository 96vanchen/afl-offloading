

from tqdm import tqdm
from scipy import io
from agent import Agent
from common.replay_buffer import Buffer
import torch
import os
import numpy as np
import matplotlib.pyplot as plt
import time



class Runner:
    def __init__(self, args, map_mec):
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.ep_reward_list = np.array([])
        self.loc_uav_circle_save = np.array([])
        self.critic_loss_save = np.array([])
        self.actor_loss_save = np.array([])
        self.delay_T = []
        self.rate_false_T = []

        self.t_delay_trans = np.array([])
        self.a0_T = np.array([])

        self.args = args
        self.noise = args.noise_rate
        self.epsilon_init = args.epsilon_init
        self.epsilon = None
        self.FREQUENCY_OF_UPDATE = 100

        self.episode_limit = args.max_episode_len
        self.map_mec = map_mec
        self.agents = self._init_agents()
        self.global_agent = self._init_agents()[0]
        self.buffer = Buffer(args)
        self.save_path = self.args.save_dir + '/' + self.args.scenario_name
        if not os.path.exists(self.save_path):
            os.makedirs(self.save_path)

    def _init_agents(self):
        agents = []
        for i in range(self.args.n_agents):
            agent = Agent(i, self.args)
            agents.append(agent)
        return agents

    def lr_adjust(self, lr, i):
        if i <= self.episode_limit/5:
            s = lr
        elif i <= self.episode_limit/3:
            s = lr/2
        elif i <= self.episode_limit/2:
            s = lr / 3
        else:
            s = lr / 4
        return s

    def p_aggressive(self, main_agent, agents):
        ## Calculate aggregate weights ; independent agent update weights
        p_aggressive = []
        for i in range(self.args.n_agents):
            para_ou_d = 0
            for main_param, agent_param in zip(main_agent.policy.critic_network.parameters(),
                                               agents[i].policy.critic_network.parameters()):
                main_param_new = main_param.clone().detach()
                agent_param_new = agent_param.clone().detach()
                para_ou_d = para_ou_d + ((main_param_new - agent_param_new).norm(2)) ** 2
            para_ou_d = para_ou_d ** 0.5
            p_aggressive.append(1/para_ou_d)
        p_aggressive = torch.tensor(p_aggressive)
        p_aggressive = torch.softmax(p_aggressive, dim=0)
        return p_aggressive

    def combine_agents_reward_based(self, main_agent, agents):
        p_aggressive = self.p_aggressive(main_agent, agents)
        for i in range(self.args.n_agents):
            for main_param, agent_param in zip(main_agent.policy.critic_network.parameters(),
                                               agents[i].policy.critic_network.parameters()):
                if i == 0:
                    main_param.data.copy_(agent_param * p_aggressive[i])
                else:
                    main_param.data.copy_(main_param + agent_param * p_aggressive[i] * 0.5)

            for main_param, agent_param in zip(main_agent.policy.critic_target_network.parameters(),
                                               agents[i].policy.critic_target_network.parameters()):
                if i == 0:
                    main_param.data.copy_(agent_param * p_aggressive[i])
                else:
                    main_param.data.copy_(main_param + agent_param * p_aggressive[i])
        return main_agent

    def distribute_agents(self, main_agent, agents):
        p_aggressive = self.p_aggressive(main_agent, agents)
        p_aggressive_max = torch.max(p_aggressive)
        for i in range(self.args.n_agents):
            p_aggressive[i] = 1*p_aggressive[i]/p_aggressive_max
            if p_aggressive[i] < 0.5:
                p_aggressive[i] = 0.5

        for i in range(self.args.n_agents):
            for main_agent_param, agent_param in zip(main_agent.policy.critic_target_network.parameters(),
                                                     agents[i].policy.critic_target_network.parameters()):
                agent_param.data.copy_(main_agent_param*p_aggressive[i] + agent_param*(1-p_aggressive[i]))

            for main_agent_param, agent_param in zip(main_agent.policy.critic_network.parameters(),
                                                     agents[i].policy.critic_network.parameters()):
                agent_param.data.copy_(main_agent_param*p_aggressive[i] + agent_param*(1-p_aggressive[i]))
        return agents

    def run(self):
        i = 0
        t1 = time.time()
        while i < self.episode_limit:
            self.epsilon = self.lr_adjust(self.epsilon_init, i)
            map_mec = self.map_mec
            self.map_mec.map_init_circle()
            s_total = []
            for ue in range(map_mec.M):
                s_single = map_mec.s_update_single(ue)
                s_single_normal = map_mec.s_norm(s_single)
                s_total.append(s_single_normal)
            j = 0
            ep_reward = 0

            self.a0_T = np.array([])
            while j < self.map_mec.T:
                a_total = []
                with torch.no_grad():
                    for agent_id, agent in enumerate(self.agents):
                        action = agent.select_action(s_total[agent_id], self.noise, self.epsilon)
                        a_total.append(action)
                r = map_mec.reward_slot(a_total, s_total)
                reward_coo = np.ones(self.args.n_agents) * r
                reward_single = np.array([])
                for index in range(map_mec.M):
                    r_single = map_mec.reward_slot_single(a_total, s_total, index)
                    reward_single = np.append(reward_single, r_single)
                reward = 0 * reward_coo + 1 * reward_single

                self.a0_T = np.append(self.a0_T, a_total[0])

                map_mec.map_update_slot()  # map update
                s_total_ = []
                for ue in range(map_mec.M):
                    s_single_ = map_mec.s_update_single(ue)
                    s_single_normal_ = map_mec.s_norm(s_single_)
                    s_total_.append(s_single_normal_)
                ep_reward += reward

                # experience
                self.buffer.store_episode(s_total, a_total, reward, s_total_)
                s_total = s_total_

                # sample
                if self.buffer.current_size >= self.args.batch_size:
                    transitions = self.buffer.sample(self.args.batch_size)
                    for agent in self.agents:
                        agent.learn(transitions)

                if j == self.map_mec.T - 1:
                    print('Episode:', i, ' Steps: %2d' % j, ' Reward: %7.2f' % ep_reward[0])
                    self.ep_reward_list = np.append(self.ep_reward_list, ep_reward)
                j = j + 1
            self.delay_T.append(self.map_mec.delay_trans_single_T)
            self.rate_false_T.append(self.map_mec.false_single_T / self.map_mec.T)

            i = i + 1

            if i % self.FREQUENCY_OF_UPDATE == 0:
                self.global_agent = self.combine_agents_reward_based(self.global_agent, self.agents)
                self.agents = self.distribute_agents(self.global_agent, self.agents)

        print('Running time: ', time.time() - t1)
        self.ep_reward_list = self.ep_reward_list.reshape(self.episode_limit, self.map_mec.M)
        io.savemat('ep_reward_list.mat', {'array': self.ep_reward_list})
        io.savemat('delay_T.mat', {'array': self.delay_T})
        io.savemat('rate_false_T.mat', {'array': self.rate_false_T})



