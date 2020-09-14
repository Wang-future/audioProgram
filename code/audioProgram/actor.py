#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import json
import re
import sys
sys.path.append(r'../auxClass/')
from wangLog import log
from check import Check
from textParser import TextParser
from classifier import Classifier
from ruleParser import RuleParser
class Actor():
    """用于处理代码转换

            该类主要是用于对处理用户输入的中文文本

            Attributes:

    """
    def __init__(self):
        with open(file='./conf/actorConf.json', mode='r', encoding='utf-8') as f:
            content = f.read()
            content_json = json.loads(content)
            self.Head = content_json['Head']
            self.End = content_json['End']
        # 用户检查校验更正文本的输入与输出
        self.myCheck = Check()
        self.parser = TextParser()
        self.classifier = Classifier()
        self.ruleParser = RuleParser()
    def textCheck(self, inputText):
        return self.myCheck.inputCheck(inputText)

    def codeCheck(self, codeText):
        return self.myCheck.outputCheck(codeText)

    # 根据输入的句子生成代码
    def genSenCode(self, senText):

        # 对句子进行细分，逐句翻译
        codeList = self.parser.splitSen(senText)

        # 分类
        for item in codeList:
            label = self.classifier.classify(item)
            # 根据label 使用对应规则生成代码
    def genMidCode(self, preText):
        outCodeText = self.Head

        # 文本分块
        sentenceList = self.parser.splitText(preText)

        # 逐句进行代码翻译
        for item in sentenceList:
            outCodeText += self.genSenCode(item)

        # 补齐尾部
        outCodeText += self.End
    def toCode(self, seqId, text):
        # 记录参数
        dict = {}
        dict['seqId'] = seqId
        dict['text'] = text
        strInput = json.dumps(dict)

        # check the text
        text = self.textCheck(text)
        log.info('after check text:' + text)

        # genMidCode
        outCodeText = self.genMidCode(text)
        log.info('after genMidCode:' + outCodeText)

        # return code
        lastCode = self.codeCheck(outCodeText)
        log.info('last code:' + lastCode)
        return lastCode