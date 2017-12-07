import pytest
import os
import glob
from painting_analysis.lib.data_assembler import DataAssembler
from painting_analysis.lib.artist_lookup import ArtistLookup

@pytest.fixture
def data_assembler():
    return DataAssembler()

@pytest.fixture
def artist_lookup():
    return ArtistLookup().golden_copy

def test_load_data_moves_800_paintings_into_the_training_data_folder(data_assembler):
    data_assembler.load_data()
    training_data_filenames = os.listdir('./images/training_data')
    assert len(training_data_filenames) == 800

def test_load_data_moves_80_paintings_by_each_artist_into_the_training_data_folder(data_assembler, artist_lookup):
    data_assembler.load_data()
    artists = artist_lookup.keys()
    for artist in artists:
        assert len(glob.glob('images/training_data/' + artist + '*')) == 80

def test_load_data_moves_200_images_into_the_test_data_folder(data_assembler):
    data_assembler.load_data()
    assert len(os.listdir('./images/test_data/')) == 200

def test_load_data_moves_20_paintings_by_each_artist_into_the_test_data_folder(data_assembler, artist_lookup):
    data_assembler.load_data()
    artists = artist_lookup.keys()
    for artist in artists:
        assert len(glob.glob('images/test_data/' + artist + '*')) == 20

def test_load_targets_creates_a_list_with_800_elements(data_assembler):
    targets = data_assembler.load_targets()
    assert len(targets) == 800

def test_load_targets_assigns_correct_artist_number(data_assembler, artist_lookup):
    targets = data_assembler.load_targets()
    training_data_filenames = os.listdir('./images/training_data')
    for index, filename in enumerate(training_data_filenames):
        artist_name = filename.split("_")[0]
        assert targets[index] == artist_lookup[artist_name]
