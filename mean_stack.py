# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from astropy.io import fits
import numpy as np

def mean_fits(images):
  y = np.zeros([((fits.open(images[1]))[0].data).shape[0],((fits.open(images[1]))[0].data).shape[1]],dtype = float)
  
  for image in images:
     HDUlist = fits.open(image)
     dat = HDUlist[0].data
     y = y + dat
  
  
  return y/len(images)





if __name__ == '__main__':
  
  
  data  = mean_fits(['data/image0.fits', 'data/image1.fits', 'data/image2.fits'])
  print(data[100, 100])
   
  
  plt.imshow(data.T, cmap=plt.cm.viridis)
  plt.colorbar()
  plt.show()