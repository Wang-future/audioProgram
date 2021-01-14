#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os
class TextToCode:
    def __init__(self, inputPath,outputPath):
        self.inputPath = inputPath
        self.outputPath = outputPath
        self.transformerModelPath = '/data/project/audioProgram/code/audioProgram/transformerModel/selfTrain'
        self.problemName = 'my_problem'
    def textToCode(self,text):
        # 写进去
        try:
            with open(self.inputPath,"w",encoding="utf-8") as file:
                file.write(text)
        except Exception as e:
            print(e)

        # 调用获取
        command = "t2t-decoder --t2t_usr_dir=/data/project/audioProgram/code/audioProgram/transformerModel/selfTrain --problem=my_problem  --data_dir=./transformerModel/selfTrain/data  --model=transformer --hparams_set=transformer_small --output_dir=./transformerModel/selfTrain/newTrain --decode_hparams=\"beam_size=5,alpha=0.6\"  --decode_from_file=" +self.inputPath + " --decode_to_file=" +self.outputPath
        # print(command)
        os.system(command)
        retList = []
        try:
            with open(self.outputPath,"r",encoding="utf-8") as file:
                for line in file.readlines():
                    retList.append(line)
        except Exception as e:
            print(e)
        print(retList)
        return retList
if __name__ == "__main__":
    myTextToCode = TextToCode('./useByTextToCode/input.txt','./useByTextToCode/output.txt')
    myTextToCode.textToCode('发出信号`信号.SIGUSR1`到当前进程')
    