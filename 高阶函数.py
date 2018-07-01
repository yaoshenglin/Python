import math
# import sys
# sys.setrecursionlimit(100)
# print(sys.getrecursionlimit())

def pow2(x):
    return x**2

def powN(x,y):
    return x**y

def add(x,y,f):
    return f(x) + f(y)

res = add(3,-6,pow2)
print(res)

def powT(x,y,f):
    return f(x,3)+f(y,5)

res = powT(3,2,powN)
print(res)