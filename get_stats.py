from sklearn.externals import joblib

from painting_analysis.lib.stats_generator import StatsGenerator

clf_type = 'neural_network' # available options: svm ; tree ; neural_network
method = 'grayscale_hog' # available options: flatten_pixels ; grayscale_hog

stats_generator = StatsGenerator(clf_type, method)
stats_generator.get_accuracy_of_model()
