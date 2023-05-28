import win32gui
import win32ui
import win32api
import win32con
import win32com
import time

def window_capture(filename,hwnd):
    hwnd = hwnd or 0  # 窗口的编号，0号表示当前活跃窗口
    # 根据窗口句柄获取窗口的设备上下文DC（Divice Context）
    hwndDC = win32gui.GetWindowDC(hwnd)
    # 获取窗口的设备上下文Device Context。GetWindowDC包括了非客户区，而GetDC仅为客户区
    hwndDC = win32gui.GetDC(hwnd)
    # 根据窗口的DC获取mfcDC
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    # mfcDC创建可兼容的DC
    saveDC = mfcDC.CreateCompatibleDC()
    # 创建bigmap准备保存图片
    saveBitMap = win32ui.CreateBitmap()
    # 获取监控器信息
    # left,top,right,bottom = win32gui.GetWindowRect(hwnd)
    left,top,right,bottom = win32gui.GetWindowRect(hwnd)
    w = right - left
    h = bottom - top
    # print w,h　　　#图片大小
    image = { 'w':100,'h':100 }
    # 截取从左上角（0，0）长宽为（w，h）的图片
    startX = int(w/2+132)
    starty = int(h/2-230)
    # 为bitmap开辟空间
    saveBitMap.CreateCompatibleBitmap(mfcDC,image['w'], image['h'])
    # 高度saveDC，将截图保存到saveBitmap中
    saveDC.SelectObject(saveBitMap)
    saveDC.BitBlt((0,0), (image['w'], image['h']), mfcDC, (startX, starty), win32con.SRCCOPY)
    # saveDC.BitBlt(((w-image['w'])/2,(h-image['h'])/2), (image['w'], image['h']), mfcDC, (0, 0), win32con.SRCCOPY)
    saveBitMap.SaveBitmapFile(saveDC, filename)

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
window_capture("position.jpg",hwnd)
# ocr = PaddleOCR(use_angle_cls = True,lang="en")
# text=ocr.ocr("./position.jpg",cls=True)
# print(text)
# beg = time.time()
# for i in range(10):
#     window_capture("haha.jpg")
# end = time.time()
# print(end - beg)