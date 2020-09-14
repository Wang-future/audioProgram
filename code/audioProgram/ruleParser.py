#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import re
from textParser import textParser
import sys
sys.path.append(r'../auxClass/')
from wangLog import WangLog

#global
g_undefineStr = '#undefine#'
# 该类用来做解析，
class RuleParser:
    """基于规则的代码提取

            该类主要是对分好类别的句子做代码提取， 使用类型为 #int# #char# #void#…… 后面生成代码时在逐步替换成对应语言

            Attributes:

        """
    def __init__(self):
        None

    def matchType(self,str):
        if str in ['整型', '整数']:
            return '#int#'

        if str in ['字符型', '字符']:
            return '#char#'

        if str in ['字符串型', '字符串']:
            return '#string#'

        if str in ['浮点型', '浮点']:
            return '#float#'

        if str in ['双浮点型', '双浮点']:
            return '#double#'

        if str in ['空类型', '空']:
            return '#void#'
        return g_undefineStr

    def getType(self, index, retWords):
        # 上下文窗口定义为 5
        contextWin = 10

        judgeTypeWords = []
        lenWord = len(retWords)
        for step in range(1, contextWin):
            left =  index - step
            if left >= 0:
                judgeTypeWords.append(retWords[left])
            else:
                break

        for step in range(1, contextWin):
            right = index + step
            if right < len(retWords):
                judgeTypeWords.append(retWords[right])
            else:
                break
        # print(judgeTypeWords)
        strType = g_undefineStr
        for newIndex in range(0, len(judgeTypeWords)):
            ret = self.matchType(judgeTypeWords[newIndex])
            if ret != g_undefineStr:
                strType = ret
                break
        return strType

    # 提取变量名 变量需要按顺序输出
    def extrVariable(self,text):
        # 变量提取时 要把可能的变量值给剔除
        valuePattern1 = re.compile(r'\"(.*?)\"')
        valuePattern2 = re.compile(r'\'(.*?)\'')
        text = valuePattern1.sub('', text)
        text = valuePattern2.sub('', text)
        # C++ pattern
        cPattern = re.compile(r'[A-Za-z_]+[A-Za-z_0-9]*')
        lis = cPattern.findall(text)
        # 剔除在‘’ 或者 “" 里面的
        return lis

    # 提取变量值
    def extrValue(self, text):
        valuePattern1 = re.compile(r'\"(.+?)\"|\'(.+?)\'')
        lis = valuePattern1.findall(text)
        # valuePattern2 = re.compile(r'\'(.+?)\'')
        # lis2 = valuePattern2.findall(text)
        # lis1.extend(lis2)
        valueList = []
        for item in lis:
            if len(item[0]) > 0:
                valueList.append(item[0])
            else:
                valueList.append(item[1])
            if (len(item[0]) > 0) and (len(item[1]) > 0):
                log.error("这里不应该两项都大于0的，提取出的值为：" + item[0] + ", " + item[1])
        return valueList

    # 定义类型
    def defineType(self, text):
        # 输出code
        midCode = ''

        # 提取值
        variableList = self.extrVariable(text)
        valueList = self.extrValue(text)

        # 获取到其分词与词性标注
        selfWords = variableList + valueList
        retWords, retPos = textParser.postaggerFun(text, selfWords)

        print(retWords)
        print(retPos)

        #记录提取的定义量与变量
        typeList = []
        varList = []
        # 提取类型
        for index in range(0, len(retWords)):
            if retWords[index] in variableList:
                # 方向遍历寻找最近匹配 提取最近的5个词进行类型定义
                strType = self.getType(index, retWords)
                typeList.append(strType)
                varList.append(retWords[index])
        # midCode += strType + ' ' + retWords[index] + ';'

        print(typeList)
        print(varList)
        # 就近匹配更改类型
        # 前向
        for index in range(1, len(typeList)):
            if typeList[index] == g_undefineStr:
                typeList[index] = typeList[index-1]

        #逆向
        for index in range(len(typeList)-2, -1, -1):
            if typeList[index] == g_undefineStr:
                typeList[index] = typeList[index+1]

        # genMidCode
        for index in range(0, len(varList)):
            midCode += typeList[index] + ' ' + varList[index] + ';' + '\n'
        return midCode

    # 计算类型
    def caculateType(self, text):
        
if __name__ == '__main__':
    my = RuleParser()
    # text = '定义整型string1、字符型sf、sf2、fs4、fsf"'
    text = '定义string1、sf、sf2、fs4、fsf并设置其类型为字符串"'
    print(my.defineType(text))
