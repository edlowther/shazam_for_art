from skimage.transform import resize
import skimage
import os
from skimage import io
from skimage.viewer import ImageViewer
from skimage.color import rgb2gray

class PaintingProcessor:
    def __init__(self, painting):
        self.painting = painting

    def resized_painting(self):
        return resize(self.painting, (200, 200))

    def flatten(self):
        # resized_painting = self.resized_painting()
        # grayscale_painting = rgb2gray(resized_painting)
        # return skimage.feature.hog(grayscale_painting, orientations=9, pixels_per_cell=(8, 8), cells_per_block=(3, 3), block_norm='L2-Hys', transform_sqrt=False, feature_vector=True)


        painting_flattened = []
        for row in self.resized_painting():
            for pixel in row:
                for colour in pixel:
                    painting_flattened.append(colour)
        return painting_flattened
