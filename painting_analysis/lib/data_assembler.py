import glob
import os
import shutil
from random import shuffle

class DataAssembler:

    def load_data(self):
        artists = ['constable', 'hopper', 'kandinsky', 'lowry', 'monet', 'rembrandt', 'rothko', 'rubens', 'turner', 'van-gogh']
        for filename in glob.glob('./images/training_data/*'):
            os.remove(filename)
        for filename in glob.glob('./images/test_data/*'):
            os.remove(filename)
        for artist in artists:
            filenames = glob.glob('images/all/' + artist + '*')
            shuffle(filenames)
            for filename in filenames[:80]:
                shutil.copy2(filename, 'images/training_data')
            for filename in filenames[80:100]:
                shutil.copy2(filename, 'images/test_data')
