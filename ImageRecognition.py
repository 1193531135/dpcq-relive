from cnocr import CnOcr
import time
imageUrl = './position.jpg'
haha = './haha.jpg'
modelUrl = './models'
config = {
  "rec_model_name":"ch_PP-OCRv3_det",
  "rec_root":modelUrl
}
ocr = CnOcr()

def ImageRead(url):
  startTime = time.time() * 1000
  out = ocr.ocr(img_fp=url)
  endTime = time.time() * 1000
  print(endTime - startTime)
  print(out)
ImageRead(imageUrl)
ImageRead(haha)