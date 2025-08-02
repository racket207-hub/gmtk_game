import pygame
import settings
#import math 



class Player(pygame.sprite.Sprite):
    def __init__(self, state):
        super().__init__()
        self.state = state
        self.player_walk = settings.get_sprites(self.state)
        self.player_index = 0

        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(center = (settings.WINDOW_WIDTH/2, settings.WINDOW_HEIGHT/2))
        self.speed = 4

    def set_state(self, new_state):
        if new_state != self.state:
            self.state = new_state
            self.player_walk = settings.get_sprites(self.state)
            self.player_index = 0  # Optionally reset animation


    def animation_state(self):
        self.player_index += 0.1
        if self.player_index >= len(self.player_walk): self.player_index = 0
        self.image = self.player_walk[int(self.player_index)]


    # def get_player_position_and_rotation():

    # keys = pygame.key.get_pressed()

    # direction = pygame.Vector2(keys[pg.K_d] - keys[pg.K_a], keys[pg.K_s] - keys[pg.K_w])

    # if direction.length() > 0:
    #     new_pos = player_pos + direction.normalize() * self.speed
    #     new_rot = -math.degrees(math.atan2(direction.y, direction.x))

    #     return (new_pos, new_rot)
    
    # return (player_pos, player_rotation)

    #movement method, it checks the state of the 'state' variable and 
    #moves the player accordingly, it also limits the movement of the 
    #player to the border of the screen with clamp_ip
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
            case "STOP":
                self.rect.x += 0
                self.rect.y += 0
        self.rect.clamp_ip(settings.screen_rect)

    
    
    def update(self, state):
        self.set_state(state)
        self.movement(state)
        self.animation_state()
        