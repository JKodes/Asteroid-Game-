import pygame
import os


#Initialize Pygame
pygame.init()


#Set display window and Caption
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
display_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Asteriod")

#background for the game
game_bg = pygame.image.load(os.path.join('Assets', 'asteroid_bg.jpg'))

#Set FPS and Clock
FPS = 60
clock = pygame.time.Clock()


#main game loop
running = True
while running:
    #Check to see if user wants to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Fill in the game an add background
    display_window.fill((0,0,0))
    display_window.blit(game_bg,(0,0))


    #Update display and tick clock
    pygame.display.update()
    clock.tick(FPS)



#End game 
pygame.quit()