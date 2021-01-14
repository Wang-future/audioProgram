#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
调用「百度翻译 API」实现英汉互译及多语言翻译
@Author: Newyee
@Python: 3.6.5
@Create: 2019-04-18
"""
# 导入相关模块
import hashlib
import random
import requests
import time
import os

# 你的APP ID
appID = '20210107000665791'
# 你的密钥
secretKey = 'Mhfzq9mjZ9FtKa7fZY3u'
# 百度翻译 API 的 HTTP 接口
apiURL = 'http://api.fanyi.baidu.com/api/trans/vip/translate'


def baiduAPI_translate(query_str, to_lang):
    '''
    传入待翻译的字符串和目标语言类型，请求 apiURL，自动检测传入的语言类型获得翻译结果
    :param query_str: 待翻译的字符串
    :param to_lang: 目标语言类型
    :return: 翻译结果字典
    '''
    # 生成随机的 salt 值
    salt = str(random.randint(32768, 65536))
    # 准备计算 sign 值需要的字符串
    pre_sign = appID + query_str + salt + secretKey
    # 计算 md5 生成 sign
    sign = hashlib.md5(pre_sign.encode()).hexdigest()
    # 请求 apiURL 所有需要的参数
    params = {
        'q': query_str,
        'from': 'auto',
        'to': to_lang,
        'appid': appID,
        'salt':salt,
        'sign': sign
    }
    try:
        # 直接将 params 和 apiURL 一起传入 requests.get() 函数
        response = requests.get(apiURL, params=params)
        # 获取返回的 json 数据
        result_dict = response.json()
        # 得到的结果正常则 return
        if 'trans_result' in result_dict:
            return result_dict
        else:
            print('Some errors occured:\n', result_dict)
    except Exception as e:
        print('Some errors occured: ', e)


def baiduAPI_translate_main(query_str, dst_lang=''):
    '''
    解析翻译结果后输出，默认实现英汉互译
    :param query_str: 待翻译的字符串，必填
    :param dst_lang: 目标语言类型，可缺省
    :return: 翻译后的字符串
    '''
    if dst_lang:
        # 指定了目标语言类型，则直接翻译成指定语言
        result_dict = baiduAPI_translate(query_str, dst_lang)
    else:
        # 未指定目标语言类型，则默认进行英汉互译
        result_dict = baiduAPI_translate(query_str, 'zh')
        if result_dict['from'] == 'zh':
            result_dict = baiduAPI_translate(query_str, 'en')
    # 提取翻译结果字符串，并输出返回
    try:
        dst = result_dict['trans_result'][0]['dst']
    except Exception as e:
        with open(".\\notTranslate.txt","a",encoding="utf-8") as file_handle:   # .txt可以不自己新建,代码会自动新建
            file_handle.write(query_str)
            file_handle.write('\n')
        return None

    # print('{}: {} -> {}: {}'.format(result_dict['from'], query_str, result_dict['to'], dst))
    return dst

def enToChina(enText):
    chText = baiduAPI_translate_main(enText)
    time.sleep(1)
    return chText

if __name__ == '__main__':
    preDataDir = './extractData'
    for file in os.listdir(preDataDir):
        file_name = preDataDir + "\\" + file
        if 'question' not in file_name:
            continue
        if 'train' not in file_name:
            continue
        print("处理："+file_name)
        filein = open(file_name, "r",encoding='UTF-8')

        codeFileName = ''
        if 'train' in file_name:
            codeFileName = preDataDir + "\\" + 'answer_conala-train.json.txt'
        else:
            codeFileName = preDataDir + "\\" + 'answer_conala-test.json.txt'
        fileCode = open(codeFileName, "r",encoding='UTF-8')

        translateList = []
        resultList = []
        codeList = []
        for line in filein.readlines():
            # print(line)
            line = line.replace('[wrap]','\n').replace('[tab]','\t').replace('[enter]','\r')
            translateList.append(line)
        for line in fileCode.readlines():
            # print(line)
            codeList.append(line)
        if len(codeList)!= len(translateList):
            print("error:translateList 与 codeList 长度不同！")
        else:

            for index in range(0,len(translateList)):
                # print(translateList[index])
                chText = enToChina(str(translateList[index]))
                # resultList.append(chText)
                if chText:
                    with open(".\\chData\\ch_new_{0}.txt".format(file),"a",encoding="utf-8") as file_handle:   # .txt可以不自己新建,代码会自动新建
                        file_handle.write(chText)
                        file_handle.write('\n')
                    with open(".\\chData\\pre_new_{0}.txt".format(file),"a",encoding="utf-8") as file_handle:   # .txt可以不自己新建,代码会自动新建
                        file_handle.write(translateList[index])
                        file_handle.write('\n')

                    with open(".\\chData\\code_new_{0}.txt".format(file),"a",encoding="utf-8") as file_handle:   # .txt可以不自己新建,代码会自动新建
                        file_handle.write(codeList[index])
                        file_handle.write('\n')
        print("结束处理："+file_name)
    # 保存结果
    # if len(resultList) > 0:
    #     with open(".\\chData\\question_ch_{0}.txt".format('question_conala-train.json.txt'),"a",encoding="utf-8") as file_handle:   # .txt可以不自己新建,代码会自动新建
    #         for item in resultList:
    #             file_handle.write(item)
    #             file_handle.write('\n')
    # preDataDir = './extractData'
    # for file in os.listdir(preDataDir):
    #     file_name = preDataDir + "\\" + file
    #     if 'question' not in file_name:
    #         continue
    #     filein = open(file_name, "r",encoding='UTF-8')
    #
    #     translateList = []
    #     resultList = []
    #     for line in filein.readlines():
    #         print(line)
    #         translateList.append(line)
    #     for item in translateList:
    #         chText = enToChina(str(item))
    #         resultList.append(chText)
    #         if len(resultList) > 1000:
    #             with open(".\\chData\\question_ch_{0}.txt".format(file),"a",encoding="utf-8") as file_handle:   # .txt可以不自己新建,代码会自动新建
    #                 for item in resultList:
    #                     file_handle.write(item)
    #                     file_handle.write('\n')
    #             resultList.clear()
    #     # 保存结果
    #     if len(resultList) > 0:
    #         with open(".\\chData\\question_ch_{0}.txt".format(file),"a",encoding="utf-8") as file_handle:   # .txt可以不自己新建,代码会自动新建
    #             for item in resultList:
    #                 file_handle.write(item)
    #                 file_handle.write('\n')
        # with open(".\\chData\\question_ch_{0}.txt".format(file),"a",encoding="utf-8") as file_handle:   # .txt可以不自己新建,代码会自动新建
        #     for item in resultList:
        #         file_handle.write(item)
        #         file_handle.write('\n')
    # baiduAPI_translate_main('This is English.')
    # baiduAPI_translate_main('这是中文')
    # baiduAPI_translate_main('翻译成法语', 'fra')