#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import json,time,os
# save data to json file
preDataDir = './comparedData'
preList = []
outList = []
chList = []
isCompared = True
# 依次读取根目录下的每一个文件
if len(os.listdir(preDataDir)) not in (2,3):
    print('preDataDir 文件个数不是2或者3')
    isCompared= False
else:
    check = False
    for file in os.listdir(preDataDir):
        if 'pre' in file:
            check = True
    if not check:
        print('preDataDir 中的源对比文件没有标记pre')
        isCompared = False
if isCompared:
    for file in os.listdir(preDataDir):
        file_name = preDataDir + "\\" + file
        filein = open(file_name, "r",encoding='UTF-8')
        if 'pre' in file_name:
            for line in filein.readlines():
                preList.append(line)

        elif 'ch' in file_name:
            for line in filein.readlines():
                chList.append(line)
        else:
            for line in filein.readlines():
                outList.append(line)
    if len(preList) != len(outList) or len(preList) != len(chList):
        print('对比文件长度不一， 正确的文件长度：' + str(len(preList)) + ', 待对比的：' +str(len(outList)) + ', 中文：' +str(len(chList)))
    print('\n开始对比')
    count = 0
    disCount = 1
    for index in range(0,min(len(preList),len(outList))):
        if preList[index] == outList[index]:
            count +=1
        else:
            print(str(disCount) + ' 处于第' + str(index+1) + '行'+ '\n')
            print('中文：'+chList[index]+'\n')
            print('正确的：' + preList[index] + '\n')
            print('错误的：' + outList[index] + '\n')
            disCount += 1
    print('结果，对比的长度有：' + str(min(len(preList),len(outList))) + ', 一样的有：' + str(count)+', 正确率：'+str(count/min(len(preList),len(outList))) + '\n')

