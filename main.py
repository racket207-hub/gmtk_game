import pygame
import settings
from sys import exit
from Player_class import Player
from Enemy_class import Enemy


def player_input(game, state, event):
    if game:
        if event.type == pygame.KEYDOWN:
            #match case to check the pressed key
            match event.key:
                case pygame.K_w | pygame.K_UP:
                    state = "UP"
                case pygame.K_s | pygame.K_DOWN:
                    state = "DOWN"
                case pygame.K_d | pygame.K_RIGHT:
                    state = "RIGHT"
                case pygame.K_a | pygame.K_LEFT:
                    state = "LEFT"
        print(state)
        return state
    


def main():
    pygame.init()
    pygame.display.set_caption('Return from Death')
    clock = pygame.time.Clock()
    game_active = True
    state = "STOP"

    #player
    player = pygame.sprite.GroupSingle()
    player.add(Player())
    

    #enemy
    enemy = pygame.sprite.Group()
    enemy.add(Enemy())

    #game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            state = player_input(game_active, state, event)


        #screen
        settings.screen.fill(settings.BG_COLOR)

        #updating
        player.draw(settings.screen)
        enemy.draw(settings.screen)
        player.update(state)
        pygame.display.update()
        

        clock.tick(60)   
main()