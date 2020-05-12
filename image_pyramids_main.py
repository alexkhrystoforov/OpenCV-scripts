import cv2 as cv
import numpy as np

img = cv.imread('photo0.jpg', 0)

layer = img.copy()
gp = [layer]

for i in range(6):
    layer = cv.pyrDown(layer)
    gp.append(layer)
    cv.imshow(str(i), layer)

cv.imshow('original', img)
cv.waitKey(0)
cv.destroyAllWindows()