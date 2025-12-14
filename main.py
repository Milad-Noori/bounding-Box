import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import cv2

# img = cv2.imread('images/Screenshot 2025-12-09 173308.png')
# row,column,channel = img.shape
# pt1=(100,280)
# pt2=(370,row-1)
# color = (255,0,0)
# thickness = 1
# cv2.rectangle(img,pt1,pt2,color,thickness)
# cv2.imshow('img',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()




# -----------------------------------------------------------------------------------------


# img = cv2.imread('images/Screenshot 2025-12-09 173308.png')
# row,column,channel = img.shape
# pt1=(100,280)
# pt2=(370,row-10)
# color = (128/255,128/255,128/255 )
# thickness = 1
# img =cv2.normalize(img,None,0,1,norm_type=cv2.NORM_MINMAX ,dtype=cv2.CV_32F)
# mask = np.zeros_like(img)
# cv2.rectangle(mask,pt1,pt2,color,thickness=-1)
# img = img+ 0.2 * mask
# cv2.imshow('img',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# --------------------------------------------------------------------------------------

img = np.zeros((500,500,3),dtype="uint8")
center = (250,250)
radius = 100
color = (0,0,255)
thickness = 1
cv2.circle(img, center, radius, color, thickness)

img1 = np.zeros((500,500,3),dtype="uint8")
center1 = (250,250)
radius1 = 200
color1 = (255,0,0)
thickness1 = 1
cv2.circle(img1, center1, radius1, color1, thickness1)

img2 = np.zeros((500,500,3),dtype="uint8")
center2 = (20,50)
radius2 = 50
color2 = (180,180,180)
thickness2 = 1
cv2.circle(img2, center2, radius2, color2, thickness2)

img3 = img1+img2+img
plt.imshow(img3)
plt.show()


