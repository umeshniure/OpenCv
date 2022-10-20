import cv2 as cv
import numpy as np

# Generating a blank image
# we pass height, width, no. of color channel, and datatype as parameter in np.zeros()
blank_img = np.zeros((500, 500, 3), dtype='uint8')
# cv.imshow('Blank', blank_img)


# 1. paint the image a certain color
blank_img[:] = 0, 255, 0  # green color
cv.imshow('Green', blank_img)

# paint the certain pixels only
blank_img[200:300, 300:400] = 0, 0, 255  # red color
cv.imshow('Green', blank_img)

# 2. draw a rectangle.
# rectangle() method takes following parameter
# rectangle(img, pt1, pt2, color, thickness=None, lineType=None, shift=None)
# possible thickness value: thickness=2, thickness=cv.FILLED -> thickness = -1

# cv.rectangle(blank_img, (0, 0), (250, 250), (255, 255, 0), thickness=-1)
cv.rectangle(blank_img, (0, 0), (blank_img.shape[1] // 2, blank_img.shape[0] // 2), (255, 255, 0), thickness=-1)
cv.imshow('Drawing Rectangle', blank_img)

# 3. draw a circle.
# circle() method take following parameter: circle(image, center, radius, color, thickness, lineType, shift)
cv.circle(blank_img, (blank_img.shape[1] // 2, blank_img.shape[0] // 2), 50, (0, 0, 255), thickness=2)
cv.imshow('Drawing Circle', blank_img)

# 4. Draw a line.
# line() method parameters: line(image, point1, point2, color, thickness, lineType, shift)
cv.line(blank_img, (0, 0), (blank_img.shape[1] // 2, blank_img.shape[0] // 2), (0, 255, 0), thickness=2)
cv.imshow('Drawing Line', blank_img)

# 5. Write text on an image
cv.putText(blank_img, 'Umesh Niure', (200, 200), cv.FONT_HERSHEY_TRIPLEX, 1.0, (123, 234, 255), thickness=2)
cv.imshow('Text on image', blank_img)

cv.waitKey(0)
