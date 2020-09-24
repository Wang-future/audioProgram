#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import json
import re
import sys
sys.path.append(r'../auxClass/')
from wangLog import log
from classifier import Classifier
from textParser import TextParser

class Check():
    """用于对输入文本进行校验

            该类主要是用于对输入的中文文本进行检验，以及对输出的代码进行替换等

            Attributes:
                segmentor: 分词
                postagger: 词性标注
                parser： 依存句法分析
                recognizer： 命名实体实别
                labeller： 语义角色标注
    """
    def __init__(self):
        with open(file='./data/replaceRule/replaceRule.json', mode='r', encoding='utf-8') as f:
            content = f.read()
            self.replaceDict = json.loads(content)
            print(self.replaceDict)
        self.classifier = Classifier()
        self.parser = TextParser()

    def inputCheck(self, text):
        return True

    def outputCheck(self, seqId, text):
        # 记录参数
        dict = {}
        dict['seqId'] = seqId
        dict['text']  =text
        strInput = json.dumps(dict)
        log.info('Input:' + strInput)

        # 匹配替换
        for key in self.replaceDict.keys():
            # re.subn(regex, newstring, subject)
            strinfo = re.compile(key)
            text = strinfo.sub(self.replaceDict[key], text)
        return text

    # 文本检测, 返回分句及其对应的检测结果
    # 1 代表符合要求,2代表需要模糊匹配或者人机
    # [["定义变量a","1"],["定义变量a","2"],"定义","1"]
    def textDetection(self, text):
        # 进行检查
        # 先进行分句
        senList = self.parser.splitText(text)
        # 获取分类结果
        retList = []
        # 逐句获取分类结构
        for sen in senList:
            tempRes = self.classifier.simpleClassify(sen)
            tempList = []
            tempList.append(sen)
            tempList.append(tempRes)
            # 结果存储进retList
            retList.append(tempList)
        return retList

if __name__ == '__main__':
    mCheck = Check()
    seqId ="testId"
    text = " int a; if #zuokuohao# a > 2 #youkuohao#"
    newText = mCheck.outputCheck(seqId, text)
    print(newText)

