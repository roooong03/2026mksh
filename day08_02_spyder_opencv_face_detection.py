# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 09:40:33 2026

@author: user
"""
# day08_02_spyder_opencv_face_detection
# prompt: 我想要在剛剛的程式延伸 能夠偵測到人臉 用一些線條或圓形 把臉框起來 請問要再做什麼修改

import cv2

# 建立 Webcam
cap = cv2.VideoCapture(0)

# 第一步：載入人臉模型
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

while True:

    ret, frame = cap.read()

    if not ret:
        break

    # 第二步：轉灰階
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 第三步：偵測人臉
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    # 第四步：畫框
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)

    # 顯示畫面
    cv2.imshow("Webcam", frame)

    # ESC 離開
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()