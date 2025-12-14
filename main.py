import pandas as pd
import numpy as np
import cv2

img = cv2.imread('images/Screenshot 2025-12-09 173308.png')
row,column,channel = img.shape
pt1=(100,280)
pt2=(370,row-1)
color = (255,0,0)
thickness = 1
cv2.rectangle(img,pt1,pt2,color,thickness)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()