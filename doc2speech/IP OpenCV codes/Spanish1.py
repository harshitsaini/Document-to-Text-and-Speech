import sys
import cv2
from PIL import Image
from pytesseract import *
import numpy as np
import pytesseract

src_path= 'C://Users//Harshit//Desktop//Machine Learning//Image Analysis//Output Images//Machine Printed//Spanish Images//Spanish1//'
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
    #print(img.dim)
 # IMAGE CONDITIONING
    img= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

 # THRESHOLDING
    #ret, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    #ret, img = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)
    img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
    cv2.imwrite(src_path+'thresholded.png',img)

    result= pytesseract.image_to_string(Image.open(src_path+'thresholded.png'),lang='spa', config=tessdata_dir_config)
    #kt=Image.open(src_path+"thres.png")
    #os.remove(temp)
    return result

print('-----Start recognize text from image -----')
print(get_string(src_path+ "span1_img.png"))
print("-------DONE-------")