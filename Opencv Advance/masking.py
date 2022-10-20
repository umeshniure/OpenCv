# using bitwise, we can perform masking in open cv.
# masking allows us to focus on certain part of image we would like to focus on.
import cv2 as cv
import numpy as np

image = cv.imread('../Images/dog.jpg')
cv.imshow('Normal Image', image)

blank_image = np.zeros(image.shape[:2], dtype='uint8')
cv.imshow('blank Image', blank_image)

mask = cv.circle(blank_image, (image.shape[1] // 2 + 40, image.shape[0] // 2 - 45), 100, 255, -1)
cv.imshow('Masking', mask)

masked_img = cv.bitwise_and(image, image, mask=mask)
cv.imshow('Masked image', masked_img)

cv.waitKey(0)
