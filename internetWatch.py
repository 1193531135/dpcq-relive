import re
import threading

def threadingOpen(func):
    threaProcess = threading.Timer(1,threadingOpen,args=func)
    threaProcess.start()
def LInput(text,reg):
    val = input(text)
    if (not re.search(reg,val)) == False:
        print(not(re.search(reg,val)))
        print('非法输入，请重新输入')
        LInput(text,reg)
    else:
        return val
# LInput('input:',r'^[a-z]{1,2}$')
time = 0
time2 = 1
def printff():
    time = time + 1
    print('time =>>>>> ',time)
def printff2():
    time2 = time2 + 1
    print('time2 =>>>>> ',time2)
threadingOpen(printff)
threadingOpen(printff2)