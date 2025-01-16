import torch
import torch.nn as nn
import torch.nn.functional as F


# define the actor network
class Actor(nn.Module):
    def __init__(self, args):
        super(Actor, self).__init__()
        self.max_action = args.high_action
        self.fc1 = nn.Linear(args.obs_shape, 64)
        self.fc2 = nn.Linear(64, 64)
        self.action_out = nn.Linear(64, args.action_shape)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        actions = self.max_action * torch.tanh(self.action_out(x))

        return actions


class Critic(nn.Module):
    def __init__(self, args):
        super(Critic, self).__init__()
        self.max_action = args.high_action
        self.fc1 = nn.Linear(args.obs_shape + args.action_shape, 64)
        self.fc2 = nn.Linear(64, 64)
        self.q_out = nn.Linear(64, 1)

    def forward(self, state, action):
        x = torch.cat([state, action], dim=1)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        q_value = self.q_out(x)
        return q_value
