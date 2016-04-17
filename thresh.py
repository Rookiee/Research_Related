# coding: utf-8   
# 渐进显示, 打断时输出阈值 
import numpy as np 
import cv2

img = cv2.imread("D:/Pics/boldt.jpg",0)

cv2.namedWindow("Test")
for i in np.arange(256):
	ret, binary = cv2.threshold(img,i,255, cv2.THRESH_BINARY);
	cv2.imshow("Test", binary);
	if cv2.waitKey(30)==ord('q'):
		print i
		break

cv2.destroyAllWindows()


