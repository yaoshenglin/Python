# -*- coding: UTF-8 -*-

print "Hello world"
print("Hello, World!");


def changeme( mylist ):
    mylist.append([1,2,3,4]);
    print "函数内取值: ", mylist
    return

# Call changeme function
mylist = [10,20,30];
changeme( mylist );
print "ccc: ", mylist
