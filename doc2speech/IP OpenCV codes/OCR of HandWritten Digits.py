import sys

import cv2
import numpy as np
import pytesseract
from matplotlib import pyplot as plt
from PIL import Image
from pytesseract import *

pytesseract.pytesseract.tesseract_cmd = (
    "H:/Program Files (x86)/Tesseract-OCR/tesseract.exe"
)
TESSDATA_PREFIX = "H://Program Files (x86)//Tesseract-OCR"
tessdata_dir_config = (
    '--tessdata-dir "H:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'
)

img = cv2.imread(
    "C:\\Users\\Harshit\\Desktop\\Machine Learning\\Image Analysis\\Output Images\\Handwritten&Cursive\\Digits\\digits.png"
)
# print(img.shape)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# cv2.imshow('gray',gray)
# cv2.waitKey(0)
# cv2.destroyAllWindows(0)

# Now we split the image to 5000 cells, each 20x20 size
cells = [np.hsplit(row, 100) for row in np.vsplit(gray, 50)]

# Make it into a Numpy array. It size will be (50,100,20,20)
x = np.array(cells)

# Now we prepare train_data and test_data.
train = x[:, :50].reshape(-1, 400).astype(np.float32)  # Size = (2500,400)
test = x[:, 50:100].reshape(-1, 400).astype(np.float32)  # Size = (2500,400)

print(train.shape)
print(test.shape)

# Create labels for train and test data
k = np.arange(10)
# print(k)
train_labels = np.repeat(k, 250)[:, np.newaxis]
test_labels = train_labels.copy()


# Initiate kNN, train the data, then test it with test data for k=1
knn = cv2.ml.KNearest_create()
knn.train(train, cv2.ml.ROW_SAMPLE, train_labels)
ret, result, neighbours, dist = knn.findNearest(test, k=5)

# knn = cv2.KNearest()
# knn.train(train,train_labels)
# ret,result,neighbours,dist = knn.find_nearest(test,k=5)

# Now we check the accuracy of classification
# For that, compare the result with test_labels and check which are wrong
matches = result == test_labels
correct = np.count_nonzero(matches)
accuracy = correct * 100.0 / result.size
print(accuracy)

# save the data
np.savez("knn_data.npz", train=train, train_labels=train_labels)

# Now load the data
with np.load("knn_data.npz") as data:
    print(data.files)
    train = data["train"]
    train_labels = data["train_labels"]
