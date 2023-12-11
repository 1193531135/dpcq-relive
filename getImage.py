import win32gui
import win32ui
import win32api
import win32con
import win32com
import time

def window_capture(filename,hwnd):
    hwnd = hwnd or 0  # 窗口的编号，0号表示当前活跃窗口
    # 根据窗口句柄获取窗口的设备上下文DC（Divice Context）
    # hwndDC = win32gui.GetWindowDC(hwnd)
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
    image = { 'w':200,'h':200 }
    # 截取从左上角（startX，starty）长宽为（w，h）的图片
    startX = int(0)
    starty = int(0)
    nameImage = [(108,18),(126,20)]
    # # 为bitmap开辟空间
    # saveBitMap.CreateCompatibleBitmap(mfcDC,w, h)
    # # 高度saveDC，将截图保存到saveBitmap中
    # saveDC.SelectObject(saveBitMap)
    # saveDC.BitBlt((0,0), (w, h), mfcDC, (startX, starty), win32con.SRCCOPY)
    # 为bitmap开辟空间
    saveBitMap.CreateCompatibleBitmap(mfcDC,nameImage[1][0],nameImage[1][1])
    # 高度saveDC，将截图保存到saveBitmap中
    saveDC.SelectObject(saveBitMap)
    saveDC.BitBlt((0,0), (nameImage[1]), mfcDC, (nameImage[0]), win32con.SRCCOPY)
    # saveDC.BitBlt(((w-image['w'])/2,(h-image['h'])/2), (image['w'], image['h']), mfcDC, (0, 0), win32con.SRCCOPY)
    saveBitMap.SaveBitmapFile(saveDC, filename)

# window_capture("haha.jpg")
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
window_capture("position.jpg",hwnd)
endTime = time.time() * 1000
print(endTime - startTime)