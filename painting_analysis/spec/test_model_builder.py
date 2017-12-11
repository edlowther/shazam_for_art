import pytest
import sklearn
from painting_analysis.lib.model_builder import ModelBuilder

class MockDataAssembler:
    def __init__(self, method, reshuffle_training_data):
        self.load_data_called_count = 0
        self.load_targets_called_count = 0
        self.method = method

    def load_data(self):
        self.load_data_called_count += 1
        return [[0, 0], [1, 1]]

    def load_targets(self):
        self.load_targets_called_count += 1
        return [0, 1]

def test_build_method_can_initialise_decision_trees():
    model_builder = ModelBuilder(clf_type="tree", method="flatten_pixels", data_assembler_class=MockDataAssembler)
    assert isinstance(model_builder.build(), sklearn.tree.tree.DecisionTreeClassifier)

def test_build_method_can_initilialise_neural_network():
    model_builder = ModelBuilder(clf_type="neural_network", method="flatten_pixels", data_assembler_class=MockDataAssembler)
    assert isinstance(model_builder.build(), sklearn.neural_network.MLPClassifier)

def test_build_method_can_initilialise_svm_classifier():
    model_builder = ModelBuilder(clf_type="svm", method="flatten_pixels", data_assembler_class=MockDataAssembler)
    assert isinstance(model_builder.build(), sklearn.svm.SVC)

def test_build_method_loads_data_and_targets_from_data_assembler():
    model_builder = ModelBuilder(clf_type="svm", method="flatten_pixels", data_assembler_class=MockDataAssembler)
    model_builder.build()
    assert model_builder.data_assembler.load_data_called_count == 1
    assert model_builder.data_assembler.load_targets_called_count == 1

def test_it_passes_the_method_down_to_the_data_assembler():
    model_builder = ModelBuilder(clf_type="svm", method="flatten_pixels", data_assembler_class=MockDataAssembler)
    assert model_builder.data_assembler.method == "flatten_pixels"
