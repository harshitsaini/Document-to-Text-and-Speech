import sys
import cv2
from PIL import Image
from pytesseract import *
import numpy as np
import pytesseract

src_path= 'C://Users//Harshit//Desktop//Machine Learning//Image Analysis//Output Images//Machine Printed//Spanish Images//'
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

ex_fl= "Spanish0//"

def getThresholded(img,smooth_it):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    if smooth_it==True:
        kernel = np.ones((3, 3), np.float32) / 9
        smooth = cv2.filter2D(img, -1, kernel)
        cv2.imwrite(src_path +ex_fl+ "smoothened.png", smooth)
        img=smooth
    threshed = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 121, 2)
    cv2.imwrite(src_path +ex_fl+ 'thresholded.png',threshed)
    return threshed

def getClosed(img,iterations,kernel_size):
    kernel = np.ones((kernel_size,kernel_size), np.uint8)
    k = iterations
    closed=img
    while (k != 0):
        closed = cv2.morphologyEx(closed, cv2.MORPH_CLOSE, kernel)
        k -= 1
    cv2.imwrite(src_path +ex_fl+ "closed.png", closed)
    return closed

def getOpened(img,iterations,kernel_size):
    kernel = np.ones((kernel_size,kernel_size), np.uint8)
    k = iterations
    opened=img
    while (k != 0):
        opened = cv2.morphologyEx(opened, cv2.MORPH_OPEN, kernel)
        k -= 1
    cv2.imwrite(src_path +ex_fl+ "opened.png", opened)
    return opened

def getMorph(img,iterations,kernel_size,erode_it):
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    if erode_it == True :
        eroded = cv2.erode(img, kernel, iterations=iterations)
        cv2.imwrite(src_path +ex_fl+ 'eroded.png', eroded)
        return eroded
    else:
        dilated= cv2.dilate(img, kernel, iterations=iterations)
        cv2.imwrite(src_path +ex_fl+ "dilated.png", dilated)
        return dilated

def img_show(*args):
    for it,value in enumerate(args):
        cv2.imshow('Image Number: '+str(it),value)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def get_string0(img_path):
    img=cv2.imread(img_path)
    conditioned = getThresholded(img,False)#Dont know why i was smoothing my grayscale pic !!!???
    final =conditioned
    cv2.imwrite(src_path+ex_fl+'final.png',final)
    print('Conditioning Done !')
    result= pytesseract.image_to_string(Image.open(src_path+ex_fl+'final.png'),lang='spa', config=tessdata_dir_config)
    #os.remove(temp)
    return result

print('-----Start recognize text from image -----')
print(get_string0(src_path+"Spanish0//span_img.png"))
print("-------DONE-------\n\n")

ex_fl= "Spanish1//"

print('-----Start recognize text from image -----')
print(get_string0(src_path+"Spanish1//span1_img.png"))
print("-------DONE-------\n\n")

ex_fl= "Spanish2//"

print('-----Start recognize text from image -----')
print(get_string0(src_path+"Spanish2//span2_img.png"))
print("-------DONE-------\n\n")