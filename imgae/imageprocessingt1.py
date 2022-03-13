import numpy as np
import cv2 as cv



image = cv.imread('mom.jpg',0)

equalize = cv.equalizeHist(image)

res = np.hstack((image,equalize))

cv.imwrite('momnew.jpg', res)
