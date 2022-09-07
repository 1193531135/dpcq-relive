import math
from os import system
from itertools import repeat
import threading
import win32gui
import win32api
import win32con
import time

import scapy.all as scapy

# import scapy_http.http
# 鼠标点击事件函数
def mouseClick(windowProcess,x,y):
    print(x,y)
    x = int(x)
    y = int(y)
    long_position = win32api.MAKELONG(x, y)#模拟鼠标指针 传送到指定坐标
    win32api.SendMessage(windowProcess, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, long_position)#模拟鼠标按下
    win32api.SendMessage(windowProcess, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, long_position)#模拟鼠标弹起
def mouseDrag(windowProcess,x,y,x2,y2):
    x = int(x)
    y = int(y)
    x2 = int(x2)
    y2 = int(y2)
    # win32api.SetCursorPos((x, y))
    long_position = win32api.MAKELONG(x, y)#模拟鼠标指针 传送到指定坐标
    long_position2 = win32api.MAKELONG(x2, y2)#模拟鼠标指针 传送到指定坐标
    win32api.SendMessage(windowProcess, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, long_position)#模拟鼠标按下
    time.sleep(0.15)
    win32api.SendMessage(windowProcess, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, long_position2)#模拟鼠标弹起
# 地图
def MapDown():
    mouseClick(process,(width - 178),115)
# 挂机点击
def HangDown():
    mouseClick(process,(width - 150),145)
#复活 
def ReliveDown():
    mouseClick(process,width/2,height/2+60)
#设置 
def settingDown():
    mouseClick(process,(width - 15),85)

# 帝魂专用方法
# 牛
def NiuDown():
    
    mouseClick(process,(width/2+90),(height/2-110))
# 蛇
def SheDown():
    
    mouseClick(process,(width/2+40),(height/2-75))
# 猪
def ZhuDown():
    
    mouseClick(process,(width/2+45),(height/2))
# 猪2
def Zhu2Down():
    mouseClick(process,(width/2+25),(height/2))
# 狮子
def ShiZiDown():
    
    mouseClick(process,(width/2+30),(height/2+90))
# 蜜蜂
def MiFengDown():
    
    mouseClick(process,(width/2-55),(height/2+85))
# 蜜蜂2
def MiFeng2Down():
    mouseClick(process,(width/2-100),(height/2+80))
# 蝙蝠
def BianFuDown():
    
    mouseClick(process,(width/2-150),(height/2+105))
# 蜘蛛
def ZhiZhuDown():
    
    mouseClick(process,(width/2-165),(height/2+50))
# 蜘蛛2
def ZhiZhu2Down():
    
    mouseClick(process,(width/2-170),(height/2+45))
# 豹子
def BaoZiDown():
    
    mouseClick(process,(width/2-180),(height/2-50))
# 蝎子
def XieZiDown():
    
    mouseClick(process,(width/2-145),(height/2-120))
# 兔子
def TuZiDown():
    
    mouseClick(process,(width/2-45),(height/2-130))



# 常用快捷方法
# 背包点击
def BackDown():
    mouseClick(process,(width/2+140),(height-25))
def FireDown():
    mouseClick(process,(width/2+290),(height-25))
# 正常背包页码点击
def BackPageDown(pageSize):
    OnePageX = width/2 - 135
    clienX = OnePageX + ((pageSize-1)*40)
    clienY = height/2-210
    mouseClick(process,clienX,clienY)
    # 切换页面过快，等待0.5s再点击物品
    return [OnePageX,clienY]
def goodsDown(PageOneX,PageOneY,goodsRowID,goodsColumnID):
    x = (PageOneX-6) + ((goodsColumnID - 1)*39)
    y = PageOneY + (goodsRowID*39)
    mouseClick(process,x,y)
    return [x,y]
def sellGoodsDown(x,y,clickRow):
    mouseClick(process,x+40,y+15+18*clickRow)
def sellGoodsConfirm():
    mouseClick(process,(width/2 - 60),(height/2+35))
# 卖出时装碎片单个
def clickGoodsMenu(pageNum,row,column,goodsType = 'suipian'):
    clickRow = 5
    if goodsType == 'suipian':clickRow = 5
    if goodsType == 'huoneng':clickRow = 2
    pageSizeX,pageSizeY = BackPageDown(pageNum)
    time.sleep(0.2)
    # 点击物品
    goodsX,goodsY = goodsDown(pageSizeX,pageSizeY,row,column)
    time.sleep(0.2)
    # 点击物品菜单属性
    sellGoodsDown(goodsX,goodsY,clickRow)
    time.sleep(0.2)
    # 碎片点击确定卖出
    if goodsType == 'suipian':sellGoodsConfirm() 
    # 火能再次点击当前
    if goodsType == 'huoneng':sellGoodsDown(goodsX,goodsY,clickRow)
#  时装碎片卖出流程
def sellClothesFragments(packPage,startRow,startColumn,endRow,endColumn):
    # packPage = 2
    # startRow = 4
    # startColumn = 5
    # endRow = 8
    # endColumn = 7
    if(startRow == endRow):
        for column in range(startColumn,endColumn+1):
            clickGoodsMenu(packPage,startRow,column)
    else:
        for row in range(startRow,endRow+1):
            if row == startRow:
                for column in range(startColumn,9):
                    clickGoodsMenu(packPage,row,column)
            elif row == endRow:
                for column in range(1,endColumn+1):
                    clickGoodsMenu(packPage,row,column)
            else:
                for column in range(1,9):
                    clickGoodsMenu(packPage,row,column)
# 自动斩魔快捷
def zhanMo():
    for d in range(1,21):
        for i in range(1,45):
            mouseClick(process,width/2+255,height/2+90)
            time.sleep(0.05)
        # 点击直接完成
        mouseClick(process,width/2+150,height/2+185)
        time.sleep(0.2)
        # 确定
        mouseClick(process,width/2-55,height/2+35)
        time.sleep(0.2)
# 自动吃火
def eatFire(house):
    # 打开异火
    # FireDown()
    # 点开猎火页面
    # 23s一轮
    cishu = int(house*3600/23)
    for _ in range(0,cishu):
        mouseClick(process,width/2-317,height/2-230)
        time.sleep(0.2)
        # 获取火
        for i in range(1,70):
            time.sleep(0.15)
            mouseClick(process,width/2-67,height/2+170)
        # 点开吞火页面
        mouseClick(process,width/2-187,height/2-230)
        time.sleep(0.5)
        # 点击主火
        mouseClick(process,width/2+120,height/2-125)
        time.sleep(0.5)
        # 蓝色以下一键吞掉
        mouseClick(process,width/2,height/2+170)
        # 首次点击被吞噬
        time.sleep(0.5)
        mouseClick(process,width/2+120,height/2+70)
        # 循环吞噬蓝火
        for i in range(1,16):
            mouseClick(process,width/2,height/2+115)
            time.sleep(0.2)
            mouseClick(process,width/2-80,height/2+30)
            mouseClick(process,width/2+75,height/2+30)
            time.sleep(0.2)
def eatSmallFire():
    packPage = 2
    startRow = 1
    startColumn = 1
    endRow = 8
    endColumn = 8
    def clickAfterClickFire(a,b,c,d):
        clickGoodsMenu(a,b,c,d)
        time.sleep(0.2)
        # 点击火的界面
        mouseClick(process,width/2-320,height/2+170)
        time.sleep(0.2)
        # 一键吞掉
        mouseClick(process,width/2,height/2+170)
        # BackDown
        BackDown()
        time.sleep(0.2)
        BackDown()
    if(startRow == endRow):
        for column in range(startColumn,endColumn+1):
            clickAfterClickFire(packPage,startRow,column,'huoneng')
    else:
        for row in range(startRow,endRow+1):
            if row == startRow:
                for column in range(startColumn,9):
                    clickAfterClickFire(packPage,row,column,'huoneng')
            elif row == endRow:
                for column in range(1,endColumn+1):
                    clickAfterClickFire(packPage,row,column,'huoneng')
            else:
                for column in range(1,9):
                    clickAfterClickFire(packPage,row,column,'huoneng')
def eatBlueFire():
    packPage = 2
    startRow = 6
    startColumn = 1
    endRow = 8
    endColumn = 2
    def clickAfterClickFire(a,b,c,d):
        clickGoodsMenu(a,b,c,d)
        time.sleep(0.2)
        # 点击火的界面
        mouseClick(process,width/2-320,height/2+170)
        time.sleep(0.2)
        # 点击主火
        mouseClick(process,width/2+120,height/2-125)
        time.sleep(0.2)
        # 循环吞噬蓝火
        for i in range(1,100):
            mouseClick(process,width/2,height/2+115)
            time.sleep(0.2)
            mouseClick(process,width/2-80,height/2+30)
            # 取消防止弹窗bug
            mouseClick(process,width/2+75,height/2+30)
            time.sleep(0.2)
        # BackDown
        BackDown()
        time.sleep(0.2)
        BackDown()
    if(startRow == endRow):
        for column in range(startColumn,endColumn+1):
            clickAfterClickFire(packPage,startRow,column,'huoneng')
    else:
        for row in range(startRow,endRow+1):
            if row == startRow:
                for column in range(startColumn,9):
                    clickAfterClickFire(packPage,row,column,'huoneng')
            elif row == endRow:
                for column in range(1,endColumn+1):
                    clickAfterClickFire(packPage,row,column,'huoneng')
            else:
                for column in range(1,9):
                    clickAfterClickFire(packPage,row,column,'huoneng')

state = False
def relive():
    def http_header(packet):
        global state
        http_packet = str(packet)
        if http_packet.find("GET /S50276/com/ui/role/shizhuang/2110001_3.swf HTTP/1.1") != -1:
            if(state == False):
                state = True
                ReliveDown()
            else:
                state = False
                time.sleep(0.7)
                HangDown()

    scapy.sniff(prn=http_header,count=0,iface="Realtek PCIe GbE Family Controller",filter="tcp",store=0)

# 全包检索43s，卖出帝魂
def sellDiHun(minPageNum = 1,maxPageNum = 5):
    MapDown()
    # 点击传送
    time.sleep(0.2)
    mouseClick(process,width/2+295,height/2-11)
    # 打开背包
    time.sleep(0.5)
    mouseClick(process,width/2-45,height/2+95)
    # 确定背包第一页的位置
    PageOneX = width/2 + 45
    PageOneY = height/2 - 189
    # 确定背包左上角第一格的位置
    cellOneX = PageOneX - 6
    cellOneY = PageOneY + 39
    # 所放仓库的每一个位置的集合形成的数组
    HuiShouArray = []
    # HuiShouArray的指针
    count = 1
    for i in range(1,43):
        # 横向标个数
        columnItem = 7 if i%7 == 0 else i%7
        # 行数
        rowItem = math.ceil(i/7)
        x = (cellOneX - 305) + (columnItem-1)*39
        y = cellOneY + (rowItem-1)*39
        HuiShouArray.append({
            "x":x,
            "y":y,
        })
    # 循环五个背包页
    time.sleep(0.2)
    for pageSum in range(minPageNum,maxPageNum+1):
        # 打开背包页码
        packX = PageOneX + (pageSum-1)*39
        mouseClick(process,packX,PageOneY)
        time.sleep(0.2)
        # 行列循环背包
        for row in range(1,9):
            for column in range(1,9):
                goodsX = cellOneX + (column-1)*39
                goodsY = cellOneY + (row-1)*39
                mouseDrag(process,goodsX,goodsY,HuiShouArray[count-1]['x'],HuiShouArray[count-1]['y'])
                # time.sleep(0.05)
                count += 1
                # 达到仓库极限进行清除
                if count == 43 or (pageSum == 5 and row == 8 and column == 8):
                    count = 1
                    mouseClick(process,(cellOneX - 305),(cellOneY+225))
                    time.sleep(0.2)
                    mouseClick(process,(cellOneX - 155),(cellOneY+180))
                    time.sleep(0.2)
    # 关掉仓库
    time.sleep(0.2)
    mouseClick(process,width/2 - 15,height/2 - 229)
    # 关掉背包
    time.sleep(0.2)
    BackDown()
    # 关掉地图
    time.sleep(0.2)
    MapDown()
    time.sleep(0.2)
    # x = (PageOneX-6) + ((goodsColumnID - 1)*39)
    # y = PageOneY + (goodsRowID*39)
def DiHunClick(id,runTimeArray):
    MapDown()
    time.sleep(0.2)
    if(id == 1):
        NiuDown()
        time.sleep(runTimeArray[id])
    if(id == 2):
        SheDown()
        time.sleep(runTimeArray[id])
    if(id == 3):
        ZhuDown()
        time.sleep(runTimeArray[id])
        HangDown()
        time.sleep(1)
        Zhu2Down()
        time.sleep(0.5)
    if(id == 4):
        ShiZiDown()
        time.sleep(runTimeArray[id])
    if(id == 5):
        MiFengDown()
        time.sleep(runTimeArray[id])
        HangDown()
        time.sleep(1)
        MiFeng2Down()
        time.sleep(0.5)
    if(id == 6):
        BianFuDown()
        time.sleep(runTimeArray[id])
    if(id == 7):
        ZhiZhuDown()
        time.sleep(runTimeArray[id])
        HangDown()
        time.sleep(1)
        ZhiZhu2Down()
        time.sleep(0.5)
    if(id == 8):
        BaoZiDown()
        time.sleep(runTimeArray[id])
    if(id == 9):
        XieZiDown()
        time.sleep(runTimeArray[id])
    if(id == 10):
        TuZiDown()
        time.sleep(runTimeArray[id])
    time.sleep(0.2)
    # 点击位置后关闭地图
    MapDown()
# 
def Guaji(oneSleep = 150):
    # 怪物选择青铜
    # settingDown()
    count = 1
    runTimeArray = {
        1:11,
        2:4,
        3:6,
        4:9,
        5:3,
        6:4,
        7:4,
        8:7,
        9:7,
        10:4,
    }
    allTime = 1800
    for _ in repeat(None):
        # 地图上点击位置后，延时到达后
        DiHunClick(count,runTimeArray)
        # 点击挂机按钮
        HangDown()
        # 停留时长
        time.sleep(oneSleep)
        # 第一个击杀后才开始30分钟复活时间
        if count != 1:
            allTime = allTime - runTimeArray[count] - oneSleep
        # 当最后一个击杀完毕，等待帝魂剩下重置时间后，时间重置
        if count == 10:
            # 减去跑路到第一个帝魂的时间,再减去刷背包时间43s(实际4个包+传送大概35s)
            # 先休息差2-5 50s刷新,但是防止一些问题，可以多休息10s
            time.sleep(allTime-runTimeArray[1]-50+10)
            # 2-5 50s
            sellDiHun(2,5)
            allTime = 1800
        count += 1
        if count == 11:count = 1
    
 
# 拉取全部的窗口
def getProcessName(jubing, mouse,array,selectName):
    if(win32gui.IsWindow(jubing) and win32gui.IsWindowVisible(jubing)):
        name = win32gui.GetWindowText(jubing)
        if name.find(selectName) != -1:
            array.append({
                'name': name,
                'processId': jubing,
            })
# 检验子窗口
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
        if(name.find('无标题 - QQ浏览器') != -1 and not chidrenNeed):
            childrenS.append({
                'name': name or 'null',
                'processId': jubing,
            })

# 全局变量
# flash宽高
width = 0
height = 0
# flash进程
process = 0
# 是否开启地图
mapState=False
funcArry = [
    { "name":"帝魂挂机","id":1,"state":False },
    { "name":"自动复活","id":2,"state":False },
    { "name":"帝魂挂机","id":1,"state":False },
]



# mainProgram
def loadFuncMenu(ProcessId,chidrenNeed):
    global height,width,process
    system('cls')
    childrenID = []
    win32gui.EnumChildWindows(ProcessId,lambda a,b:getChildren(a,b,childrenID,chidrenNeed),0)
    if len(childrenID) == 0:
        input('未检测到目标浏览器的flash，请检查游戏是否打开')
        return getBrowser()
    print('!!进入当前功能页请勿缩放，最小最大化指定的的窗口!!')
    print('!!测试是否为选定页面，将会打开并隔一秒关闭页面的地图')
    flashID = childrenID[0]["processId"]
    process = flashID
    # 退出全屏
    # win32gui.ShowWindow(ProcessId,win32con.SW_SHOWNORMAL)
    # 进入全屏
    # win32gui.ShowWindow(ProcessId,win32con.SW_SHOWMAXIMIZED)
    # 确定好id后开始测试
    # 获取窗口宽高得使用父id
    left,top,right,bottom = win32gui.GetWindowRect(flashID)
    width = right-left
    height = bottom - top
    # MapDown()
    # time.sleep(1)
    # MapDown()
    # a = input('是否为当前页面(是=1，否=2，输入id):')
    # if a == '2':
    #     return getBrowser()
    # mouseClick(flashID,width/2,height/2)
    # sellClothesFragments(3,1,1,8,8)
    # mouseDrag(process,983,303,674,305)
    # mouseDrag(process,1023,303,714,305)
    # sellDiHun(3,4)
    # time.sleep(800)
    # Guaji()
    # relive()
    eatFire(4)
    # eatSmallFire()
    # eatBlueFire()
    # zhanMo()


    
# 检索主进程
def findMainProcess(name,chidrenNeed):
    system('cls')
    print('开始检索主进程...')
    array = []
    MainProcessId = 0
    win32gui.EnumWindows(lambda j,m:getProcessName(j,m,array,name), 0)
    if len(array) == 0:
        input('未找到目标进程（按任意键返回菜单）')
        return getBrowser()
    # 只有一个，直接进入控制
    if len(array) == 1:
        MainProcessId = array[0]['processId']
    if len(array) > 1:
        for index,item in enumerate(array):
            print(f"{index}. {item['name']}")
        print('进入进程前，请准备好窗口大小，窗口大小保证能完全正常展示游戏内所有的窗口，进入后不再变动')
        MainProcessId = array[int(input(f"""查询到 {len(array)} 条进程， 选择id，按下回车键（enter）:"""))]['processId']
    loadFuncMenu(MainProcessId,chidrenNeed)


# 选择浏览器类型
def getBrowser():
    system('cls')
    printArray = [
        { "id":1,"name":"175浏览器 （不支持自动复活功能）" },
        { "id":2,"name":"qq浏览器" },
        { "id":3,"name":"360大厅" },
    ]
    print("!!! 请将浏览器的tab页切换到需要控制的页面 !!!")
    for item in printArray:
        print(f"""{item['id']}. {item['name']}""")
    id = int(input('输入需要控制的浏览器类型的id，按下回车键（enter）:'))
    name = ''
    chidrenNeed = False
    if id == 1:
        name = "175游戏浏览器"
        chidrenNeed = True
    if id == 2:
        # name = input('输入qq浏览器游戏页的标题（例如： =》》 【斗破苍穹2】双线1215服 《《=，不要有漏字错字多字和空格）:')
        name = "【斗破苍穹2】双线1215服"
    if id == 3:
        # name = input('输入360游戏大厅录入的游戏名（例如： =》》 dpcq 《《=，不要有漏字错字多字和空格）:')
        name = 'dpcq'
        chidrenNeed = True
    findMainProcess(name,chidrenNeed)



getBrowser()
# 获取主进程id
# findMainProcess()
# array = []
# index = 1
# print('检索子进程...')
# win32gui.EnumChildWindows(MainProcessId,getProcessName,0)
# # system('cls')
# for item2 in array:
#     print(f"{index}. {item2['name']}")
#     index += 1
# 选择窗口
# print('————————————————')
# print('|   id   | name')
# print('————————————————')
# lin = 1
# for x, index in array:
#     idName = f'{lin}'
#     if(len(idName) == 1):
#         idName = f'  {idName}    '
#     if(len(idName) == 2):
#         idName = f'  {idName}   '
#     if(len(idName) == 3):
#         idName = f'  {idName}  '
#         print(f'| {idName}| {array[lin-1][x]}')
#     lin += 1
# now_id = int(input('输入窗口id：'))
# windowProcess = array[now_id - 1]['processId']

# 检索子窗口
# childrenS = []

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

# def http_header(packet):
#   http_packet = str(packet)
#   if http_packet.find('GET /S50276/com/ui/role/shizhuang/2110001_3.swf HTTP') != -1:
#     # obj = http_packet.split('\r\n')
#     # obj = http_packet.replace('\r\n','\n')
#     # if obj[0].find('b'):
#     #     obj = obj[1:]
#     # string = packet.sprintf("{Raw:%Raw.load%}\n")
#     # print(string)
#     # if string.find('/crossPromo/manage/template/detail') != -1:
#     print("<=================This is start===========================>")

# scapy.sniff(prn=http_header,count=0,iface="Realtek PCIe GbE Family Controller",filter="tcp")


# 'GET /S50276/com/ui/role/shizhuang/2110001_3.swf HTTP/1.1\r\nHost: ymcdn.aip.cn\r\nConnection: keep-alive\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36 Core/1.77.106.400 QQBrowser/10.9.4626.400\r\nAccept: */*\r\nX-Requested-With: ShockwaveFlash/34.0.0.231\r\nReferer: http://s5013.dpcq.yegame.com/user/game.php\r\nAccept-Encoding: gzip, deflate\r\nAccept-Language: zh-CN,zh;q=0.9\r\n\r\n'
