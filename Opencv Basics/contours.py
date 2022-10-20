# in general term, contours are similar to edges but from mathematics point of view, contours and edges are different.
# Contours are useful tools when we get into shape analysis and object detection and recognition

import cv2 as cv
import numpy as np

image = cv.imread('../Images/dog.jpg')
cv.imshow('Normal Image', image)

blank_image = np.zeros(image.shape, dtype='uint8')
cv.imshow('Blank Image', blank_image)

gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow('Gray image', gray_image)

blurred_gray_image = cv.GaussianBlur(gray_image, (3, 3), cv.BORDER_DEFAULT)
cv.imshow('Blurred image', blurred_gray_image)

# grab edges of images using canny
canny_image = cv.Canny(blurred_gray_image, 125, 175)
cv.imshow('Canny image', canny_image)

# another method of detecting contours instead of using canny
# threshold() looks for an image and tries to binarize it
ret, threshold = cv.threshold(gray_image, 125, 255, cv.THRESH_BINARY)
cv.imshow('Threshold image', threshold)

# here, variable contours is a python list of all the coordinates of the contours found on the images variable
# hierarchies represents the hierarchy of the contours RETR_LIST returns all the contours in the image,
# RETR_EXTERNAL returns only external contours, RETR_TREE return all the hierarchical contours
# CHAIN_APPROX_NONE is a contour approximation method. (How we want to approximate the contours.)
# CHAIN_APPROX_SIMPLE essentially compresses all the contours returned

contours, hierarchies = cv.findContours(canny_image, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
# contours, hierarchies = cv.findContours(threshold, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')

# drawing the contours found in the image on the blank image
cv.drawContours(blank_image, contours, -1, (0, 0, 255), thickness=1)
cv.imshow('Contours drawn', blank_image)

cv.waitKey(0)
