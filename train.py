from network import *
from environment import *
import parameters as p
import tensorflow as tf
import matplotlib.pyplot as plt

# snn = SpikingNeuralNetwork()
# env = VrepEnvironment()

# weights_r = []
# weights_l = []
# weights_i = []
# steps = []
# cumulative_reward_per_episode = []
# cumulative_reward = 0
# params = {}

# Initialize environment, get initial state, initial reward
# s, r = env.reset()

# 导入训练集
(train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.mnist.load_data()

# for i in range(100):
#     snn.simulate(train_images[i])

# output = nest.GetStatus(snn.spike_detector, keys="n_events")
# print(output)
