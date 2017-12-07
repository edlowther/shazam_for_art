import skimage
from skimage import io
from skimage.transform import resize
from sklearn import tree
from sklearn.neural_network import MLPClassifier
from sklearn import svm
import os

from scripts.painting_processor import PaintingProcessor
from scripts.artist_lookup import artist_lookup

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
            for artist in artist_lookup:
                if artist in filename:
                    artist_number = artist_lookup[artist]
                    targets.append(artist_number)

        return targets

    def build(self, clf_type='tree'):
        if clf_type == 'tree':
            clf = tree.DecisionTreeClassifier()
        elif clf_type == 'neural_network':
            clf = MLPClassifier()
        elif clf_type == 'svm':
            clf = svm.SVC()
        clf.fit(self.load_data(), self.define_targets())
        return clf
