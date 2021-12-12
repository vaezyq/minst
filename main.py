import keras
from keras.datasets import mnist
import matplotlib.pyplot as plt

from network import *
from environment import *
import parameters as p
import tensorflow as tf
import matplotlib.pyplot as plt

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
nest.ResetKernel()
snn = SpikingNeuralNetwork()

# 导入训练集
(train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.mnist.load_data()

for i in range(1, 100):
    snn.simulate(train_images[i], train_labels[i - 1])

    print("&&&&&&&&&&&&&&&&")
    output = nest.GetStatus(snn.spike_detector, keys="n_events")
    print(output)
    print(train_labels[i])
    print("&&&&&&&&&&&&&&&&")

print(output)
