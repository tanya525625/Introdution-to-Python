#Implement noise filtering from a one-dimensional signal using the moving average method
import numpy as np
import matplotlib.pyplot as plt

def moving_avg(data, window_size):
  res = [np.mean(data[i-window_size:i] ) for i in range(window_size,data.shape[0]+window_size)]
  return res

x = np.arange(0, 10, 0.1)
y = np.sin(x)
plt.grid()
noise = 0.1*(np.random.rand(len(x))-0.5)
plt.plot(x, y+noise, 'b-', alpha=1)
res = moving_avg(y+noise, 10)
plt.plot(x, res, 'r-', alpha=0.8)
plt.savefig('1.png')
