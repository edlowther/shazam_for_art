import skimage
from skimage import io
from skimage.transform import resize
from sklearn import tree
from sklearn.neural_network import MLPClassifier
import os

from scripts.painting_processor import PaintingProcessor


class ModelCreator:

    def load_data(self):
        paintings = io.imread_collection('./images/*.jpg')
        filenames = os.listdir('./images')
        data = []
        filenames_index = 0
        for painting in paintings:
            print("Loading:", filenames[filenames_index])
            filenames_index += 1
            painting_flattened = PaintingProcessor(painting).flatten()
            data.append(painting_flattened)
        return data

    def define_targets(self):
        targets = []

        for filename in os.listdir('./images'):
            if "lowry" in filename:
                targets.append(0)
            elif "turner" in filename:
                targets.append(1)
            elif "rembrandt" in filename:
                targets.append(2)
            elif "monet" in filename:
                targets.append(3)
            elif "hopper" in filename:
                targets.append(4)

        return targets

    def build(self):
        clf = tree.DecisionTreeClassifier()
        clf = clf.fit(self.load_data(), self.define_targets())
        return clf
