#date:2020/12/02
#author:kang

import pygame
from random import*

class Bullet_Supply(pygame.sprite.Sprite):
    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/bullet_supply.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.width,self.height = bg_size[0],bg_size[1]
        self.rect.left = randint(0,self.width-self.rect.width) 
        self.rect.bottom = -100

        self.speed = 3
        self.active = False
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.active = False

    def reset(self):
        self.active = True
        self.rect.left = randint(0,self.width-self.rect.width) 
        self.rect.bottom = -100
        
class Bomb_Supply(pygame.sprite.Sprite):
    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/bomb_supply.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.width,self.height = bg_size[0],bg_size[1]
        self.rect.left = randint(0,self.width-self.rect.width) 
        self.rect.bottom = -100

        self.speed = 3
        self.active = False
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.active = False

    def reset(self):
        self.active = True
        self.rect.left = randint(0,self.width-self.rect.width) 
        self.rect.bottom = -100

#ending:2020/12/02/21:44
#author:kang
        
