#!/usr/bin/env python
# -*- coding: UTF-8 -*-
if __name__ == "__main__":
    f1 = open('C:\\Users\\wang\\Desktop\\new.txt', 'r+', encoding="utf-8")  # 以读写方式打开，可读可写
    f2= open('C:\\Users\\wang\\Desktop\\new2.txt', 'a', encoding="utf-8")  # 以读写方式打开，可读可写
    data = f1.readlines()  # 读取文件内容
    f1.seek(0)  # seek() 方法用于移动文件读取指针到指定位置。
    for i in data:  # 循环读取
        indexx = i.rfind('=')-1
        indexy = 0
        count = 0
        myindex = 0
        for ch in i:
            if ch == '.':
                count +=1;
            if count == 2:
                indexy = myindex+1
                break
            myindex +=1

        # print(indexx)
        # print(indexy)
        # print(i)
        getStr = i[indexy:indexx]
        print(i)
        print(getStr)
        i = i.replace("\"O2\"","\""+getStr+"\"")
        f2.write(i)
        print(i)
    f1.close()
    f2.close()