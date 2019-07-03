
"""
Author - Manas Gupta, A-STAR, Singapore
Experiment #1
Date - 3/7/2019
Topic - Boiler plate code for custom gym environment
"""

import gym

class NASEnv(gym.Env):
	metadata = {'render.modes': ['human']}

	def __init__(self):	
		# observation_space = Fixed discrete space of 1 parameter
		self.observation_space = spaces.Discrete(1)
		# action_space = Fixed discrete space of 1 parameter													                         
		self.action_space = spaces.Discrete(1)
		
	def step(self, action):
		# print("Testing step function")
		obs, rew, ep_done = 0,0,0
		# print("Resultant Obs is ", obs)
		# print("rew is ", rew)
		# print("ep_done is ", ep_done)
		return [obs, rew, ep_done, {}]
	
	def reset(self):
		# print("Testing reset function")
		obs = 0
		# print("Obs is ", obs)
		return obs
		
	def render(self, mode='human', close=False):
		return 0