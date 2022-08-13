from turtle import window_height, window_width
import pygame
import os

pygame.init()

window_width = 1000
window_height = 700
display_surface = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Asteriod")


default_black  = (105, 105, 105)

fps = 60
clock = pygame.time.Clock()



rocket= pygame.image.load(os.path.join('Assets', 'station_rocket.png'))

run = True 


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    display_surface.fill(default_black)


    display_surface.blit(rocket, (200, 100))



    pygame.display.update()
    clock.tick(fps)

pygame.quit()

