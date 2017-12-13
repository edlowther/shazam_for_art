import os
import glob

from scripts.stats_generator import StatsGenerator
from scripts.artist_lookup import artist_lookup

clf_type = "svm"

test_image_filenames = os.listdir('./test_images')
stats_generator = StatsGenerator(test_image_filenames, clf_type)
stats_generator.get_accuracy_of_model()

# for artist_name in artist_lookup:
# number_to_keep = 80
# for artist_name in artist_lookup:
#     for filename in glob.glob('./images/{}*.jpg'.format(artist_name))[number_to_keep:]:
#         os.rename(filename, filename.replace("/images/", "/images_all/"))

# test_image = io.imread('./images/hopper_124.jpg')
# print(test_image)
# print(test_image.shape)
