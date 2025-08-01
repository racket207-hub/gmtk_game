import pygame
import settings
from random import randrange, choice

class Enemy(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()

        self.image = pygame.Surface(settings.ENTITY_SURFACE)
        #self.image.fill((255, 0, 0))
        edges = list(range(0, 100, 10)) + list(range(540, 640, 10)) + list(range(100, 540, 10)) + list(range(640, 100, 10))
        x_range = choice(edges)
        y_range = choice(edges)
        # x_range = choice(randrange([0, 640, 10]), randrange([640, 490, 10]))
        # y_range = choice(randrange([0, 640, 10]), randrange([640, 490, 10]))
        # x_range = 50
        # y_range = 100
        self.rect = self.image.get_rect(center = (x_range, y_range))
        self.speed = 4
        if type == 'goon':
            self.image.fill((255, 0, 0))
        else:
            self.image.fill((0, 255, 0))

    # def enemy_spawner(self, timer):
    #     for event in pygame.event.get():
    #         if event.type == timer:
    #            self.draw(settings.screen)
    #            print("draw")

    # def update(self, timer):
    #     self.enemy_spawner(timer)