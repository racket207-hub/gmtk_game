import pygame
import settings

class Player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.Surface((32, 32))
        self.image.fill((0, 200, 255))
        self.rect = self.image.get_rect(center = (200, 300))
        self.speed = 4

    #movement method, it checks the state of the 'state' variable and 
    #moves the player accordingly, it also limits the movement of the 
    #player to the border of the screen with clamp_ip
    def movement(self, state):
        #print(state)
        match state:
            case "UP":
                self.rect.y -= self.speed
            case "DOWN":
                self.rect.y += self.speed
            case "LEFT":
                self.rect.x -= self.speed
            case "RIGHT":
                self.rect.x += self.speed
        self.rect.clamp_ip(settings.screen_rect)
    
    def update(self, state):
        self.movement(state)
        