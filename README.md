## Shazam for art

### MVP

We upload to a computer an image of a painting it hasn't "seen" before and it takes a guess at the name of the artist.

### How should we get to MVP?

### Research Questions:

How might it be done using scikit?

How does scikit work?

What frameworks work with scikit?

What is required to replace the machine learning capability provided by scikit?


### Action Log

Monday:
* Decided on MVP and how to reach MVP
* Webscraping - python code that efficiently automated downloading several images
from an online image bank to our local repo
* Initial scikit setup - provided instructions on how to set up, and followed steps
for intial image processing

Tuesday:
We set out to answer these three key questions:
  1. Which feature extraction to do first? HOG, Pixel, Colour Histogram etc
  2. What is the order of the scikit pipeline?
  3. How does classification work?
      - Do we implement 'supervised'
      - Do we implement 'unsupervised'
  4. Imported algorithm from scikit-learn to process an 'unseen' image vs our image bank and return a value. 0 => Lowry, 1 => Turner. Our program successfully assigned the correct value to the unseen image. 
  5. MVP reached
    
