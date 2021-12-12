import nest
import numpy as np
import parameters as p
import random


class SpikingNeuralNetwork():

    # 创建输入模型
    def __init__(self):
        # # NEST options
        # self.spike_detector = None
        # self.neuronPop1 = None
        # np.set_printoptions(precision=1)
        # nest.set_verbosity('M_WARNING')
        # nest.ResetKernel()
        # nest.SetKernelStatus({"local_num_threads": 1, "resolution": p.time_resolution})

        # 28*28个poisson_generator作为输入
        self.neuronPop1 = nest.Create("poisson_generator", 784)
        # 10个LIF神经元
        self.neuronPop2 = nest.Create("iaf_psc_alpha", 10)
        # 10个spike_detector
        self.spike_detector = nest.Create("spike_recorder", 10)

        # neuronPop1与neuronPop2通过all_to_all方式连接
        nest.Connect(self.neuronPop1, self.neuronPop2, syn_spec={"weight": 20.0})
        # neuronPop2与spike_detector通过one_to_one方式连接
        nest.Connect(self.neuronPop2, self.spike_detector, "one_to_one")

        self.conn_one = nest.GetConnections(target=self.neuronPop2[0])
        self.conn_two = nest.GetConnections(target=self.neuronPop2[1])

        # # Create Poisson neurons
        # self.spike_generators = nest.Create("poisson_generator", p.img_resolution[0] * p.img_resolution[1],
        #                                     params=p.poisson_params)
        #
        # self.neuron_pre = nest.Create("parrot_neuron", p.resolution[0] * p.resolution[1])
        # # Create motor IAF neurons
        # self.neuron_post = nest.Create("iaf_psc_alpha", 10, params=p.iaf_params)
        # # Create Output spike detector
        # self.spike_detector = nest.Create("spike_detector", 10, params={"withtime": True})
        #
        # # Create R-STDP synapses
        # self.syn_dict = {"model": "stdp_dopamine_synapse",
        #                  "weight": {"distribution": "uniform", "low": p.w0_min, "high": p.w0_max}}
        # self.vt = nest.Create("volume_transmitter")
        # nest.SetDefaults("stdp_dopamine_synapse",
        #                  {"vt": self.vt[0], "tau_c": p.tau_c, "tau_n": p.tau_n, "Wmin": p.w_min, "Wmax": p.w_max,
        #                   "A_plus": p.A_plus, "A_minus": p.A_minus})
        # nest.Connect(self.spike_generators, self.neuron_pre, "one_to_one")
        # nest.Connect(self.neuron_pre, self.neuron_post, "all_to_all", syn_spec=self.syn_dict)
        # nest.Connect(self.neuron_post, self.spike_detector, "one_to_one")

    def simulate(self, dvs_data, reward):

        # print(self.conn_one)

        print("***************")
        # for i in range(10):
        #     if (i == reward):
        #         conn = nest.GetConnections(target=self.neuronPop2[i])
        #         nest.SetStatus(conn, {"n": 2.0})
        #     else:
        #         conn = nest.GetConnections(target=self.neuronPop2[i])
        #         nest.SetStatus(conn, {"n": -2.0})

        # conn = nest.GetConnections(target=self.neuronPop2[0])
        # status = nest.GetStatus(conn)
        # weights = conn.get('weight')
        # weightReward = [weights[x] - 2 for x in range(0, 784)]
        # nest.SetStatus(conn, 'weight', weightReward)
        # weightReward = [weights[x] + 2 for x in range(0, 100)]
        # print(weightReward)
        for i in range(10):
            if (i == reward):

                conn = nest.GetConnections(target=self.neuronPop2[i])
                weights = conn.get('weight')
                weightReward = [weights[x] + 0.1 for x in range(0, 784)]
                nest.SetStatus(conn, 'weight', weightReward)
            else:
                conn = nest.GetConnections(target=self.neuronPop2[i])
                weights = conn.get('weight')
                weightReward = [weights[x] - 0.1 for x in range(0, 784)]
                nest.SetStatus(conn, 'weight', weightReward)

        print("***************")

        # print(self.conn_two)
        time = nest.biological_time

        nest.SetStatus(self.neuronPop1, {"origin": time})
        nest.SetStatus(self.neuronPop1, {"stop": 50})
        for j in range(28):
            for k in range(28):
                nest.SetStatus(self.neuronPop1[j * 28 + k], {'rate': dvs_data[j][k]})
                # nest.SetStatus(self.neuronPop1[j * 28 + k], {'rate': train_images[i][j][k]})
        nest.Simulate(50)

        # # 设置神经元的脉冲
        # time = nest.GetKernelStatus("time")
        # nest.SetStatus(self.spike_generators, {"origin": time})
        # nest.SetStatus(self.spike_generators, {"stop": p.sim_time})
        #
        # # Set poisson neuron firing frequency
        # dvs_data = dvs_data.reshape(dvs_data.size)
        # for i in range(dvs_data.size):
        #     rate = dvs_data[i] / p.max_spikes
        #     rate = np.clip(rate, 0, 1) * p.max_poisson_freq
        #     nest.SetStatus([self.spike_generators[i]], {"rate": rate})
