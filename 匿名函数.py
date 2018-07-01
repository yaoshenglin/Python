
print("")

#匿名函数，冒号前面代表参数，后面代表执行逻辑
calc = lambda x,y:x**y
print(calc(2,5))
print("")

# res = map(lambda x:x**2,[1,5,7,4,8])
res = map(lambda x,y:x**y,[2,2,2,2,2],[1,2,3,4,5])

# print(res.__iter__())

for x in res:
    print(x)