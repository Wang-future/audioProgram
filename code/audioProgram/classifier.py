#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import json
import re
import sys
sys.path.append(r'../auxClass/')
from wangLog import log



class Classifier():
    """用于对输入文本进行分类

            该类主要是用于对输入的中文文本进行分类，返回分类结果等

            Attributes:
    """
    def __init__(self):
        self.defClass = ['定义']
        self.calClass = ['赋值','增加','减少','自增','自减','加上','减上','相乘','乘上','取余','除去','除以']
        self.rangClass = ['遍历']
        self.judgeClass = ['如果','否则','当']

    def simpleClassify(self,text):
        # 如果是定义类 返回1
        # 如果是计算类 返回10
        # 如果是判断类 返回100
        # 如果是循环类 返回1000
        # 如果是调用算法类 返回10000
        # 多个分类返回 合并值
        retValue = 0
        for item in self.defClass:
            if item in text:
                retValue+=1
                break

        for item in self.calClass:
            if item in text:
                retValue+=10
                break

        for item in self.rangClass:
            if item in text:
                retValue+=100
                break

        for item in self.judgeClass:
            if item in text:
                retValue+=1000
                break

        return retValue

if __name__ == "__main__":
    None
    # str = "定义一个变量1，并将其赋值为20！"
    # str1 = "如果a为1，就将其赋值为2"
    # str2 = "遍历数组a，并对每个元素增加1"
    # myClassifier = Classifier()
    # print(myClassifier.simpleClassify(str2))
