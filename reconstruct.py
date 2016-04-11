# coding: utf-8
import cv2
import numpy as np 

size  = 3
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (size, size))
def myerosin(img):
	erodeImg = cv2.erode(img, kernel, iterations = 1)
	img = cv2.max(erodeImg, img)
	return erodeImg

def mydilation(img):
	# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
	dilationImg = cv2.dilate(img, kernel)
	img = cv2.min(dilationImg, img)
	return dilationImg

loopNum = 2
def ReconstructionByErosion(img):	#closing
	
	for i in np.arange(loopNum):
		img = myerosin(img)

	return img


def ReconstructionByDilation(img):	#opening
	for i in np.arange(loopNum):
		img = mydilation(img)
	return img 


def ClosingOpening(img):
	img = ReconstructionByDilation(ReconstructionByErosion(img))
	return img



img = cv2.imread("C:\\Users\\Administrator\\Desktop\\result.jpg",0)
imgCopy = img.copy()
# dst = ReconstructionByErosion(img)
dst = ClosingOpening(imgCopy)

cv2.imshow("original", img)
cv2.imshow("New", dst)

print dst == imgCopy

cv2.waitKey()
