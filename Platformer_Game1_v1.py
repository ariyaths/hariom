# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 20:41:13 2021

@author: HariOm12
"""

import sys
import random
import pygame
from pygame import locals as pyglcl

pygame.init()
vec = pygame.math.Vector2  # 2 for two dimensional

HEIGHT = 450
WIDTH = 400
ACC = 0.5 # Acceleration
FRIC = -0.05 # Friction, original amount = -0.12
FPS = 60

FramePerSec = pygame.time.Clock()

displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Platformer_Game1")


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((128,255,40))
        self.rect = self.surf.get_rect()

        self.pos = vec((10, 385)) # Position
        self.vel = vec(0,0) # Velocity
        self.acc = vec(0,0) # Acceleration
        self.jumping = False

    def move(self):
        self.acc = vec(0,0.5)
        # top_pos = 50

        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[pyglcl.K_LEFT]:
            self.acc.x = -ACC

        if pressed_keys[pyglcl.K_RIGHT]:
            self.acc.x = ACC

        self.acc.x = self.acc.x + (self.vel.x * FRIC)
        self.vel = self.vel + self.acc
        self.pos = self.pos + (self.vel + (0.5 * self.acc))

        if self.pos.x > WIDTH:
            self.pos.x = 0

        if self.pos.x < 0:
            self.pos.x = WIDTH

        # if self.pos.y < top_pos:
        #     self.pos.y = top_pos
        #     self.vel = -self.vel

        self.rect.midbottom = self.pos

    def update(self):
        hits = pygame.sprite.spritecollide(P1 , platforms, False)
        if P1.vel.y > 0:
            if hits:
                self.pos.y = hits[0].rect.top + 1
                self.vel.y = 0

    def jump(self):
        hits = pygame.sprite.spritecollide(self, platforms, False)
        if hits and not self.jumping:
           self.jumping = True
           self.vel.y = -15

    def cancel_jump(self):
        if self.jumping:
            if self.vel.y < -3:
                self.vel.y = -3


class Platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((random.randint(50,100), 12))
        self.surf.fill((0,255,0))
        self.rect = self.surf.get_rect(center = (random.randint(0,WIDTH-10),
                                                 random.randint(0, HEIGHT-30)))


def check(platform, groupies):
    if pygame.sprite.spritecollideany(platform,groupies):
        return True
    else:
        for entity in groupies:
            if entity == platform:
                continue
            if (abs(platform.rect.top - entity.rect.bottom) < 50) and (abs(platform.rect.bottom - entity.rect.top) < 50):
                return True
        C = False


def plat_gen():
    while len(platforms) < HARD :
        width = random.randrange(50,100)
        p  = Platform()
        C = True

        while C:
             p = Platform()
             p.rect.center = (random.randrange(0, WIDTH - width),
                             random.randrange(-50, 0))
             C = check(p, platforms)

        platforms.add(p)
        all_sprites.add(p)


P1 = Player()
PT1 = Platform()

PT1.surf = pygame.Surface((WIDTH, 20))
PT1.surf.fill((255,0,0))
PT1.rect = PT1.surf.get_rect(center = (WIDTH/2, HEIGHT - 10))

all_sprites = pygame.sprite.Group()
all_sprites.add(PT1)
all_sprites.add(P1)

platforms = pygame.sprite.Group()
platforms.add(PT1)

for x in range(random.randint(5, 6)):
    pl = Platform()
    platforms.add(pl)
    all_sprites.add(pl)


while True:
    for event in pygame.event.get():
        pressed_keys = pygame.key.get_pressed()

        if event.type == pyglcl.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: # or pressed_keys[pyglcl.K_UP]:
                P1.jump()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                P1.cancel_jump()

    if P1.rect.top <= HEIGHT / 3:
        P1.pos.y = P1.pos.y + abs(P1.vel.y)

        for plat in platforms:
            plat.rect.y = plat.rect.y + abs(P1.vel.y)

            if plat.rect.top >= HEIGHT:
                plat.kill()

    displaysurface.fill((0,0,0))
    P1.move()
    P1.update()
    plat_gen()

    for entity in all_sprites:
        displaysurface.blit(entity.surf, entity.rect)

    pygame.display.update()
    FramePerSec.tick(FPS)
