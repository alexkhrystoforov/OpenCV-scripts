import numpy as np
import cv2 as cv

cap = cv.VideoCapture('video.mp4')
fgbg = cv.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()
    if frame is None:
        break

    fgmask = fgbg.apply(frame)


    cv.imshow('Frame', frame)
    cv.imshow('FG MASK frame', fgmask)

    keyboard = cv.waitKey(30)
    if keyboard == 'q' or keyboard == 27:
        break

cap.release()
cv.destroyAllWindows()