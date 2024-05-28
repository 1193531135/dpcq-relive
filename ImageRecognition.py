from cnocr import CnOcr
import time
# imageUrl = './position.jpg'
# haha = './haha.jpg'
# modelUrl = './models'
rec_root="./models/cnocr"
det_root="./models/cnstd"
# config = {
  # "rec_model_name":"densenet_lite_136-gru",
  # "det_model_name":"ch_PP-OCRv3_det",
  # "rec_model_fp":rec_model_fp,
  # "cand_alphabet":True,
  # "rec_root":modelUrl
# }

def selectDihun(text):
    rtName = False
    diHunArr = ['达摩烈坤牛','极焱火蛇','九幽电猪','梨花九极狮','紫雾赤电蜂','凌霄蝙蝠','冰蚕大磷蛛','血雨噬魔豹','白莲玉蝎','琉璃玉兔']
    for nameIndex in range(0,len(diHunArr)):
        name = diHunArr[nameIndex]
        state = textFitting(text,name,2)
        if state:
            rtName = state
            break
    return rtName
# 文字拟合
def textFitting(text,baseText,wordSum):
    rtName = False
    name = baseText
    qualifiedSum = 0
    for nameUnitIndex in range(0,len(name)):
        nameUnit = name[nameUnitIndex]
        for textUnitIndex in range(0,len(text)):
            textUnit = text[textUnitIndex]
            if textUnit == nameUnit:
                qualifiedSum += 1
                break
    if qualifiedSum >= wordSum:
        rtName = name
    return rtName


startTime = time.time() * 1000
print('开始加载模型...')
ocr = CnOcr(cand_alphabet=[str])
# ocr = CnOcr(cand_alphabet=[str],rec_root=rec_root,det_root=det_root)
print('模型加载成功')
endTime = time.time() * 1000
print(f'''time: {endTime - startTime}''')

def ImageRead(url):
  # startTime = time.time() * 1000
  # out = ocr.ocr(img_fp=url)
  out = ocr.ocr_for_single_line(img_fp=url)
  # endTime = time.time() * 1000
  name = selectDihun(out['text'])
  print(name if name else 'error:' + out['text'])
  # return out['text']
  # print(f'''time: {endTime - startTime}''')
  # print(f'''print: {out['text']}''')
  # print(f'''length: {len(out)}''')
ImageRead('./readImage/bf1.png')
ImageRead('./readImage/bf2.png')
ImageRead('./readImage/bf3.png')
ImageRead('./readImage/bf4.png')
print("---------")