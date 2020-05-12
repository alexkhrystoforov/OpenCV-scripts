import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('color-balls.jpeg', cv.IMREAD_GRAYSCALE)
_, mask = cv.threshold(img, 220, 255, cv.THRESH_BINARY_INV)

kernel = np.ones((2,2), np.uint8)

# with iterations=2 works better

dilation = cv.dilate(mask, kernel=kernel, iterations=2)
erosion = cv.erode(mask, kernel=kernel, iterations=1)
opening = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel=kernel)
closing = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel=kernel)
mg = cv.morphologyEx(mask, cv.MORPH_GRADIENT, kernel=kernel)
th = cv.morphologyEx(mask, cv.MORPH_TOPHAT, kernel=kernel)


titles = ['original', 'mask', 'dilatoin', 'erosion', 'opening', 'closing', 'mg', 'th']
images = [img, mask, dilation, erosion, opening, closing, mg, th]

for i in range(len(titles)):
    plt.subplot(3,3,i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])


plt.show()