#### BY CHANGING THE KERNEL OF EROSION AND DILATION
 ###NOT USEFUL BECAUSE LINES COULD ALSO OCCUR WITH ANY ANGLE :p####

import sys
import cv2
from PIL import Image
from pytesseract import *
import numpy as np
src_path= 'C://Users//Harshit//Desktop//Initial_img//'

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


def get_string (img_path):
    img=cv2.imread(img_path)

# IMAGE CONDITIONING
    img= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ones=np.array([1,0,1])
    zeroes = np.array([1, 0, 1])
    kernel = np.uint8(ones)
    #ones=np.ones(3,np.uint8)
    #zeroes=np.zeros(3,np.uint8)
    np.concatenate((kernel, zeroes), axis=0)
    np.concatenate((kernel, ones), axis=0)
    #kernel= np.ones((3,3),np.uint8)
    cv2.imwrite(src_path + "removed_noise.png",img)
    print ("noise removal done")
 # THRESHOLDING
    #img= cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11,2)
    ret,img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    #img = cv2.erode(img, kernel, iterations=1000)
    #img = cv2.dilate(img, kernel, iterations=50)

    cv2.imwrite(src_path + "thres1.png",img)

    img = cv2.dilate(img, kernel, iterations=10)
    cv2.imwrite(src_path + "thres2.png", img)

    ret, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
    cv2.imwrite(src_path + "thres3.png", img)

    kernel= np.ones((3,3,),np.uint8)

    img = cv2.dilate(img, kernel, iterations=20)
    cv2.imwrite(src_path + "thres4.png", img)

# from here
    ''' linek = np.zeros((11, 11), dtype=np.uint8)

    linek[5, ...] = 1
    x = cv2.morphologyEx(img, cv2.MORPH_OPEN, linek, iterations=1)
    img -= x

    cv2.imwrite(src_path + "thres4.png", img)
    '''

    print("thresh done")
    result= pytesseract.image_to_string(Image.open(src_path+'thres4.png'),lang='spa', config=tessdata_dir_config)
    #kt=Image.open(src_path+"thres.png")
    #os.remove(temp)
    return result

print('-----Start recognize text from image -----')
print(get_string(src_path+ "7ab_original.jpg"))
print("-------DONE-------")