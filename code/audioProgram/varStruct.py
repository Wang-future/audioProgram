#!/usr/bin/env python
# -*- coding: UTF-8 -*-
class varStruct():
    """用于记录变量信息

           该类主要是记录变量的信息

           Attributes:
               isArray: 是否是数组
               value:  值是多少
               isPointer: 是否是指针
               type： 有 int char string float double bool void
               textType: 该变量所在句子的分类
       """
    def __inft__(self, _isArray, _value, _type, _isPointer, _textType) :
        self.isArray = _isArray
        self.value = _value
        self.type  = _type
        self.isPointer = _isPointer
        self._textType = _textType