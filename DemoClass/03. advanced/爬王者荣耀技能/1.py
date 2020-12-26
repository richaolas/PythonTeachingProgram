import pygame

pygame.init()  # 游戏初始化
SCREENSIZE = pygame.Rect(0, 0, 900, 700)  # 获得屏幕的矩形区域
screen = pygame.display.set_mode(SCREENSIZE.size)  # 设置游戏窗口大小
pygame.display.set_caption("nba2k20")  # 设置游戏标题
ballx, bally = SCREENSIZE.center
RED = 255, 0, 0
BLUE = 0, 0, 255
GREEN = 0, 255, 0
BLACK = 0,0,0
rx = SCREENSIZE.centerx
ry = SCREENSIZE.bottom - 40
rw = 200
rh = 30
rx2 = SCREENSIZE.centerx
ry2 = SCREENSIZE.top + 10
rw2 = 200
rh2 = 30
vy = 1  #竖方向移动1个像素
vx = 1  #横方向移动1个像素
score1 = 0
score2 = 0
while True:  # 游戏循环
    screen.fill(BLACK)
    for event in pygame.event.get():  # 获取用户事件
        if event.type == pygame.QUIT:  # 发现用户按了关闭按钮
            pygame.quit()  # 卸载初始化的时候加载到内存的模块
            exit()  # 唯一作用，退出正在执行的程序
        elif event.type == pygame.MOUSEMOTION:
            rx = event.pos[0] - rw/2

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        rx2 -= 5
    elif keys[pygame.K_d]:
        rx2 += 5

    bally += vy
    ballx += vx
    pygame.draw.circle(screen, RED, (ballx, bally), 30)
    pygame.draw.rect(screen, BLUE, (rx, ry, rw, rh))  # 画屏幕下方的矩形
    pygame.draw.rect(screen, GREEN, (rx2, ry2, rw2, rh2))  # 画屏幕上方的矩形
    if bally + 30 > ry and rx < ballx < rx + rw: #and not or
        vy = -vy
    elif bally > ry - 30:
        score2 += 1
        ballx, bally = SCREENSIZE.center
    elif bally < ry2 + 10:
        score1 += 1
        ballx, bally = SCREENSIZE.center
    if rx < SCREENSIZE.left:
        rx = SCREENSIZE.left
    elif rx > SCREENSIZE.right - rw:
        rx = SCREENSIZE.right - rw
    if rx2 < SCREENSIZE.left:
        rx2 = SCREENSIZE.left
    elif rx2 > SCREENSIZE.right - rw2:
        rx2 = SCREENSIZE.right - rw2
    pygame.display.update()  # 更新屏幕
