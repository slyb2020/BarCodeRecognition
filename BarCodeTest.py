import cv2
from PIL import Image, ImageDraw, ImageFont
import csv
import  pyzbar.pyzbar as pyzbar
import numpy as np
import time


time1 = (time.strftime("%Y!%m@%d(%H*%M)%S`", time.localtime()))
time2 = time1.replace('!', '年')
time3 = time2.replace('@', '月')
time4 = time3.replace('(', '日')
time5 = time4.replace('*', '时')
time6 = time5.replace(')', '分')
timenow = time6.replace('`', '秒')

barcodeData1 = ''

found = set()
capture = cv2.VideoCapture(0,cv2.CAP_DSHOW)
Files = 'qrcode+barcode.data'
while(1):
    ret, frame = capture.read()
    test = pyzbar.decode(frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    barcodes = pyzbar.decode(gray)
    for barcode in barcodes:
        (x, y, w, h) = barcode.rect
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 0), 2)
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type
        if barcodeData == '' or barcodeData != barcodeData1:
            barcodeData1 = barcodeData

            imgPIL = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            font = ImageFont.truetype('arialbd.ttf', 25)
            fillColor = (0, 255, 0)
            position = (x, y - 25)
            strl = barcodeData
            draw = ImageDraw.Draw(imgPIL)
            draw.text(position, strl, font=font, fill=fillColor)
            imgPIL.save('Identification_result.jpg','jpeg')
            print("Recongize result>>>type:{0} countent:{1}".format(barcodeType, barcodeData))
        else:
            pass
        if barcodeType not in found or barcodeData not in found:
            with open(Files, 'a+') as w:
                csv_write = csv.writer(w)
                date = ['类型： ' + barcodeType + ' 识别结果： ' + barcodeData + ' 时间：' + timenow]
                csv_write.writerow(date)
            found.add(barcodeData)
    cv2.imshow('qrcode+barcode', frame)
    k = cv2.waitKey(1)
    if k == 27:
        break