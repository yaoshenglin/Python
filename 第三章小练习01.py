
# 1.输入用户名密码，正确后登录系统，打印
#   1.修改个人信息
#   2.打印个人信息
#   3.修改密码
# 2.每个选项写一个方法
# 3.登录时输错3次退出程序

import pathlib

def writeFile(path,content):
    f = open(path,"w")
    f.write(content)
    f.close()

def readFile(path):
    f = open(path, "r")
    content = f.read()
    f.close()
    return content

dictInfo = {"alex":{"password":"abc123","age":24,"position":"Engineer","department":"IT"},
            "rain": {"password":"df2@432", "age":25, "position":"Teacher", "department":"Teching"}}

filePath = "E:\程序目录\文件\用户信息.txt"
path = pathlib.Path(filePath)
if path.exists() == False:
    strInfo = str(dictInfo)
    writeFile(filePath,strInfo)


def modify_info():
    print("1.修改年龄\n2.修改职位\n3.修改部门")
    content = input("请输入你要选择的操作：")

def show_info(x):
    print(x)


step = 1
while step > 0:
    print("1.修改个人信息\n2.打印个人信息\n3.修改密码\n0.退出")
    content = input("请输入你要选择的操作：")
    if content.isdigit():
        value = int(content)
        if value == 1:
            modify_info()
        elif value == 2:
            pass
        elif value == 3:
            pass
        else:
            step = 0
    else:
        print("输入有误，请重新输入")