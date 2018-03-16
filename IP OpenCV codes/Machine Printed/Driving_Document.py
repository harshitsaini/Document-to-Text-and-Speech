import sys
import cv2
from PIL import Image
from pytesseract import *
import numpy as np
import pytesseract

src_path= 'C://Users//Harshit//Desktop//Machine Learning//Image Analysis//Output Images//Machine Printed//Document Bucket//'
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

ex_fl= ""

def getThresholded(img,smooth_it):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    if smooth_it==True:
        kernel = np.ones((10, 10), np.float32) / 100
        smooth = cv2.filter2D(img, -1, kernel)
        cv2.imwrite(src_path +ex_fl+ "smoothened.png", smooth)
        img=smooth
    threshed = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 151, 0)
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
    #print(type(img))
    '''conditioned = getThresholded(img,True)#Dont know why i was smoothing my grayscale pic !!!???
    #conditioned = getMorph(conditioned,1,3,False)
    conditioned=getClosed(conditioned,3,3)
    final = conditioned'''
    ###########################CANNY EDGE DETECTION ###################################
    img = cv2.imread(src_path + ex_fl + "Driving_Document.png")
    edges = cv2.Canny(img, 100, 200)
    cv2.imwrite(src_path + 'canny.png', edges)
    cv2.imshow('Edges',edges)
    ##############################DEFINING CONTOURS####################################
    conditioned = getMorph(edges, 3, 5, False)
    final= conditioned

    [a, contours, c] = cv2.findContours(final, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    print(len(contours))

    cv2.drawContours(img, contours, -1, (0, 255, 0), 2)

    #print(contours[0])
    inf= 1000000000000

    txt_cdts=[]
    txt_blocks=[]
    for it in contours:
        Min = [inf, inf]
        Max = [-inf, -inf]
        for kt in it:
           Max[0]= max(it[0], Max[0])
           Max[1]= max(it[1], Max[1])
           Min[0] = min(it[0], Min[0])
           Min[1] = min(it[1], Min[1])
        txt_cdts.append(Min,Max)

    print(contours[0])
    #cv2.imshow('threshed', final)
    #cv2.imshow('oh yeah', img)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    ###################################################################################

    cv2.imwrite(src_path+ex_fl+'final.png',final)
    print('Conditioning Done !')
    result= pytesseract.image_to_string(Image.open(src_path+ex_fl+'final.png'),lang='spa', config=tessdata_dir_config)
    #os.remove(temp)
    return result

ex_fl= "Driving Document//"
print('-----Start recognize text from image -----')
print(get_string0(src_path+ex_fl+"Driving_Document.png"))
print("-------DONE-------\n\n")

