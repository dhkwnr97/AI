import numpy as np
import cv2 as cv

img = cv.imread('input.png',0)
cimg = cv.cvtColor(img,cv.COLOR_GRAY2BGR)
circles = cv.HoughCircles(img,cv.HOUGH_GRADIENT,1,20, param1=40,param2=20,minRadius=0,maxRadius=0)
circles = np.uint16(np.around(circles))

#if want show predicting whole images
for i in circles[0,:]:
    # draw the outer circle
    cv.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

cv.imshow('detected circles',cimg)
cv.waitKey(0)
cv.destroyAllWindows()

'''
#if want show predicting average image
xav=0; yav=0; rav=0
for i in circles[0, :]:
    xav+=i[0]; yav+=i[1]; rav+=i[2]
xav=int(round(xav/circles.shape[1]))
yav=int(round(yav/circles.shape[1]))
rav=int(round(rav/circles.shape[1]))
print(xav, yav, rav)
cv.circle(cimg,(xav,yav),rav,(0,255,0),2)
cv.circle(cimg,(xav,yav),1,(0,255,0),3)

cv.imshow('detected circles',cimg)
cv.waitKey(0)
cv.destroyAllWindows()
'''