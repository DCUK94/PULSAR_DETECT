import matplotlib.pyplot as plt
from helper import running_stats
import numpy as np
from astropy.io import fits



def median_bins_fits(images, B):
 
  mn, sd  =  running_stats(images)
  
  dim = mn.shape 
  
  left_bin = np.zeros(dim)
  bins = np.zeros((dim[0], dim[1], B))
  bin_width = 2 * sd / B 
  minval = mn - sd
  maxval = mn + sd
  
   
  for image in images:
    HDUlist = fits.open(image)
    dat = HDUlist[0].data
    
    for i in range(dim[0]):
        for j in range(dim[1]):
          value = dat[i, j]

        
          if value < minval[i,j]:
            left_bin[i, j] += 1
                
          elif value >= minval[i,j] and value < maxval[i,j] :
            bin = int((value - (minval[i,j]))/bin_width[i, j])
            bins[i, j, bin] += 1
  
      
  return (mn, sd, left_bin, bins) 

def median_approx_fits(images, B):
  mn, sd, left_bin, bins = median_bins_fits(images, B)
  
  dim = mn.shape   
  md = np.zeros(dim)
  bin_width = 2 * sd / B 
  minval = mn - sd
  
  
  for i in range(dim[0]):
    for j in range(dim[1]):    
      count = left_bin[i, j]
      for b, bincount in enumerate(bins[i, j]):
        count += bincount
        if count >= (len(images) + 1 )/2:
          break
      md[i, j] = minval[i, j] + bin_width[i, j]*(b  + 0.5)
      
  return md


if __name__ == '__main__':
  
  mean, std, left_bin, bins = median_bins_fits(['data/image0.fits', 'data/image1.fits', 'data/image2.fits'], 5)
  median = median_approx_fits(['data/image0.fits', 'data/image1.fits', 'data/image2.fits'], 5)
  
  
  plt.imshow(median.T, cmap=plt.cm.viridis)
  plt.colorbar()
  plt.show()