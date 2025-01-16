import numpy as np
import torch
import os
from ddpg.ddpg import DDPG


class Agent:
    def __init__(self, agent_id, args):

        self.critic_loss_save = []
        self.actor_loss_save = []

        self.args = args
        self.agent_id = agent_id
        self.policy = DDPG(args, agent_id)
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    def select_action(self, o, noise_rate, epsilon):
        if np.random.uniform() < epsilon:
            u = np.random.uniform(-self.args.high_action, self.args.high_action, self.args.action_shape)
        else:
            inputs = torch.tensor(o, dtype=torch.float32).unsqueeze(0)
            inputs = inputs.to(self.device)
            pi = self.policy.actor_network(inputs).squeeze(0)
            u = pi.cpu().numpy()
            noise = noise_rate * self.args.high_action * np.random.randn(*u.shape)  # gaussian noise
            u += noise
            u = np.clip(u, -self.args.high_action, self.args.high_action)
        return u.copy()

    def learn(self, transitions):
        critic_loss, actor_loss = self.policy.train(transitions)

        self.critic_loss_save = critic_loss
        self.actor_loss_save = actor_loss


