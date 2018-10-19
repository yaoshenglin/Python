
import os
import shutil
import re
import time

# strPath = "E:\\PyProgramPack\\魔兽争霸ID互转工具.py"
# strPath = "E:\PyProgramPack\\Test.py"


# def CopyFile(srcfile,dstfile):
#     if not os.path.isfile(srcfile):
#         print("%s not exist!"%(srcfile))
#     else:
#         fpath,fname = os.path.split(dstfile)    #分离文件名和路径
#         oldPath = os.path.join(dstfile,os.path.basename(srcfile))   #旧文件路径
#         if os.path.isfile(oldPath):
#             print(oldPath)
#             os.remove(oldPath)                     # 先删除旧文件
#         if not os.path.exists(fpath):
#             os.makedirs(fpath)                #如果不存在，则创建路径
#         shutil.copy(srcfile,dstfile)          #移动文件
#         print("copy %s -> %s"%( srcfile,dstfile))

# CopyFile("E:\\程序目录\\工具\\subprocess功能测试.py","E:\\PyProgramPack")

def readFile(path):
    f = open(path, "r")
    jsonInfo = f.read()
    f.close()
    return eval(jsonInfo)

def writeFile(path, value):
    f = open(path, "w")
    f.write(str(value))
    f.close()

# list = [{'A':'1'},{'B':'2'}]
# writeFile('用户信息111.txt',list)
# list = readFile('用户信息111.txt')
# print(list)
# list = readFile('用户信息111.txt')
# tString = 'Shanshan Du,26,13698424612,Operation,2017-07-02'
# listValues = tString.split(',')
# listKeys = ['name','age','phone','job','date']
# dictInfo = {}
# print(listValues)
# for i in range(len(listKeys)):
#     key = listKeys[i]
#     value = listValues[i]
#     if i == 1:
#         dictInfo[key] = int(value)
#     else:
#         dictInfo[key] = value
# print(dictInfo)
# if not dictInfo in list:
#     list.append(dictInfo)
#
# print(len(list))
# writeFile('用户信息111.txt',list)

inputStr = "hello crifan, nihao crifan";
inputStr = re.sub(r"hello (\w+), nihao \1", "\g<1>", inputStr);
print(inputStr)

inputStr = "hello crifan, nihao crifan";
inputStr = re.sub(r"hello (?P<name>\w+), nihao (?P=name)", "\g<name>", inputStr)
print(inputStr)


def pythonReSubDemo():
    """
        demo Pyton re.sub
    """
    inputStr = "hello 123 world 456 nihao 789";

    def _add111(matched):
        intStr = matched.group("number");  # 123
        intValue = int(intStr);
        addedValue = intValue + 111;  # 234
        addedValueStr = str(addedValue);
        return addedValueStr;

    replacedStr = re.sub("(?P<number>\d+)", _add111, inputStr, 2);
    print("replacedStr=", replacedStr);  # hello 234 world 567 nihao 789


###############################################################################
if __name__ == "__main__":
    pythonReSubDemo();