# coding: utf-8

''' 
导入本目录下的hos.py
'''
import hos
import cv2

pathName = 'C:/Users/Administrator/Desktop/result1.bmp'
imgGray = cv2.imread(pathName,0)
imgGaussian = hos.GaussianFilter(imgGray,(3,3),1)

