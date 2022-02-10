import numpy as np
import cv2
capture =cv2.VideoCapture(0,cv2.CAP_DSHOW)
capture.set(3,640)
capture.set(4,480)
while True:
    # 读取摄像头中的图像，ok为是否读取成功的判断参数
    ret,img =capture.read()
    cv2.imshow('frame', img)
    k =cv2.waitKey(1)
    if k ==27:
        break