
name = "Alex Li"

def change_name():
    name = "Alex2"

    def change_name2():
        name = "Alex3"
        print("第三层打印：",name)

    change_name2()
    print("第二层打印：",name)

change_name()
print("在外面看看name改了么？",name)