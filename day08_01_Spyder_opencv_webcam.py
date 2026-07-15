# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 09:30:31 2026

@author: user
"""
# day08_01_Spyder_opencv_webcam
# 我想在SPYDER裡 使用Opencv讀入Webcam視訊鏡頭的畫面 即時更新
# 要做哪些步驟 有哪些可能卡住的地方?
# 因為中文的注音輸入法會卡住Q的鍵 可以改成ESC的鍵退出嗎
import cv2

print(cap.isOpened())

while True:

    ret, frame = cap.read()

    if not ret:
        print("讀不到畫面")
        break
    
    cv2.imshow("Webcam", frame)

    if cv2.waitKey(1) == 27:   # ESC 鍵
        break

cap.release()
cv2.destroyAllWindows()
