# day02_8b_processing_python_array
img = None
img2 = None

a = [
    [1,1,1,1,1],
    [1,1,1,1,1],
    [1,1,1,1,1]
]

def setup():
    global img, img2
    size(500,300)
    img = loadImage("cat2.png")
    img2 = loadImage("cat3.png")


def draw():
    background(255)

    for i in range(3):
        for j in range(5):

            if a[i][j] == 1:
                image(img, j*100, i*100, 100, 100)

            elif a[i][j] == 2:
                image(img2, j*100, i*100, 100, 100)


def mousePressed():
    i = mouseY // 100
    j = mouseX // 100

    if 0 <= i < 3 and 0 <= j < 5:
        a[i][j] = (a[i][j] + 1) % 3
