import cv2
import cv2 as cv

img = cv.imread('../Images/cat2.jpg')
cv.imshow('Cat image', img)

# # Converting to grayscale
# gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Greyscale image', gray_img)
#
# # blur an image
# # second parameter is a kernel size, and it should be odd number tuple / Blur strength
# blur_img = cv.GaussianBlur(img, (9, 9), cv.BORDER_DEFAULT)
# cv.imshow('Blur Image', blur_img)

# # Edge cascade /  find edges presented in an images
# canny_img = cv.Canny(img, 125, 175)
# cv.imshow('Canny image', canny_img)
#
# # dilating an image using specific structuring element
# dilated_img = cv.dilate(canny_img, (7, 7), iterations=2)
# cv.imshow('Dilated Image', dilated_img)
#
#
# # Eroding a dilated image
# eroded_img = cv.erode(dilated_img, (3, 3), iterations=1)
# cv.imshow('Eroded Dilated Image', eroded_img)

# resize an image
resized_img = cv.resize(img, (500, 500), interpolation=cv.INTER_AREA)
cv.imshow('Resized image', resized_img)

# Cropping an image
cropped_img = img[0:200, 200:600]
cv.imshow('Cropped image', cropped_img)


cv2.waitKey(0)
