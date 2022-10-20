# every color image consist of different color channel
# RGB image contains red color channel, green color channel, and blue color channel
import cv2 as cv
import numpy as np

image = cv.imread('../Images/dog.jpg')
cv.imshow('Normal Image', image)

blank_image = np.zeros(image.shape[:2], dtype='uint8')

# splitting BGR image to their respective B, G, R color channel
blue_image, green_image, red_image = cv.split(image)

blue = cv.merge([blue_image, blank_image, blank_image])
green = cv.merge([blank_image, green_image, blank_image])
red = cv.merge([blank_image, blank_image, red_image])

# cv.imshow('Blue image', blue_image)
# cv.imshow('Green image', green_image)
# cv.imshow('Red image', red_image)

cv.imshow('Blue image', blue)
cv.imshow('Green image', green)
cv.imshow('Red image', red)

# Displaying Shape (h, w, color channel) of above splitted images
print(image.shape)
print(blue_image.shape)
print(green_image.shape)
print(red_image.shape)

# Merging those splitted imaged
merged_image = cv.merge([blue_image, green_image, red_image])
cv.imshow('Merged image', merged_image)

cv.waitKey(0)
