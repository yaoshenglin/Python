#!/usr/bin/python3
# -*- coding:utf-8 -*-
__author__ = 'YSL-PC'

import os
import re

def readFile(path):
    f = open(path, "r")
    jsonInfo = f.read()
    f.close()
    return eval(jsonInfo)

def writeFile(path, dicInfo):
    f = open(path, "w")
    value = str(dicInfo)
    f.write(value)
    f.close()

class staff(object):               #员工类
    def __init__(self,*args):      #员工信息初始化：从字符串列表传参赋值
        self.id = 0 if len(args) < 1 else args[0]
        self.name = '' if len(args) < 2 else args[1]
        self.age = 0 if len(args) < 3 else args[2]
        self.phone = '' if len(args) < 4 else args[3]
        self.dept = '' if len(args) < 5 else args[4]
        self.enroll_date = '' if len(args) < 6 else args[5]
        self.allinfo = '' if len(args) == 0 else ','.join(args)
        # print(len(args))
        # print(args)
    def update(self,**kwargs):       #员工信息更新：从字典传参赋值
        if 'id' in kwargs:
            self.id = kwargs['id']
        if 'name' in kwargs:
            self.name = kwargs['name']
        if 'age' in kwargs:
            self.age = kwargs['age']
        if 'phone' in kwargs:
            self.phone = kwargs['phone']
        if 'dept' in kwargs:
            self.dept = kwargs['dept']
        if 'enroll_date' in kwargs:
            self.enroll_date = kwargs['enroll_date']
        self.allinfo = ','.join(map(str,[self.id, self.name, self.age, self.phone, self.dept, self.enroll_date]))
    def print_info(self,info):     #员工信息打印显示：传入的参数为"*"或数据记录的若干个关键字
        if info == '*':
            print(self.allinfo)
        else:
            info = info.split(',')
            res = []
            for i in info:
                if hasattr(self,i.strip()):
                    res.append(str(getattr(self,i.strip())))
            print(','.join(res))

def verify(staff_temp,condition):             #员工信息验证函数，传入一个员工对象和条件字符串
    if condition.strip() == '*':return True   #如果条件为'*',即所有记录都满足条件
    condition_list = condition.split()           #检索条件字符串转列表
    if len(condition_list) == 0:return False
    logic_str = ['and','or','not']    #逻辑运算字符串 且、或、非
    logic_exp = []                  #单个条件的逻辑表达式组成的列表，形如[‘age',' ','>','=',20] 或 [‘dept',' ','like',' ','HR']
    logic_list = []                 #每个条件的表达式的计算结果再重组后的列表，形如 [‘True','and','False','or','not','False']
    for i in condition_list:
        if i in logic_str:
            if( len(logic_exp) != 0 ):
                logic_list.append(str(logic_cal(staff_temp,logic_exp)))  #逻辑表达式计算并将返回的True或False转化成字符串添加到列表
            logic_list.append(i)
            logic_exp = []
        else:
            logic_exp.append(i)
    value = logic_cal(staff_temp, logic_exp)
    logic_list.append(str(value))
    return eval(' '.join(logic_list))    #列表转化成数学表达式完成所有条件的综合逻辑运算，结果为True或False

def logic_cal(staff_temp,logic_exp):   #单个逻辑表达式的运算函数
    # print('logic_exp',logic_exp)
    logic_exp = re.search('(.+?)([<>=]{1,2}|like)(.+)',''.join(logic_exp))  #表达式列表优化成三个元素，形如[‘age','>=',20] 或 [‘dept','like','HR']
    if(logic_exp):
        logic_exp = list(logic_exp.group(1,2,3))
        if(hasattr(staff_temp,logic_exp[0])):
            logic_exp[0] = getattr(staff_temp,logic_exp[0])
        else:
            return False
        if logic_exp[1] == '=':        #指令中的'='转化成程序中相等判别的"=="
            logic_exp[1] = '=='
        if logic_exp[1] == 'like':     #运算符为like的表达式运算
            return re.search(logic_exp[2].strip("'").strip('"'),logic_exp[0]) and True
        elif(logic_exp[0].isdigit() and logic_exp[2].isdigit()):   #两头为数字的运算，直接eval函数转数学表达式
            return eval(''.join(logic_exp))
        elif(logic_exp[1] == '=='):    #非数字的运算，即字符串运算，此时逻辑符只可能是‘=’，若用eval函数则字符串会转成无定义变量而无法计算，所以拿出来单独用"=="直接计算
            return logic_exp[0] == logic_exp[2].strip("'").strip('"')   #字符串相等判别，同时消除指令中字符串引号的影响，即输引号会比记录中的字符串多一层引号
        else:          #其他不合语法的条件格式输出直接返回False
            return False
    else:
        return False

def error(command):        #错误提示函数，指令不合语法调用该函数报错
    print('\033[31;1m语法错误，请重新输入！\033[0m\n')

def getContion(command):
    condition = '*'
    command = command.strip()
    if len(command) > 0:
        # command_parse = re.search('([0-9a-zA-Z\_]+)\s+(.*)', command)
        command_parse = re.search('^where\s+(.*)', command)  # 限制条件语法where
        if command_parse:
            condition = command_parse.group(1)
        else:
            condition = ''

    return condition

def command_exe(command):   #指令执行主函数，根据指令第一个字段识别何种操作，并分发给相应的处理函数执行
    command = command.strip()
    dictCommand = {
        'add':add,
        'delfrom':delfrom,
        'update':update,
        'find':find,
    }
    headerType = command.split()[0]     # 语法类型
    # print(headerType)
    f = dictCommand.get(headerType,error)
    return f(command)

def find(command):
    command = command.strip()
    command_parse = re.search(r'find\s+(.+)\s+from\s+([0-9a-zA-Z\_]+)\s*(.*)', command)  # 指令解析
    # print(command_parse)
    if command_parse:
        info = command_parse.group(1).strip()  # 检索结束后需显示的信息，"*"为显示整体记录
        tableName = command_parse.group(2).strip()  # 表名
        condition = command_parse.group(3).strip()  # 检索条件
        condition = getContion(condition)
        if len(condition) == 0 :
            error(command)
            return
        listInfo = dictInfo.get(tableName)  # 根据表名获取对应全部数据
        listInfo = [] if listInfo == None else listInfo
        count = 0
        staff_list = []
        for line in listInfo:
            # print(line)
            staff_temp = staff(*line.strip().split(','))
            if (verify(staff_temp, condition)):  # 验证员工信息是否符合条件
                count += 1
                staff_list.append(staff_temp)
        print("数据库本次共\033[31;1m查询到%d条\033[0m员工信息，如下:" % count)
        for staff_temp in staff_list:
            staff_temp.print_info(info)  # 查询记录打印
    else:
        error(command)

def add(command):        #增加员工记录函数
    command_parse = re.search(r'add\s+([0-9a-zA-Z\_]+)\s+(.*)',command)    #正则表达式指令解析
    if(command_parse):
        tableName = command_parse.group(1)  # 表名
        if len(tableName) > 0:
            listInfo = dictInfo.get(tableName)  # 根据表名获取对应全部数据
            listInfo = [] if listInfo == None else listInfo
            info = command_parse.group(2).strip()       #需新增的员工信息，不含id
            id = 0                                      #新增员工id
            for line in listInfo:
                # print(line)
                staff_temp = staff(*line.strip().split(','))
                # print(type(staff_temp.id))
                if int(staff_temp.id) > id:
                    id = int(staff_temp.id)
            id += 1
            info_new = ''.join([str(id),',',info])  #id与其他信息合并成完整记录
            listInfo.append(info_new)
            dictInfo[tableName] = listInfo
            writeFile(path,dictInfo)
            print("数据库本次\033[31;1m新增1条\033[0m员工信息：\n%s"%info_new)  #新增记录打印
        else:
            error(command)
    else:
        error(command)

def delfrom(command):    #删除员工记录函数
    command_parse = re.search(r'delfrom\s+([0-9a-zA-Z\_]+)\s*(.*)',command)   #指令解析
    # print(command_parse.groups())
    if(command_parse):
        tableName = command_parse.group(1)  # 表名
        condition = command_parse.group(2).strip()  #检索条件
        condition = getContion(condition)
        if len(condition) == 0 :
            error(command)
            return
        count = 0           #删除记录计数
        staff_list = []     #删除记录的员工对象列表
        listInfo = dictInfo.get(tableName)  # 根据表名获取对应全部数据
        listInfo = [] if listInfo == None else listInfo
        listInfoCopy = listInfo.copy()
        # print(condition)
        for line in listInfoCopy:
            staff_temp = staff(*line.strip().split(','))
            if (verify(staff_temp, condition)):  #验证员工信息是否符合条件
                count += 1
                staff_list.append(staff_temp)
                listInfo.remove(line)
                # continue
        # print(listInfo)
        dictInfo[tableName] = listInfo
        writeFile(path, dictInfo)
        print("数据库本次共\033[31;1m删除%d条\033[0m员工信息，如下:"%count)
        for staff_temp in staff_list:
            staff_temp.print_info('*')   #删除记录打印
    else:
        error(command)

def update(command):     #修改和更新员工记录函数
    command_parse=re.search(r'update\s+(.*?)\s+set\s+(.*?)\s+where\s+(.*)',command)   #指令解析
    # print(command_parse.groups())
    if(command_parse):
        tableName = command_parse.group(1).strip()  # 表名
        info = command_parse.group(2).strip()       #需更新的信息
        condition = command_parse.group(3).strip()  #检索条件
        if len(condition) == 0 :
            error(command)
            return

        listInfo = dictInfo.get(tableName)  # 根据表名获取对应全部数据
        listInfo = [] if listInfo == None else listInfo
        info = ''.join(['{', info.replace('=', ':'), '}'])   #将需更新的信息按字典格式修饰字符串
        info = eval(re.sub(r'(\w+)\s*:', r'"\1":', info))    #将字符串进一步修饰最终转化成字典
        count = 0
        staff_list = []
        for i in range(len(listInfo)):
            line = listInfo[i]
            staff_temp = staff(*line.strip().split(','))
            if(verify(staff_temp,condition)):    #验证员工信息是否符合条件
                staff_temp.update(**info)        #调用员工对象成员函数更新信息
                count += 1
                staff_list.append(staff_temp)
                line = staff_temp.allinfo
                listInfo[i] = line
        dictInfo[tableName] = listInfo
        writeFile(path, dictInfo)
        print("数据库本次共\033[31;1m更新%d条\033[0m员工信息，如下:"%count)
        for staff_temp in staff_list:
            staff_temp.print_info('*')  #更新记录打印
    else:
        error(command)

if __name__=='__main__':     #主函数，数据库指令输入和执行
    dictInfo = {}
    path = os.path.abspath("用户信息.txt")
    if os.path.exists(path) : dictInfo = readFile(path)
    while(True):
        command=input("请按语法输入数据库操作指令：")    #指令输入
        if command=='exit':
            print("数据库操作结束，成功退出！".center(50, '*'))
            break
        command_exe(command)        #指令执行
    # command_exe('find name,age from staff_table where age >22')
    # command_exe('add staff_table Alex Li,25,134435344,IT,2015-10-29')
    # command_exe('delfrom staff_table where id=1')
    # command_exe('update staff_table set dept="Market" where dept="IT"')
