import pygame

import lib

class BaseUnit(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, weapon) -> None:
        super().__init__()

        self.pos = pygame.math.Vector2(x, y)
        self.vel = pygame.math.Vector2()

        self.weapon = weapon

        self.movement_speed = 100

        self.image = pygame.Surface([20, 35])
        self.image.fill(lib.color.WHITE)

        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def update(self) -> None:
        self.pos += self.vel * lib.delta_time
        self.rect.center = self.pos
