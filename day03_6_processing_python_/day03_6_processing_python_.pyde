# day03_6_processing_python_countdown
# 修改自day03_5_processing_python_countdown
# 有時變負數、而且太快開始、而且不能暫停!
# (1)用max()找最大值 max(負數,0)
#stay# (2)要可以{修改}鬧鐘 用mouseDragged來滑動 用day03_3的mouseDrsgged來滑動
# (3)要可以暫停
target=0 #我們的目標時間
def setup(): #設定的函式
     global target  #要可以修改外面的target變數
     size(500,200) #視窗大小
     mm=minute() #分鐘(現在的時間)
     ss=second() #秒鐘(現在的時間)
     target=(mm+0)*60+ss+10#我們的target目標時間
    
def draw(): #畫圖的函式
    background(0) #背景黑色
    textSize(150) #字很大 150號字
    remain=max(target-minute()*60-second(),0) #剩下的秒數
    mm=remain//60 #分鐘
    ss=remain%60 #秒鐘
    text(nf(mm,2)+":"+nf(ss,2),80,150) #換成數字
