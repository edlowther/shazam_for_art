from skimage.transform import resize

class PaintingProcessor:
    def __init__(self, painting):
        self.painting = painting

    def resized_painting(self):
        return resize(self.painting, (200, 200))

    def flatten(self):
        painting_flattened = []
        for row in self.resized_painting():
            for pixel in row:
                for colour in pixel:
                    painting_flattened.append(colour)
        return painting_flattened
