
# import cv2
# import numpy as np 
# img = cv2.imread("C:/Users/Administrator/Desktop/0100.BMP")
# cv2.imshow("Original", img)
# rows, cols, depth = img.shape
# M = cv2.getRotationMatrix2D((cols/2, rows/2),30, 1)
# dst = cv2.warpAffine(img, M, (cols, rows))
# cv2.imshow("Result", dst)

# print "Original: ", img.shape, img.size
# print "Result: ", dst.shape, dst.size


# if cv2.waitKey() == ord('q'):
# 	cv2.destroyAllWindows()



import cv2
import numpy as np 
img = cv2.imread("C:/Users/Administrator/Desktop/test.bmp")
kernel = np.ones((3,3), np.uint8)
# dilation = cv2.dilate(img, kernel, iterations = 1)
dilation = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
cv2.imshow("result", dilation)
cv2.imwrite("c:/Users/Administrator/Desktop/resule.bmp", dilation)

canny = cv2.Canny(dilation, 100,200)
cv2.imshow("canny", canny)
if cv2.waitKey() == ord('q'):
	cv2.destroyAllWindows()