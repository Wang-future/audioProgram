# -*- coding: utf-8 -*
"""
    日志工具类
"""
import logging
import time
import os
import sys
cur_path = os.path.dirname(os.path.realpath(__file__))
log_path = "D:/王/硕士/项目/audioProgram/logData/"
# 如果不存在这个文件夹，就自动创建一个
if not os.path.exists(log_path):
    os.mkdir(log_path)

class WangLog:
    def __init__(self):
        # fmt = logging.Formatter('[%(asctime)s] [%(levelname)s] [%(threadName)s] [%(pathname)s:%(lineno)s]: %(message)s',
        #                         "%Y-%m-%d %H:%M:%S")
        # wamg_handler = logging.StreamHandler()
        # wamg_handler.setFormatter(fmt)
        self.log_name = os.path.join(log_path, '%s.log' % time.strftime('%Y_%m_%d'))
        try:
            self.myFile = open(self.getLogName(), 'a')
        except Exception as e:
            print(e)
    def getLogName(self):
        return os.path.join(log_path, '%s.log' % time.strftime('%Y_%m_%d'))

    def changeFileName(self):
        if self.getLogName() != self.log_name:
            self.log_name = self.getLogName()
            self.myFile.close()
            try:
                self.myFile = open(self.getLogName(), 'a')
            except Exception as e:
                print(e)

    def info(self, message):
        self.changeFileName()
        back_frame = sys._getframe().f_back
        filename = back_frame.f_code.co_filename
        currTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        strTmp = currTime + ' [INFO] ' + filename + " " +  str(sys._getframe().f_back.f_lineno) + "行 : " +message
        self.myFile.write('\n' + strTmp)

    def debug(self, message):
        self.changeFileName()
        back_frame = sys._getframe().f_back
        filename = back_frame.f_code.co_filename
        currTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        strTmp = currTime + ' [DEBUG] ' + filename + " " +  str(sys._getframe().f_back.f_lineno) + "行 : " + message
        self.myFile.write('\n' + strTmp)

    def error(self, message):
        self.changeFileName()
        back_frame = sys._getframe().f_back
        filename = back_frame.f_code.co_filename
        currTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        strTmp = currTime + ' [ERROR] ' + filename + " " +  str(sys._getframe().f_back.f_lineno) + "行 : " + message
        self.myFile.write('\n' + strTmp)

    def warn(self, message):
        self.changeFileName()
        back_frame = sys._getframe().f_back
        filename = back_frame.f_code.co_filename
        currTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        strTmp = currTime + ' [WARN] ' + filename + " " +  str(sys._getframe().f_back.f_lineno) + "行 : " + message
        self.myFile.write('\n' + strTmp)

log = WangLog()

if __name__ == "__main__":

    # 使用例子
    log2 = WangLog()
    for i in range(0, 10):
        log2.info('test')

        log2.error('test')

        log2.debug('test')
        time.sleep(1)