import pygame

import lib

class Trench(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int) -> None:
        super().__init__()

        self.pos = pygame.math.Vector2(x, y)

        self.image = pygame.Surface([75, 600])
        self.image.fill(lib.color.WHITE)