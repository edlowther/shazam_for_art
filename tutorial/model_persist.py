from skimage import io
from sklearn.externals import joblib

from scripts.painting_processor import PaintingProcessor
from scripts.model_creator import ModelCreator

clf = ModelCreator().build()
joblib.dump(clf, 'model.pkl')
