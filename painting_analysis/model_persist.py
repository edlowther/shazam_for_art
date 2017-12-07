from sklearn.externals import joblib

from scripts.model_creator import ModelCreator

# clf_type = 'tree'
# clf_type = 'neural_network'
clf_type = 'svm'

clf = ModelCreator().build(clf_type)
joblib.dump(clf, './models/{}.pkl'.format(clf_type))
