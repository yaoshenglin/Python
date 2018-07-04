
import os
import sys
import filetype
import shutil
import re
import string

strPath = "E:\\PyProgramPack\\魔兽争霸ID互转工具.py"
strPath = "E:\PyProgramPack\\Test.py"


def CopyFile(srcfile,dstfile):
    if not os.path.isfile(srcfile):
        print("%s not exist!"%(srcfile))
    else:
        fpath,fname = os.path.split(dstfile)    #分离文件名和路径
        oldPath = os.path.join(dstfile,os.path.basename(srcfile))   #旧文件路径
        if os.path.isfile(oldPath):
            print(oldPath)
            os.remove(oldPath)                     # 先删除旧文件
        if not os.path.exists(fpath):
            os.makedirs(fpath)                #如果不存在，则创建路径
        shutil.copy(srcfile,dstfile)          #移动文件
        print("copy %s -> %s"%( srcfile,dstfile))

if __name__ == '__main__':
    path = 'E:\\PyProgramPack\\Test.py'
    ftype = filetype.guess(path)
    print(ftype)
    allFileNum = 0
    print(os.path.abspath("Test.py"))
    # CopyFile("E:\\程序目录\\第二模块练习\\PyInstaller打包工具.py","E:\\PyProgramPack")

    listCommon = ['E:','cd '+os.path.dirname(strPath),'strCommand']
    print(' & '.join(listCommon))



