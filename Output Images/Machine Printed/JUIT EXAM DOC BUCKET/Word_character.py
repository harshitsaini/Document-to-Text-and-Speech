import os
import sys
import cv2
from PIL import Image
from pytesseract import *
import numpy as np
import pytesseract

src_path= 'C://Users//Harshit//Desktop//Machine Learning//Image Analysis//Output Images//Machine Printed//JUIT EXAM DOC BUCKET//'
#src_path= 'C://Users//Harshit//Desktop//Machine Learning//Image Analysis//Output Images//Machine Printed//'
#pytesseract.pytesseract.tesseract_cmd = 'H://Program Files (x86)//Tesseract-OCR//tesseract'
pytesseract.pytesseract.tesseract_cmd = 'H:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
TESSDATA_PREFIX='H://Program Files (x86)//Tesseract-OCR'
tessdata_dir_config = '--tessdata-dir "H:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'


def getThresholded(img,smooth_it):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    if smooth_it==True:
        kernel = np.ones((8, 8), np.float32) / 64
        smooth = cv2.filter2D(img, -1, kernel)
        cv2.imwrite(new_path+ "smoothened.png", smooth)
        img=smooth
    #threshed = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 151, 0)
    _,threshed = cv2.threshold(img,200,255,cv2.THRESH_BINARY)
    cv2.imwrite(new_path+ 'thresholded.png',threshed)
    return threshed

def getClosed(img,iterations,kernel_size):
    kernel = np.ones((kernel_size,kernel_size), np.uint8)
    k = iterations
    closed=img
    while (k != 0):
        closed = cv2.morphologyEx(closed, cv2.MORPH_CLOSE, kernel)
        k -= 1
    cv2.imwrite(new_path+ "closed.png", closed)
    return closed

def getOpened(img,iterations,kernel_size):
    kernel = np.ones((kernel_size,kernel_size), np.uint8)
    k = iterations
    opened=img
    while (k != 0):
        opened = cv2.morphologyEx(opened, cv2.MORPH_OPEN, kernel)
        k -= 1
    cv2.imwrite(new_path+ "opened.png", opened)
    return opened

def getMorph(img,iterations,kernel_size,erode_it):
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    if erode_it == True :
        eroded = cv2.erode(img, kernel, iterations=iterations)
        cv2.imwrite(new_path+ 'eroded.png', eroded)
        return eroded
    else:
        dilated= cv2.dilate(img, kernel, iterations=iterations)
        cv2.imwrite(new_path+ "dilated.png", dilated)
        return dilated

def img_show(*args):
    for it,value in enumerate(args):
        cv2.imshow('Image Number: '+str(it),value)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def horizontal_dilation(img,iterations,kernel_size):
    kernel= np.array([[0,0,0],[1,1,1],[0,0,0]])

    dilated = cv2.dilate(img, kernel, iterations=iterations)
    cv2.imwrite(new_path + "dilated.png", dilated)
    return dilated
