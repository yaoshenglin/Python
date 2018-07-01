
import sys

def calc(n,count):
    print(n,count)
    if count < 5:
        return calc(n/2,count+1)
    else:
        return n

res = calc(188,1)
print('res ',res)