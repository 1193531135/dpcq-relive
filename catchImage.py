from os import system
from itertools import repeat
import threading
import win32gui
import win32api
import win32con
import time
import json
import re
import mss

def capture_process_screenshot(MainProcessId, output_file):
    window = win32gui.GetWindowRect(MainProcessId)
    left, top, right, bottom = window
    if window:
        region = {
          "left": left,
          "top": top,
          "width": right - left,
          "height": bottom - top
        }
        with mss.mss() as sct:
            region = window
            sct.shot(output=output_file)
            # cropped_screenshot = sct.crop((left, top, right, bottom))
            # cropped_screenshot.save(output_file)
            print(f"截图已保存到 {output_file}")

def getProcessName(jubing, mouse,array,selectName):
    if(win32gui.IsWindow(jubing) and win32gui.IsWindowVisible(jubing)):
        name = win32gui.GetWindowText(jubing)
        if name.find(selectName) != -1:
            array.append({
                'name': name,
                'processId': jubing,
            })
def findMainProcess():
    system('cls')
    print('开始检索主进程...')
    array = []
    MainProcessId = 0
    name = ""
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
            print(f"{index}. {item['name']} -- {item['processId']}")
        MainProcessId = array[int(input(f"""查询到 {len(array)} 条进程， 选择id，按下回车键（enter）:"""))]['processId']
        capture_process_screenshot(MainProcessId,"catchImage.png")


findMainProcess()