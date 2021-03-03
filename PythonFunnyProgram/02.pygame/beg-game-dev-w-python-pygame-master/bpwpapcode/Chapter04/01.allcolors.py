import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))

all_colors = pygame.Surface((4096, 4096), depth=24)

for r in range(256):
    print(r + 1, "out of 256")
    # 第4位代表横坐标，高4位代表纵坐标
    # 范围 [0-15] x [0-15] 横纵16个方格
    x = (r & 15) * 256  # 15 -> 0b1111
    y = (r >> 4) * 256
    # 每个方格又分成 256x256 个像素
    # 所以图像尺寸：256 x 16 = 4096
    for g in range(256):
        for b in range(256):
            all_colors.set_at((x + g, y + b), (r, g, b))

pygame.image.save(all_colors, "allcolors.bmp")
