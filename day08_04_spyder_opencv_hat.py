# day08_04_spyder_opencv_hat
import cv2
import numpy as np

# 載入人臉模型
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)


# 載入帽子圖片 (PNG透明背景)
hat = cv2.imread("hat.png", cv2.IMREAD_UNCHANGED)


cap = cv2.VideoCapture(0)


# Alpha 平滑
alpha = 0.25

prev_x = 0
prev_y = 0
prev_w = 0
prev_h = 0



def overlay_image(background, overlay, x, y):

    h, w = overlay.shape[:2]

    # 防止超出畫面
    if x < 0 or y < 0:
        return background

    if x+w > background.shape[1]:
        return background

    if y+h > background.shape[0]:
        return background


    # 有透明通道
    if overlay.shape[2] == 4:

        alpha_mask = overlay[:,:,3] / 255.0

        for c in range(3):
            background[y:y+h, x:x+w, c] = (
                alpha_mask * overlay[:,:,c] +
                (1-alpha_mask) *
                background[y:y+h, x:x+w, c]
            )

    return background



while True:

    ret, frame = cap.read()

    if not ret:
        break


    gray = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2GRAY
    )


    faces = face_cascade.detectMultiScale(
        gray,
        1.1,
        5,
        minSize=(80,80)
    )


    for (x,y,w,h) in faces:


        # Alpha smoothing
        x = int(prev_x*(1-alpha)+x*alpha)
        y = int(prev_y*(1-alpha)+y*alpha)
        w = int(prev_w*(1-alpha)+w*alpha)
        h = int(prev_h*(1-alpha)+h*alpha)


        prev_x=x
        prev_y=y
        prev_w=w
        prev_h=h



        # -------------------------
        # 計算帽子位置
        # -------------------------

        hat_width = w

        hat_height = int(
            hat.shape[0] *
            hat_width /
            hat.shape[1]
        )


        resized_hat = cv2.resize(
            hat,
            (hat_width, hat_height)
        )


        # 帽子放在臉上方
        hat_x = x
        hat_y = y - hat_height + 40


        frame = overlay_image(
            frame,
            resized_hat,
            hat_x,
            hat_y
        )



        # 畫臉框(測試用)
        cv2.rectangle(
            frame,
            (x,y),
            (x+w,y+h),
            (0,255,0),
            2
        )



    cv2.imshow(
        "Hat Filter",
        frame
    )


    # ESC離開
    if cv2.waitKey(1)==27:
        break



cap.release()
cv2.destroyAllWindows()