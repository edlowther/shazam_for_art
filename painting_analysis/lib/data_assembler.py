import glob
import os
import shutil
from random import shuffle

from painting_analysis.lib.painting_processor import PaintingProcessor
from painting_analysis.lib.data_loader import DataLoader
from painting_analysis.lib.artist_lookup import ArtistLookup

class DataAssembler:
    def __init__(self, method="flatten_pixels", reshuffle_training_data=True, painting_processor_class=PaintingProcessor):
        self.artist_lookup = ArtistLookup().golden_copy
        self.reshuffle_training_data = reshuffle_training_data
        self.data_loader = DataLoader(method, './images/training_data/', painting_processor_class)

    def load_data_and_targets(self):
        if self.reshuffle_training_data:
            self.move_files()
        return self.data_loader.load_paintings_and_targets()

    def move_files(self):
        for filename in glob.glob('./images/training_data/*'):
            os.remove(filename)
        for filename in glob.glob('./images/test_data/*'):
            os.remove(filename)
        for artist in self.artist_lookup.keys():
            filenames = glob.glob('images/all/' + artist + '*')
            shuffle(filenames)
            for filename in filenames[:80]:
                shutil.copy2(filename, 'images/training_data')
            for filename in filenames[80:100]:
                shutil.copy2(filename, 'images/test_data')
