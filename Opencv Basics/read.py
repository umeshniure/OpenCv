import cv2 as cv

# reading images
img = cv.imread('../Images/cat2.jpg')

# cv.imshow() Display images in a new separate window
cv.imshow('cat', img)
cv.waitKey(0)

# Reading videos
# VideoCapture() method takes either integer values 0, 1, 2, etc. as a parameter or path to a video file
# use integer value to use our webcam or camera source
capture = cv.VideoCapture('../Videos/SampleVideo1.mp4')

# use while loop and read video frame by frame
while True:
    # capture.read() rads above video in capture frame by frame
    # isTrue represent boolean value if the video frame was read successfully or not
    isTrue, frame = capture.read()

    cv.imshow('SampleVideo1', frame)

    # if keyboard letter d is pressed, exit out of loop
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
