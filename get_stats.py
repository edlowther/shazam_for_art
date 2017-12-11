from sklearn.externals import joblib

from painting_analysis.lib.stats_generator import StatsGenerator

# clf_type = 'svm' # available options: svm ; tree ; neural_network
method = 'texture' # available options: flatten_pixels ; grayscale_hog ; daisy

# for clf_type in ["svm", "tree", "neural_network"]:
for clf_type in ["svm", "tree"]:
    stats_generator = StatsGenerator(clf_type, method, "v5")
    stats_generator.get_accuracy_of_model()
