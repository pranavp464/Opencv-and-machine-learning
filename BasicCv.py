import cv2 as cv

img = cv.imread('Photos/park.jpg')
cv.imshow('Original',img)

#Convert an image into greyscale
grey = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Grey',grey)

#Blur a image
blur =cv.GaussianBlur(img , (3,3) , cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

# Egde Cascade
cany = cv.Canny(img,125,175)
cv.imshow('cany',cany)

#Dilating the image
dilated = cv.dilate(cany,(3,3),iterations=1)
cv.imshow('Dilated',dilated)

#Eroding
eroded =  cv.erode(dilated,(3,3),iterations=1)
cv.imshow('Eroded',eroded)

#Reize
resized = cv.resize(img,(500,500))
cv.imshow('resized',resized)

#Cropping
cropped = img[50:200, 200:500]
cv.imshow('Cropped',cropped)

cv.waitKey(0)