import pygame
import costants
from sys import exit
import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((costants.WINDOW_HEIGHT, costants.WINDOW_WIDTH))
    pygame.display.set_caption('Return from Death')
    clock = pygame.time.Clock()
    game_active = True
    keys = []

    #player
    player = pygame.sprite.GroupSingle()
    player.add(Player(300))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if game_active:
                if event.type == pygame.KEYDOWN:
                    #match case to check the pressed key
                    match event.key:
                        case pygame.K_w | pygame.K_UP:
                            keys.append("UP")
                        case pygame.K_s | pygame.K_DOWN:
                            keys.append("DOWN")
                        case pygame.K_d | pygame.K_RIGHT:
                            keys.append("RIGHT")
                        case pygame.K_a | pygame.K_LEFT:
                            keys.append("LEFT")


        screen.fill(costants.BG_COLOR)
        player.draw(screen)
        player.update(keys)

        pygame.display.update()
        clock.tick(60)   
main()