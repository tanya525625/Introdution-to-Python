# Image clustering into 3 clusters.
# Input: RGB Image Matrix
# Output: RGB image matrix of three colors R, G, B. Each color means a cluster

import numpy as np
from PIL import Image, ImageFile
from kmeans import kmeans
from kmeans import assign_clusters

def rgb2h(img):
  DMax = np.max( img, axis=2 ).astype(np.int32)
  DMin = np.min( img, axis=2 ).astype(np.int32)

  diff = (DMax-DMin)
  diff[diff == 0] = 1

  r = (img[:,:,0]).astype(np.int32)
  g = (img[:,:,1]).astype(np.int32)
  b = (img[:,:,2]).astype(np.int32)

  rIsMax = (r>=g)&(r>=b)
  gIsMax = (g>=r)&(g>=b)
  bIsMax = (b>=r)&(b>=g)
  h = (DMax!=DMin)*(((60*(r-g) /diff + 240)*bIsMax)+((60*(b-r)/diff + 120)* gIsMax )+((60*(g-b)/diff + 360*(g<b))*rIsMax))
  return h

def cluster_labels2img(hue, colors):
  hueFlat = hue.flatten()
  hue_vectorized = np.array([np.array([hueFlat[i]]) for i in range(hue.shape[0]*hue.shape[1])])
  centers = kmeans( hue_vectorized, 3, 0.01 )
  labels = assign_clusters(hue_vectorized, centers)
  rgbArray = np.zeros( (len(labels), 3) )
  for i in range(labels.max()+1):
    rgbArray[labels == i] = colors[i]
  rgbArray.shape = ((hue.shape[0], hue.shape[1], 3))
  return Image.fromarray(rgbArray.astype(np.uint8))

def transformation(src, res):
  cluster_labels2img(rgb2h(np.array(Image.open(src))), [[18,18,237],[82,237,68],[169,175,43]]).save(res)

# Attach to prog img with name "lake.jpg" for the transformation
transformation("lake.jpg", "lake2.jpg")
