import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def region_of_interest(img, vertices):
    mask = np.zeros_like(img)
    # channel_count = img.shape[2] // dont need this if apply for grey image
    # match_mask_color = (255,) * channel_count
    match_mask_color = (255)
    cv.fillPoly(mask, vertices, match_mask_color)
    masked_image = cv.bitwise_and(img, mask)
    return masked_image


def draw_lines(img, lines):
    img = np.copy(img)
    blank_img = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)

    for line in lines:
        for x1, y1, x2, y2 in line:
            cv.line(blank_img, (x1, y1), (x2, y2), (0, 255, 0), thickness=3)
    img = cv.addWeighted(img, 0.8, blank_img, 1, 0.0)
    return img


img = cv.imread('road.jpeg')
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

print(img.shape)
width = img.shape[1]
height = img.shape[0]
print(width)
print(height)

region_of_interest_vertices = [
    (0, height),
    (0, (height-40)),
    ((width / 2) - 10, 440),
    (width, height-40),
    (width, height)
]

# canny before cropped to avoid border edges of ROI

gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
canny_img = cv.Canny(gray_img, 100, 200)
cropped_image = region_of_interest(canny_img,
                                   np.array([region_of_interest_vertices], np.int32))


lines = cv.HoughLinesP(cropped_image,
                       rho=6,
                       theta=np.pi/60,
                       threshold=1,
                       lines=np.array([]),
                       minLineLength=10,
                       maxLineGap=25)

img_with_line = draw_lines(img, lines)
plt.imshow(img_with_line)
plt.show()
