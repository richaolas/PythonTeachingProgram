a = [1,2,3]
print(sum(a))






# # import pygame
# #
# #
# # class MySprite(pygame.sprite.Sprite):
# #     def __init__(self, target):
# #         pygame.sprite.Sprite.__init__(self)
# #         self.target_surface = target
# #         self.image = None
# #         self.master_image = None
# #         self.rect = None
# #         self.topleft = 0, 0
# #         self.frame = 0
# #         self.old_frame = -1
# #         self.frame_width = 1
# #         self.frame_height = 1
# #         self.first_frame = 0
# #         self.last_frame = 0
# #         self.columns = 1
# #         self.last_time = 0
# #
# #     def load(self, filename, width, height, columns):
# #         self.master_image = pygame.image.load(filename).convert_alpha()
# #         self.frame_width = width
# #         self.frame_height = height
# #         self.rect = 0, 0, width, height
# #         self.columns = columns
# #         rect = self.master_image.get_rect()
# #         self.last_frame = (rect.width // width) * (rect.height // height) - 1
# #
# #     def update(self, current_time, rate=60):
# #         if current_time > self.last_time + rate:
# #             self.frame += 1
# #             if self.frame > self.last_frame:
# #                 self.frame = self.first_frame
# #             self.last_time = current_time
# #
# #         if self.frame != self.old_frame:
# #             frame_x = (self.frame % self.columns) * self.frame_width
# #             frame_y = (self.frame // self.columns) * self.frame_height
# #             rect = (frame_x, frame_y, self.frame_width, self.frame_height)
# #             self.image = self.master_image.subsurface(rect)
# #             self.old_frame = self.frame
# #
# #
# # pygame.init()
# # screen = pygame.display.set_mode((800, 600), 0, 32)
# # pygame.display.set_caption("精灵类测试")
# # font = pygame.font.Font(None, 18)
# # framerate = pygame.time.Clock()
# #
# # cat = MySprite(screen)
# # cat.load("sprite.png", 100, 100, 4)
# # group = pygame.sprite.Group()
# # group.add(cat)
# #
# # while True:
# #     x = framerate.tick(30) # 相对时间
# #     ticks = pygame.time.get_ticks() # 绝对时间
# #     #print(x, ticks)
# #
# #     for event in pygame.event.get():
# #         print("#1", event.type, id(event))
# #         if event.type == pygame.QUIT:
# #             pygame.quit()
# #             exit()
# #
# #     for event in pygame.event.get():
# #         print("#2", event.type, id(event))
# #
# #     key = pygame.key.get_pressed()
# #     if key[pygame.K_ESCAPE]:
# #         exit()
# #
# #     screen.fill((0, 0, 100))
# #
# #     group.update(ticks, 500)
# #     group.draw(screen)
# #     #cat.draw(screen)
# #     pygame.display.update()
# #
# # '''
# # pygame.event.get()
# # get events from the queue
# # get(eventtype=None) -> Eventlist
# # get(eventtype=None, pump=True) -> Eventlist
# # This will get all the messages and remove them from the queue. If a type or sequence of types is given only those messages will be removed from the queue.
# #
# # If you are only taking specific events from the queue, be aware that the queue could eventually fill up with the events you are not interested.
# #
# # If pump is True (the default), then pygame.event.pump()internally process pygame event handlers will be called.
# #
# # Changed in pygame 1.9.5: Added pump argument
# #
# # '''
# #
# # a = 16
# # b = 10
# # for i in range(min(a,b)+1,max(a, b)):
# #     print(i)
#
# a = [[None]*10] * 10
# print(a)