import cv2
from PIL import Image
import numpy as np


image = cv2.imread('maze5.jpg')


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)



ksize = 1
gX = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=ksize)
gY = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=0, dy=1, ksize=ksize)


gX = cv2.convertScaleAbs(gX)
gY = cv2.convertScaleAbs(gY)


edge = cv2.addWeighted(gX, 1, gY, 1, 0)

params = cv2.SimpleBlobDetector_Params()
params.filterByArea = True
params.minArea = 100
detector = cv2.SimpleBlobDetector_create(params)
keypoints = detector.detect(edge)

blank = np.zeros((1, 1))
blobs = cv2.drawKeypoints(edge, keypoints, blank, (0, 0, 255),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

print(type(keypoints))
print(keypoints[0].pt)



cv2.imshow("maze", blobs)
cv2.waitKey(0)

"""
indices = np.where(edge != [0])
coordinates = zip(indices[0], indices[1])
print(list(coordinates))

"""