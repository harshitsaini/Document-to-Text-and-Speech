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
'''
    tessdata_dir_config = '--tessdata-dir "<replace_with_your_tessdata_dir_path>"'
    # Example config: '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'
    # It's important to include double quotes around the dir path.
    pytesseract.image_to_string(image, lang='chi_sim', config=tessdata_dir_config)
'''

#if not os.path.exists(directory):
    #os.makedirs(directory)

answer=""
line_image_bucket=[]
ex_fl= "" ; new_path="" ; block_path="" ; line_path=""
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

def get_blocks(img_path):
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

def get_lines(img_path): ### getting lines out of a block
    kt=""
    print(img_path)
    ###########################CANNY EDGE DETECTION ###################################
    img = cv2.imread(img_path)
    print(img.shape)
    thresholded= getThresholded(img,smooth_it=True)
    opened= getOpened(thresholded,iterations=1,kernel_size=3)
    edges = cv2.Canny(opened, 100, 200)
    cv2.imwrite(new_path + 'canny.png', edges)
    #cv2.imshow('Edges',edges)
    ##############################DEFINING CONTOURS####################################
    #conditioned = getMorph(edges, 1, 3, erode_it=False)
    conditioned= horizontal_dilation(edges,15,15)
    final= conditioned

    #[a, contours, c] = cv2.findContours(final, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    [a, contours, c] = cv2.findContours(final, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    print("No of text lines detected from this block are:"+str(len(contours)))
    #cv2.drawContours(img, contours, -1, (0, 255, 0), 1)
    #cv2.imshow("LINED CONTOURS",img)
    #cv2.waitKey(5000)

    it=1
    for npaContour in contours:
        [intX, intY, intW, intH] = cv2.boundingRect(npaContour)
        #cv2.rectangle(img,(intX, intY),(intX+intW,intY+intH),(0, 0, 255),2)

        imgROI = np.asarray(img[intY:intY+intH, intX:intX+intW])
        line_image_bucket.append(imgROI)
        #cv2.imshow('line'+str(it),imgROI)
        #cv2.waitKey(3000)
        if not os.path.exists(new_path+'line'+str(it)+'//'):
            os.makedirs(new_path+'line'+str(it)+'//')
        cv2.imwrite(new_path+'line'+str(it)+'//'+'line.png', imgROI)
        result = pytesseract.image_to_string(Image.open(new_path+'line'+str(it)+'//'+'line.png'), lang='eng', config=tessdata_dir_config)
        kt= kt+" "+result
        it+=1

    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    ###################################################################################
    #os.remove(temp)
    return kt

#new_path= src_path+"IOT(T-1)2018//"
new_path= src_path+"OS (T-1)2011//"
#new_path= src_path+"OS(T-1)2013//"

print('\n-----Start recognize text blocks from image -----')
#ltn= get_blocks(new_path+"IOT(T-1)2018-1.png")
ltn= get_blocks(new_path+"OS (T-1)2011-1.png")
#ltn= get_blocks(new_path+"OS(T-1)2013-2.png")

print("-------DONE-------\n\n")
answer= ""
print('-----Start recognize Lines from block -----')
for it in range(1,ltn+1):
    #new_path = src_path +"IOT(T-1)2018//block"+str(it)+'//'
    new_path = src_path +"OS (T-1)2011//block"+str(it)+'//'
    #new_path = src_path +"OS(T-1)2013//block"+str(it)+'//'
    answer+=get_lines(new_path+'block.png')
print("-------Lines Extracted-------\n\n")

from pprint import pprint

' '.join(answer.split())

pprint(answer)

with open('output_text.txt','w') as file:
	for data in answer:
		file.write(data)
	file.close()

new_cwd= src_path+'OS (T-1)2011//Overall Line Bucket//'

if not os.path.exists(new_cwd):
            os.makedirs(new_cwd)
os.chdir(new_cwd)
for line_id in range(len(line_image_bucket)):
	cv2.imwrite("line"+str(line_id+1)+".png", line_image_bucket[line_id])