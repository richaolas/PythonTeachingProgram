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

# initialize pygame
pygame.init()
# create a screen
screen = pygame.display.set_mode([800,600])
# fill with color WHITE
screen.fill([255,255,255])
# load and show the image of lanbo
jpgFileName = './res/first/lanbo800_600.jpg'
imgRect = pygame.image.load(jpgFileName)
screen.blit(imgRect,[0,0])
# load and show the sound of firstblood
wavFileName = './res/first/FirstBlood.wav'
sndTrack = pygame.mixer.music.load(wavFileName)

r = pygame.rect()


pygame.mixer.music.play()
# flip
pygame.display.flip()
# LOOP: mRunning
mRunning = True
while mRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mRunning = False
    screen.fill([255, 255, 255])
    screen.blit(imgRect, [0, 0])
    #pygame.display.flip()

pygame.quit()
sys.quit()