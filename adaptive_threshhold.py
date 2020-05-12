import cv2 as cv
import numpy as np

img = cv.imread('adapt.jpg', 0)

_, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11 ,2)
th3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11 ,2)


cv.imshow('Image', img)
cv.imshow('TR1', th1)
cv.imshow('meanC_TR', th2)
cv.imshow('gauss_TR', th3)

cv.waitKey(0)
cv.destroyAllWindows()