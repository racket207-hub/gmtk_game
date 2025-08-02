import pygame

WINDOW_HEIGHT = 640
WINDOW_WIDTH = 640
BG_COLOR = (10, 0, 10)
screen = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
screen_rect = screen.get_rect()
ENTITY_SURFACE = (32, 32)



def get_sprites(state):
    match state:
        case "UP":
            player_image_1 = pygame.image.load('assets/Sprites/Player/idle_up_1.png').convert_alpha()
            player_image_2 = pygame.image.load('assets/Sprites/Player/idle_up_2.png').convert_alpha()
            player_image_3 = pygame.image.load('assets/Sprites/Player/idle_up_3.png').convert_alpha()
            player_image_4 = pygame.image.load('assets/Sprites/Player/idle_up_4.png').convert_alpha()
        case "DOWN" | "STOP":
            player_image_1 = pygame.image.load('assets/Sprites/Player/idle_down_1.png').convert_alpha()
            player_image_2 = pygame.image.load('assets/Sprites/Player/idle_down_2.png').convert_alpha()
            player_image_3 = pygame.image.load('assets/Sprites/Player/idle_down_3.png').convert_alpha()
            player_image_4 = pygame.image.load('assets/Sprites/Player/idle_down_4.png').convert_alpha()
        # case "LEFT":
        #     player_image_1 = pygame.image.load('assets/Sprites/Player/idle_left_1.png').convert_alpha()
        #     player_image_2 = pygame.image.load('assets/Sprites/Player/idle_left_2.png').convert_alpha()
        #     player_image_3 = pygame.image.load('assets/Sprites/Player/idle_left_3.png').convert_alpha()
        #     player_image_4 = pygame.image.load('assets/Sprites/Player/idle_left_4.png').convert_alpha()
        case "RIGHT" | "LEFT":
            player_image_1 = pygame.image.load('assets/Sprites/Player/idle_right_1.png').convert_alpha()
            player_image_2 = pygame.image.load('assets/Sprites/Player/idle_right_2.png').convert_alpha()
            player_image_3 = pygame.image.load('assets/Sprites/Player/idle_right_3.png').convert_alpha()
            player_image_4 = pygame.image.load('assets/Sprites/Player/idle_right_4.png').convert_alpha()
        
    #return a list of the player images
    #this is used to animate the player sprite
    #the player will change its image based on the state
    #it is in, this is done to create a walking animation
    #for the player
    return [player_image_1, player_image_2, player_image_3, player_image_4]


