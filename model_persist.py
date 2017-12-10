import traceback
from sklearn.externals import joblib

from painting_analysis.lib.model_builder import ModelBuilder
from painting_analysis.lib.data_loader import DataLoader

# clf_type = 'svm' # available options: svm ; tree ; neural_network
# method = 'flatten_pixels' # available options: flatten_pixels ; grayscale_hog
reshuffle_training_data = False

for method in ["flatten_pixels", "grayscale_hog"]:
    # data_loader = DataLoader(method, './images/training_data/')
    # paintings_data = data_loader.load_paintings()
    # targets = data_loader.load_targets()
    for clf_type in ["svm", "tree", "neural_network"]:
        try:
            builder = ModelBuilder(clf_type, method, reshuffle_training_data)
            clf = builder.build()
            joblib.dump(clf, './models/{}_{}_v3.pkl'.format(clf_type, method))
        except Exception as e:
            print("failure on", clf_type, ", method:", method, ", error type:", type(e), ", error:", e)
            traceback.print_exc()
