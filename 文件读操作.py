
# import chardet

filePath = "E:\程序目录\文件\write.txt"
f = open(file=filePath,mode="rb")
data = f.read()
print(data.decode("gbk"))

f.close()

print("------------------")

f = open("E:\程序目录\文件\write.txt","r")
for i in f:
    i = i.replace("\n","")
    print(i)

f.close()

