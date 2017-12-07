import glob
import os
import shutil
from random import shuffle

class DataAssembler:

    def load_data(self):
        for filename in glob.glob('./images/training_data/*'):
            os.remove(filename)
        artists = ['constable', 'hopper', 'kandinsky', 'lowry', 'monet', 'rembrandt', 'rothko', 'rubens', 'turner', 'van-gogh']
        for artist in artists:
            filenames = glob.glob('images/all/' + artist + '*')
            shuffle(filenames)
            for filename in filenames[:80]:
                shutil.copy2(filename, 'images/training_data')
