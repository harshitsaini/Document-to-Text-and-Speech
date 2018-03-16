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

#if not os.path.exists(directory):
    #os.makedirs(directory)


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

def get_blocks(img_path):
    img=cv2.imread(img_path)
    ###########################CANNY EDGE DETECTION ###################################
    img = cv2.imread(src_path + ex_fl + "Driving_Document.png")
    edges = cv2.Canny(img, 100, 200)
    cv2.imwrite(src_path + 'canny.png', edges)
    #cv2.imshow('Edges',edges)
    ##############################DEFINING CONTOURS####################################
    conditioned = getMorph(edges, 3, 5, False)
    final= conditioned
    #[a, contours, c] = cv2.findContours(final, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    [a, contours, c] = cv2.findContours(final, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    print("No of text blocks detected are blocks "+str(len(contours)))

    #cv2.drawContours(img, contours, -1, (0, 255, 0), 2)
    it=1
    for npaContour in contours:
        [intX, intY, intW, intH] = cv2.boundingRect(npaContour)
        cv2.rectangle(img,(intX, intY),(intX+intW,intY+intH),(0, 0, 255),2)

        imgROI = np.asarray(img[intY:intY+intH, intX:intX+intW])
        #cv2.imshow('block',imgROI)
        #intChar = cv2.waitKey(0)
        cv2.imwrite(src_path + ex_fl + 'blocks//block'+str(it)+'.png', imgROI)
        it+=1

    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    ###################################################################################

    cv2.imwrite(src_path+ex_fl+'final.png',final)
    print('Blocks Extracted !')
    #result= pytesseract.image_to_string(Image.open(src_path+ex_fl+'final.png'),lang='spa', config=tessdata_dir_config)
    #os.remove(temp)
    return len(contours)

def get_words(img_path):
    
    img=cv2.imread(img_path+'.png')
    ###########################CANNY EDGE DETECTION ###################################
    img = cv2.imread(img_path+ ".png")
    edges = cv2.Canny(img, 100, 200)
    cv2.imwrite(img_path + 'canny.png', edges)
    #cv2.imshow('Edges',edges)
    ##############################DEFINING CONTOURS####################################
    conditioned = getMorph(edges, 3, 5, False)
    final= conditioned
    #[a, contours, c] = cv2.findContours(final, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    [a, contours, c] = cv2.findContours(final, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    print('This block have'+ str(len(contours)) +'characters')

    #cv2.drawContours(img, contours, -1, (0, 255, 0), 2)
    it=1
    for npaContour in contours:
        [intX, intY, intW, intH] = cv2.boundingRect(npaContour)
        cv2.rectangle(img,(intX, intY),(intX+intW,intY+intH),(0, 0, 255),2)

        imgROI = np.asarray(img[intY:intY+intH, intX:intX+intW])
        #cv2.imshow('block',imgROI)
        #intChar = cv2.waitKey(0)
        cv2.imwrite(img_path+ 'character'+str(it)+'.png', imgROI)
        it+=1

    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    ###################################################################################

    #cv2.imwrite(src_path+ex_fl+'final.png',final)
    #result= pytesseract.image_to_string(Image.open(src_path+ex_fl+'final.png'),lang='spa', config=tessdata_dir_config)
    #os.remove(temp)
    return len(contours)

ex_fl= "Driving Document//"
print('-----Start recognize text from image -----')
#print(get_string0(src_path+ex_fl+"Driving_Document.png"))
ltn= get_string0(src_path+ex_fl+"Driving_Document.png")
print("-------DONE-------\n\n")

ex_fl= "Driving Document//blocks//"
print('-----Start recognize text from image -----')
for it in range(1,ltn+1):
    get_string1(src_path+ex_fl+'block'+str(it))
    print("-------Characters Extracted-------\n\n")

