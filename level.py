import pygame

import lib
import soldier

class Level():
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        self.trenches = pygame.sprite.Group()
        self.soldiers = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()

        test = soldier.RifleMan(100, 100)
        self.soldiers.add(test)

    def draw(self):
        self.trenches.draw(self.display_surface)
        self.soldiers.draw(self.display_surface)
        self.bullets.draw(self.display_surface)

    def update(self):
        self.trenches.update()
        self.soldiers.update()
        self.bullets.update()