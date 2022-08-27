import cv2
import numpy as np

src_path = "C://Users//Harshit//Desktop//Machine Learning//Image Analysis//Output Images//Machine Printed//Document Bucket//"
ex_fl = "Driving Document//"
img = cv2.imread(src_path + ex_fl + "Driving_Document.png")
edges = cv2.Canny(img, 100, 200)
cv2.imwrite(src_path + "canny.png", edges)
# cv2.imshow(edges)
