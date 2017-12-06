from skimage import io

from scripts.painting_processor import PaintingProcessor
from scripts.model_creator import ModelCreator



clf = ModelCreator().build()
<<<<<<< HEAD
test_image = io.imread('./test_images/rembrandt_22.jpg')
=======
test_image = io.imread('./test_images/hopper_158.jpg')
>>>>>>> master
print(clf.predict([PaintingProcessor(test_image).flatten()]))

# test_image = io.imread('./images/hopper_124.jpg')
# print(test_image)
# print(test_image.shape)
