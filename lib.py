# Standar imports
import pygame
import random

# Constants
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 720

WINDOW_TITLE = "Trenches"

# Variables
delta_time = 0

# Colors
class ColorLibrary():
    def __init__(self):
        self.BLACK = pygame.Color(0, 0, 0, 255)
        self.WHITE = pygame.Color(255, 255, 255, 255)

    def get_random_color(self):
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        return color

color = ColorLibrary()