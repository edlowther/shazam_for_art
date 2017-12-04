import skimage

import os

from skimage import io

filename = os.path.join(skimage.data_dir, './moon.png')

moon = io.imread(filename)

print(moon)
