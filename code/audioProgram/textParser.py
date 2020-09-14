#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os
import re
import json
import jieba # 导入结巴分词库
import jieba.posseg as postag

class TextParser:
    """用于对中文文本进行解析

        该类主要是用于对输入的中文文本进行分词、词性标注、最后该类需要通过接入其他人工作使用，目前使用jieba分词实现

        Attributes:
            segmentor: 分词
            postagger: 词性标注
            parser： 依存句法分析
            recognizer： 命名实体实别
            labeller： 语义角色标注
    """
    def __init__(self):
        with open(file='./conf/textParserConf.json', mode='r', encoding='utf-8') as f:
            content = f.read()
            content_json = json.loads(content)
            self.LTP_PATH = content_json['LTP_PATH']
            self.SelfDefineWordsPath = content_json['SelfDefineWordsPath']
    # 分词
    def segmentorFun(self, sentence, selfWords):
        for item in selfWords:
            jieba.add_word(item)
        words = postag.cut(sentence)
        retWords = []
        for w in words:
            retWords.append(w.word)
        return retWords

    def postaggerFun(self, sentence,selfWords):
        for item in selfWords:
            jieba.add_word(item)
        words = postag.cut(sentence)
        retWords = []
        retPos= []
        for w in words:
            retWords.append(w.word)
            retPos.append(w.flag)
        return retWords,retPos

    def splitText(self,text) :
        pattern = r'[?|。|！|？|!|?|.]'  # 定义分隔符
        result = re.split(pattern,text)
        return result

    def splitSen(self,sentence):
        if len(sentence) == 0 :
            return []
        pattern = r'[；|：|，|;|:|,|?|。|！|？|!|?|.]'  # 定义分隔符，不包括顿号'、'
        result = re.split(pattern, sentence)
        return result

textParser = TextParser()
if __name__ =="__main__":
    None
    # test
    test = TextParser()
    # result = test.splitText("请定义变量a，并将其赋值为4.如果a大于5，将其增加1；否则将其减少1.")
    # for item in result:
    #     print( test.splitSen(item))
    sentence ="定义整形变量_a0fb_并赋值为1"#"用户能够登录系统"#"登录系统之前需要注册用户"
    swords = ['a']
    words,pos = test.postaggerFun(sentence,swords)
    print(words)
    print(pos)
