import os
import random
import sys

import pygame

os.environ['SDL_VIDEO_CENTERED'] = '1'  # 居中显示


class Button(pygame.sprite.Sprite):
    '''
    按钮
    '''

    def __init__(self, loc, res_url):
        self.image = pygame.image.load(res_url)
        self.rect = self.image.get_rect()
        self.rect.center = loc

    def isPressd(self, loc):
        return self.inRect(loc, self.rect)

    def inRect(self, pos, rect):
        x, y = pos
        rx, ry, rw, rh = rect.x, rect.y, rect.width, rect.height
        if (rx <= x <= rx + rw) and (ry <= y <= ry + rh):
            return True
        return False

    def update(self, screen):
        screen.blit(self.image, self.rect)

class Land(pygame.sprite.Sprite):

    def __init__(self):
        self.image_left = pygame.image.load("./res/assets/land.png")
        self.rect_left = self.image_left.get_rect()
        self.rect_left.right = width
        self.rect_left.bottom = height
        self.image_right = pygame.image.load("./res/assets/land.png")
        self.rect_right = self.image_right.get_rect()
        self.rect_right.left = self.rect_left.right
        self.rect_right.bottom = height
        #self.image2 = pygame.image.load("./res/assets/land.png")
        #self.rect2 = self.image1.get_rect()

    def update(self,*args, **kwargs):
        self.rect_left.x -= 5
        self.rect_right.x -= 5
        if self.rect_right.x <= 0:
            self.rect_left.left = self.rect_right.right
            self.rect_left, self.rect_right = self.rect_right, self.rect_left
        screen.blit(self.image_left, self.rect_left)
        screen.blit(self.image_right, self.rect_right)

class Bird(pygame.sprite.Sprite):
    """定义一个鸟类"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        """定义初始化方法"""
        # 定义鸟的3种状态列表
        self.birdStatus = [
            pygame.image.load("./res/assets/bird0_0.png"),
            pygame.image.load("./res/assets/bird0_1.png"),
            pygame.image.load("./res/assets/bird0_2.png"),
            pygame.image.load("./res/assets/dead.png")]
        self.image = self.birdStatus[0]
        self.rect = self.image.get_rect()
        self.rect.center = (120, width // 2)
        self.frame = 0  # 默认飞行状态
        self.dead = False  # 默认小鸟生命状态为活着
        self.speed = 0
        self.mass = 10
        self.GRAVITY = 9.8
        self.acc = self.GRAVITY / self.mass
        self.live = False
        self.bump = 0
        self.isBump = False


    def update(self, screen):
        if self.live:
            self.rect.centery += self.speed
            self.speed += self.acc

        if self.isBump:
            self.bump += 1
            if self.bump <= 5:
                self.rect.y -= 1
            elif self.bump <= 5*2:
                self.rect.y += 1
            else:
                self.bump = 0

        self.frame = (self.frame + 0.3) % 3
        self.image = bird.birdStatus[int(bird.frame)]
        screen.blit(self.image, self.rect)


class Pipeline(pygame.sprite.Sprite):
    """定义一个管道类"""

    def __init__(self, location, pipeType):
        pygame.sprite.Sprite.__init__(self)
        """定义初始化方法"""
        self.image = pygame.image.load("./res/assets/pipe_" + pipeType + ".png")
        self.rect = self.image.get_rect()
        if pipeType == 'down':
            self.rect.centerx = location[0]
            self.rect.y = -self.rect.height + location[1]
        elif pipeType == 'up':
            self.rect.centerx = location[0]
            self.rect.y = location[1]
        else:
            raise TypeError('type error')

    def update(self):
        """"管道移动方法"""
        self.rect.centerx -= 5
        # self.wallx -= 5  # 管道X轴坐标递减，即管道向左移动
        # 当管道运行到一定位置，即小鸟飞越管道，分数加1，并且重置管道
        if self.rect.centerx < -80:
            global score
            score += 1

        if self.rect.centerx < -100:
            self.kill()


def createMap():
    """定义创建地图的方法"""
    screen.fill((255, 255, 255))  # 填充颜色
    screen.blit(background, (0, 0))  # 填入到背景

    # 显示管道
    pipeline_groups.draw(screen)
    pipeline_groups.update()

    # 显示小鸟
    if bird.dead:  # 撞管道状态
        bird.frame = 2

    #screen.blit(bird.image, bird.rect)
    bird.update(screen)  # 鸟移动

    # 显示分数
    screen.blit(font.render('Score:' + str(score), -1, (255, 255, 255)), (100, 50))  # 设置颜色及坐标位置
    pygame.display.update()  # 更新显示


def checkDead():
    # 上方管子的矩形位置
    # upRect = pygame.Rect(Pipeline.wallx, -300,
    #                      Pipeline.pineUp.get_width() - 10,
    #                      Pipeline.pineUp.get_height())
    #
    # # 下方管子的矩形位置
    # downRect = pygame.Rect(Pipeline.wallx, 500,
    #                        Pipeline.pineDown.get_width() - 10,
    #                        Pipeline.pineDown.get_height())
    # # 检测小鸟与上下方管子是否碰撞
    # if upRect.colliderect(bird.birdRect) or downRect.colliderect(bird.birdRect):
    #     bird.dead = True
    # 检测小鸟是否飞出上下边界
    if not 0 < bird.birdRect[1] < height:
        bird.dead = True
        return True
    else:
        return False


def getResutl():
    final_text1 = "Game Over"
    final_text2 = "Your final score is:  " + str(score)
    ft1_font = pygame.font.SysFont("Arial", 70)  # 设置第一行文字字体
    ft1_surf = font.render(final_text1, 1, (242, 3, 36))  # 设置第一行文字颜色
    ft2_font = pygame.font.SysFont("Arial", 50)  # 设置第二行文字字体
    ft2_surf = font.render(final_text2, 1, (253, 177, 6))  # 设置第二行文字颜色
    screen.blit(ft1_surf, [screen.get_width() / 2 - ft1_surf.get_width() / 2, 100])  # 设置第一行文字显示位置
    screen.blit(ft2_surf, [screen.get_width() / 2 - ft2_surf.get_width() / 2, 200])  # 设置第二行文字显示位置
    pygame.display.flip()  # 更新整个待显示的Surface对象到屏幕上


def generate_pipeline_pair():
    space_min, space_max = 100, 200
    top_min = 100
    space = random.randint(space_min, space_max)
    pos = random.randint(top_min, max(320, 512 - top_min - space))
    pipeline_down = Pipeline((width + 100, pos), 'down')  # 实例化管道类
    pipeline_up = Pipeline((width + 100, pos + space), 'up')  # 实例化管道类
    return pipeline_down, pipeline_up

def begin_screen():
    screen.blit(background, (0, 0))  # 填入到背景

if __name__ == '__main__':
    """主程序"""
    pygame.init()  # 初始化pygame
    pygame.font.init()  # 初始化字体
    font = pygame.font.SysFont("Arial", 50)  # 设置字体和大小
    size = width, height = 288, 512  # 设置窗口
    screen = pygame.display.set_mode(size)  # 显示窗口

    clock = pygame.time.Clock()  # 设置时钟

    bird_loc_x = 120
    bird = Bird()  # 实例化鸟类

    score = 0

    background = pygame.image.load("./res/assets/bg_day.png")  # 加载背景图片


    title = Button((width//2, 100), "./res/assets/title.png")
    button_play = Button((width // 4, height-112-26), "./res/assets/button_play.png")
    button_score = Button((width * 3 // 4, height-112-26), "./res/assets/button_score.png")
    land = Land()
    pipeline_groups = pygame.sprite.Group()

    pipeline_groups.add(generate_pipeline_pair())
    map_position = 0
    begin = False
    bird.isBump = True
    while not begin:
        clock.tick(30)  # 每秒执行60次
        # 轮询事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_play.isPressd(event.pos):
                    begin = True

        screen.blit(background, (0, 0))  # 填入到背景
        land.update(screen)

        title.update(screen)
        bird.update(screen)  # 鸟移动
        button_play.update(screen)
        button_score.update(screen)

        pygame.display.flip()

    bird.live = True
    bird.isBump = False
    while True:
        clock.tick(30)  # 每秒执行60次
        # 轮询事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if (event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN) and not bird.dead:
                bird.speed = -9

        map_position += 5
        if map_position >= 200:
            pipeline_groups.add(generate_pipeline_pair())
            map_position = 0

        if pygame.sprite.spritecollide(bird, pipeline_groups, False, None):  # 检测小鸟生命状态
            print("spritecollide")
            # getResutl()  # 如果小鸟死亡，显示游戏总分数
        # if checkDead():  # 检测小鸟生命状态
        #    getResutl()  # 如果小鸟死亡，显示游戏总分数
        # else:
        createMap()  # 创建地图

    pygame.quit()
