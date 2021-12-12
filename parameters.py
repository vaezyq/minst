

time_resolution = 0.1                # Network simulation time resolution
poisson_params = {}

# Input image
img_resolution = [28, 28]  # Original DVS frame resolution
crop_top = 8  # Crop at the top
crop_bottom = 8  # Crop at the bottom
resolution = [8, 4]  # Resolution of reduced image

sim_time = 50.0  # Length of network simulation during each step in ms
max_poisson_freq = 300.  # Maximum Poisson firing frequency for n_max
max_spikes = 15.  # number of events during each step for maximum poisson frequency
