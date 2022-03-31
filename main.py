import win32gui
import win32api
import win32con

# 拉取全部的窗口
array = []


def getProcessName(jubing, mouse):
    if(win32gui.IsWindow(jubing) and win32gui.IsWindowVisible(jubing)):
        name = win32gui.GetWindowText(jubing)
        if(name != ''):
            array.append({
                'name': name,
                'processId': jubing,
            })


win32gui.EnumWindows(getProcessName, 0)

# 选择窗口
print('————————————————')
print('|   id   | name')
print('————————————————')
lin = 1
for x, index in array:
    idName = f'{lin}'
    if(len(idName) == 1):
        idName = f'  {idName}    '
    if(len(idName) == 2):
        idName = f'  {idName}   '
    if(len(idName) == 3):
        idName = f'  {idName}  '
    print(f'| {idName}| {array[lin-1][x]}')
    lin += 1
now_id = int(input('输入窗口id：'))
windowProcess = array[now_id - 1]['processId']

# # 检索子窗口
# childrenS = []


# def getChildren(jubing, mouse):
#     if(win32gui.IsWindow(jubing) and win32gui.IsWindowVisible(jubing)):
#         name = win32gui.GetWindowText(jubing)
#         if(name != ''):
#             childrenS.append({
#                 'name': name,
#                 'processId': jubing,
#             })


# win32gui.EnumChildWindows(windowProcess,getChildren,0)
# print(childrenS)


# 退出全屏
win32gui.ShowWindow(windowProcess,win32con.SW_SHOWNORMAL)

# 强制修改窗口大小和位置
windwo_width = 1920
windwo_height = 1040
windowHead = 113 #头部高度
# 渲染器少两边少 8个像素
win32gui.MoveWindow(windowProcess, 0, 0, windwo_width, windwo_height, True)


long_position = win32api.MAKELONG(int(windwo_width/2), int((windwo_height-windowHead)/2) + windowHead)#模拟鼠标指针 传送到指定坐标
win32api.SendMessage(windowProcess, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, long_position)#模拟鼠标按下
# win32api.SendMessage(windowProcess, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, long_position)#模拟鼠标弹起
