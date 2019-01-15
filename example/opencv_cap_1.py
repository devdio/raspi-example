# -*- coding: utf-8 -*-

import numpy as np
import cv2

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
cv2.imwrite('image.jpg', frame)
cap.release()

img_file = './image.jpg'
img = cv2.imread(img_file)
cv2.imshow('IMG', img)
cv2.waitKey(0)
cv2.destroyAllWindows()






