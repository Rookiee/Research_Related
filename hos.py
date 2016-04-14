# coding: utf-8

'''
按照文章方法计算四阶矩，函数为get4moments
'''

import cv2
import numpy as np


# Img: 待处理的Img； N：size of kernel
def get4moments(Img, N):
    # 使用均值滤波对原始图像处理
    img1 = cv2.blur(Img, (N, N))
    # 因为要计算四阶矩，对一个随机变量X，四阶矩即 E(X^4)
    # 随机变量X 是原始图像 和 模糊后图像 的差值
    diff = (Img - img1) ** 4
    # 再对X进行均值滤波
    img2 = cv2.blur(diff, (N, N))

    # HOSMap = img2**4
    HOSMap = img2.copy()  # 同时复制大小和数据类型
    # 下面定义HOSMap的方法无效，？
    # HOSMap = np.zeros(img2.shape, dtype = Img.dtype)

    '''
	numpy.ndenumerate: Multidimensional index iterator.
	Example:
	>>> a = np.array([[1, 2], [3, 4]])
	>>> for index, x in np.ndenumerate(a):
	...     print index, x
	(0, 0) 1
	(0, 1) 2
	(1, 0) 3
	(1, 1) 4
	'''

    for (x, y) in np.ndenumerate(HOSMap):
        # x: 每一个像素（坐标、索引），
        # y: 对应的像素值
        # 由于计算的是四阶矩，每个像素都要4次方，其值可能大于255
        # 如果大于255，用100除， 100是文章中推荐的值
        # print x,y
        if y / 100 > 255:
            HOSMap[x] = 255

    return HOSMap


# 一般先对原始图像进行高斯模糊, N为kernel大小,
def GaussianFilter(img, N):
    """

    :param img:
    :param N:
    :return:
    """
    return cv2.GaussianBlur(img, (N, N), 0)


if __name__ == '__main__':

    # 	# 绝对路径
    absName = "C:/Users/Administrator/Desktop/0000.bmp"
    img = cv2.imread(absName, 0)

    imgGaussian = GaussianFilter(img, 7)
    HosMap = get4moments(imgGaussian, 3)
    # 对获取的图像进行50次叠加
    HosMap *= 50
    # 如果叠加后某像素大于255, 则取255
    for (x,y) in np.ndenumerate(HosMap):
        if y > 255:
            HosMap[x] = 255
    # 二值化
    ret, HosMap = cv2.threshold(HosMap, 128, 255, cv2.THRESH_BINARY)
    cv2.imshow("result", HosMap)
    cv2.imwrite("C:/Users/Administrator/Desktop/test.bmp", HosMap)

    '''
    # imgSample = []
    # for i in range(30):
    #     imgSample.append(GaussianFilter(img, 5))
    #     imgSample[i] = get4moments(imgSample[i],3)
    #     print i

    # lastImg = np.zeros(img.shape, np.uint8)
    # index = np.arange(30)
    # i = 0
    # for singleImg in imgSample:
    #     print index[i]
    #     i = i + 1
    #     lastImg = lastImg + singleImg
    #     for (x, y) in np.ndenumerate(lastImg):
    #         if y > 255:
    #             print y, 'at', x, "bigger than 255"
    #             lastImg[x] = 255

    # cv2.imshow("test", lastImg)
    '''
    if cv2.waitKey() == 27:
        cv2.destroyWindow()





