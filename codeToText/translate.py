import os
import re
from wangLog import log
class CodeToData():
    def __init__(self, dataPath, savePath):
        self.dataPath = dataPath
        self.savePath = savePath
    
    def getAllFiles(self, path):
        files= os.listdir(path) #得到文件夹下的所有文件名称
        retFilesPath = []
        for file in files: #遍历文件夹
            if not os.path.isdir(file): #判断是否是文件夹，不是文件夹才保存
                str = path+"/"+file
                retFilesPath.append(str) #保存文件路径
        return files

    # 读取path的文件内容
    def getFileContent(self, path):
        s = []
        if not os.path.isdir(path): #判断是否是文件夹，不是文件夹才打开
            f = open(path)#打开文件
            iter_f = iter(f)#创建迭代器
            str = ""
            for line in iter_f: #遍历文件，一行行遍历，读取文本
                str = str + line
            s.append(str) #每个文件的文本存到list中
        return s

    def saveResult(self, fileContent, translateResult, savePath):
        # 如果存在，先删除
        if os.path.exists(savePath):
            os.remove(savePath)
        saveList = []
        # 这里会过滤掉不符合的
        for index in range(0,len(fileContent)):
            if (len(fileContent[index]) != 0 and len(translateResult[index]) != 0):
                str = "{" + "\"code\":"+ "\""+fileContent[index]+ "\","+\
                         "\"text\":"+ "\""+translateResult[index]+ "\"}"
                saveList.append(str)
                #大于1000条就开始保存，防止丢失
                if len(saveList) > 1000:
                    with open(savePath, 'w+') as f:
                        for item in saveList:
                            f.write(item)
                            f.write('\n')
                        f.close()
        if len(saveList) > 0:
            with open(savePath, 'w+') as f:
                for item in saveList:
                    f.write(item)
                    f.write('\n')
                f.close()
    def getContentLabel(self, text):
        # 0代表判断不出，1代表定义类型，二代表计算类型，三代表判断类型，四代表循环类型
        label = 0
        # 下面代码类型的判断应该要有先后
        # python 没有定义类型，故这里不会返回1
        # 判断类型
        if 'if' in text:
            return 3
        if 'else' in text:
            return 3
        if 'elif' in text:
            return 3
        
        # 循环类型
        if 'while' in text:
            return 4
        if 'for' in text:
            return 4

        #计算类型
        if '=' in text:
            return 2
        return label

    def addVariableName(self,matched):
        return "变量" + matched.group()
    def templateOfCalculate(self, text):
        # 计算类别显然会有赋值，所以以等于号作为划分
        # 以第一个等于号两边划分
        if text.find('=') == -1:
            return ""
        leftString = text[:text.find('=')]
        rightString = text[text.find('=')+1:]
        # 去掉字符串所有空格
        leftString = leftString.strip()
        leftString = leftString.replace(' ', '')
        rightString = rightString.strip()
        rightString = rightString.replace(' ', '')
        print(leftString)
        print(rightString)
        # 处理左边的字符串
        leftText = ""
        if '[' in leftString and ']' in leftString:
            #这是数组
            value = leftString[leftString.find('[')+1, leftString.find(']')]
            if value.isdigit():
                leftText =  "将数组"+leftString[:leftString.find('[')]+"第"+value+"个元素"
            else:
                # 返回空
                return ""
        else:
            leftText = "将变量" + leftString
        leftText = leftText + "赋值为"
        # 处理右边的字符串
        rightString = rightString.replace('+','加')

        rightString = rightString.replace('-', '减')
        rightString = rightString.replace('/', '除以')
        rightString = rightString.replace('*', '乘以')
        # 处理括号
        while(rightString.find(')') != -1):
            index = rightString.find(')')
            # 反向遍历找到(
            i = index
            while i >= 0:
                if(rightString[i] =='('):
                    for j in range(i,index-1):
                        tmplist1 = list(rightString)
                        tmplist1[j] = tmplist1[j+1]
                        rightString = ''.join(tmplist1)
                    tmplist1 = list(rightString)
                    tmplist1[index-1] = '的'
                    tmplist1[index] = '值'
                    rightString = ''.join(tmplist1)
                    break
                i = i - 1
        #在变量前面加上变量二字
        pattern = re.compile('[a-zA-Z]+')
        rightString = re.sub(pattern,self.addVariableName,rightString,0)
        print(text + ":"+leftText+rightString)
        return leftText+rightString

    def translateToText(self,fileContent):
        translateResult = []
        for item in fileContent:
            if len(item) == 0:
                log.info("fileContent is empty, return!")
                translateResult.append(item)
            else:
                # 根据规则转换
                label = self.getContentLabel(item)
                log.info(item + ", label:" + str(label))
                # 计算类型
                if label == 2:
                    res = self.templateOfCalculate(item)
                    translateResult.append(res)
                    

    def work(self):
        # 首先获取所有待转换文件
        allFiles = self.getAllFiles(self.dataPath)
        for file in allFiles:
            #获取文件内容
            fileContent = self.getFileContent(file)
            # 获取他的转换结果
            translateResult = self.translateToText(fileContent)
            # 转存进文件
            self.saveResult(fileContent,translateResult, self.savePath + "/"+file)

if __name__ == "__main__":
    myCodeToData = CodeToData("./codeData", "./textData")
    myCodeToData.templateOfCalculate("a = (abd*1) + (8+3)+cd")