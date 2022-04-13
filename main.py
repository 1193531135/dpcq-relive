from itertools import count
import win32gui
import win32api
import win32con
import time

import scapy.all as scapy

# import scapy_http.http

# 拉取全部的窗口
# array = []


# def getProcessName(jubing, mouse):
#     if(win32gui.IsWindow(jubing) and win32gui.IsWindowVisible(jubing)):
#   name = win32gui.GetWindowText(jubing)
#   if(name != ''):
#       array.append({
#     'name': name,
#     'processId': jubing,
#       })


# win32gui.EnumWindows(getProcessName, 0)

# # 选择窗口
# print('————————————————')
# print('|   id   | name')
# print('————————————————')
# lin = 1
# for x, index in array:
#     idName = f'{lin}'
#     if(len(idName) == 1):
#   idName = f'  {idName}    '
#     if(len(idName) == 2):
#   idName = f'  {idName}   '
#     if(len(idName) == 3):
#   idName = f'  {idName}  '
#     print(f'| {idName}| {array[lin-1][x]}')
#     lin += 1
# now_id = int(input('输入窗口id：'))
# windowProcess = array[now_id - 1]['processId']

# # 检索子窗口
# childrenS = []


# def getChildren(jubing, mouse):
#     if(win32gui.IsWindow(jubing) and win32gui.IsWindowVisible(jubing)):
#   name = win32gui.GetClassName(jubing)
#   if(name.find('MacromediaFlashPlayerActiveX') != -1):
#       childrenS.append({
#     'name': name or 'null',
#     'processId': jubing,
#       })

# win32gui.EnumChildWindows(windowProcess,getChildren,0)
# print(childrenS)

# windowProcess = childrenS[len(childrenS)-1]['processId']


# 退出全屏
# win32gui.ShowWindow(windowProcess,win32con.SW_SHOWNORMAL)

# # 强制修改窗口大小和位置
# windwo_width = 1920
# windwo_height = 1040
# windowHead = 110 #头部高度
# # 渲染器少两边少 8个像素
# win32gui.MoveWindow(windowProcess, 0, 0, windwo_width, windwo_height, True)

# time.sleep(2)

# long_position = win32api.MAKELONG(921, 545)#模拟鼠标指针 传送到指定坐标
# win32api.SendMessage(windowProcess, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, long_position)#模拟鼠标按下
# win32api.SendMessage(windowProcess, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, long_position)#模拟鼠标弹起


# 
stars = lambda n: "*" * n

def http_header(packet):
  http_packet=str(packet)
  if http_packet.find('POST') != -1 or http_packet.find('Get') != -1:
    # obj = http_packet.split('\r\n')
    # obj = http_packet.replace('\r\n','\n')
    # if obj[0].find('b'):
    #     obj = obj[1:]
    string = packet.sprintf("{Raw:%Raw.load%}\n")
#     print(string)
    if string.find('laien.test') != -1 and string.find('/crossPromo/manage/template/detail') != -1:
        print(string)
    # obj存在再往下
    # if len(obj) > 0:
    #     trueObj = {}
    #     for item in obj:
    #   arry = item.split(': ')
    #   print(arry)
    #   name = arry[0]
    #   trueObj[name] = arry[1]
    #     return trueObj

# def GET_print(packet1):
#     ret = "***************************************GET PACKET****************************************************\n"
#     ret += "\n".join(packet1.sprintf("{Raw:%Raw.load%}\n").split(r"\r\n"))
#     ret += "**************************************Get End*****************************************************\n"
#     return ret

scapy.sniff(prn=http_header, filter="tcp port 80")