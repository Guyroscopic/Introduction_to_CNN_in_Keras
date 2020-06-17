FILES AND THEIR DESCRIPTIONS:

1) Image Data.zip:

This is a compressed .zip folder which conatains a small datastet of cat and dog photos in directories named "cat" and "dog", respectively.

2) split images into dirs.py:

This is a python script which allows you to create "train", "test" and  "valid" directories and copy files from the "Image Dataset" to these directories according to a user specified ratio. This script aranges directories and images in a format that the "CustomCNN.ipynb" file expects.

3) CustomCNN.ipynb:

This is a Juppyter Notebook file and to run this you should have Jupyter Notebook installed on your system. This file uses the keras API to create a CNN and contains all the Machine Laerning code. It contains:

Data Augmentation code

Creating a keras Sequential Model

Training the Model

Prdicting with the model

4) testCNN1.h5:

This is the Model that I myself trained and saved. It has about 80-85% accuracy on the test set. It is a pre-trained model and you can tweak it to your liking.
