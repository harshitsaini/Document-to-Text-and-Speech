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

def get_words(img_path):
    ###########################CANNY EDGE DETECTION ###################################
    img = cv2.imread(img_path)  ;        print(img.shape)
    img = cv2.resize(img, (1465,1737)) ; print(img.shape)
    thresholded= getThresholded(img,smooth_it=True)
    opened= getOpened(thresholded,iterations=1,kernel_size=3)
    edges = cv2.Canny(opened, 100, 200)
    cv2.imwrite(new_path + 'canny.png', edges)
    #cv2.imshow('Edges',edges)
    ##############################DEFINING CONTOURS####################################
    conditioned = getMorph(img=edges, iterations=5, kernel_size=7, erode_it=False)
    final= conditioned
    #[a, contours, c] = cv2.findContours(final, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    [a, contours, c] = cv2.findContours(final, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    print("No of text blocks detected are blocks :"+str(len(contours)))

    #cv2.drawContours(img, contours, -1, (0, 255, 0), 2)
    it=1
    for npaContour in contours:
        [intX, intY, intW, intH] = cv2.boundingRect(npaContour)
        cv2.rectangle(img,(intX, intY),(intX+intW,intY+intH),(0, 0, 255),1)

        imgROI = np.asarray(img[intY:intY+intH, intX:intX+intW])
        #cv2.imshow('block',imgROI)
        #intChar = cv2.waitKey(3500)
        if not os.path.exists(new_path+'block'+str(it)+'//'):
            os.makedirs(new_path+'block'+str(it)+'//')
        cv2.imwrite(new_path+'block'+str(it)+'//'+'block.png', imgROI)
        it+=1    
    ###################################################################################
    print('Blocks Extracted !')
    return len(contours)



if __name__ == "__main__":


	#####   Defining Working Directory  #####
	old_cwd= os.getcwd()
	new_cwd= src_path+'OS (T-1)2011//Overall Line Bucket//'

	if not os.path.exists(new_cwd):
		os.makedirs(new_cwd)
	os.chdir(new_cwd)

	print("Working Directory changed from "+old_cwd+ " to "+new_cwd)

	##### Extracting upper limit of number of lines in whole document #####
	Max_line_number=1
	with open("Max_line_number.txt") as file:
		Max_line_number= int(str(file.read()).strip())
	print("Max_line_number is: "+str(Max_line_number))

	word_number_bucket=[]


	##### Extracting words from lines #####
	for it in range(Max_line_number):
		word_count= new_cwd+'line'+str(it+1)+'.png'
		word_number_bucket.append(get_words(word_count)

	cnt=0

	Total_words= [cnt+=x for x in word_number_bucket]
	print("Total number of words in whole document are:"+str(Total_words))








