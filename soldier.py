import pygame
import random

import lib

_soldiers = pygame.sprite.Group()

def draw_soldiers(draw_surface):
    _soldiers.draw(draw_surface)

def update_soldiers():
    _soldiers.update()

def create_soliders(count):
    for s in range(count):
        s = Soldier(100, random.randint(50, 650))
        _soldiers.add(s)

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