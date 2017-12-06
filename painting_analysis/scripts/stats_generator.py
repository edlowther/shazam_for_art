from datetime import datetime
import csv
from skimage import io
from sklearn.externals import joblib

from scripts.painting_processor import PaintingProcessor
from scripts.artist_lookup import artist_lookup

class StatsGenerator():
    def __init__(self, test_image_filenames, clf_type):
        self.test_image_filenames = test_image_filenames
        self.clf_type = clf_type

    def get_images_to_test(self):
        test_images = []
        for test_image_filename in self.test_image_filenames:
            test_image = io.imread('./test_images/' + test_image_filename)
            test_image_flattened = PaintingProcessor(test_image).flatten()
            test_images.append(test_image_flattened)
        return test_images


    def get_accuracy_of_model(self):
        test_images = self.get_images_to_test()
        clf = joblib.load('./models/{}.pkl'.format(self.clf_type))
        results = clf.predict(test_images)

        stats_aggregator = {
            'overall': {
                'correct': 0.0,
                'total': 0.0
            }
        }
        for artist in artist_lookup:
            stats_aggregator[artist] = {
                'correct': 0.0,
                'total': 0.0
            }

        total = 0
        correct = 0.0
        for result, filename in zip(results, self.test_image_filenames):
            artist = filename.split("_")[0]
            artist_number = artist_lookup[artist]
            print(artist)
            stats_aggregator[artist]['total'] += 1
            print(result == artist_number)
            if result == artist_number:
                correct += 1
                stats_aggregator[artist]['correct'] += 1
            total += 1

        print(correct / total * 100, "% accuracy")
        print("based on a total of ", total, " tests")

        output = [
            datetime.now().isoformat(timespec='seconds'),
            self.clf_type,
            total,
            round(correct / total * 100, 1)
        ]
        for artist in artist_lookup:
            output.append(
                    round(stats_aggregator[artist]['correct'] / stats_aggregator[artist]['total'] * 100, 1)
                )
        self._update_log(output)

    def _update_log(self, results, filename='./painting_analysis/stats/log_v1.csv'):
        data = []
        with open(filename) as f:
            previous_data = csv.reader(f)
            for row in previous_data:
                data.append(row)
        with open(filename, 'w') as f:
            output = csv.writer(f)
            for row in data:
                output.writerow(row)
            output.writerow(results)
