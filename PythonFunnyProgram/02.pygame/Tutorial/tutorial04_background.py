# 1. 直接设计屏幕尺寸大小，1‘ 利用缩放贴满尺寸
# 2. 通过小块贴图 for for 帖全屏
# 3. 利用大的图片作为地图
# 4. 利用两张图片进行轮换无尽贴图

#import pygame
#picture = pygame.image.load(filename)
#picture = pygame.transform.scale(picture, (1280, 720))

def roll(self, role_x, role_y, WIN_WIDTH=640, WIN_HEIGHT=480):
    """
    地图滚动
    :param role_x: 角色相对于地图的坐标
    :param role_y:
    """
    # print(role_x, role_y)
    if role_x < WIN_WIDTH / 2:
        self.x = 0
    elif role_x > self.bottom.get_width() - WIN_WIDTH / 2:
        self.x = -(self.bottom.get_width() - WIN_WIDTH)
    else:
        self.x = -(role_x - WIN_WIDTH / 2)

    if role_y < WIN_HEIGHT / 2:
        self.y = 0
    elif role_y > self.bottom.get_height() - WIN_HEIGHT / 2:
        self.y = -(self.bottom.get_height() - WIN_HEIGHT)
    else:
        self.y = -(role_y - WIN_HEIGHT / 2)