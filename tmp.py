import turtle

x = 0.1

for i in range(1000):
    y = 1/x
    turtle.goto(x*50,y*50)
    x += 0.1
# turtle.speed(1)
# turtle.pencolor('red')
# turtle.forward(0.1)
# turtle.left(90)
# turtle.forward(100)
#
# turtle.goto()
# turtle.penup()
# turtle.home()
# turtle.pendown()
# turtle.pencolor('blue')
# turtle.forward(0.9)
# turtle.left(90)
# turtle.forward(100)

turtle.done()







# import turtle
#
# turtle.setup(100,100)
# turtle.bgpic('timg.gif')
#
# turtle.done()








# import tensorflow as tf
#
# inputs = tf.random.normal([1, 7, 7, 3])
# print(inputs.shape)
# conv = tf.keras.layers.Conv2D(6, 3, strides=2, padding='same')
# outputs = conv(inputs)
# print(outputs.shape)
#
#
# # x = tf.random.normal([1,56,56,3]) # 模拟输入，3 通道，高宽为5
# #
# #
# # layer = tf.keras.layers.Conv2D(4,kernel_size=3,strides=1,padding='SAME')
# # out = layer(x) # 前向计算
# # print(layer.p)
# # #layer.build(x)
# # #print(layer.input)
# # print(out.shape)


















# import turtle
# # turtle.speed(0)
# # #turtle.tracer(80, 40000000000)
# #
# # # for i in range(100):
# # #     turtle.forward(10)
# # #     turtle.left(1)
# # #turtle.getscreen().tracer(8, 25)
# # #turtle.tracer(0, 10)
# # #turtle.delay(40)
# # dist = 2
# # for i in range(200):
# #     turtle.fd(dist)
# #     turtle.rt(90)
# #     dist += 2
# #     #turtle.update()
#
# # importing package
# import turtle
#
# # loop for motion with
# # default tracer as 1
# for i in range(20):
#     turtle.forward(1 + 1 * i)
#     turtle.right(45)
#
# # set tracer values as (2,0)
# # 2 -> for screen update
# # 0 -> delay
# turtle.tracer(n=2, delay=0)
#
# # loop for motion with
# # above tracer values
# for i in range(20, 40):
#     turtle.forward(1 + 1 * i)
#     turtle.right(45)
#
# # set tracer values as (1,50)
# # 1 -> for screen update
# # 50 -> delay
# turtle.tracer(n=1, delay=50)
#
# # loop for motion with
# # above tracer values
# for i in range(40, 60):
#     turtle.forward(1 + 1 * i)
#     turtle.right(45)
#
# turtle.done()
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# # '''
# # 我们先大体了解游戏代码的构成，游戏代码的六个组成部分:
# # 1. 加载游戏中所需的模块：这个是标准的东西，套路啦，你懂的~
# # 2. 资源处理类：定义一些类来处理最基本的资源，这些资源将加载图像和声音，以及连接和断开网络，加载保存游戏文件以及用户可能拥有的任何其他资源。
# # 3. 游戏对象类：定义游戏对象的类。
# # 4. 任何其他游戏功能：定义其他必要的功能，例如记分板，菜单处理等。
# # 5. 初始化游戏：包括pygame对象本身，背景，游戏对象（初始化类的实例）以及可能想要添加的任何其他一些代码。
# # 6. 主循环：将任何输入处理（即，观察用户按键/鼠标按钮），更新游戏对象的代码，最后更新屏幕。
# # '''
# #
# # # import zone
# # import pygame
# # import sys
# #
# # # initialize pygame
# # pygame.init()
# # # create a screen
# # screen = pygame.display.set_mode([800,600])
# # clock = pygame.time.Clock()
# # # fill with color WHITE
# # screen.fill([255,255,255])
# # # load and show the image of lanbo
# # jpgFileName = '.dingdang.png'
# # imgRect = pygame.image.load(jpgFileName)
# # screen.blit(imgRect,[0,0])
# # # load and show the sound of firstblood
# # wavFileName = './res/first/FirstBlood.wav'
# # #sndTrack = pygame.mixer.music.load(wavFileName)
# #
# # #pygame.mixer.music.play()
# # # flip
# # #pygame.display.flip()
# # # LOOP: mRunning
# # mRunning = True
# #
# # w = 10
# # h = 20
# #
# # FPS = 30
# #
# # while mRunning:
# #     clock.tick(FPS)
# #     for event in pygame.event.get():
# #         if event.type == pygame.QUIT:
# #             mRunning = False
# #     screen.fill([255, 255, 255])
# #
# #
# #     pygame.display.flip()
# #
# # pygame.quit()
# # sys.exit()