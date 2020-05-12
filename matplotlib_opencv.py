import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np

img = cv.imread('adapt.jpg', 0)

_, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11 ,2)
th3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11 ,2)


# Plot subplots

titles = ['original', 'threshold', 'adaptMean', 'adaptGauss']
images = [img, th1, th2, th3]

for i in range(len(titles)):
    plt.subplot(3,3,i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

plt.imshow(img)
plt.xticks([])
plt.yticks([])
plt.show()

# cv.waitKey(0)
# cv.destroyAllWindows()