import cv2
import numpy as np
import math

src_path= 'C://Users//Harshit//Desktop//initial_img//'
shapes_img='shapes.jpg'

class ShapeRecognition():

    def __init__(self,img):
        self.img=img
    def preprocessing(self,img):
        '''lower= np.array([0,0,0],dtype= np.uint8)
        upper= np.array([15,15,15], dtype=np.uint8)
        mask = cv2.inRange(self.img,lower,upper)
        cv2.imshow('masked imaged',mask)'''
        [a,contours,c]=cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        return contours

img = cv2.imread(src_path+shapes_img)
shape_recog= ShapeRecognition(img)

#imgGray = cv2.cvtColor(imgTrainingNumbers, cv2.COLOR_BGR2GRAY)          # get grayscale image
gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#ret,thresh= cv2.threshold(gray,245,255,cv2.THRESH_BINARY)
thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
#################################################################
'''kernel = np.ones((3, 3), np.uint8)
k = 20
closed = thresh
while (k != 0):
    closed = cv2.morphologyEx(closed, cv2.MORPH_CLOSE, kernel);
    k -= 1
    # cv2.imwrite(src_path + "closed.png", closed)
    '''

#blurred= cv2.pyrMeanShiftFiltering(img,31,91)

##################################################################
contours=shape_recog.preprocessing(thresh)
print (len(contours))
cv2.drawContours(img, contours, -1, (0,255,0), 2)
cv2.imshow('threshed',thresh)
cv2.imshow('oh yeah',img)
#cv2.imshow('closed',blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()
