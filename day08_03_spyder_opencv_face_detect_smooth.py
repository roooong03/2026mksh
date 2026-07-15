# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 10:01:39 2026

@author: user
"""
# day08_03_spyder_opencv_face_detect_smooth
# Promt:face detect face detect出來的人臉會有點抖動 為什麼 要怎麼改成沒有抖動的版本
import cv2

# 載入人臉分類器
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# 開啟攝影機
cap = cv2.VideoCapture(0)

# Alpha 平滑參數
alpha = 0.25

# 儲存上一幀的人臉位置
prev_x = 0
prev_y = 0
prev_w = 0
prev_h = 0


while True:

    # 讀取影像
    ret, frame = cap.read()

    if not ret:
        break

    # 轉灰階（人臉辨識需要）
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    # 偵測人臉
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(80, 80)
    )


    for (x, y, w, h) in faces:

        # -------- Alpha 平滑 --------
        x = int(prev_x * (1-alpha) + x * alpha)
        y = int(prev_y * (1-alpha) + y * alpha)
        w = int(prev_w * (1-alpha) + w * alpha)
        h = int(prev_h * (1-alpha) + h * alpha)


        # 更新位置
        prev_x = x
        prev_y = y
        prev_w = w
        prev_h = h


        # 畫人臉框
        cv2.rectangle(
            frame,
            (x, y),
            (x+w, y+h),
            (0, 255, 0),
            2
        )


        # 在框上顯示文字
        cv2.putText(
            frame,
            "Face",
            (x, y-10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0,255,0),
            2
        )


    # 顯示畫面
    cv2.imshow("Face Detection", frame)


    # ESC 離開
    key = cv2.waitKey(1)

    if key == 27:
        break


# 關閉
cap.release()
cv2.destroyAllWindows()
