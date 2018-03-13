import cv2
import numpy as np
src_path= 'C://Users//Harshit//Desktop//Initial_img//'
img = cv2.imread(src_path+'thres.png')
edges = cv2.Canny(img,100,200)
cv2.imwrite(src_path+'canny.png',edges)
cv2.imshow(edges)