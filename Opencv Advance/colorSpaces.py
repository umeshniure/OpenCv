# color space is basically space of colors. a system of representing an array of pixel colors.
# RGB is a kind of color space, grayscale is a kind of color space. LAB, HSV, are all color space.

import cv2 as cv
import matplotlib.pyplot as plt

image = cv.imread('../Images/dog.jpg')
cv.imshow('Normal Image', image)

plt.imshow(image)
plt.show()

# BGR to grayscale
grey_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow('Grey scaled image', grey_image)

# BGR to HSV (Hue Saturation Value)
hsv_image = cv.cvtColor(image, cv.COLOR_BGR2HSV)
cv.imshow('HSV image', hsv_image)

# BGR to LAB (or L*a*b)
lab_image = cv.cvtColor(image, cv.COLOR_BGR2LAB)
cv.imshow('LAB image', lab_image)

# BGR to RGB
rgb_image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
cv.imshow('RGB image', rgb_image)

# HSV to BGR
hsv_to_bgr = cv.cvtColor(hsv_image, cv.COLOR_HSV2BGR)
cv.imshow('HSV to BGR image', hsv_to_bgr)

# LAB to BGR
lab_to_bgr = cv.cvtColor(lab_image, cv.COLOR_Lab2BGR)
cv.imshow('LAB to BGR image', lab_to_bgr)

cv.waitKey(0)
