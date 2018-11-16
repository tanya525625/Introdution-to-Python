# Calculate the value of Pi approximately
# by the method of random points in a square \ circle

import numpy as np
import matplotlib.pyplot as plt

def pi(N):
  r = 1
  data = np.random.rand(2, N)
  top_half = (data[0,:] **2 + data[1,:]**2) <= r**2
  N_circ = top_half.sum()
  return 4*N_circ/N

for k in [100, 1000, 10000, 100000, int(1e+6)]:
  print(pi(k))
