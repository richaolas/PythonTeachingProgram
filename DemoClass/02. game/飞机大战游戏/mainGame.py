import pygame
from pygame.locals import *
import random

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 800

class Bullet(pygame.sprite.Sprite):
    def __init__(self, bullet_img, init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        self.rect = bullet_img.get_rect()
        self.rect.midbottom = init_pos
        self.speed = 10

    def move(self):
        self.rect.top -= self.speed

class Enemy(pygame.sprite.Sprite):
    def __init__(self, enemy_img, enemy_down_imgs, init_pos, bullet_img):
        pygame.sprite.Sprite.__init__(self)
        self.image = enemy_img
        self.rect = enemy_img.get_rect()
        self.rect.topleft = init_pos
        self.speed = 1
        self.down_imgs = enemy_down_imgs
        self.down_index = 0
        self.bullet_image = bullet_img
        self.bullets = pygame.sprite.Group()
        self.shoot_frequency = 0

    def move(self):
        self.rect.top += self.speed
        self.shoot()
        self.moveBullet()

    def drawImg(self, scr):
        for i in range(7):
            scr.blit(self.down_imgs[self.down_index // 2], self.rect)
            self.down_index += 1

    def shoot(self):
        if self.shoot_frequency % 500 == 0:
            bullet = Enemy_Bullet(self.bullet_image, self.rect.midbottom)
            self.bullets.add(bullet)
        self.shoot_frequency += 1
        if self.shoot_frequency > 500:
            self.shoot_frequency = 1

    def moveBullet(self):
        for bullet in self.bullets:
            bullet.move()
            if bullet.rect.bottom < 0:
                self.bullets.remove(bullet)

    def drawBullets(self, scr):
        self.bullets.draw(scr)

class Enemy_Bullet(pygame.sprite.Sprite):
    def __init__(self, bullet_img, init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        self.rect = bullet_img.get_rect()
        self.rect.midbottom = init_pos
        self.speed = 1

    def move(self):
        self.rect.top += self.speed

class Player(pygame.sprite.Sprite):
    def __init__(self, plane_img, init_pos):
        player_rect = []
        player_rect.append(pygame.Rect(5, 99, 98, 126))  # 玩家精灵图片区域
        player_rect.append(pygame.Rect(170, 360, 98, 126))
        player_rect.append(pygame.Rect(165, 234, 102, 126))  # 玩家爆炸精灵图片区域
        player_rect.append(pygame.Rect(330, 624, 102, 126))
        player_rect.append(pygame.Rect(432, 624, 102, 126))
        player_rect.append(pygame.Rect(330, 498, 102, 126))
        self.image = []  # 用来存储玩家对象精灵图片的列表
        for i in range(len(player_rect)):
            self.image.append(plane_img.subsurface(player_rect[i]).convert_alpha())
        self.rect = player_rect[0]
        self.rect.topleft = init_pos
        self.speed = 1
        self.img_index = 0  # 玩家精灵图片索引
        self.temp = 0 #切换造型自增
        self.bullets = pygame.sprite.Group()  # 玩家飞机所发射的子弹的集合
        bullet_rect = pygame.Rect(1004, 987, 9, 21)
        self.bullet_image = plane_img.subsurface(bullet_rect)
        self.is_hit = False

    def moveUp(self):
        if self.rect.top <= 0:
            self.rect.top = 0
        else:
            self.rect.top -= self.speed

    def moveDown(self):
        if self.rect.top >= SCREEN_HEIGHT - self.rect.height:
            self.rect.top = SCREEN_HEIGHT - self.rect.height
        else:
            self.rect.top += self.speed

    def moveLeft(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        else:
            self.rect.left -= self.speed

    def moveRight(self):
        if self.rect.left >= SCREEN_WIDTH - self.rect.width:
            self.rect.left = SCREEN_WIDTH - self.rect.width
        else:
            self.rect.left += self.speed

    def drawPlane(self, scr):
        self.temp += 1
        if self.temp >= 2:
            self.temp = 0
        if self.is_hit:
            tmp_index = 0
            while tmp_index < 48:
                self.img_index = tmp_index // 8
                scr.blit(self.image[self.img_index], self.rect)
                tmp_index += 1
        else:
            scr.blit(self.image[self.img_index], self.rect)
            self.img_index = self.temp % 2

    def shoot(self):
        bullet = Bullet(self.bullet_image, self.rect.midtop)
        self.bullets.add(bullet)

    def moveBullet(self):
        for bullet in self.bullets:
            bullet.move()
            if bullet.rect.bottom < 0:
                self.bullets.remove(bullet)

    def drawBullets(self, scr):
        self.bullets.draw(scr)

class MainWindow():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('飞机联盟大纲')
        self.background = pygame.image.load('resources/image/background.png').convert()
        plane_img = pygame.image.load('resources/image/shoot.png')
        self.game_over = pygame.image.load('resources/image/gameover.png')
        self.player = Player(plane_img, [200, 600])
        # 定义敌机对象使用的surface相关参数
        self.enemies = pygame.sprite.Group()
        self.enemy_rect = pygame.Rect(534, 612, 57, 43)
        self.enemy_img = plane_img.subsurface(self.enemy_rect)
        self.enemies_down = pygame.sprite.Group()
        self.enemy_down_imgs = []
        self.enemy_down_imgs.append(plane_img.subsurface(pygame.Rect(267, 347, 57, 43)))
        self.enemy_down_imgs.append(plane_img.subsurface(pygame.Rect(873, 697, 57, 43)))
        self.enemy_down_imgs.append(plane_img.subsurface(pygame.Rect(267, 296, 57, 43)))
        self.enemy_down_imgs.append(plane_img.subsurface(pygame.Rect(930, 697, 57, 43)))
        enemy_bullet_rect = pygame.Rect(69, 78, 9, 21)
        self.enemy_bullet_img = plane_img.subsurface(enemy_bullet_rect)
        self.running = True

    def show(self):
        shoot_frequency = 0
        enemy_frequency = 0
        score = 0
        while self.running:
            self.screen.blit(self.background, (0, 0))
            enemy_frequency = self.createEnemy(enemy_frequency)
            self.moveEnemy()
            self.enemies.draw(self.screen)
            shoot_frequency = self.checkPressed(shoot_frequency)
            self.player.moveBullet()
            self.player.drawPlane(self.screen)
            self.player.drawBullets(self.screen)
            score = self.judgeEnemy(score)
            self.updateScore(score)
            pygame.display.update()
            self.checkQuit()
        self.screen.blit(self.game_over, (0, 0))
        self.checkReplay()

    def createEnemy(self, frequency):
        if frequency % 300 == 0:
            self.enemy_pos = [random.randint(0, SCREEN_WIDTH - self.enemy_rect.width), 0]
            self.enemy = Enemy(self.enemy_img, self.enemy_down_imgs, self.enemy_pos, self.enemy_bullet_img)
            self.enemies.add(self.enemy)
        frequency += 1
        if frequency >= 500:
            frequency = 0
        return frequency

    def moveEnemy(self):
        for enemy in self.enemies:
            enemy.move()
            enemy.drawBullets(self.screen)
            # 判断玩家是否被击中
            if pygame.sprite.collide_circle(enemy, self.player):
                self.enemies_down.add(enemy)
                self.enemies.remove(enemy)
                self.player.is_hit = True
                self.running = False
                break
            if enemy.rect.top > SCREEN_HEIGHT:
                self.enemies.remove(enemy)
            for b in enemy.bullets:
                if pygame.sprite.collide_circle(b, self.player):
                    self.player.is_hit = True
                    self.running = False
                    break

    def judgeEnemy(self, sc):
        # 将被击中的敌机对象添加到击毁敌机Group中，用来渲染击毁动画
        down_dic = pygame.sprite.groupcollide(self.enemies, self.player.bullets, 1, 1)
        for enemy_down in down_dic:
            self.enemies_down.add(enemy_down)
        # 绘制敌机击毁动画
        for enemy_down in self.enemies_down:
            enemy_down.drawImg(self.screen)
            self.enemies_down.remove(enemy_down)
            sc += 1
        return sc

    def updateScore(self, score):
        score_font = pygame.font.Font(None, 36)
        score_text = score_font.render('Score: ' + str(score), True, (128, 128, 128))
        text_rect = score_text.get_rect()
        text_rect.topleft = [10, 10]
        self.screen.blit(score_text, text_rect)

    def checkPressed(self, frequency):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[K_UP]:
            self.player.moveUp()
        if key_pressed[K_DOWN]:
            self.player.moveDown()
        if key_pressed[K_LEFT]:
            self.player.moveLeft()
        if key_pressed[K_RIGHT]:
            self.player.moveRight()
        if key_pressed[K_SPACE]:
            # 控制发射子弹频率,并发射子弹
            if frequency %40 == 0:
                self.player.shoot()
            frequency += 1
            if frequency >= 40:
                frequency = 0
        return frequency

    def checkReplay(self):
        while 1:
            pygame.display.update()
            self.checkQuit()
            key_pressed = pygame.key.get_pressed()
            if key_pressed[K_F1]:
                self.running = True
                self.player.is_hit = False
                for i in self.enemies:
                    self.enemies.remove(i)
                self.show()
                break

    def checkQuit(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()


if __name__ == "__main__":
    game = MainWindow()
    game.show()