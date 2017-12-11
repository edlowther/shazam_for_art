import numpy as np
from skimage import io
from skimage import img_as_float
from skimage import feature
from skimage.exposure import histogram
from skimage.transform import resize
from itertools import chain
from skimage.color import rgb2gray
from skimage.feature import local_binary_pattern

class PaintingProcessor:
    def __init__(self, image_filename):
        self.image = io.imread(image_filename)

    def resize_painting(self):
        return resize(self.image, (200, 200))

    def flatten_pixels(self):
        painting_flattened = []
        for row in self.resize_painting():
            for pixel in row:
                for colour in pixel:
                    painting_flattened.append(colour)
        return painting_flattened

    def grayscale_hog(self):
        grayscale_painting = rgb2gray(self.resize_painting())
        return feature.hog(grayscale_painting,
                                    orientations=9,
                                    pixels_per_cell=(8, 8),
                                    cells_per_block=(3, 3),
                                    block_norm='L2-Hys',
                                    transform_sqrt=False,
                                    feature_vector=True)

    def daisy(self):
        grayscale_painting = rgb2gray(self.resize_painting())
        # daisy_features = feature.daisy(grayscale_painting, step=180, radius=58, rings=2, histograms=6,
        #                  orientations=8)
        daisy_features = feature.daisy(grayscale_painting)
        features_flattened = []
        for x in daisy_features:
            for y in x:
                for z in y:
                    features_flattened.append(z)
        return features_flattened

    def grayscale_histogram(self):
        grayscale_painting = rgb2gray(self.resize_painting())
        return histogram(grayscale_painting, nbins=200)[0]

    def colour_histogram(self):
        result = []
        red_channel_copy = self.resize_painting().copy()
        red_channel_copy[:,:,1:] = 0
        result += list(histogram(rgb2gray(red_channel_copy), nbins=200)[0])
        green_channel_copy = self.resize_painting().copy()
        green_channel_copy[:,:,0::2] = 0
        result += list(histogram(rgb2gray(green_channel_copy), nbins=200)[0])
        blue_channel_copy = self.resize_painting().copy()
        blue_channel_copy[:,:,:2] = 0
        result += list(histogram(rgb2gray(blue_channel_copy), nbins=200)[0])
        return result

    def simple_mean(self):
        return [self.image.mean()]

    def colour_means(self):
        result = []
        result.append(self.image[:, :, 0].mean())
        result.append(self.image[:, :, 1].mean())
        result.append(self.image[:, :, 2].mean())
        return result

    def grid_simple_means(self):
        GRID_WIDTH = 20
        resized_painting = self.resize_painting()
        result = []
        for i in range(10):
            for j in range(10):
                result.append(resized_painting[
                    i*GRID_WIDTH:i*GRID_WIDTH+GRID_WIDTH,
                    j*GRID_WIDTH:j*GRID_WIDTH+GRID_WIDTH,
                    :
                ].mean())
        return result

    def grid_colour_means(self):
        GRID_WIDTH = 20
        resized_painting = self.resize_painting()
        result = []
        for i in range(10):
            for j in range(10):
                grid = resized_painting[
                    i*GRID_WIDTH:i*GRID_WIDTH+GRID_WIDTH,
                    j*GRID_WIDTH:j*GRID_WIDTH+GRID_WIDTH,
                    :
                ]
                result.append(grid[:, :, 0].mean())
                result.append(grid[:, :, 1].mean())
                result.append(grid[:, :, 2].mean())
        return result

    def texture(self):
        n_bins = 20
        lbp = local_binary_pattern(rgb2gray(self.image), 24, 3, 'uniform')
        return np.histogram(lbp, normed=True, bins=n_bins, range=(0, n_bins))[0]
