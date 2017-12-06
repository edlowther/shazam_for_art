from sklearn.decomposition import PCA
from pylab import *
from skimage import data, io, color

filename = '../images/lowry_0.jpg'
lowry_gray = io.imread(filename,as_grey=True)

subplot(2, 2, 1)
io.imshow(lowry_gray)
xlabel('Original Image')

for i in range(1, 4):
    n_comp = 5 ** i
pca = PCA(n_components = n_comp)
pca.fit(lowry_gray)
lowry_gray_pca = pca.fit_transform(lowry_gray)

subplot(2, 2, 2)
io.imshow(lowry_gray_pca)
xlabel('Image after applying PCA')

lowry_gray_restored = pca.inverse_transform(lowry_gray_pca)
subplot(2, 2, i+1)
io.imshow(lowry_gray_restored)
xlabel('Restored image n_components = %s' %n_comp)
# print 'Variance retained %s %%' %((1 - sum(pca.explained_variance_ratio_) / size(pca.explained_variance_ratio_)) * 100)
# print 'Compression Ratio %s %%' %(float(size(lowry_gray_pca)) / size(lowry_gray) * 100)
show()
