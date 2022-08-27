import cv2
import numpy as np


# Function to apply thresholding to given Image
def getThresholded(img, smooth_it=True):

    # Reducing image to grayscale
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Application of smoothening
    if smooth_it == True:
        kernel = np.ones((8, 8), np.float32) / 64
        smooth = cv2.filter2D(img, -1, kernel)
        # cv2.imwrite(new_path + "smoothened.png", smooth)
        img = smooth

    # Application of Otsu Thresholding
    _, threshed = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY)
    # cv2.imwrite(new_path + 'thresholded.png', threshed)
    return threshed


# Function to apply morphological closing
def getClosed(img, iterations=1, kernel_size=3):

    # Generation of a 2D kernal of given kernel size
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    k = iterations
    closed = img
    while k != 0:
        closed = cv2.morphologyEx(closed, cv2.MORPH_CLOSE, kernel)
        k -= 1
    # cv2.imwrite(new_path + "closed.png", closed)
    return closed


# Function to apply morphological opening
def getOpened(img, iterations=1, kernel_size=3):
    # Generation of a 2D kernal of given kernel size
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    k = iterations
    opened = img
    while k != 0:
        opened = cv2.morphologyEx(opened, cv2.MORPH_OPEN, kernel)
        k -= 1
    # cv2.imwrite(new_path + "opened.png", opened)
    return opened


# Function to apply morphological erosion/dilation
def getMorph(img, iterations=1, kernel_size=3, erode_it=False):
    # Generation of a 2D kernal of given kernel size
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    if erode_it == True:
        eroded = cv2.erode(img, kernel, iterations=iterations)
        # cv2.imwrite(new_path + 'eroded.png', eroded)
        return eroded
    else:
        dilated = cv2.dilate(img, kernel, iterations=iterations)
        # cv2.imwrite(new_path + "dilated.png", dilated)
        return dilated


# Function to show multiple images
def img_show(*args):
    for it, value in enumerate(args):
        cv2.imshow("Image Number: " + str(it), value)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Function to apply morphological horizontal dilation
def horizontal_dilation(img, iterations=1):
    # Generation of a 2D kernal
    kernel = np.array([[0, 0, 0], [1, 1, 1], [0, 0, 0]], dtype=np.uint8)

    dilated = cv2.dilate(img, kernel, iterations=iterations)
    # cv2.imwrite(new_path + "dilated.png", dilated)
    return dilated
