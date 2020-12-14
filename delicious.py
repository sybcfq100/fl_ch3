# -*- coding: utf-8 -*-
"""
@Time        : 16/11/2020
@Author      : sybcf
@File        : delicious
@Description : 
"""
# 遍历文件夹及文件地址
'''
import os

for folderName, subfolders, filenames in os.walk('C:\\Users\\sybcf'):
    print('The current folder is ' + folderName)
for subfolder in subfolders:
    print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
for filename in filenames:
    print('FILE INSIDE ' + folderName + ': ' + filename)

print('')

import zipfile, os
os.chdir('C:\\Users\\sybcf\\Desktop') #move to the folder with wm.zip
wmZip = zipfile.ZipFile('wm.zip')
print(wmZip.namelist())
spamInfo = wmZip.getinfo('0V.csv')
print(spamInfo.file_size)
print(spamInfo.compress_size)
print('Compressed fiel is %sx smaller!' %(round(spamInfo.file_size / spamInfo.compress_size,2)))
wmZip.close()
'''
import zipfile, os


#os.makedirs('D:/JJ_RtestData_CD')
#os.chdir('D:/JJ_RtestData_CD')
#wmZip = zipfile.ZipFile('C:/Users/sybcf/Desktop/wm.zip')
#wmZip.extractall()
wmZip = zipfile.ZipFile('C:/Users/sybcf/Desktop/wm.zip')
wmZip.extract('0V.csv', 'C:/Users/sybcf/Desktop')
#wmZip.close()
