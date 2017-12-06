import skimage
import os
from skimage import io
from skimage.viewer import ImageViewer
from skimage.color import rgb2gray


filename = os.path.join('images/constable_5.jpg')
angel = io.imread(filename)

gray_angel = rgb2gray(angel)

print(gray_angel.shape)
print(gray_angel)

hog_angel = skimage.feature.hog(gray_angel, orientations=9, pixels_per_cell=(8, 8), cells_per_block=(3, 3), block_norm='L2-Hys', transform_sqrt=False, feature_vector=True)

print(hog_angel)
print(hog_angel.shape)

# import matplotlib.pyplot as plt # import
# plt.imshow(hog_angel2D) #load
# plt.show()  # show the window
