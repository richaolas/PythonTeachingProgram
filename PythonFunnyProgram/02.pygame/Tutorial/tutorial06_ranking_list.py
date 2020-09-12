'''
我们先大体了解游戏代码的构成，游戏代码的六个组成部分:
1. 加载游戏中所需的模块：这个是标准的东西，套路啦，你懂的~
2. 资源处理类：定义一些类来处理最基本的资源，这些资源将加载图像和声音，以及连接和断开网络，加载保存游戏文件以及用户可能拥有的任何其他资源。
3. 游戏对象类：定义游戏对象的类。
4. 任何其他游戏功能：定义其他必要的功能，例如记分板，菜单处理等。
5. 初始化游戏：包括pygame对象本身，背景，游戏对象（初始化类的实例）以及可能想要添加的任何其他一些代码。
6. 主循环：将任何输入处理（即，观察用户按键/鼠标按钮），更新游戏对象的代码，最后更新屏幕。
'''
# import zone
import pygame
import sys
import random

# initialize pygame
pygame.init()
# create a screen
screen = pygame.display.set_mode([800,600])
clock = pygame.time.Clock()
# fill with color WHITE
screen.fill([255,255,255])
# load and show the image of lanbo
roles = []
scores = []
colors = []
for i in range(10):
    roles.append(pygame.image.load('./res/youxia/(%d).png'%(i+1)))
    scores.append(random.randint(30, 100))
    colors.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

# LOOP: mRunning
mRunning = True

FPS = 30

xmin, xmax = 100, 600
ymin = 20
h = 20
width = 0  #process
speed = 5

while mRunning:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mRunning = False
    screen.fill([255, 255, 255])

    for i in range(len(roles)):
        y = ymin + (h  + 40) * i
        w = width
        dst = scores[i] / 100 * (xmax-xmin) # 最终目标的长度
        if width > dst:                  # 如果没有达到最周目标，继续画
            w = dst
        pygame.draw.rect(screen, colors[i], (xmin, y, w, h))
        screen.blit(roles[i], [xmin + w + 4, y - (roles[i].get_rect().height-h)//2])

    if xmin + width < xmax:
        width += speed
    else:
        width = xmax - xmin

    pygame.display.flip()

pygame.quit()
sys.exit()