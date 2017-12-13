from sklearn.externals import joblib

from painting_analysis.lib.model_builder import ModelBuilder
from painting_analysis.lib.data_loader import DataLoader

# clf_type = 'svm' # available options: svm ; tree ; neural_network
# method = 'flatten_pixels' # available options: flatten_pixels ; grayscale_hog
reshuffle_training_data = False

for method in ["flatten_pixels",
                "grayscale_hog",
                "daisy",
                "grayscale_histogram",
                "colour_histogram",
                "colour_means",
                "grid_simple_means",
                "grid_colour_means"]:
    # for clf_type in ["svm", "tree", "neural_network", "bayes"]:
    try:
        clf = ModelBuilder(["svm", "tree", "neural_network", "bayes"], method, reshuffle_training_data).build()
        # joblib.dump(clf, './models/{}_{}_v7.pkl'.format(clf_type, method))
    except Exception as err:
        print("failure on", method)
        print(err)
