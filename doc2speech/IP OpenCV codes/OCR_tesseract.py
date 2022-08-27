import sys

import cv2
import numpy as np
from PIL import Image
from pytesseract import *

src_path = "C://Users//Harshit//Desktop//Initial_img//Handwritten&Cursive//AB//"

import pytesseract

# pytesseract.pytesseract.tesseract_cmd = 'H://Program Files (x86)//Tesseract-OCR//tesseract'
pytesseract.pytesseract.tesseract_cmd = (
    "H:/Program Files (x86)/Tesseract-OCR/tesseract.exe"
)
TESSDATA_PREFIX = "H://Program Files (x86)//Tesseract-OCR"
tessdata_dir_config = (
    '--tessdata-dir "H:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'
)
"""
tessdata_dir_config = '--tessdata-dir "<replace_with_your_tessdata_dir_path>"'
# Example config: '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'
# It's important to include double quotes around the dir path.
pytesseract.image_to_string(image, lang='chi_sim', config=tessdata_dir_config)

"""


def get_string(img_path):
    img = cv2.imread(img_path)

    # IMAGE CONDITIONING
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    kernel = np.ones((5, 5), np.uint8)
    # img=cv2.dilate(img,kernel,iterations=1)
    # img=cv2.erode(img,kernel,iterations=1000)
    # img = cv2.dilate(img, kernel, iterations=50)
    # cv2.imwrite(src_path + "removed_noise.png",img)
    # print ("noise removal done")
    # THRESHOLDING
    # img= cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11,2)
    ret, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    # img = cv2.erode(img, kernel, iterations=1000)
    # img = cv2.dilate(img, kernel, iterations=50)

    cv2.imwrite(src_path + "thres1.png", img)

    img = cv2.dilate(img, kernel, iterations=2)
    cv2.imwrite(src_path + "thres2.png", img)

    """ laplacian = cv2.Laplacian(img, cv2.CV_64F)
    sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=7)
    sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)
    cv2.imwrite(src_path + "thres3.png", laplacian)
    cv2.imwrite(src_path + "thres4.png", sobelx)
    cv2.imwrite(src_path + "thres5.png", sobely)
    ret, img = cv2.threshold(sobelx, 127, 255, cv2.THRESH_BINARY_INV)
    cv2.imwrite(src_path + "thres6.png", img)"""
    print("thresh done")
    result = pytesseract.image_to_string(
        Image.open(src_path + "thres1.png"), lang="spa", config=tessdata_dir_config
    )
    # kt=Image.open(src_path+"thres.png")
    # os.remove(temp)
    return result


print("-----Start recognize text from image -----")
print(get_string(src_path + "Plain.jpg"))
print("-------DONE-------")
