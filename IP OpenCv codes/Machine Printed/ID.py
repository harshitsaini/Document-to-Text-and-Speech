import sys
import cv2
from PIL import Image
from pytesseract import *
import numpy as np
src_path= 'C://Users//Harshit//Desktop//Initial_img//Machine Printed//ID CARD//'
original = src_path+ "ID1.jpg"
import pytesseract
#pytesseract.pytesseract.tesseract_cmd = 'H://Program Files (x86)//Tesseract-OCR//tesseract'
pytesseract.pytesseract.tesseract_cmd = 'H:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
TESSDATA_PREFIX='H://Program Files (x86)//Tesseract-OCR'
tessdata_dir_config = '--tessdata-dir "H:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'
'''
tessdata_dir_config = '--tessdata-dir "<replace_with_your_tessdata_dir_path>"'
# Example config: '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'
# It's important to include double quotes around the dir path.
pytesseract.image_to_string(image, lang='chi_sim', config=tessdata_dir_config)
'''

def getThresholded(img,smooth_it):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    if smooth_it==True:
        kernel = np.ones((7, 7), np.float32) / 49
        smooth = cv2.filter2D(img, -1, kernel)
        cv2.imwrite(src_path + "smoothened.png", smooth)
        img=smooth
    # ret, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    threshed = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 121, 2)
    #img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY, 11, 2)
    cv2.imwrite(src_path + 'thresholded.png',threshed)
    return threshed

def getClosed(img,iterations,kernel_size):
    kernel = np.ones((kernel_size,kernel_size), np.uint8)
    k = iterations
    closed=img
    while (k != 0):
        closed = cv2.morphologyEx(closed, cv2.MORPH_CLOSE, kernel)
        k -= 1
    cv2.imwrite(src_path + "closed.png", closed)
    return closed

def getOpened(img,iterations,kernel_size):
    kernel = np.ones((kernel_size,kernel_size), np.uint8)
    k = iterations
    opened=img
    while (k != 0):
        opened = cv2.morphologyEx(opened, cv2.MORPH_OPEN, kernel)
        k -= 1
    cv2.imwrite(src_path + "opened.png", opened)
    return opened

def getMorph(img,iterations,kernel_size,erode_it):
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    if erode_it == True :
        eroded = cv2.erode(img, kernel, iterations=iterations)
        cv2.imwrite(src_path + 'eroded.png', eroded)
        return eroded
    else:
        dilated= cv2.dilate(img, kernel, iterations=iterations)
        cv2.imwrite(src_path + "dilated.png", dilated)
        return dilated

def img_show(*args):
    for it,value in enumerate(args):
        cv2.imshow('Image Number: '+str(it),value)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def get_string (img_path):
    img=cv2.imread(img_path)
    conditioned = getThresholded(img,True)
    opened=getOpened(conditioned,50,12)
    final =opened
    cv2.imwrite(src_path+'final.png',final)
    #img_show(img,conditioned,opened)
    print('Conditioning Done !')
    result= pytesseract.image_to_string(Image.open(src_path+'final.png'),lang='eng', config=tessdata_dir_config)
    #os.remove(temp)
    return result

print('-----Start recognize text from image -----')
print(get_string(src_path+ "ID1.jpg"))
print("-------DONE-------")