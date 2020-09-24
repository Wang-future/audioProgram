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
    def simpleClassify(self,text):
        # 如果是定义类 返回1
        # 如果是计算类 返回10
        # 如果是判断类 返回100
        # 如果是循环类 返回1000
        # 如果是调用算法类 返回10000
        #多个分类返回 合并值
        return 1