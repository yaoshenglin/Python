import subprocess
import os
import shutil
from time import sleep
import subprocess

strPath = "E:\PyProgramPack\Test.py"
fileDir, fileName = os.path.split(strPath)
shell_cmd = "E: && cd %s && pyinstaller -F --version-file=file_version_info.txt --icon=tubiao\\bitbug_favicon.ico %s"%(fileDir,fileName)
# os.system("cd E:")
# print(os.system("cd E:"))
# output = subprocess.Popen("cd E: && cd E:\PyProgramPack && pyinstaller -F -w Test.py",stdin=subprocess.PIPE,stdout=subprocess.PIPE,shell=True).communicate()
# str = output[0]
# print("输出完成")
# print(str.decode("gbk"))
# print(subprocess.getoutput("cd E: && cd E:\PyProgramPack"))

# 根据路径删除文件
def DeleteFile(path):
    if os.path.exists(path):
        print("删除 --> "+path)
        if os.path.isfile(path):
            os.remove(path) #文件
        elif os.path.isdir(path):
            shutil.rmtree(path) #目录

def MoveFile(srcfile,dstfile):
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
        print("move %s -> %s"%( srcfile,dstfile))

if __name__ == '__main__':
    # shell_cmd = 'python3 subprogram.py'
    print(shell_cmd)
    return_code = os.system(shell_cmd)  # 执行shell命令
    # p = subprocess.Popen(shell_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    # r = os.popen(shell_cmd, 'r', 1)
    # print(r.read())
    # out, err = p.communicate()
    if return_code == 0:
        print("执行成功")
    else:
        print("执行异常，错误代号：%d"%return_code)

    sleep(1.5)
    path1 = os.path.join(fileDir, "__pycache__")
    path2 = os.path.join(fileDir, "build")
    path3 = os.path.join(fileDir, os.path.splitext(fileName)[0] + ".spec")
    path4 = os.path.join(fileDir, "dist", os.path.splitext(fileName)[0] + ".exe")
    MoveFile(path4, fileDir)
    path4 = os.path.join(fileDir, "dist")
    listPath = [path1, path2, path3, path4]
    for i in range(len(listPath)):
        path = listPath[i]
        DeleteFile(path)

