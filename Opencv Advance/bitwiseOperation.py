import cv2 as cv
import numpy as np

# four bitwise operators OR, AND, XOR, NOT

blank = np.zeros((400, 400), dtype='uint8')
rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
circle = cv.circle(blank.copy(), (200, 200), 200, 255, -1)

cv.imshow('Rectangle', rectangle)
cv.imshow('circle', circle)

# Bitwise AND operator --> intersecting region only
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('bitwise_AND', bitwise_and)

# Bitwise OR operator --> intersecting region and non intersection region
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('bitwise_OR', bitwise_or)

# Bitwise XOR operator --> non intersection region
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('bitwise_XOR', bitwise_xor)

# Bitwise NOT operator
bitwise_not = cv.bitwise_not(circle)
cv.imshow('bitwise_NOT', bitwise_not)

cv.waitKey(0)
