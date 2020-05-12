import numpy as np
import cv2

img = cv2.imread('photo0.jpg', -1)

print(img.shape)
print(img.size) # кол-во пикселей
print(img.dtype)

b, g, r = cv2.split(img)
img = cv2.merge((b, g, r))

head_messi = img[130:256, 315:418] # take messi head

img[109:235, 480:583] = head_messi


cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()