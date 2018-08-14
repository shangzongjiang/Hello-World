import numpy as np
import skimage.io as io

from skimage import data_dir
str='C:/Users/szj/Desktop/2/*.jpg'
coll = io.ImageCollection(str)
print(len(coll))
io.imshow(coll[1])