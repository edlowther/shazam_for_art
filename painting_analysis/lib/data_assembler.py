import glob
import os
import shutil
from random import shuffle
from painting_analysis.lib.artist_lookup import ArtistLookup

class DataAssembler:
    def __init__(self):
        self.artist_lookup = ArtistLookup().golden_copy

    def load_data(self):
        self._move_files()

    def load_targets(self):
        targets = []
        for filename in os.listdir('./images/training_data'):
            artist_name = filename.split("_")[0]
            targets.append(self.artist_lookup[artist_name])
        return targets

    def _move_files(self):
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
