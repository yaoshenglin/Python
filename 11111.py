# this method is used for monitoring

import time
import subprocess
import locale
import codecs
import threading


alist = []


def getstdout(p, asy):
    if asy:
        alist.clear()
    mylist = []
    while True:
        data = p.stdout.readline()
        if data == b'':
            if p.poll() is not None:
                break
        else:
            if asy:
                alist.append(data.decode(codecs.lookup(locale.getpreferredencoding()).name))
            else:
                mylist.append(data.decode(codecs.lookup(locale.getpreferredencoding()).name))
    return mylist

while True:
    ps = subprocess.Popen('netstat -an | findstr "8080"', stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
    resultlist = getstdout(ps, False)
    if len(resultlist) >= 1:
        newlist = []
        for i in alist:
            if i.find('192.168') > 0:
                newlist.append(i)
        newlist.sort()
        print('Sum of requests from LAN:', len(newlist))
    else:
        print(time.strftime("%Y-%m-%d %H:%M:%S"))
        subprocess.Popen('taskkill.exe /f /im node.exe', shell=False)
        time.sleep(3)
        pss = subprocess.Popen('start cmd.exe /k node app.js', stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE, shell=True)
        th = threading.Thread(target=getstdout, args=[pss, True])
        th.start()
    time.sleep(10)