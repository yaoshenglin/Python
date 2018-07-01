
def writeDefaultData(x):
    f = open(filePath, "w")
    for i in range(8):
        content = "%d.中国，你好" % (i + 1)
        if i < 7:
            content = content + "\n"
        f.write(content)
        # print(i)
    f.close()

filePath = "E:\程序目录\文件\write.txt"

# writeDefaultData(filePath)

f = open(filePath,"a")

if f.seekable():
    f.seek(13)
f.write("[路飞学城]")
# f.truncate(35)
#
# i = 10
# while i > -1 :
#     data = f.readline()
#     if len(data) == 0:
#         i = 0
#         break
#     print("%s %d"%(data,f.tell()))
#     i -= 1

f.close()