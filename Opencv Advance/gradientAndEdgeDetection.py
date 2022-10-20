import cv2 as cv
import numpy as np

image = cv.imread('../Images/dog.jpg')
cv.imshow('Normal Image', image)

gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow('Gray image', gray_image)

# 1. laplacian edge detection method
lap = cv.Laplacian(gray_image, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian edges', lap)

# 2. sobel edge detection method.
# sobel computes gradient in two direction x and y
sobelx = cv.Sobel(gray_image, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray_image, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobelx, sobely)
cv.imshow('SobelX', sobelx)
cv.imshow('SobelY', sobely)
cv.imshow('Combined Sobel', combined_sobel)

# 3. canny edge detection method
canny = cv.Canny(gray_image, 150, 175)
cv.imshow('Canny Edges', canny)

cv.waitKey(0)
