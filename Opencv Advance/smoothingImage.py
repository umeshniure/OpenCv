import cv2 as cv
import numpy as np

image = cv.imread('../Images/dog.jpg')
cv.imshow('Normal Image', image)

# the first method of blurring
# 1. averaging
average_blurr_image = cv.blur(image, (7, 7))
cv.imshow('Average blurred', average_blurr_image)

# 2. gaussian blur
gaussian_blur_image = cv.GaussianBlur(image, (7, 7), 0)
cv.imshow('GaussianBlur image', gaussian_blur_image)

# median blur is effective in removing noise in the images
# 3. median blur
median_blur_image = cv.medianBlur(image, 7)
cv.imshow('Median blur image', median_blur_image)

# advance blur method, and used in advance image processing
# Bilateral blur
bilateral_image = cv.bilateralFilter(image, 5, 15, 15)
cv.imshow('Bilateral image', bilateral_image)





cv.waitKey(0)