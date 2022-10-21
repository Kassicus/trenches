import pygame
import random

import lib

class Soldier(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        
        self.pos = pygame.math.Vector2(x, y)
        self.velocity = pygame.math.Vector2(0, 0)

        self.width = 15
        self.height = 25

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(lib.color.WHITE)

        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def update(self):
        self.pos += self.velocity * lib.delta_time
        self.rect.center = self.pos

class RifleMan(Soldier):
    def __init__(self, x, y):
        super().__init__(x, y)