
import os
import sys
import urllib.request
# import urllib2

#根据路径读取数据
def readFile(filePath):
    if os.path.isfile(filePath):
        # 文件存在
        f = open(filePath, "rb")
        s = f.read()
        s = s.decode("utf8")
        f.close()
        return s

#根据路径写入数据
def writeFile(filePath, content):
    strDir = os.path.dirname(filePath)
    if os.path.isdir(strDir) :
        f = open(filePath, "wb")
        content = content.encode("utf8")
        f.write(content)
        f.close()
    else:
        print("路径不存在，写入失败")

filePath = "E:\程序目录\文件\content.html"
url = "http://mail.126.com"
url = "http://www.google.com"

#发起请求
req = urllib.request.Request(url)

fd = urllib.request.urlopen(req,10)
# data = fd.read()

print ("URL Retrieved:",fd.geturl())

info = fd.info()
for key,value in info.items():
    print ("%s           =              %s" % (key,value))

data = fd.read()
if not len(data):
    print("没有获取到数据")
    exit(0)

# 输出结果
s = data.decode("utf8")
writeFile(filePath,s)
# print(data.decode("utf8"))
