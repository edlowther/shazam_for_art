from sklearn.externals import joblib

from painting_analysis.lib.stats_generator import StatsGenerator

clf_type = 'svm' # available options: svm ; tree ; neural_network
method = 'flatten_pixels' # available options: flatten_pixels ; grayscale_hog

stats_generator = StatsGenerator(clf_type, method)
stats_generator.get_accuracy_of_model()
