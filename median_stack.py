import matplotlib.pyplot as plt
from astropy.io import fits
import numpy as np 

def median_fits(images):
    
    dat = []
    
    y = np.zeros([((fits.open(images[1]))[0].data).shape[0],((fits.open(images[1]))[0].data).shape[1]],dtype = float)
    for image in images:
      HDUlist = fits.open(image)
      y = HDUlist[0].data
      dat.append(y)
    r = np.median(dat, axis = 0)
    
    
    
    return r


if __name__ == '__main__':
  
  result = median_fits(['data/image0.fits', 'data/image1.fits'])
  print(result[100, 100])
  
 
  result = median_fits(['data/image{}.fits'.format(str(i)) for i in range(11)])
  print(result[100, 100])
  
  plt.imshow(result.T, cmap=plt.cm.viridis)
  plt.colorbar()
  plt.show()