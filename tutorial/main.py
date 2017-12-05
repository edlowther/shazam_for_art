import skimage
from skimage import io
filename = './images/lowry_0.jpg'
lowry_0 = io.imread(filename)
print(lowry_0.shape)
print(lowry_0.size)
print(lowry_0.shape[0] * lowry_0.shape[1]  * lowry_0.shape[2])
print(lowry_0.mean())

lowries = io.imread_collection('./images/lowry_*.jpg')
print(lowries[0])
