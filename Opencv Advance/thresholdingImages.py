# thresholding is the binarization of the image
# take an image and convert it to binary image
# ie. image where pixels are eiter 0, or 255, 0r white
# simple thresholding or adaptive thresholding
import cv2 as cv
import numpy as np

image = cv.imread('../Images/dog.jpg')
cv.imshow('Normal Image', image)

gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow('Gray image', gray_image)

# Simple thresholding
# threshold() only accepts gray image
threshold, thresh = cv.threshold(gray_image, 150, 255, cv.THRESH_BINARY)
cv.imshow('Threshold image', thresh)

threshold, thresh_inverse = cv.threshold(gray_image, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Inverse of threshold image', thresh_inverse)

# adaptive threshold
adaptive_threshold = cv.adaptiveThreshold(gray_image, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow('Adaptive thresholding', adaptive_threshold)

cv.waitKey(0)
