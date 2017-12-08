## Shazam for art

### Machine-Learning-Practice

[Based on this tutorial](https://machinelearningmastery.com/machine-learning-in-python-step-by-step/)

##This Practice looks at:

1. Installing the Python and SciPy platform.
2. Loading the dataset.
3. Summarizing the dataset.
4. Visualizing the dataset.
5. Evaluating some algorithms.
6. Making some predictions.

##I installed the following:

* scipy
* numpy
* matplotlib
* pandas
* sklearn


1. Import Libraries
2. Load Dataset
3. Get visualisation on the data

![screen shot 2017-12-05 at 14 15 49](https://user-images.githubusercontent.com/27693622/33612716-62f8bb24-d9ca-11e7-900d-cf429e13afa9.png)

![screen shot 2017-12-05 at 14 15 59](https://user-images.githubusercontent.com/27693622/33612755-8385d26e-d9ca-11e7-95a5-6d8c9dbaf97d.png)


Tuesday:
We set out to answer these three key questions:
  1. Which feature extraction to do first? HOG, Pixel, Colour Histogram etc
  2. What is the order of the scikit pipeline?
  3. How does classification work?
      - Do we implement 'supervised'
      - Do we implement 'unsupervised'
  4. Imported algorithm from scikit-learn to process an 'unseen' image vs our image bank and return a value. 0 => Lowry, 1 => Turner. Our program successfully assigned the correct value to the unseen image.
  5. MVP reached
  
Wednesday: 
  We included and compared 3 algorithms to check the artist of a painting. From sklearn we imported DecisionTree, SVM and Neural_Network. The results were as follows: 

At a glance svm_pixels appeared to be the most effective algorithm in terms of predicting the correct artist. This was a big break through as we had achieved 50% accuracy. 

Thursday: 
We tested existing code and created an effective TDD with higher test coverage in our analysis branch. We also researched Django using tutorials and began to build our front end website with Django. 





