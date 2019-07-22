"""
Author - Manas Gupta, A-STAR, Singapore
Experiment #1
Date - 19/7/2019
Topic - Gym environment for Neural Architecture Search. Testing DQN hyper-param tuning
"""

import gym
from gym import spaces
import numpy as np
import warnings
warnings.filterwarnings("ignore")

class NASEnv(gym.Env):
	metadata = {'render.modes': ['human']}

	def __init__(self):
		self.state_len = 4          # No. of dimensions in observation space
		self.num_actions = 40       # No. of action choices
		self.datatype = "int"       # Datatype to encode observation space
		#Create action_space and observation_space
		self.observation_space = spaces.Box(low = 0, high = self.num_actions, shape=(self.state_len,), dtype = self.datatype)
		self.action_space = spaces.Discrete(self.num_actions)
		#Create variables for processing and tracking
		self.layer_index = 0
		self.state = np.zeros((self.state_len,), dtype = self.datatype)
		self.episode = 1

	def eval(self, state):
		upper = self.num_actions
		lower = 0
		rew = 0
		max_reward = 1
		for index, value in enumerate(state):
			max = (self.num_actions/self.state_len) * (index + 1)
			# print("Max is ",max)
			# print("Value is ", value)
			if value >= max:
				rew += (upper - value) / (upper - max) * max_reward
			else:
				rew += (value - lower) / (max - lower) * max_reward
			# print("Rew is ",rew)
		return rew

	def step(self, action):
		# print("Testing step function")
		# print("Action is ",action)
		#Update state with given action
		self.state[self.layer_index] = action
		#Increment layer
		self.layer_index += 1
		#Evaluate performance at end of episode		
		if self.layer_index == self.state_len:
			ep_done = True
			rew = self.eval(self.state)
			# print("State is ",self.state)
			# print("Rew is ", rew)
			self.episode += 1
			# print("Episode ",self.episode)
		else:
			ep_done = False
			rew = 0
		return [self.state, rew, ep_done, {}]
	
	def reset(self):
		# print("Testing reset function")
		self.layer_index = 0
		self.state = np.zeros((self.state_len,), dtype = self.datatype)
		# print("Obs upon reset is ", self.state)
		return self.state
		
	def render(self, mode='human', close=False):
		return 0