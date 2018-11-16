#Implement a k-means clustering algorithm

import numpy as np

def calc_eps(X, k=0.01):
  min_dist = np.min(np.linalg.norm(X[0] - X[1:]))
  for i in range(2, X.shape[0]):
    min_dist = min(min_dist, np.min(np.linalg.norm(X[i] - X[i-1:])))
  return k*min_dist

def isConverged(clusters, newCl, eps):
  return np.max(np.linalg.norm(clusters - newCl, axis=1)) < eps

def kmeans(X, k, eps=None):
    if eps == None:
      eps = calc_eps(X)
    clusters = X[np.random.choice(X.shape[0], k, replace=False), :]
    while True:
      klJ = np.empty(X.shape[0], dtype=int)
      for i in range(0, X.shape[0]):
        klJ[i] = (np.linalg.norm(X[i] - clusters, axis=1)).argmin()
      k = (np.max(klJ)) + 1
      newCl = np.zeros((k, X.shape[1]))
      n = np.zeros(k)
      for i in range(0, X.shape[0]):
        newCl[klJ[i]] += X[i]
        n[klJ[i]] += 1
      newCl /= n[:, None]
      if isConverged(clusters, newCl, eps):
        break
      else:
        clusters = newCl
    return newCl

X = np.array([[1, 4], [2, 5], [3, 6]])

clusters = kmeans(X, 2)
print(clusters)
