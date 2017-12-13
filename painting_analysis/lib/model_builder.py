from sklearn import tree
from sklearn import neural_network
from sklearn import svm
from sklearn.naive_bayes import GaussianNB
from sklearn.externals import joblib

from painting_analysis.lib.data_assembler import DataAssembler

class ModelBuilder:
    def __init__(self,
                clf_types,
                method,
                reshuffle_training_data=True,
                data_assembler_class=DataAssembler,
                preloaded_data=False,
                preloaded_targets=False):
        self.clf_types = clf_types
        self.method = method
        self.data_assembler = data_assembler_class(method, reshuffle_training_data)
        self.preloaded_data = self.data_assembler.load_data()
        self.preloaded_targets = self.data_assembler.load_targets()

    def build(self):
        for clf_type in self.clf_types:
            if clf_type == "tree":
                clf = tree.DecisionTreeClassifier()
            elif clf_type == "neural_network":
                clf = neural_network.MLPClassifier()
            elif clf_type == "svm":
                clf = svm.SVC()
            elif clf_type == "bayes":
                clf = GaussianNB()
            clf.fit(self.preloaded_data, self.preloaded_targets)
            joblib.dump(clf, './models/{}_{}_v7.pkl'.format(clf_type, self.method))
