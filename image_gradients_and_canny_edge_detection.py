import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('photo0.jpg', cv.IMREAD_GRAYSCALE)
lap = cv.Laplacian(img, cv.CV_64F)
lap = np.uint8(np.absolute(lap))

soberX = cv.Sobel(img, cv.CV_64F, 1, 0) # detect Vertical edges
soberY = cv.Sobel(img, cv.CV_64F, 0, 1) # detect horizonal edges

soberCombined = cv.bitwise_or(soberX, soberY)

soberX = np.uint8(np.absolute(soberX))
soberY = np.uint8(np.absolute(soberY))

titles = ['image', 'Laplacian', 'soberX', 'soberY', 'soberCombined']
images = [img, lap,soberX, soberY, soberCombined]

for i in range(len(titles)):
    plt.subplot(3,3,i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])


plt.show()
