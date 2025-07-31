from re import match
import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.Surface((32, 32))
        self.image.fill((0, 200, 255))
        self.rect = self.image.get_rect(center = (80, 300))
        self.speed = 4
        # self.state = "STOP"

    def movement(self, state):
        match state:
            case "UP":
                self.rect.y -= self.speed
            case "DOWN":
                self.rect.y += self.speed
            case "LEFT":
                self.rect.x -= self.speed
            case "RIGHT":
                self.rect.x += self.speed

        # if state == "LEFT":
        #     self.rect.y -= self.speed
        # elif state == "RIGHT":
        #     self.rect.x += self.speed
        # elif state == "UP":
        #     self.rect.y -= self.speed
        # elif state == "DOWN":
        #     self.rect.y += self.speed 
    
    def update(self, state): #, *args, **kwargs
        # return super().update(*args, **kwargs)
        self.movement(state)
        