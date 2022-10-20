import cv2 as cv
import numpy as np

image = cv.imread('../Images/dog.jpg')
cv.imshow('Normal Image', image)


# image translation
def translate(img, x, y):
    translation_matrix = np.float32([[1, 0, x], [0, 1, y]])
    image_dimension = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, translation_matrix, image_dimension)


# -x --> translate to left
# x --> translate to Right
# -y --> translate to up
# y --> translate to down

translated_image = translate(image, -100, 100)
cv.imshow('Translated image', translated_image)


# image Rotation
def rotate(img, angle, rotation_point=None):
    (height, width) = img.shape[:2]

    if rotation_point is None:
        rotation_point = (width // 2, height // 2)

    rotation_matrix = cv.getRotationMatrix2D(rotation_point, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotation_matrix, dimensions)


# -ve angle value for clockwise rotation
# _ve angle value for counter-clockwise rotation
rotated_image = rotate(image, -45, (200, 200))
cv.imshow('Rotated Image', rotated_image)

# resize an image
resized_img = cv.resize(image, (700, 700), interpolation=cv.INTER_LINEAR)
cv.imshow('Resized image', resized_img)

# Flipping an image
# flipCode (second parameter) --> 0 represents flipping vertically (X-axis)
# 1 represents flipping horizontally (y-Axis)
# -1 represents flipping both horizontally and vertically
flipped_image = cv.flip(image, -1)
cv.imshow('Flipped image', flipped_image)

# Cropping an image
cropped_image = image[0:200, 200:600]
cv.imshow('Cropped image', cropped_image)

cv.waitKey(0)
