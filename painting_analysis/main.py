import os
import glob

from lib.stats_generator import StatsGenerator

clf_type = "svm"
method = "flatten_pixels"
test_image_folder = "./images/test_data/"
stats_generator = StatsGenerator(test_image_folder, clf_type, method)
stats_generator.get_accuracy_of_model()
