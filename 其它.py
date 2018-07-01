
import subprocess

p = subprocess.Popen("date", stdout=subprocess.PIPE, shell=True)
subp=subprocess.Popen('date',shell=True,stdout=subprocess.PIPE)
while subp.poll()==None:
    line = p.stdout.readline()
    line = line.strip()
    if line:
        print(line.decode("gbk"))
## Talk with date command i.e. read data from stdout and stderr. Store this info in tuple
## Interact with process: Send data to stdin. Read data from stdout and stderr,
## until end-of-file is reached.Wait for process to terminate. The optional input
## argument should be a string to be sent to the child process, or None,
## if no data should be sent to the child. ##
print("wait")
(output, err) = p.communicate()
print("wait")
## Wait for date to terminate. Get return returncode ##
p_status = p.wait()
print("Command output : ", output)
print("Command exit status/return code : ", p_status)

subp=subprocess.Popen('python -u /tmp/test.py',shell=True,stdout=subprocess.PIPE)
# while subp.poll()==None:
#     pass
#     print(subp.readline())
print(subp.returncode)