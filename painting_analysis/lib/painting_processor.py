from skimage import io
from skimage import feature
from skimage.transform import resize
from itertools import chain
from skimage.color import rgb2gray

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
