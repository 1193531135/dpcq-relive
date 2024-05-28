# import os
# import shutil
# __file__ = __file__.replace('\\','/')
# nowDir = os.path.dirname(__file__)
# # 模型地址检测
# def modelsCheck():
#     print('开始检测模型')
#     isCnocr = os.path.exists(f'C:/Users/{os.getlogin()}/AppData/Roaming/cnocr')
#     # 目录不存在
#     if not isCnocr:
#         print('未检测到模型,开始安装模型...')
#         shutil.copytree(f"""{nowDir}/models/cnocr""",f"""C:/Users/{os.getlogin()}/AppData/Roaming/cnocr""")
#         shutil.copytree(f"""{nowDir}/models/cnstd""",f"""C:/Users/{os.getlogin()}/AppData/Roaming/cnstd""")
#         print('安装完成')
#     else:
#         print('检测到模型已存在')
#     input('输入回车退出')
# modelsCheck()


import os
import json
# 读取配置项
def readConifg():
    global config
    path = './config.json'
    # conifg文件存在就读取
    if os.path.exists(path):
        f = open(path,'r', encoding='utf-8')
        readData = f.read()
        readData = json.loads(readData)
        print(readData)
        print(type(readData))
readConifg()