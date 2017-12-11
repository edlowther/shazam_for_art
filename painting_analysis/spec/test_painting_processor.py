import pytest
import glob
import numpy as np
from random import choice

from painting_analysis.lib.painting_processor import PaintingProcessor

@pytest.fixture
def painting_processor():
    sample_filename = choice(glob.glob('./images/training_data/*'))
    return PaintingProcessor(sample_filename)

def test_resize_method_turns_an_image_into_200px_by_200px(painting_processor):
    assert painting_processor.resize_painting().shape == (200, 200, 3)

def test_flatten_pixels_returns_1d_list(painting_processor):
    flattened_image = painting_processor.flatten_pixels()
    dimensions_of_list = len(np.array(flattened_image).shape)
    assert dimensions_of_list == 1

def test_flatten_pixels_returns_list_with_same_number_of_elements_as_size_of_resized_image(painting_processor):
    flattened_image = painting_processor.flatten_pixels()
    assert len(flattened_image) == painting_processor.resize_painting().size

def test_grayscale_hog_returns_1d_list(painting_processor):
    grayscale_hog = painting_processor.grayscale_hog()
    dimensions_of_list = len(np.array(grayscale_hog).shape)
    assert dimensions_of_list == 1
