import csv
from datetime import datetime
from sklearn.externals import joblib

from painting_analysis.lib.painting_processor import PaintingProcessor
from painting_analysis.lib.data_loader import DataLoader
from painting_analysis.lib.artist_lookup import ArtistLookup

class StatsGenerator:
    def __init__(self, test_image_folder, clf_type, method):
        self.clf_type = clf_type
        self.method = method
        self.data_loader = DataLoader(method, test_image_folder, PaintingProcessor)
        self.artist_lookup = ArtistLookup().golden_copy

    def get_accuracy_of_model(self):
        test_images, targets = self.data_loader.load_paintings_and_targets()
        clf = joblib.load('./models/{}_{}_v3.pkl'.format(self.clf_type, self.method))
        results = clf.predict(test_images)

        stats_aggregator = {
            'overall': {
                'correct': 0.0,
                'total': 0.0
            }
        }
        for artist_name in self.artist_lookup:
            stats_aggregator[artist_name] = {
                'correct': 0.0,
                'total': 0.0
            }

        for result, target in zip(results, targets()):
            for artist in self.artist_lookup:
                if self.artist_lookup[artist] == target:
                    artist_name = artist
            print(artist_name)
            print(result == target)
            stats_aggregator['overall']['total'] += 1
            stats_aggregator[artist_name]['total'] += 1
            if result == target:
                stats_aggregator['overall']['correct'] += 1
                stats_aggregator[artist_name]['correct'] += 1

        print(stats_aggregator['overall']['correct'] / stats_aggregator['overall']['total'] * 100, "% accuracy")
        print("based on a total of ", stats_aggregator['overall']['total'], " tests")

        output = [
            datetime.now().isoformat(timespec='seconds'),
            self.clf_type,
            self.method,
            stats_aggregator['overall']['total'],
            round(stats_aggregator['overall']['correct'] / stats_aggregator['overall']['total'] * 100, 1)
        ]
        for artist in self.artist_lookup:
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
