import pygame
import settings
from random import randrange, choice

#method to spawn multiple enemies around the player
#returns the x and y coordinates 
def enemy_spawner():
    x_range = 0
    y_range = 0
    step = 10
    edge = choice(['top', 'bottom', 'left', 'right'])
    match edge:
        case 'top':
            x_range = randrange(0, settings.WINDOW_WIDTH, step)
            y_range = randrange(32, 150, step)
        case 'bottom':
            x_range = randrange(0, settings.WINDOW_WIDTH, step)
            y_range = randrange(490, settings.WINDOW_HEIGHT, step)
        case 'left':
            x_range = randrange(32, 150, step)
            y_range = randrange(0, settings.WINDOW_HEIGHT, step)
        case 'right':
            x_range = randrange(490, settings.WINDOW_WIDTH, step)
            y_range = randrange(0, settings.WINDOW_HEIGHT, step)
    return x_range, y_range

class Enemy(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()

        self.image = pygame.Surface(settings.ENTITY_SURFACE)
        self.rect = self.image.get_rect(center = enemy_spawner())
        self.speed = 4
        if type == 'goon':
            self.image.fill((255, 0, 0))
        else:
            self.image.fill((0, 255, 0))

