import pygame
import costants
from sys import exit
from Player_class import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((costants.WINDOW_HEIGHT, costants.WINDOW_WIDTH))
    pygame.display.set_caption('Return from Death')
    clock = pygame.time.Clock()
    game_active = True

    #player
    player = pygame.sprite.GroupSingle()
    print(player)
    player.add(Player())
    state = "STOP"

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if game_active:
                if event.type == pygame.KEYDOWN:
                    #match case to check the pressed key
                    if event.key == pygame.K_w or pygame.K_UP:
                        state = "UP"  
                    if event.key == pygame.K_s or pygame.K_DOWN:
                        state = "DOWN"   
                    if event.key == pygame.K_d or pygame.K_RIGHT:
                        state = "RIGHT"  
                    if event.key == pygame.K_s or pygame.K_LEFT:
                        state = "LEFT"   
                    #match event.key:
                        #case pygame.K_w | pygame.K_UP:
                        #    keys.append("UP")
                        #case pygame.K_s | pygame.K_DOWN:
                        #   keys.append("DOWN")
                        # case pygame.K_d | pygame.K_RIGHT:
                        #     keys.append("RIGHT")
                        # case pygame.K_a | pygame.K_LEFT:
                        #     keys.append("LEFT")


        screen.fill(costants.BG_COLOR)
        player.draw(screen)
        player.update(state)

        pygame.display.update()
        clock.tick(60)   
main()