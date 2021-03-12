import pygame


#
#
# pygame.init()
# screen = pygame.display.set_mode((800, 600), 0, 32)
# pygame.display.set_caption("精灵类测试")
# font = pygame.font.Font(None, 18)
# framerate = pygame.time.Clock()
#
# cat = MySprite(screen)
# cat.load("sprite.png", 100, 100, 4)
# group = pygame.sprite.Group()
# group.add(cat)
#
# while True:
#     x = framerate.tick(30) # 相对时间
#     ticks = pygame.time.get_ticks() # 绝对时间
#     #print(x, ticks)
#
#     for event in pygame.event.get():
#         print("#1", event.type, id(event))
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             exit()
#
#     for event in pygame.event.get():
#         print("#2", event.type, id(event))
#
#     key = pygame.key.get_pressed()
#     if key[pygame.K_ESCAPE]:
#         exit()
#
#     screen.fill((0, 0, 100))
#
#     group.update(ticks, 500)
#     group.draw(screen)
#     #cat.draw(screen)
#     pygame.display.update()

def min2maxrange(a, b):
    '''
    from min to max, exclude min and max, (min, max)
    '''
    return range(min(a, b) + 1, max(a, b))


class Block(pygame.sprite.Sprite):

    def __init__(self, image, loc):
        super(Block, self).__init__()
        self.image = image
        self.normal = image.copy()
        self.clicked = image.copy()
        pygame.draw.rect(self.clicked, (255, 0, 0), (0, 0, 40 - 1, 40 - 1), 2)
        self.rect = pygame.Rect(loc, image.get_size())

        self.isclicked = False
        self.visible = False

    def click(self):
        self.isclicked = not self.isclicked
        self.image = self.clicked if self.isclicked else self.normal
    # def click(self, x, y):
    #     if self.rect.left <= x <= self.rect.right and self.rect.top <= y <= self.rect.bottom:
    #         self.isclicked = not self.isclicked
    #         self.image = self.clicked if self.isclicked else self.normal
    #         return True
    #     return False


class Map:

    def __init__(self):
        super(Map, self).__init__()
        self.width = 10
        self.height = 10
        self.size = 40
        self.offsize = (0, 0)

        self.selected = []
        self.imageSouce = pygame.image.load('images/NARUTO.png')
        self.images = []
        for index in range(0, self.imageSouce.get_width() // self.size):
            self.images.append(self.imageSouce.subsurface(self.size * index, 0, self.size, self.size))

        self.reset()

    def reset(self):
        self.rows = [[None] * (self.width + 2)] * (self.height + 2)
        self.cols = [[None] * (self.width + 2)] * (self.height + 2)
        # print(self.blocks)
        self.blocks = pygame.sprite.Group()

        for r in range(self.height + 2):
            for c in range(self.width + 2):
                if r == 0 or r == self.height + 1 or c == 0 or c == self.width + 1:
                    pass
                    # pygame.draw.rect(screen, (255, 255, 255), (
                    # self.offsize[0] + c * self.size, self.offsize[1] + r * self.size, self.size, self.size), self.blocks[r][c])
                    # blockrow.append(None)
                else:
                    block = Block(self.images[0], (self.offsize[0] + c * self.size, self.offsize[1] + r * self.size))
                    self.blocks.add(block)
                    self.rows[r][c] = block
                    self.cols[c][r] = block
                    # blockrow.append(Block(self.images[0], (self.offsize[0] + c * self.size, self.offsize[1] + r * self.size)))
                    # pygame.draw.rect(screen, (255, 0, 0), (
                    # self.offsize[0] + c * self.size, self.offsize[1] + r * self.size, self.size, self.size), self.blocks[r][c])

        # for c in range(self.width + 2):
        #     for r in range(self.height + 2):
        #         blockcol = []

        # for r in range(self.height):
        #     self.bl
        #     row = []
        #     for c in range(self.width):
        #         row.append()

    def draw(self, screen):
        self.blocks.draw(screen)
        # for r in range(self.height + 2):
        #    for c in range(self.width + 2):
        #        if self.blocks[r][c]:
        #            self.blocks[r][c]
        # if r == 0 or r == self.height + 1 or c == 0 or c == self.width + 1:
        # pygame.draw.rect(screen, (255, 255, 255), (
        # self.offsize[0] + c * self.size, self.offsize[1] + r * self.size, self.size, self.size), self.blocks[r][c])
        #    pass
        # else:

        # pygame.draw.rect(screen, (255, 0, 0), (
        # self.offsize[0] + c * self.size, self.offsize[1] + r * self.size, self.size, self.size), self.blocks[r][c])

    def click(self, x, y):
        x -= self.offsize[0]
        y -= self.offsize[1]
        r = y // self.size
        c = x // self.size
        if 1 <= r <= self.height and 1 <= c <= self.width:
            # self.blocks_array[r][c].click()
            block = self.rows[r][c]
            if block:
                self.blocks.remove(block)
                self.rows[r][c] = None
                self.cols[c][r] = None

        # if self.

    def link(self, r1, c1, r2, c2):
        # 测试横向连接
        if r1 == r2:
            any(self.rows[r1][min(c1, c2) + 1:max(c1, c2)])

        if c1 == c2:
            any(self.cols[c1][min(r1, r2) + 1:max(r1, r2)])
            # for i in min2maxrange(c1, c2):
            #    if self.blocks_array[r1][i]:

        # pass


class Game(object):

    def __init__(self):
        super(Game, self).__init__()
        pygame.init()

        self.screen = pygame.display.set_mode((800, 600), 0, 32)
        pygame.display.set_caption("连连看")
        self.clock = pygame.time.Clock()
        imageSouce = pygame.image.load('images/NARUTO.png')
        self.images = []
        size = 40
        for index in range(0, imageSouce.get_width() // size):
            self.images.append(imageSouce.subsurface(size * index, 0, size, size))
        # for index in range(0, int(self.__iconKind)):
        #     region = imageSouce.crop((self.__iconWidth * index, 0,
        #                               self.__iconWidth * index + self.__iconWidth - 1, self.__iconHeight - 1))
        #     self.images.append(ImageTk.PhotoImage(region))

    def run(self):

        # self.blocks = pygame.sprite.Group()
        # self.blocks.add(Block(None, (100, 100)))
        m = Map()

        while True:
            x = self.clock.tick(30)  # 相对时间
            ticks = pygame.time.get_ticks()  # 绝对时间
            # print(x, ticks)

            for event in pygame.event.get():
                # print("#1", event.type, id(event))
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # for b in self.blocks:
                    m.click(*pygame.mouse.get_pos())
            self.screen.fill((0, 0, 100))
            m.draw(self.screen)
            # self.blocks.draw(self.screen)
            #
            # for event in pygame.event.get():
            #     print("#2", event.type, id(event))
            #
            # key = pygame.key.get_pressed()
            # if key[pygame.K_ESCAPE]:
            #     exit()
            #
            # screen.fill((0, 0, 100))
            #
            # group.update(ticks, 500)
            # group.draw(screen)
            # #cat.draw(screen)
            pygame.display.update()


game = Game()
game.run()

# m = Map()
