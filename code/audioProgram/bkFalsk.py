#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Flask, jsonify, request
import sys
import json
import time
import requests
sys.path.append(r'../auxClass/')
from wangLog import log
from textToCode import TextToCode
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)

# global
app = Flask(__name__)
# 辅助函数
def todayDate():
    return time.strftime("%Y-%m-%d",time.localtime(time.time()))

# 小程序相关接口，获取用户信息
@app.route('/getOpenid',methods=['GET'])
def getOpenid():
    # url一定要拼接，不可用传参方式
    url = "https://api.weixin.qq.com/sns/jscode2session"
    appid = "wx1fc08f048fad7da0"
    secret = "5a01e2474b1391ff0bf14a2c98efd646"
    jscode = request.args.get("code") #获取get请求参数
    murl = url + "?appid=" + appid + "&secret=" + secret + "&js_code=" + jscode + "&grant_type=authorization_code"
    r = requests.get(murl)
    print('in getOpenid')
    print(r.json())
    openid = r.json()['openid']
    return openid
# actor = Actor()

# 输入
    # seqId:请求id
    # message:用户文本
# 返回
    # seqId:请求id
    # text:转换的代码
    # senlist:需要中间确认的文本其中 ret_code需要为3方有效
    # ret_code:1代表转换成功,text为代码;2代表文本无效,text为失效原因;3代表文本需要用户确认,使用senlist表示
    # 确认的文本
# 注意 中间有需要模糊替代的东西
@app.route('/dataSend', methods=['GET', 'POST'])
def dataSend():
    # input
    data = json.loads(request.get_data(as_text=True))
    seqId = data["seqId"]
    message = data["message"] #request.json.get('message')
    language = data["language"] #request.json.get('language')
    log.info('seqId:' + seqId + ', message:' + message + ', language:'+language)

    myTextToCode = TextToCode('./useByTextToCode/input.txt','./useByTextToCode/output.txt')
    # retList = myTextToCode.textToCode(message)
    #  用第一个代替

    # output
    retDict = {}
    retDict['seqId'] = seqId
    retDict['ret_code'] = 2

    if message:
        # senList, carryResList = actor.toCode(seqId,message)
        # retDict['ret_code'] = carryResList[0]
        # retDict['text'] = carryResList[1]
        # retDict['senList'] = senList
        retList = myTextToCode.textToCode(message)
        retDict['text'] = retList[0]
        retDict['ret_code'] = 1

    else:
        retDict['ret_code'] = 2
        retDict['text'] = "你的输入为空， 执行成功"
    return retDict


@app.route('/CourtInformation',methods=["get"])
def getCourtInformation():
    data = json.loads(request.get_data())
    print(data)
    # result = getCombination(data);
    return data

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, ssl_context=('./cer/secret.pem', './cer/secret.key'))


