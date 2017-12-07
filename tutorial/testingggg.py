
import skimage
import os
from skimage import io
from skimage.viewer import ImageViewer
from skimage.color import rgb2gray

filename = os.path.join('images_all/rembrandt_83.jpg')
turner = io.imread(filename)

print(turner.shape)
# print(turner)
# print(skimage.filters.median(turner, flatten=True, selem=None, out=None, mask=None, shift_x=False, shift_y=False))
# print(skimage.filters.rank_order(turner))   #working

# turner_1 = skimage.filters.gabor_kernel(frequency=1, theta=0, bandwidth=1, sigma_x=None, sigma_y=None, n_stds=3, offset=0)
# print(turner_1)    #not passing in the argument.


gray_turner = rgb2gray(turner)
print(gray_turner.shape)
print(gray_turner)


g_turner = skimage.feature.canny(gray_turner, sigma=1.0, low_threshold=None, high_threshold=None, mask=None, use_quantiles=False)
g1_turner = skimage.filters.median(gray_turner, selem=None, out=None, mask=None, shift_x=False, shift_y=False)
g2_turner = skimage.filters.frangi(gray_turner, scale_range=(1, 10), scale_step=2, beta1=0.5, beta2=15, black_ridges=True)
g3_turner = skimage.filters.hessian(gray_turner, scale_range=(1, 10), scale_step=2, beta1=0.5, beta2=15)
g4_turner = skimage.filters.threshold_local(gray_turner, block_size=21, method='gaussian', offset=0, mode='reflect', param=None)


import matplotlib.pyplot as plt
plt.imshow(g3_turner)
plt.show()
