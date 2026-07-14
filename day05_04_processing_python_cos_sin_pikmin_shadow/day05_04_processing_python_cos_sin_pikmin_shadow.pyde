# day05_04_processing_python_cos_sin_pikmin_shadow
# 修改自day05_03_processing_python_cos_sin_pikmin
# 會有殘影唷
def setup():
    size(400,300) #400*300的一半(200,150)
    
def draw():
    background(54,39,155) #背景,深藍色
    for i in range(6):
        a=(PI*2/6)*i+radians(frameCount)*(mouseX/10)
        #rect(200+100*cos(a)-25,150+80*sin(a)-25,50,50) #手動對齊
        rectMode(CENTER) #改成直接對齊
        #rect(200+100*cos(a),150+80*sin(a),50,50)
        # #要有【殘影】remaining 剩下的影子
        for r in range(-3,1): #range(-3,1)會-3, -2, -1, 0
            fill(255,255/(-r+1)) #漸層的半透明白色
            rect(200+100*cos(a+r*.01),150+80*sin(a+r*0.1),50,50)
