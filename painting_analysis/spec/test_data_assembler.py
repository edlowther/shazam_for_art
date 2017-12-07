import pytest
import os
import glob
from painting_analysis.lib.data_assembler import DataAssembler

def test_load_data_moves_800_paintings_into_the_training_data_folder():
    data_assembler = DataAssembler()
    data_assembler.load_data()
    training_data_filenames = os.listdir('./images/training_data')
    assert len(training_data_filenames) == 800

def test_load_data_moves_80_paintings_by_each_artist_into_the_training_data_folder():
    data_assembler = DataAssembler()
    data_assembler.load_data()
    artists = ['constable', 'hopper', 'kandinsky', 'lowry', 'monet', 'rembrandt', 'rothko', 'rubens', 'turner', 'van-gogh']
    for artist in artists:
        assert len(glob.glob('images/training_data/' + artist + '*')) == 80
