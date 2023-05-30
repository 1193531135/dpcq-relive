import win32gui
import win32ui
import win32api
import win32con
import win32com
import time
import json
import threading
import re
def getPixel(hwnd,position,hwndDC):
    x,y = position
    hwndDC = hwndDC or win32gui.GetDC(hwnd)
    pixel = win32gui.GetPixel(hwndDC,x,y)
    return pixel
def mouseClick(windowProcess,x,y):
    # print(x,y)
    x = int(x)
    y = int(y)
    long_position = win32api.MAKELONG(x, y)#模拟鼠标指针 传送到指定坐标
    win32api.SendMessage(windowProcess, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, long_position)#模拟鼠标按下
    win32api.SendMessage(windowProcess, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, long_position)#模拟鼠标弹起
def window_capture(filename,hwnd):
    hwnd = hwnd or 0  # 窗口的编号，0号表示当前活跃窗口
    # 获取窗口的设备上下文Device Context。GetWindowDC包括了非客户区，而GetDC仅为客户区
    hwndDC = win32gui.GetDC(hwnd)
    # 获取监控器信息
    left,top,right,bottom = win32gui.GetWindowRect(hwnd)
    w = right - left
    h = bottom - top
    width = w
    height = h
    # 获取居中的像素点
    # (-1 -1 1120657) (0 -1 1120657) (1 -1 1120657)
    # (-1 0 1316745) (0 0 399157) (0 0 399157)
    # (-1 1 399157) (0 1 399157) (1 1 13497846)
    # pixel = win32gui.GetPixel(hwndDC,int(w/2),int(h/2 + 50))
    # mouseClick(hwnd,(width/2-45),(height/2-130))
    def sss(x,y):
        mouseClick(hwnd,int(x),int(y))
        return win32gui.GetPixel(hwndDC,int(x),int(y))
    # pixel = sss((width/2-75),(height/2+74))
    def goodsDown(PageOneX,PageOneY,goodsRowID,goodsColumnID):
        PageOneX = width/2 - 135
        PageOneY = height/2-210
        x = (PageOneX-6) + ((goodsColumnID - 1)*39)
        y = PageOneY + (goodsRowID*39)
        # mouseClick(hwnd,x,y)
        print()
        return [x,y]
    def BackPageDown(pageSize):
      OnePageX = width/2 - 135
      clienX = OnePageX + ((pageSize-1)*40)
      clienY = height/2-210
      mouseClick(hwnd,clienX,clienY)
      # 切换页面过快，等待0.5s再点击物品
      return [OnePageX,clienY]
    x,y = goodsDown(1,1,1,1)
    # x = width/2 + 132
    # y = height/2 + 192
    # 8903149
    # BackPageDown(2)
    # mouseClick(hwnd,int(x),int(y))
    # time.sleep(0.3)
    pixel = win32gui.GetPixel(hwndDC,int(x),int(y)) 
    # mouseClick(hwnd,int(x),int(y))
    # pixel = win32gui.GetPixel(hwndDC,int(w/2+90),int(h/2-115)) 
    # 65280 挂机检测右上点 （站立）
    # pixel = win32gui.GetPixel(hwndDC,int(w/2 + 162),int(h/2 - 240)) 
    # 65280 挂机检测右下点（站立）
    # pixel = win32gui.GetPixel(hwndDC,int(w/2 + 162),int(h/2 - 220)) 
    # 65280 挂机检测左下下点（站立）
    # pixel = win32gui.GetPixel(hwndDC,int(w/2 + 132),int(h/2 - 240)) 

    # 65280 挂机检测右上点
    # pixel = win32gui.GetPixel(hwndDC,int(w/2 + 162),int(h/2 - 270)) 
    # 65280 挂机检测右下点
    # pixel = win32gui.GetPixel(hwndDC,int(w/2 + 162),int(h/2 - 250)) 
    # 65280 挂机检测左上点
    # pixel = win32gui.GetPixel(hwndDC,int(w/2 + 132),int(h/2 - 270)) 
    # 65280 挂机检测左下点
    # pixel = win32gui.GetPixel(hwndDC,int(w/2 + 132),int(h/2 - 260)) 
    print(pixel)
    print(pixel == 65280)
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
window_capture("haha.jpg",hwnd)
# sum = 0
# time1 = 1
# def setInterval1s():
#     global sum
#     sum = sum + 1
#     print(sum)
#     threaProcess = threading.Timer(1,setInterval1s)
#     threaProcess.start()
# setInterval1s()
# beg = time.time()
# for i in range(10):
#     window_capture("haha.jpg")
# end = time.time()
# print(end - beg)