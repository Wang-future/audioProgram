#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import json,time,os
# save data to json file
preDataDir = './conala-corpus'
questionList = []
answerList = []
# 依次读取根目录下的每一个文件
for file in os.listdir(preDataDir):
    file_name = preDataDir + "\\" + file
    filein = open(file_name, "r")
    # 获取json数据
    data = json.load(filein)

    # 使用四个空格的替换为[tab]
    for item in data:
        # print(item)
        question = item['rewritten_intent']
        if not question:
            question = item['intent']
        # 替换question的\n  与 tab
        question = question.replace("\n",'[wrap]').replace('    ','[tab]').replace('\r','[enter]')

        snippet = item['snippet']
        # print(snippet)
        # 替换snippet\n  与 tab
        snippet = snippet.replace("\n",'[wrap]').replace('    ','[tab]').replace('\r','[enter]')

        # print(question + ":" + snippet)
        if question and snippet:
            questionList.append(question)
            answerList.append(snippet)
    if len(questionList) != len(answerList):
        print("error: questionList的长度与answerList不同！")
    else:
        print(len(questionList))
        print(len(answerList))
        with open(".\\extractData\\question_{0}.txt".format(file),"w",encoding="utf-8") as file_handle:   # .txt可以不自己新建,代码会自动新建

            for item in questionList:
                file_handle.write(item)
                file_handle.write('\n')
        with open(".\\extractData\\answer_{0}.txt".format(file),"w",encoding="utf-8") as file_handle:   # .txt可以不自己新建,代码会自动新建
            for item in answerList:
                file_handle.write(item)
                file_handle.write('\n')