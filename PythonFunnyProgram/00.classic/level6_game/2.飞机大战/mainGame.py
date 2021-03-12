import random

import pygame
from pygame.locals import *

vec = pygame.math.Vector2

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 800

CREATE_ENEMY = pygame.USEREVENT + 1
SHOOT_TIMER = pygame.USEREVENT + 2


class TextureSpliter(object):
    def __init__(self, name):
        self.image = pygame.image.load('resources/image/{0}.png'.format(name))
        self.images = {}
        f = open('resources/image/{0}.pack'.format(name))
        lines = f.readlines()
        line_num = len(lines)
        for idx in range(5, line_num, 7):
            name = lines[idx].strip()
            xy = list(map(int, lines[idx + 2].strip().split(':')[1].split(',')))
            size = list(map(int, lines[idx + 3].strip().split(':')[1].split(',')))
            self.images[name] = self.image.subsurface(pygame.Rect(xy, size))

    def texture(self, names):
        images = []
        for name in names:
            images.append(self.images[name])
        return images


texture_spliter = TextureSpliter('shoot')


class MovableBase(pygame.sprite.Sprite):
    def __init__(self,
                 normal_images=[pygame.Surface((50, 50))],
                 crash_images=[],
                 pos=(0, 0), speed=(0, 0), auto=False):
        pygame.sprite.Sprite.__init__(self)
        self.images = normal_images  # normal image list
        self.crash_images = crash_images  # crash image list
        self.speed = vec(speed)
        self.pos = vec(pos)
        self.crash = False  # 是否被击中

        self.image = self.images[0]
        self.rect = self.images[0].get_rect()
        self.rect.center = pos
        self.auto = auto
        self.frame = 0

    def crashed(self):
        self.crash = True
        self.frame = 0

    def out_of_range(self, full=True):
        if full:
            if self.rect.bottom < 0:
                return True
            if self.rect.top > SCREEN_HEIGHT:
                return True
            return False

    def update(self, screen):
        if self.auto:
            self.pos += self.speed
        else:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.pos.x += -self.speed.x
                if self.pos.x < 0:
                    self.pos.x = 0
            if keys[pygame.K_RIGHT]:
                self.pos.x += self.speed.x
                if self.pos.x > SCREEN_WIDTH:
                    self.pos.x = SCREEN_WIDTH
            if keys[pygame.K_UP]:
                self.pos.y += -self.speed.y
                if self.pos.y < 0:
                    self.pos.y = 0
            if keys[pygame.K_DOWN]:
                self.pos.y += self.speed.y
                if self.pos.y > SCREEN_HEIGHT:
                    self.pos.y = SCREEN_HEIGHT

        show_image = None
        if not self.crash:
            self.frame = (self.frame + 0.13) % len(self.images)
            show_image = self.images[int(self.frame)]
        else:
            self.frame = (self.frame + 0.13)
            if int(self.frame) >= len(self.crash_images):
                show_image = self.crash_images[len(self.crash_images) - 1]
                self.kill()
            else:
                show_image = self.crash_images[int(self.frame)]
        self.image = show_image
        self.rect.center = self.pos


class Hero(MovableBase):
    def __init__(self):
        super().__init__(texture_spliter.texture(['hero1', 'hero2']),
                         texture_spliter.texture(
                             ['hero_blowup_n1', 'hero_blowup_n2', 'hero_blowup_n3', 'hero_blowup_n4']),
                         pos=(SCREEN_WIDTH // 2, 500), speed=(5, 5))
        self.bullets = pygame.sprite.Group()  # 玩家飞机所发射的子弹的集合
        self.can_shoot = True
        pygame.time.set_timer(SHOOT_TIMER, 500)

    def update(self, screen):
        super().update(screen)
        for e in pygame.event.get(SHOOT_TIMER):
            self.can_shoot = True
        if self.can_shoot:
            key_pressed = pygame.key.get_pressed()
            if key_pressed[K_SPACE]:
                self.shoot()
                self.can_shoot = False

        self.bullets.update(screen)
        self.bullets.draw(screen)

    def hit_enemy(self, enemies):
        ret = pygame.sprite.groupcollide(self.bullets, enemies, False, False, pygame.sprite.collide_mask)
        cnt = 0
        for k, v in ret.items():
            remove = False
            for e in v:
                if not e.crash:
                    remove = True
                    e.crash = True
                    cnt += 1
            if remove:
                k.remove(self.bullets)

        ret = pygame.sprite.spritecollide(self, enemies, False, pygame.sprite.collide_mask)

        for e in ret:
            if not e.crash:
                self.crash = True
                e.crash = True
                cnt += 1

        return cnt

    def shoot(self):
        bullet = MovableBase(texture_spliter.texture(['bullet2']), None, self.rect.midtop, speed=(0, -5), auto=True)
        self.bullets.add(bullet)


class Enemies(object):
    def __init__(self):
        super().__init__()
        pygame.time.set_timer(CREATE_ENEMY, 1200)
        self.enemies = pygame.sprite.Group()

    def create_enemy(self):
        enemy = MovableBase(
            texture_spliter.texture(['enemy1']),
            texture_spliter.texture(['enemy1_down1', 'enemy1_down2', 'enemy1_down3', 'enemy1_down4']),
            pos=(random.randint(0, SCREEN_WIDTH), 10), speed=(0, 5), auto=True)
        self.enemies.add(enemy)

    def update(self, screen):
        for e in pygame.event.get(CREATE_ENEMY):
            self.create_enemy()
        pygame.event.clear(CREATE_ENEMY)

        out_of_ranges = []
        for e in self.enemies.sprites():
            if e.out_of_range():
                out_of_ranges.append(e)

        for e in out_of_ranges:
            self.enemies.remove(e)

        self.enemies.update(screen)
        self.enemies.draw(screen)


class MainWindow():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('2.飞机大战')
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.background = pygame.image.load('resources/image/background.png')
        self.game_over = pygame.image.load('resources/image/gameover.png')
        self.running = True

    def show(self):
        score = 0
        hero = Hero()
        hero_group = pygame.sprite.Group()
        hero_group.add(hero)
        enemies = Enemies()
        clock = pygame.time.Clock()
        self.running = True
        while self.running:
            clock.tick(30)
            self.screen.blit(self.background, (0, 0))
            enemies.update(self.screen)
            hero.update(self.screen)
            score += hero.hit_enemy(enemies.enemies)
            hero_group.draw(self.screen)
            self.updateScore(score)
            if not hero.groups():
                self.running = False
            pygame.display.update()
            self.checkQuit()
        self.screen.blit(self.game_over, (0, 0))
        self.checkReplay()

    def updateScore(self, score):
        score_font = pygame.font.Font(None, 36)
        score_text = score_font.render('Score: ' + str(score), True, (128, 128, 128))
        text_rect = score_text.get_rect()
        text_rect.topleft = [10, 10]
        self.screen.blit(score_text, text_rect)

    def checkReplay(self):
        while True:
            pygame.display.update()
            self.checkQuit()
            key_pressed = pygame.key.get_pressed()
            if key_pressed[K_SPACE]:
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
