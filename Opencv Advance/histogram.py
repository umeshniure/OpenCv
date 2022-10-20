# histogram allows us to visualize the pixel intensities of in an image.
# kind of graph or a plot that give us high level intuition of pixel distribution in an image.
# we can create histogram for grayscale and RGB images
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

image = cv.imread('../Images/cat2.jpg')
cv.imshow('Normal Image', image)

blank_image = np.zeros(image.shape[:2], dtype='uint8')

# gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray scaled image', gray_image)

# masking for BGR image
mask = cv.circle(blank_image, (image.shape[1] // 2, image.shape[0] // 2), 300, 255, -1)

masked = cv.bitwise_and(image, image, mask=mask)
cv.imshow('Masked image', masked)

# masking for Grayscaled image
# masked = cv.bitwise_and(gray_image, gray_image, mask=mask)
# cv.imshow('Masked image', masked)

# gray_histogram = cv.calcHist([gray_image], [0], mask, [256], [0, 256])
#
# plt.figure()
# plt.title('grayscale image histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# plt.plot(gray_histogram)
# plt.xlim([0, 256])
# plt.show()

# histogram of BGR color image
plt.figure()
plt.title('BGR color image histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
    hist = cv.calcHist([image], [i], mask, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])

plt.show()

cv.waitKey(0)
