import math
from os import system
from itertools import repeat
import threading
import win32gui
import win32api
import win32con
import time
import json
import re
import scapy.all as scapy

# import scapy_http.http
# LInput() 限制级别input
def LInput(text,reg):
    val = input(text)
    if (not re.search(reg,val)) == True:
        print('非法输入，请重新输入')
        LInput(text,reg)
# 返回指定坐标像素点
def GetPixel(x,y):
    global hwndDC
    pixel = win32gui.GetPixel(hwndDC,x,y)
    return pixel
# 鼠标点击事件函数
def mouseClick(windowProcess,x,y):
    # print(x,y)
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
    mouseClick(process,(width/2),(height/2 + 65))
    time.sleep(0.3)
    # # 唤起坐骑
    win32api.SendMessage(process, win32con.WM_KEYDOWN, 84, 0)
    win32api.SendMessage(process, win32con.WM_KEYUP, 84, 0)
    # 起来选中
    win32api.SendMessage(process, win32con.WM_KEYDOWN, 87, 0)
    win32api.SendMessage(process, win32con.WM_KEYUP, 87, 0)
    win32api.SendMessage(process, win32con.WM_KEYDOWN, 87, 0)
    win32api.SendMessage(process, win32con.WM_KEYUP, 87, 0)
    win32api.SendMessage(process, win32con.WM_KEYDOWN, 87, 0)
    win32api.SendMessage(process, win32con.WM_KEYUP, 87, 0)
#设置 
def settingDown():
    mouseClick(process,(width - 15),85)

# 帝魂专用方法
# 牛
def NiuDown():
    mouseClick(process,(width/2+90),(height/2-115))
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
    
    mouseClick(process,(width/2-170),(height/2+35))
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
    PageOneX = width/2 - 135
    PageOneY = height/2-210
    x = (PageOneX-6) + ((goodsColumnID - 1)*39)
    y = PageOneY + (goodsRowID*39)
    mouseClick(process,x,y)
    print()
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
    if goodsType == 'piliang':clickRow = 2
    if goodsType == 'first':clickRow = 1
    pageSizeX,pageSizeY = BackPageDown(pageNum)
    time.sleep(0.2)
    # 点击物品
    goodsX,goodsY = goodsDown(pageSizeX,pageSizeY,row,column)
    time.sleep(0.2)
    # 点击物品菜单属性
    sellGoodsDown(goodsX,goodsY,clickRow)
    time.sleep(0.2)
    # 批量的话再点一次
    if goodsType == 'piliang':sellGoodsDown(goodsX,goodsY,clickRow)
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
        for i in range(1,20):
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
def openSometing(double = 'piliang'):
    packPage = 2
    startRow = 1
    startColumn = 1
    endRow = 8
    endColumn = 8
    def clickAfterClickFire(a,b,c,d):
        clickGoodsMenu(a,b,c,d)
        time.sleep(0.2)
    if(startRow == endRow):
        for column in range(startColumn,endColumn+1):
            clickAfterClickFire(packPage,startRow,column,double)
    else:
        for row in range(startRow,endRow+1):
            if row == startRow:
                for column in range(startColumn,9):
                    clickAfterClickFire(packPage,row,column,double)
            elif row == endRow:
                for column in range(1,endColumn+1):
                    clickAfterClickFire(packPage,row,column,double)
            else:
                for column in range(1,9):
                    clickAfterClickFire(packPage,row,column,double)
def eatBlueFire():
    packPage = 2
    startRow = 3
    startColumn = 6
    endRow = 7
    endColumn = 7
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
        time.sleep(0.2)
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
        if http_packet.find('GET /S50276/com/ui/role/shizhuang/2110001_3.swf HTTP') != -1:
            if(state == False):
                mouseClick(process,width/2,height/2+60)
                state = True
            else:
                time.sleep(0.3)
                HangDown()
                state = False

    scapy.sniff(prn=http_header,count=0,iface="Realtek PCIe GbE Family Controller",filter="tcp",store=0)

#赏金
def shangjin():
    for i in range(1,300):
        mouseClick(process,width-160,315)
        time.sleep(1)
        HangDown()
        time.sleep(1)
        mouseClick(process,340,height-100)
        time.sleep(80)
        mouseClick(process,340,height-100)
        time.sleep(40)
        mouseClick(process,width-160,315)
        time.sleep(1)
        for i in range(1,4):
            mouseClick(process,width/2+235,height/2+160)
            time.sleep(0.5)
        time.sleep(1)

# 全包检索43s，卖出帝魂
def sellDiHun(minPageNum = 1,maxPageNum = 5):
    MapDown()
    # 点击传送
    time.sleep(0.2)
    mouseClick(process,width/2+295,height/2-11)
    # 点击挂机,避免打坐
    time.sleep(0.5)
    HangDown()
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
    if(id == 10):
        NiuDown()
    if(id == 9):
        SheDown()
    if(id == 8):
        ZhuDown()
    if(id == 7):
        ShiZiDown()
    if(id == 6):
        MiFengDown()
    if(id == 5):
        BianFuDown()
    if(id == 4):
        ZhiZhuDown()
    if(id == 3):
        BaoZiDown()
    if(id == 2):
        XieZiDown()
    if(id == 1):
        TuZiDown()
def DiHunClickFZ(id,runTimeArray):
    MapDown()
    time.sleep(0.2)
    if(id == 10):
        NiuDown()
    if(id == 9):
        SheDown()
    if(id == 8):
        Zhu2Down()
    if(id == 7):
        ShiZiDown()
    if(id == 6):
        MiFeng2Down()
    if(id == 5):
        BianFuDown()
    if(id == 4):
        ZhiZhu2Down()
    if(id == 3):
        BaoZiDown()
    if(id == 2):
        XieZiDown()
    if(id == 1):
        TuZiDown()

def Guaji(oneSleep = 150,jiasu=True,sum=False):
    # 怪物选择青铜
    # settingDown()
    count = 1
    shudu = 1 if jiasu else 1.3
    runTimeArray = {
        1:11*shudu,
        2:4*shudu,
        3:6*shudu,
        4:9*shudu,
        5:3*shudu,
        6:4*shudu,
        7:4*shudu,
        8:7*shudu,
        9:7*shudu,
        10:4*shudu,
    }
    allTime = 1800
    for _ in (range(1,sum) if sum else repeat(None)):
        if count == 1:
            # 卖完帝魂,根据单个时长来确定吃几瓶药
            yao = int((oneSleep * 10)/300)
            for _2 in range(1,yao):
                time.sleep(1)
                mouseClick(process,width/2-220,height-12)
            time.sleep(0.2)
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
            sleepTime = allTime-runTimeArray[1]-50+10
            if(sleepTime < 0):
                sleepTime = 1
            time.sleep(sleepTime)
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
        if(name.find('无标题 - QQ浏览器') != -1 and (not chidrenNeed)):
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
configJSON = False
funcArry = [
    { "name":"帝魂挂机","id":1,"state":False },
    { "name":"自动复活","id":2,"state":False },
    { "name":"帝魂挂机","id":1,"state":False },
]
now_dihun_id = 0
now_dihun_time = 0
# isRuning 用于校验是否到达点
isRuning = True
# 存储整个页面的图像内容
hwndDC = 0
# 帝魂坐标
diHunPosition = {}
# 用于辅助的帝魂坐标
diHunPosition2 = {}
diHunPositionTrue = {}
def menuFunc(funcId):
    global now_dihun_time,now_dihun_id,diHunPositionTrue,isRuning,hwndDC
    # 自动复活
    if funcId == 1:
        configJSON['relive'] = (not configJSON['relive'])
        input(f'''自动复活功能成功修改为 {'已开启' if configJSON['relive'] else '已关闭'}(按任意键返回菜单)''')
        menu()
    # 挂机控制
    if funcId == 2:
        configJSON['hang'] = (not configJSON['hang'])
        print('''到怪的位置处才开始挂: 只有到怪物点的时候才开启时时挂机''')
        print('''时时挂机状态: 只有到怪物点的时候才开启''')
        input(f'''挂机控制功能成功修改为 {'到怪的位置处才开始挂' if configJSON['hang'] else '时时挂机状态'}(按任意键返回菜单)''')
        menu()
    #开启关闭挂机 
    if funcId == 6 or funcId == 7:
        positionId = input('选择怪物定位模式(1.主要模式 2.辅助拉怪)(默认1):') or '1'
        if positionId == "2":
            diHunPositionTrue = diHunPosition2
        if funcId == 7:
            t = int(input('输入延时的秒数:'))
            print('等待中...')
            time.sleep(t)
        now_dihun_id = 0 if now_dihun_id else '1'
        # 如果是开启给time附上初值
        if now_dihun_id :
            now_dihun_time = configJSON['stayTimeArray'][now_dihun_id]
        input(f'''挂机 {'已开启' if now_dihun_id else '已关闭'}(按任意键返回菜单)''')
        menu()
    if funcId == 8:
        positionId = input('选择插入的怪物位置:') or '1'
        positionP = input('选择怪物定位模式(1.主要模式 2.辅助拉怪)(默认1):') or '1'
        now_dihun_id = positionId
        if positionP == "2":
            diHunPositionTrue = diHunPosition2
        now_dihun_time = configJSON['stayTimeArray'][now_dihun_id]
    if funcId == 9:
        print(f'now_dihun_time:{now_dihun_time}')
        print(f'now_dihun_id:{now_dihun_id}')
        print(f'isRuning:{isRuning}')
        print(f'hwndDC:{hwndDC}')
        input(f'''(按任意键返回菜单)''')
        menu()
# 挂机状态控制
def guajiControl():
    global isRuning,now_dihun_time,now_dihun_id
    # 时间到零了的情况
    if now_dihun_time == 0:
        # # 开启后设置1为默认打怪
        # if now_dihun_id == 0:
        #     now_dihun_id = '1'
        # 当id为11的时候 且休息时间完毕后，切换回1
        if now_dihun_id == '11':
            now_dihun_id = '1'
        else:
            # id往下走
            now_dihun_id = str(int(now_dihun_id) + 1)
        # 更新时间
        now_dihun_time = configJSON['stayTimeArray'][now_dihun_id]
        # 开启跑路
        isRuning = True
    else:
        global timsss
        timsss = timsss + 1
        print(timsss)
        print('now_dihun_time',now_dihun_time)
        now_dihun_time = now_dihun_time - 1
# 跑图校验
def runMap():
    global isRuning
    hwndDC = win32gui.GetDC(process)
    # 在跑图的情况下检测地图是否开启
    if isRuning:
        # 校验地图是否开启 前往当前目的地
        pixel = win32gui.GetPixel(hwndDC,int(width/2 - 270),int(height/2 - 230))
        if pixel != 4461898:
            MapDown()
            time.sleep(0.2)
            # 到达后点的数据为 59 or 1005644
            # 到达后点的数据为 45652 or 1179809
        # 往当前目的地点击前往
        x,y,reachPiexl1,reachPiexl2 = diHunPositionTrue[now_dihun_id]
        mouseClick(process,int(x),int(y))
        # 校验是否到达
        isReach = win32gui.GetPixel(hwndDC,int(x),int(y))
        if isReach == 42825 or isReach == 1114249 or isReach == 45652 or isReach == 1179809 or isReach == reachPiexl1 or isReach == reachPiexl2:
            # 到达后关闭状态
            isRuning = False

    # GetPixel
timsss = 0
def setInterval1s():
     # 开启挂机之后才进行
    if now_dihun_id:
        guajiControl()
        runMap()
    threaProcess = threading.Timer(1,setInterval1s)
    threaProcess.start()
def setInterval0_4s():
    global hwndDC
    # 1.更新图形层数据
    hwndDC = win32gui.GetDC(process)
    # 复活点击功能
    relivePixel = GetPixel(int(width/2),int(height/2 + 50))
    if relivePixel == 399157:
        ReliveDown()
    # 时时挂机功能
    # 挂机标识有四个位置
    guajiCheck1 = GetPixel(int(width/2 + 162),int(height/2 - 270))
    guajiCheck2 = GetPixel(int(width/2 + 162),int(height/2 - 250))
    guajiCheck3 = GetPixel(int(width/2 + 132),int(height/2 - 270))
    guajiCheck4 = GetPixel(int(width/2 + 132),int(height/2 - 260))
    # 站立模式三个位置
    guajiCheck5 = GetPixel(int(width/2 + 162),int(height/2 - 240))
    guajiCheck6 = GetPixel(int(width/2 + 162),int(height/2 - 220))
    guajiCheck7 = GetPixel(int(width/2 + 132),int(height/2 - 230))
    guajiCheck8 = GetPixel(int(width/2 + 132),int(height/2 - 240))
    if not ( 
        guajiCheck1 == 65280 or 
        guajiCheck2 == 65280 or 
        guajiCheck3 == 65280 or 
        guajiCheck4 == 65280 or 
        guajiCheck5 == 65280 or
        guajiCheck6 == 65280 or
        guajiCheck8 == 65280 or
        guajiCheck7 == 65280 ):
        HangDown()
    threaProcess = threading.Timer(0.4,setInterval0_4s)
    threaProcess.start()
def menu():
    # global configJSON
    system('cls')
    print(f'''键位             |                功能描述                |    当前状态''')
    print('---------------------------------------------------------------------------')
    print(f'''1                |                自动复活                |    {'已开启' if configJSON['relive'] else '已关闭'}''')
    print('---------------------------------------------------------------------------')
    print(f'''2                |                挂机控制                |    {'到怪的位置处才开始挂' if configJSON['hang'] else '时时挂机状态'}''')
    print('---------------------------------------------------------------------------')
    print(f'''3                |                挂机顺序                |    {configJSON['order']}''')
    print('---------------------------------------------------------------------------')
    print(f'''4                |        单个怪停留时间('怪物id':时长)    |    {configJSON['stayTimeArray']}''')
    print('---------------------------------------------------------------------------')
    print(f'''5                |  扫描强度(自动复活和自动挂机的反应速度)  |    {configJSON['interval']}s（单位|秒）''')
    print('---------------------------------------------------------------------------')
    print(f'''6                |            (开启 | 关闭)挂机            |    {'已关闭' if (not now_dihun_id) else '已开启'}''')
    print('---------------------------------------------------------------------------')
    print(f'''7                |           延时(开启 | 关闭)挂机          |    {'已关闭' if (not now_dihun_id) else '已开启'}''')
    print('---------------------------------------------------------------------------')
    print(f'''8                |                锁定位置挂机               |   ''')
    print('---------------------------------------------------------------------------')
    print(f'''9                |          查看离下一波开始的剩余时间      |    ''')
    print('---------------------------------------------------------------------------')
    print(f'''10                |                查看所有参数              |    ''')
    print('---------------------------------------------------------------------------')
    id = input('输入需要修改的功能的键位(暂都不可使用，除了6):')
    if id == '1' :
        menuFunc(1)
    elif id == '2':
        menuFunc(2)
    elif id == '3':
        menuFunc(3)
    elif id == '4':
        menuFunc(4)
    elif id == '5':
        menuFunc(5)
    elif id == '6':
        menuFunc(6)
    elif id == '7':
        menuFunc(7)
    elif id == '8':
        menuFunc(8)
    elif id == '9':
        menuFunc(9)
    else:
        input('未找到指令所属功能(按任意键返回菜单)')
        menu()
def readConfig():
    global configJSON
    file = open('./config.json', 'r')
    content = file.read()
    configJSON = json.loads(content)
    # 计算等待时长
    timeAll = 0
    for i in configJSON['stayTimeArray'].keys():
        timeAll = timeAll + configJSON['stayTimeArray'][i]
    configJSON['stayTimeArray']['11'] = 60*30 - timeAll - 20
    file.close()
def writeConfig():
    content = json.dumps(configJSON)
    file = open('./config.json', 'w')
    file.write(content)
    file.close()
# 在获取width和height之后生成坐标
def createPosition():
    global diHunPosition,diHunPosition2,diHunPositionTrue
    diHunPosition = {
    "11":[(width/2-45),(height/2-130),45652,1179809],
    "10":[(width/2+85),(height/2-110),45652,1179809],
    "9":[(width/2+40),(height/2-75),42825,1114249],
    "8":[(width/2+45),(height/2),59,1005644],
    "7":[(width/2+30),(height/2+90),42825,1114249],
    "6":[(width/2-100),(height/2+80),42825,1114249],
    "5":[(width/2-150),(height/2+105),42825,1114249],
    "4":[(width/2-165),(height/2+50),45652,1179809],
    "3":[(width/2-180),(height/2-50),37945,1574758],
    "2":[(width/2-145),(height/2-120),74,221521],
    "1":[(width/2-45),(height/2-130),45652,1179809],}
    diHunPosition2 = json.loads(json.dumps(diHunPosition))
    diHunPosition2['8'] = [(width/2+25),(height/2),37945,1574758]
    diHunPosition2['6'] = [(width/2-75),(height/2+74),25634,393262]
    diHunPosition2['4'] = [(width/2-170),(height/2+35),42825,1114249]
    diHunPositionTrue = diHunPosition
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
    # createPosition()
    # readConfig()
    # 开启一个每秒扫描一次的线程
    # setInterval1s()
    # 0.4s扫描一次的线程
    # setInterval0_4s()
    # menu()
    # MapDown()
    # time.sleep(1)
    # MapDown()
    # a = input('是否为当前页面(是=1，否=2，输入id):')
    # if a == '2':
    #     return getBrowser()
    # mouseClick(flashID,width/2,height/2)
    # mouseClick(process,width/2-220,height-12)
    sellClothesFragments(2,1,1,8,8)
    # mouseDrag(process,983,303,674,305)
    # mouseDrag(process,1023,303,714,305)
    # sellDiHun(3,5)
    # Guaji(40,True,4)
    # Guaji(150)
    # Guaji(20)
    # relive()
    # eatFire(5)
    # openSometing()
    # openSometing('first')
    # eatSmallFire()
    # eatBlueFire()
    # shangjin()
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
        print()
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