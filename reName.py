# coding: utf-8

"""
Author: Rookiee
Date: 2016-4-4 
Location: Donghua University
Destription: Rename file names in the folder.
			 The new file names will be 0001.bmp, 0002.bmp...
			 The user need to provide two paramters:
			 absolute path: d:/test
			 extension name: txt
"""

import os

# Input the absolute path of a folder and the extension name of
# the files need to be changed.
path = raw_input("Enter the absolute path \n"
				 "(using '/' for suggestion): ")
ext = raw_input("Enter the extension name: ")

try:
	os.listdir(path)
except WindowsError:
	print ("######################")
	print ("Invalid path! ")
	print ("Enter a correct path! ")
	print ("######################")
	


if path[-1] != ('/' or '\\'):
	path = path + '/' 

# create a temp file 
tmpPath = 'c:/'

# create a new temp file, and the content is 0001, 0002, ...
tmp = open(tmpPath + 'tmp.txt', 'w')
for i in range(len(os.listdir(path))):
	tmp.write("%04d\n" %i)
tmp.close()

# get the content of created temp file
tmp = open(tmpPath + 'tmp.txt','r')
tmpContent = tmp.read().split()
tmp.close()

print ("The temp file is located in", tmpPath)
while(True):
	wait = raw_input("Would you want to save the tmp file(y/n)? ")
	if wait == 'n' or wait == 'N':
		os.remove(tmpPath+'tmp.txt')
		break
	elif wait == 'y' or wait == 'Y':
		break
	else:
		continue

	
# create a new list to store the new file name, 
# such as 0001.bmp, 0002.bmp
newNames = []
for item in tmpContent:
	newNames.append(item + '.' + ext)


# rename
j = 0
for file in os.listdir(path):
	if file.split('.')[1] == ext:
		os.rename(path+file, path+newNames[j])
		j = j+1
	else:
		continue














