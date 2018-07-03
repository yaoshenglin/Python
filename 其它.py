
import subprocess
import os

strPath = "D:\\Program Files (x86)\\Python35\\Lib\\site-packages\\PyInstaller\\utils\\cliutils\\grab_version.py"
strPath = "E:\\PyProgramPack\\PyInstaller\\utils\\cliutils\\grab_version.py"
strPath = "E:\PyProgramPack\config.exe"

fileDir, fileName = os.path.split(strPath)

if os.path.isfile(strPath):

    shell_cmd = "cd D: && cd %s && python %s D:\Program Files\JassShopPro1.4.7\config.exe"%(fileDir,strPath)
    shell_cmd = "cd D: && cd %s && pyi-grab_version %s"%(fileDir,strPath)

    print(shell_cmd)
    return_code = os.system(shell_cmd)  # 执行shell命令

    print(return_code)
else:
    print("文件没有发现")