import subprocess
import os
import locale
import codecs
import time
import sys
import random
import re

shell_cmd = "cd E: && cd E:\PyProgramPack && pyinstaller -F -w Test.py"
# os.system("cd E:")
# print(os.system("cd E:"))
# output = subprocess.Popen("cd E: && cd E:\PyProgramPack && pyinstaller -F -w Test.py",stdin=subprocess.PIPE,stdout=subprocess.PIPE,shell=True).communicate()
# str = output[0]
# print("输出完成")
# print(str.decode("gbk"))
# print(subprocess.getoutput("cd E: && cd E:\PyProgramPack"))

import shlex
import subprocess

if __name__ == '__main__':
    # shell_cmd = 'python3 subprogram.py'
    print(shell_cmd)
    # p = subprocess.Popen(shell_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    r = os.popen(shell_cmd, 'r', 1)
    print(r.read())
    print(r.readlines())
    # out, err = p.communicate()
    # print(out)
    # while p.poll() is None:
    #     line = p.stdout.readline()
    #     line = line.strip() # 去掉一些特殊字符
    #     if line:
    #         print(line.decode("gbk"))
    #         # print('{}'.format(line.decode("gbk")))
    # if p.returncode == 0:
    #     print('Subprogram success')
    # else:
    #     print('Subprogram failed')

