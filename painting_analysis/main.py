from skimage import io
from scripts.painting_processor import PaintingProcessor
from sklearn.externals import joblib
import os

from scripts.artist_lookup import artist_lookup

sample_images = []

test_image_filenames = os.listdir('./test_images')
for test_image_filename in test_image_filenames:
    test_image = io.imread('./test_images/' + test_image_filename)
    test_image_flattened = PaintingProcessor(test_image).flatten()
    sample_images.append(test_image_flattened)

clf = joblib.load('./models/neural_network.pkl')

results = clf.predict(sample_images)

index = 0

total_number_of_tests = len(test_image_filenames)
correct = 0.0

for result in results:
    artist = test_image_filenames[index].split("_")[0]
    artist_number = artist_lookup[artist]
    print(artist)
    print(result == artist_number)
    if result == artist_number:
        correct += 1
    index += 1

print(correct / total_number_of_tests * 100)
print("based on a total of ", total_number_of_tests, " tests")

# test_image = io.imread('./images/hopper_124.jpg')
# print(test_image)
# print(test_image.shape)
