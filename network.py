import nest
import numpy as np
import pylab
import parameters as p


class SpikingNeuralNetwork():

    # 创建输入模型
    def __init__(self):
        # NEST options
        np.set_printoptions(precision=1)
        nest.set_verbosity('M_WARNING')
        nest.ResetKernel()
        nest.SetKernelStatus({"local_num_threads": 1, "resolution": p.time_resolution})

        # Create Poisson neurons
        self.spike_generators = nest.Create("poisson_generator", p.img_resolution[0] * p.img_resolution[1],
                                            params=p.poisson_params)

        self.neuron_pre = nest.Create("parrot_neuron", p.resolution[0] * p.resolution[1])
        # Create motor IAF neurons
        self.neuron_post = nest.Create("iaf_psc_alpha", 10, params=p.iaf_params)
        # Create Output spike detector
        self.spike_detector = nest.Create("spike_detector", 10, params={"withtime": True})

        # Create R-STDP synapses
        self.syn_dict = {"model": "stdp_dopamine_synapse",
                         "weight": {"distribution": "uniform", "low": p.w0_min, "high": p.w0_max}}
        self.vt = nest.Create("volume_transmitter")
        nest.SetDefaults("stdp_dopamine_synapse",
                         {"vt": self.vt[0], "tau_c": p.tau_c, "tau_n": p.tau_n, "Wmin": p.w_min, "Wmax": p.w_max,
                          "A_plus": p.A_plus, "A_minus": p.A_minus})
        nest.Connect(self.spike_generators, self.neuron_pre, "one_to_one")
        nest.Connect(self.neuron_pre, self.neuron_post, "all_to_all", syn_spec=self.syn_dict)
        nest.Connect(self.neuron_post, self.spike_detector, "one_to_one")




        self.conn_l = nest.GetConnections(target=[self.neuron_post[0]])
        self.conn_r = nest.GetConnections(target=[self.neuron_post[1]])

    def simulate(self, dvs_data, reward):
        # 设置神经元的脉冲
        time = nest.GetKernelStatus("time")
        nest.SetStatus(self.spike_generators, {"origin": time})
        nest.SetStatus(self.spike_generators, {"stop": p.sim_time})

        # Set poisson neuron firing frequency
        dvs_data = dvs_data.reshape(dvs_data.size)
        for i in range(dvs_data.size):
            rate = dvs_data[i] / p.max_spikes
            rate = np.clip(rate, 0, 1) * p.max_poisson_freq
            nest.SetStatus([self.spike_generators[i]], {"rate": rate})
