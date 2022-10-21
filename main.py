# Standard imports
import pygame

# Custom imports
import lib
import soldier

pygame.init()

# Main game container
class Game():
    def __init__(self):
        self.screen = pygame.display.set_mode([lib.SCREEN_WIDTH, lib.SCREEN_HEIGHT])
        pygame.display.set_caption(lib.WINDOW_TITLE)

        self.running = True

        self.clock = pygame.time.Clock()
        self.events = pygame.event.get()

        soldier.create_soliders(1)

    def run(self):
        while self.running:
            self.events = pygame.event.get()

            for event in self.events:
                if event.type == pygame.QUIT:
                    self.running = False

            self.draw()

            self.update()
    
    def draw(self):
        self.screen.fill(lib.color.BLACK)

        soldier.draw_soldiers(self.screen)

    def update(self):
        soldier.update_soldiers()

        pygame.display.update()
        lib.delta_time = self.clock.tick() / 1000

if __name__ == '__main__':
    game = Game()
    game.run()
    pygame.quit()