# day06_01_spyder_openCV_captgure.py
# 從CHAT GPT 得到的程式
# 修改自day04_07_processing_java_video_library_Capture_start_read
import cv2

# 開啟第一台攝影機
cam = cv2.VideoCapture(0) #0:第1台 1:第2台

if not cam.isOpened():
    print("攝影機開啟失敗")
    exit()

print("攝影機已開啟")

# 設定解析度
cam.set(cv2.CAP_PROP_FRAME_WIDTH,640) #視訊寬度
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,480) #視訊高度

while True: # 迴圈會一直跑 直到有break跳開結束 
    

    #讀取一張畫面
    ret, frame = cam.read()

    if not ret:
        print("讀取失敗")
        break

    #顯示畫面
    cv2.imshow("Camera", frame)
    
    if cv2.waitKey(1)==27: #按ESC離開
        break
    #按q離開
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()