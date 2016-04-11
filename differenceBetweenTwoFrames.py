import cv2
import numpy as np 


img1 = cv2.imread("C:/Users/Administrator/Desktop/0027.BMP")
img2 = cv2.imread("C:/Users/Administrator/Desktop/result2.BMP")

img1Gray = cv2.imread("C:/Users/Administrator/Desktop/0027.BMP", 0)
img2Gray = cv2.imread("C:/Users/Administrator/Desktop/result2.BMP",0)


imgGray = np.ones(img1.shape, img1Gray.dtype)
img = np.zeros(img1.shape, np.uint8)

# cv2.absdiff(img1Gray, img2Gray, imgGray)
imgGray = img1Gray - img2Gray
cv2.absdiff(img1, img2, img)

cv2.imshow("result", img)
cv2.imshow("grayResult", imgGray)

if cv2.waitKey() == ord('q'):
	cv2.destroyAllWindows()

