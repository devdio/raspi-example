# -*- coding: utf-8 -*-

import numpy as np
import cv2

img_file = './image3.jpg'
img = cv2.imread(img_file)

cv2.imshow('IMG', img)
cv2.waitKey(0)
cv2.destroyAllWindows()



