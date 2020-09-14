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
    def classify(self,text):
        return 1