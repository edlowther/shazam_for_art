from sklearn import tree
from sklearn import neural_network
from sklearn import svm

class ModelBuilder:
    def __init__(self, clf_type, data_assembler_class):
        self.clf_type = clf_type
        self.data_assembler = data_assembler_class()

    def build(self):
        if self.clf_type == "tree":
            clf = tree.DecisionTreeClassifier()
        elif self.clf_type == "neural_network":
            clf = neural_network.MLPClassifier()
        elif self.clf_type == "svm":
            clf = svm.SVC()
        clf.fit(self.data_assembler.load_data(), self.data_assembler.load_targets())
        return clf
