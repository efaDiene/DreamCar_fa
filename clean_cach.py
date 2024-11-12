import torch 
import gc

gc.collect()

torch.cuda.empty_cache() 

#bin to npy
""" import numpy as np

arr = np.fromfile('DreamCar/example_data/ttttest/images.bin', dtype=np.float64)
np.save('DreamCar/example_data/ttttest/images.npy', arr)
 """