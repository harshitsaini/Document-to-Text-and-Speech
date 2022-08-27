import cv2
import numpy as np

src_path = "C://Users//Harshit//Desktop//Initial_img//Handwritten&Cursive//Edge_detection&Gradiants//"
original = "7ab_original.jpg"
t = "thres.png"
t1 = "thres1.png"
img = cv2.imread(src_path + original)
"""laplacian = cv2.Laplacian(img, cv2.CV_64F)
sobelx = cv2.Sobel(img, cv2.CV_64F,1,0,ksize=5)
sobely = cv2.Sobel(img, cv2.CV_64F,0,1,ksize=5)"""

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
cv2.imwrite(src_path + "thresholded.png", img)

onek = np.ones(3, np.uint8)
zerok = np.zeros(3, np.uint8)

nkernel = np.array([onek, zerok, onek])

nimg = cv2.dilate(img, nkernel, iterations=11)
cv2.imwrite(src_path + "horizontal_erosion.png", nimg)
print(nkernel)

kernel = np.ones((5, 5), np.uint8)
img = cv2.dilate(img, kernel, iterations=3)
# cv2.imwrite(src_path + "dilated.png", img)

img = cv2.erode(img, kernel, iterations=5)
# cv2.imwrite(src_path + "eroded.png", img)

img = cv2.dilate(img, kernel, iterations=3)
# cv2.imwrite(src_path + "dilated.png", img)

img = cv2.erode(img, kernel, iterations=5)
# cv2.imwrite(src_path + "eroded.png", img)

img = cv2.dilate(img, kernel, iterations=3)
cv2.imwrite(src_path + "dilated.png", img)


img = cv2.erode(img, kernel, iterations=5)
cv2.imwrite(src_path + "eroded.png", img)


#############################SMOOTHENING OF IMAGE#####################################
kernel = np.ones((7, 7), np.float32) / 49
img = cv2.filter2D(img, -1, kernel)
cv2.imwrite(src_path + "smoothened.png", img)

"""INPUT= img
MASK = np.array(INPUT/255.0, dtype='float32')

MASK = cv2.GaussianBlur(MASK, (5,5), 11)
BG = np.ones([INPUT.shape[0], INPUT.shape[1], 1], dtype='uint8')*255

OUT_F = np.ones([INPUT.shape[0], INPUT.shape[1], 1],dtype='uint8')

for r in range(INPUT.shape[0]):
    for c in range(INPUT.shape[1]):
        OUT_F[r][c]  = int(BG[r][c]*(MASK[r][c]) + INPUT[r][c]*(1-MASK[r][c]))
cv2.imwrite('brain-out.png', OUT_F)"""
#######################################################################################

edges = cv2.Canny(img, 100, 100)

cv2.imwrite(src_path + "original.png", img)
"""cv2.imwrite(src_path+'laplacian.png',laplacian)
cv2.imwrite(src_path+'sobelx.png',sobelx)
cv2.imwrite(src_path+'sobely.png',sobely)"""
cv2.imwrite(src_path + "edges.png", edges)

"""cv2.imshow('original',img)
cv2.imshow('laplacian',laplacian)
cv2.imshow('sobelx',sobelx)
cv2.imshow('sobely',sobely)
k=cv2.waitKey(0)

cv2.destroyAllWindows()"""
