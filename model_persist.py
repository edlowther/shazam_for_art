from sklearn.externals import joblib

from painting_analysis.lib.model_builder import ModelBuilder

clf_type = 'svm' # available options: svm ; tree ; neural_network
method = 'flatten_pixels' # available options: flatten_pixels ; grayscale_hog
reshuffle_training_data = False

clf = ModelBuilder(clf_type, method, reshuffle_training_data).build()
joblib.dump(clf, './models/{}_{}_v2.pkl'.format(clf_type, method))
