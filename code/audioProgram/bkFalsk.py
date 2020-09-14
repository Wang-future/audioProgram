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

@app.route('/dataSend', methods=['GET', 'POST'])
def dataSend():
    # input
    seqId = request.json.get("seqId")
    message = request.json.get('message')
    log.info('seqId:' + seqId + ', message:' + message)

    # output
    retDict = {}
    retDict['seqId'] = seqId
    retDict['ret_code'] = 0

    if message:
        carryResList = carryVoiceInstr(message)
        retDict['ret_code'] = carryResList[0]
        retDict['info'] = carryResList[1]
    else:
        retDict['ret_code'] = 0
        retDict['info'] = "你的输入为空， 执行成功"
    return retDict



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5017,ssl_context=('./zhengshu/3708790_www.iais.group.pem', './zhengshu/3708790_www.iais.group.key'))


