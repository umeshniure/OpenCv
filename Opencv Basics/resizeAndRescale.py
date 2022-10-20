# we re-size and rescale to prevent computational strain
import cv2 as cv


def rescaleFrame(frame, scale=0.75):
    # this method os rescaling works for images, videos and live videos

    # frame.shape[0] represents height of frame
    height = int(frame.shape[0] * scale)
    # frame.shape[1] represents width of frame
    width = int(frame.shape[1] * scale)

    # creating tuple
    dimension = (width, height)
    # cv.resize() resizes a frame to a particular dimension
    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)


def changeResolution(height, width):
    # this method of rescaling works for live videos only
    capture.set(3, width)
    capture.set(4, height)


img = cv.imread('../Images/cat2.jpg')
resized_image = rescaleFrame(img)
# Display images in a new separate window
cv.imshow('cat', img)
cv.imshow('resized image', resized_image)
cv.waitKey(0)

capture = cv.VideoCapture('Videos/SampleVideo2.mp4')
# use while loop and read video frame by frame
while True:
    # capture.read() rads above video in capture frame by frame
    # isTrue represent boolean value if the video frame was read successfully or not
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame, scale=0.5)

    cv.imshow('SampleVideo', frame)
    cv.imshow('Resized video', frame_resized)

    # if keyboard letter d is pressed, exit out of loop
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
