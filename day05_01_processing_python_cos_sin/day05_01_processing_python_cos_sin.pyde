# day05_01_processing_python_cos_sin_dragonballs
# 國中教cos() sin():學cos()sin()有什麼用?
# 老師在大學3D電腦圖學 很有用
size(400,400) #視窗大小 400*400 正中心(200,200)
ellipse(200,200,300,300) #圓 正中心(200,200) 圓的大小 300*300

for i in range(7): #七龍珠 有7個龍珠
    a=(PI*2/7)*i #對應的角度a 是1/7個圓*i
    fill(255,0,0)
    ellipse(200+150*cos(a),200+150*sin(a),80,80) #畫出80*80的小圓
    
    #圓心200 半徑150 X座標對應cos(a)
    #圓心200 半徑150 Y座標對應sin(a)
