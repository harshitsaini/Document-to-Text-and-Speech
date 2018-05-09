import os
import sys
import cv2
from PIL import Image
from pytesseract import *
import numpy as np
import pytesseract

src_path= 'C://Users//Harshit//Desktop//Machine Learning//Image Analysis//Output Images//Machine Printed//Document Bucket//'
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
ex_fl= "" ; new_path="" ; block_path="" ; line_path=""
def getThresholded(img,smooth_it):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    if smooth_it==True:
        kernel = np.ones((10, 10), np.float32) / 100
        smooth = cv2.filter2D(img, -1, kernel)
        cv2.imwrite(new_path+ "smoothened.png", smooth)
        img=smooth
    threshed = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 151, 0)
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
    #kernel = np.ones((kernel_size, kernel_size), np.uint8)
    '''ones = np.array([0, 1, 0])
    zeroes = np.array([0, 1, 0])
    #kernel = np.uint8(ones)
    kernel= np.array([0, 1, 0])
    # ones=np.ones(3,np.uint8)
    # zeroes=np.zeros(3,np.uint8)
    np.concatenate((kernel, ones), axis=1)zzz
    np.concatenate((kernel, zeroes), axis=1)'''
    kernel= np.array([[0,0,0],[1,1,1],[0,0,0]])

    dilated = cv2.dilate(img, kernel, iterations=iterations)
    cv2.imwrite(new_path + "dilated.png", dilated)
    return dilated

def get_blocks(img_path):
    ###########################CANNY EDGE DETECTION ###################################
    print(img_path)
    img = cv2.imread(img_path)
    #print(img.dim)
    edges = cv2.Canny(img, 100, 200)
    cv2.imwrite(new_path + 'canny.png', edges)
    #cv2.imshow('Edges',edges)
    ##############################DEFINING CONTOURS####################################
    conditioned = getMorph(edges, 3, 5, False)
    final= conditioned
    [a, contours, c] = cv2.findContours(final, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #[a, contours, c] = cv2.findContours(final, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    print("No of text blocks detected are blocks :"+str(len(contours)))

    cv2.drawContours(img, contours, -1, (0, 255, 0), 2)
    it=1
    for npaContour in contours:
        [intX, intY, intW, intH] = cv2.boundingRect(npaContour)
        #cv2.rectangle(img,(intX, intY),(intX+intW,intY+intH),(0, 0, 255),2)

        imgROI = np.asarray(img[intY:intY+intH, intX:intX+intW])
        cv2.imshow('block',imgROI)
        intChar = cv2.waitKey(0)
        if not os.path.exists(new_path+'block'+str(it)+'//'):
            os.makedirs(new_path+'block'+str(it)+'//')
        cv2.imwrite(new_path+'block'+str(it)+'//'+'block.png', imgROI)
        it+=1

    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    ###################################################################################

    #cv2.imwrite(src_path+ex_fl+'final.png',final)
    print('Blocks Extracted !')
    #result= pytesseract.image_to_string(Image.open(src_path+ex_fl+'final.png'),lang='spa', config=tessdata_dir_config)
    #os.remove(temp)
    return len(contours)

def get_lines(img_path):
    kt=""
    ###########################CANNY EDGE DETECTION ###################################
    img = cv2.imread(img_path)
    edges = cv2.Canny(img, 100, 200)
    cv2.imwrite(new_path + 'canny.png', edges)
    cv2.imshow('Edges',edges)
    ##############################DEFINING CONTOURS####################################
    #conditioned = getMorph(edges, 1, 3, False)
    conditioned= horizontal_dilation(edges,9,9)

    final= conditioned
    #[a, contours, c] = cv2.findContours(final, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    [a, contours, c] = cv2.findContours(final, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    print("No of text lines detected from this block are:"+str(len(contours)))
    #cv2.drawContours(img, contours, -1, (0, 255, 0), 2)
    it=1
    for npaContour in contours:
        [intX, intY, intW, intH] = cv2.boundingRect(npaContour)
        #cv2.rectangle(img,(intX, intY),(intX+intW,intY+intH),(0, 0, 255),2)

        imgROI = np.asarray(img[intY:intY+intH, intX:intX+intW])
        cv2.imshow('line',imgROI)
        cv2.waitKey(5000)
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

new_path= src_path+"Driving Document//"
#new_path= src_path+ "Medical Report//"
#new_path= src_path+ "Milstein-backing//"
#new_path= src_path+ "Restraining_Order//"
#new_path= src_path+ "Wachovia_bank_statement//"
#new_path= src_path+ "Handwritten Recognition Using SVM, KNN and Neural Network//"
#new_path= src_path+ "ID CARD//"
#new_path= src_path+ "OCR_DOC//"

print('\n-----Start recognize text blocks from image -----')
ltn= get_blocks(new_path+"Driving_Document.png")                                           #Perfecta
#ltn= get_blocks(new_path+"MEDICAL-REPORT.png")                                             #Have some redundancies
#ltn= get_blocks(new_path+"milstein-backing.png")                                           #Too much noise
#ltn= get_blocks(new_path+"Restraining_Order.png")
#ltn= get_blocks(new_path+"Wachovia_National_Bank_1906_statement.png")                      #needs normalization
#ltn= get_blocks(new_path+"Handwritten Recognition Using SVM, KNN and Neural Network.png")  #again normailzation
#ltn= get_blocks(new_path+"opened.png")                                                      #NEEDS normalization and noise removal
#ltn= get_blocks(new_path+"OCR_DOC.png")                                                      #NEEDS normalization and noise removal

print("-------DONE-------\n\n")
answer= ""
print('-----Start recognize Lines from block -----')
'''for it in range(1,ltn+1):
    new_path = src_path +"Driving Document//block"+str(it)+'//'
    #new_path = src_path +"Medical Report//block"+str(it)+'//'
    #new_path= src_path+ "Milstein-backing//block"+str(it)+'//'z
    #new_path = src_path + "Restraining_Order//block" + str(it) + '//'
    #new_path = src_path + "Wachovia_bank_statement//block" + str(it) + '//'
    #new_path = src_path + "Handwritten Recognition Using SVM, KNN and Neural Network//block" + str(it) + '//'
    #new_path = src_path + "ID CARD//block" + str(it) + '//'
    #new_path = src_path + "OCR_DOC//block" + str(it) + '//'
    #answer+=get_lines(new_path+'block.png')
print("-------Lines Extracted-------\n\n")

print(answer)'''

'''f = open('OutputText.txt','w')
f.write(answer)
f.close()'''