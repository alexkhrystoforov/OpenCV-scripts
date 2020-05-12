import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('photo0.jpg', 0)

canny = cv.Canny(img, 100, 200)
titles = ['image', 'canny']
images = [img, canny]

for i in range(len(titles)):
    plt.subplot(3,3,i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])


plt.show()