import cv2 as cv
import numpy as np

#Create blank image using Numpy
blank = np.zeros((500,500,3),dtype='uint8')

# Paint the image with certain colour
#blank[:] = 0,255,0
#cv.imshow("Green",blank)

#Colour a certain range of image by mapping the pixels
#blank[200:300 , 300:400] = 0,0,464
#cv.imshow("Range Pixel" , blank)

#Draw a rectangle in a the image
#cv.rectangle(blank,(0,0),(250,250),(0,255,0),thickness=2)
#cv.imshow('Rectangle',blank)
#cv.waitKey(0)

#cv.rectangle(blank,(0,0),(blank.shape[1]//2 , blank.shape[0]//2), (0,255.0),thickness=-1)
#cv.imshow('Rectangle',blank)
#cv.waitKey(0)

#Put text in a blank image
cv.putText(blank,'Hello,My name is Pranav',(50,255),cv.FONT_HERSHEY_TRIPLEX , 1.0 , (0,255.0), thickness=2)
cv.imshow('Hello',blank)
cv.waitKey(0)