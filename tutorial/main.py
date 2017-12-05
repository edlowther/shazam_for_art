from skimage import io

from scripts.painting_processor import PaintingProcessor
from scripts.model_creator import ModelCreator

clf = ModelCreator().build()
test_image = io.imread('./test_images/rembrandt_22.jpg')
print(clf.predict([PaintingProcessor(test_image).flatten()]))
