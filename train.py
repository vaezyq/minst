from network import *
from environment import *
import parameters as p
import h5py
import json

snn = SpikingNeuralNetwork()
env = VrepEnvironment()

weights_r = []
weights_l = []
weights_i = []
steps = []
cumulative_reward_per_episode = []
cumulative_reward = 0
params = {}

# Initialize environment, get initial state, initial reward
s,r = env.reset()

