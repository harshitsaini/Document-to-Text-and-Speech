from os.path import join, exists
from pytesseract import *
from os import makedirs
from . import utilities
from PIL import Image
import numpy as np
import pytesseract
import cv2


# Function to apply edge detection
def edgeDetection(img, output_path):

	# Application of thresholding on given image
	thresholded = utilities.getThresholded(img, smooth_it = True)

	# Application of morphological opening
	opened      = utilities.getOpened(thresholded,
	                                  iterations  = 1,
	                                  kernel_size = 3)

	# Application of canny edge detection on thresholded image
	edges       = cv2.Canny(opened, 100, 200)

	# cv2.imwrite(join(output_path, 'canny.png'), edges)

	return edges


# Function to get blocks out of image document
def getBlocks(image_path, output_path):

	img = cv2.imread(image_path)

	##############################DEFINING CONTOURS####################################
	edges = edgeDetection(img, output_path)

	# Application of morphological dilation
	conditioned = utilities.getMorph(img = edges, iterations = 5,
	                       kernel_size = 7, erode_it = False)

	final = conditioned.copy()

	# Generation of contours 
	contours, a = cv2.findContours(final,
	                                    cv2.RETR_EXTERNAL,
	                                    cv2.CHAIN_APPROX_SIMPLE)

	# print("No of text blocks detected are blocks :" + str(len(contours)))

	# Iterating over all mapped contours
	for idx, npaContour in enumerate(contours):
		[intX, intY, intW, intH] = cv2.boundingRect(npaContour)

		# Creating a bounding rectangle for a given contour
		img = cv2.rectangle(img, (intX, intY), 
		              (intX+intW,intY+intH), (0, 0, 255), 1)

		# Capturing region of interest
		imgROI = np.asarray(img[intY:intY + intH, intX:intX + intW])

		if not exists(join(output_path, 'block' + str(idx + 1))):
			makedirs(join(output_path, 'block' + str(idx + 1)))

		cv2.imwrite(join(output_path ,'block' + str(idx + 1),'block.png'), imgROI)

	###################################################################################
	# print('------- Blocks Extracted -------\n\n')
	return len(contours)


# Function to extracts lines out of given block
def getLines(image_path, output_path): 
	kt  = []

	img = cv2.imread(image_path)

	edges = edgeDetection(img, output_path)

	conditioned = utilities.horizontal_dilation(edges, 15)

	final       = conditioned.copy()

	# Generation of contours 
	contours, a = cv2.findContours(final, 
                                   cv2.RETR_EXTERNAL,
                                   cv2.CHAIN_APPROX_SIMPLE)

	# print("No. of text lines detected from" + \
	#       " this block are:" + str(len(contours)))

	# Iterating over all mapped contours
	for idx, npaContour in enumerate(contours):
		[intX, intY, intW, intH] = cv2.boundingRect(npaContour)

		imgROI = np.asarray(img[intY:intY+intH, intX:intX+intW])

		if not exists(join(output_path, 'line' + str(idx + 1))):
		    makedirs(join(output_path, 'line' + str(idx + 1)))
		cv2.imwrite(join(output_path, 'line' + str(idx + 1), 'line.png'), imgROI)

		result = pytesseract.image_to_string(imgROI)

		kt.append(result)

		kt = kt[::-1]

	###################################################################################
	return '\n'.join(kt)


# Function to perform Optical Character recognition
def performRecognition(doc_path, output_path, docName):

	image_path  = join(doc_path, docName)

	output_path = join(output_path, 'd2sData')

	# print('\n-----Start recognizing text blocks from image -----\n\n')
	ltn = getBlocks(image_path  = image_path,
	                output_path = output_path)

	# print("-------DONE-------\n\n")

	answer = []

	# print('-----Start extracting lines from blocks -----\n\n')
	for it in range(ltn):
		new_output_path = join(output_path, "block" + str(it + 1))
		answer.append(
		    getLines(join(new_output_path, 'block.png'),
		    new_output_path))
	# print("------- Lines Extracted -------\n\n")

	answer = answer[::-1]
	answer = '\n\n'.join(answer)
	# print(answer)

	with open(join(output_path,
	          docName.strip('.png').strip('jpg').strip('.tif') + ".txt"), 'w') as file:
		for data in answer:
			file.write(data)
		file.close()

	print('------TEXT DOCUMENT SUCCESSFULLY GENERATED-------\n\n')

	return ltn