#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Flask, jsonify, request
import sys
sys.path.append(r'../auxClass/')
from wangLog import log

defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)

# global
app = Flask(__name__)
actor = Actor()

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
    seqId = request.json.get("seqId")
    message = request.json.get('message')
    language = request.json.get('language')
    log.info('seqId:' + seqId + ', message:' + message + ', language:'+language)

    # output
    retDict = {}
    retDict['seqId'] = seqId
    retDict['ret_code'] = 2

    if message:
        senList, carryResList = actor.toCode(seqId,message)
        retDict['ret_code'] = carryResList[0]
        retDict['text'] = carryResList[1]
        retDict['senList'] = senList
    else:
        retDict['ret_code'] = 2
        retDict['text'] = "你的输入为空， 执行成功"
    return retDict



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5017,ssl_context=('./zhengshu/3708790_www.iais.group.pem', './zhengshu/3708790_www.iais.group.key'))


