import cv2 as cv
import numpy as np

img = cv.imread('photo0.jpg', 0)

lr1 = cv.pyrDown(img)
lr2 = cv.pyrDown(lr1)
hr1 = cv.pyrUp(lr2)

cv.imshow('original', img)
cv.imshow('pyrDownFirst', lr1)
cv.imshow('pyrDownSecond', lr2)
cv.imshow('pyrUpFirts', hr1)
cv.waitKey(0)
cv.destroyAllWindows()