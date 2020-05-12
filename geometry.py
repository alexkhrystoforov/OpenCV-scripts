import cv2
import numpy as np

# img = cv2.imread('photo0.jpg', -1)
img = np.zeros([512,1024,3], np.uint8)


img = cv2.line(img, (0,0), (255,255), (255,255,0), 10)
img = cv2.arrowedLine(img, (0,255), (255,255), (0,255,0), 10)
img = cv2.rectangle(img, (384,0), (510, 128), (0,0,255), 10)
img = cv2.circle(img, (255,255), 20 , (0,0,255),5)
font = cv2.FONT_HERSHEY_COMPLEX
img = cv2.putText(img, 'OpenCV', (360,250), font, 4, (0,255,255), cv2.LINE_AA)


cv2.imshow('image', img)
k = cv2.waitKey(0)

cv2.destroyAllWindows()