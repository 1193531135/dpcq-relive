import win32gui
import win32ui
import win32api
import win32con
import win32com
import time
import json
import threading
def getPixel(hwnd,position,hwndDC):
    x,y = position
    hwndDC = hwndDC or win32gui.GetDC(hwnd)
    pixel = win32gui.GetPixel(hwndDC,x,y)
    return pixel
    
def window_capture(filename,hwnd):
    hwnd = hwnd or 0  # 窗口的编号，0号表示当前活跃窗口
    # 获取窗口的设备上下文Device Context。GetWindowDC包括了非客户区，而GetDC仅为客户区
    hwndDC = win32gui.GetDC(hwnd)
    # 获取监控器信息
    left,top,right,bottom = win32gui.GetWindowRect(hwnd)
    w = right - left
    h = bottom - top
    # 获取居中的像素点
    # (-1 -1 1120657) (0 -1 1120657) (1 -1 1120657)
    # (-1 0 1316745) (0 0 399157) (0 0 399157)
    # (-1 1 399157) (0 1 399157) (1 1 13497846)
    pixel = win32gui.GetPixel(hwndDC,int(w/2 -1),int(h/2 + 50))
    print(pixel)
# window_capture("haha.jpg")
array = []
childrenArray = []
# name = ''
name = '175游戏浏览器'
def getChildren(jubing, mouse,childrenS,chidrenNeed):
    # chidrenNeed为false检索qq浏览器子进程text名 =>  '无标题 - QQ浏览器'
    if(win32gui.IsWindow(jubing) and win32gui.IsWindowVisible(jubing)):
        name = win32gui.GetClassName(jubing) if chidrenNeed else win32gui.GetWindowText(jubing)
        # name = win32gui.GetWindowText(jubing)
        # print(name)
        # MacromediaFlashPlayerActiveX 为ie下的flash适配名称
        if(name.find('MacromediaFlashPlayerActiveX') != -1 and chidrenNeed):
            childrenS.append({
                'name': name or 'null',
                'processId': jubing,
            })

def getProcessName(jubing, mouse,array,selectName):
    if(win32gui.IsWindow(jubing) and win32gui.IsWindowVisible(jubing)):
        name = win32gui.GetWindowText(jubing)
        if name.find(selectName) != -1:
            array.append({
                'name': name,
                'processId': jubing,
            })
win32gui.EnumWindows(lambda j,m:getProcessName(j,m,array,name), 0)
# print(array)
win32gui.EnumChildWindows(array[0]['processId'],lambda a,b:getChildren(a,b,childrenArray,True),0)
print(childrenArray)
hwnd = childrenArray[0]['processId']
# 窗口先设置为活跃再截图，父窗口才行
# win32gui.SetForegroundWindow(array[0]['processId'])
# window_capture("haha.jpg",hwnd)
sum = 0
interval = 1
def openThreading():
    global sum,interval
    sum = sum + 1
    print(sum)
    threaProcess = threading.Timer(interval,openThreading)
    threaProcess.start()
openThreading()
# beg = time.time()
# for i in range(10):
#     window_capture("haha.jpg")
# end = time.time()
# print(end - beg)