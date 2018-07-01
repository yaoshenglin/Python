
def stu_register(name,age,course="Python",country="CN"):
    print(name,age,country,course)

stu_register("王山炮", 22, "EN", "linux")
stu_register(name="张叫春",age=21)

def stu_register(name,age,*args):
    print(name,age,args)

stu_register("王山炮",22,"EN","linux")
stu_register(name="张叫春",age=21)

def stu_register(name,age,*args):
    print(name,age,args)

stu_register("王山炮",27,*["EN","linux"])
stu_register(name="张叫春",age=21)


def stu_register(name,age,**args):
    print(name,age,args)

stu_register("王山炮1",23,country="EN",course="linux")
data = stu_register(name="张叫春1",age=22)

print(data,"\n")


name = "Alex Li"
age = 22

def change_name():
    # global name
    name = "金角大王，一个有Tesla的男人"
    age = 25
    print("after change",name,age)

change_name()
print("在外面看看name改了么？",name,age)

print("")
def change_name():
    global name,age #引用全局变量
    name = "金角大王，一个有Tesla的男人"
    age = 25
    print("after change",name,age)

change_name()
print("在外面看看name改了么？",name,age)