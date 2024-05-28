import win32gui
import win32ui
import win32api
import win32con
import win32com
import time
# import numpy as np
# import cv2
from cnocr import CnOcr
rec_root="./models/cnocr"
det_root="./models/cnstd"
print('开始加载模型...')
ocr = CnOcr(cand_alphabet=[str],rec_root=rec_root,det_root=det_root)
print('模型加载成功')
# 地址 id x,y,x2,y2
def window_capture(filename,hwnd,x = 0,y = 0,w = 100,h = 100):
    hwnd = hwnd or 0  # 窗口的编号，0号表示当前活跃窗口
    # 根据窗口句柄获取窗口的设备上下文DC（Divice Context）
    # hwndDC = win32gui.GetWindowDC(hwnd)
    # 获取窗口的设备上下文Device Context。GetWindowDC包括了非客户区，而GetDC仅为客户区
    hwndDC = win32gui.GetDC(hwnd)
    # 根据窗口的DC获取mfcDC,（创建携带python方法的 python DC，用于执行python的操作，理解为此时还是上下文DC）
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    # mfcDC创建可兼容的DC,创建一个内存设备描述表
    saveDC = mfcDC.CreateCompatibleDC()
    # 创建bigmap（位图）准备保存图片
    saveBitMap = win32ui.CreateBitmap()
    # 获取窗口宽高信息
    # left,top,right,bottom = win32gui.GetWindowRect(hwnd)
    # w = right - left
    # h = bottom - top
    # saveBitMap.CreateCompatibleBitmap(mfcDC,w, h)
    # saveDC.SelectObject(saveBitMap)
    # saveDC.BitBlt((0,0), (w, h), mfcDC, (startX, starty), win32con.SRCCOPY)
    # 为bitmap开辟空间(以mfcDC对象创建一个兼容的bitmap)
    saveBitMap.CreateCompatibleBitmap(mfcDC,w,h)
    # 高度saveDC，将截图保存到saveBitmap中（把位图放入内存DC中）
    saveDC.SelectObject(saveBitMap)
    saveDC.BitBlt((0,0), (w,h), mfcDC, (x,y), win32con.SRCCOPY)
    # saveDC.BitBlt(((w-image['w'])/2,(h-image['h'])/2), (image['w'], image['h']), mfcDC, (0, 0), win32con.SRCCOPY)
    saveBitMap.SaveBitmapFile(saveDC, filename)
    # signedIntsArray = saveBitMap.GetBitmapBits(True)
    # img = np.frombuffer(signedIntsArray, dtype='uint8')
    # img = cv2.imread(img)
    # img = cv2.resize(img,(h,w),3)
    # img.shape = (h, w, 3)
    out = ocr.ocr_for_single_line(img_fp=filename)
    # 销毁DC
    win32gui.DeleteObject(saveBitMap.GetHandle())
    saveDC.DeleteDC()
    mfcDC.DeleteDC()
    return out['text']
array = []
# name = ''
name = ''
def getChildren(jubing, mouse,childrenS,chidrenNeed):
    if(win32gui.IsWindow(jubing) and win32gui.IsWindowVisible(jubing)):
        name = win32gui.GetWindowText(jubing)
        className = win32gui.GetClassName(jubing)
        # name = win32gui.GetWindowText(jubing)
        # print(name)
        # MacromediaFlashPlayerActiveX 为ie下的flash适配名称
        name = name if name else className
        if(True):
        # if(name.find('MacromediaFlashPlayerActiveX') != -1 and chidrenNeed):
            childrenS.append({
                'name': name,
                'processId': jubing,
                'className': className,
            })

def getProcessName(jubing, mouse,array,selectName):
    if(win32gui.IsWindow(jubing) and win32gui.IsWindowVisible(jubing)):
        name = win32gui.GetWindowText(jubing)
        className = win32gui.GetClassName(jubing)
        name = name if name else className
        if name.find(selectName) != -1:
            array.append({
                'name': name or className,
                'processId': jubing,
                'className': className,
            })
win32gui.EnumWindows(lambda j,m:getProcessName(j,m,array,name), 0)
# print(array)
for index,item in enumerate(array):
  childrenArray = []
  win32gui.EnumChildWindows(item['processId'],lambda a,b:getChildren(a,b,childrenArray,True),0)
  print(f"{index}. {item['name']}----{item['processId']}")
  if len(childrenArray) > 0:
    item['children'] = childrenArray
    for index2,item2 in enumerate(childrenArray):
      print(f"----{index2}. {item2['name']}----{item2['processId']}")

# hwnd = childrenArray[0]['processId']
# 窗口先设置为活跃再截图，父窗口才行
# win32gui.SetForegroundWindow(array[0]['processId'])
ids = input(f"""查询到 {len(array)} 条进程， 选择id，按下回车键（enter）:""").split(',')
hwnd = array[int(ids[0])]['processId'] if len(ids) == 1 else array[int(ids[0])]['children'][int(ids[1])]['processId']
print(hwnd)
startTime = time.time() * 1000
text = window_capture("position2.jpg",hwnd,115,76,67,20)
endTime = time.time() * 1000
print(f"""识别结果：{text} """)
print(f"""耗时：{endTime - startTime} ms""")