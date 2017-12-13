from sklearn.externals import joblib

from painting_analysis.lib.stats_generator import StatsGenerator

# clf_type = 'svm' # available options: svm ; tree ; neural_network
# method = 'texture' # available options: flatten_pixels ; grayscale_hog ; daisy

for method in ["flatten_pixels",
                "grayscale_hog",
                "daisy",
                "grayscale_histogram",
                "colour_histogram",
                "colour_means",
                "grid_simple_means",
                "grid_colour_means"]:
    # for clf_type in ["svm", "tree", "neural_network", "bayes"]:
    stats_generator = StatsGenerator(["svm", "tree", "neural_network", "bayes"], method, "v7")
    stats_generator.get_accuracy_of_model()
