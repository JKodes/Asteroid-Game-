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

vel = 5

rocket= pygame.image.load(os.path.join('Assets', 'station_rocket.png')).convert_alpha()
rocket_rect = rocket.get_rect()
rocket_rect.centerx = window_width// 2
rocket_rect.bottom = window_height//2


game_background = pygame.image.load(os.path.join('Assets', 'asteroid_bg.jpg'))



run = True 


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                rocket_rect.x -= vel
            if event.key == pygame.K_RIGHT:
                rocket_rect.x += vel
            if event.key == pygame.K_UP:
                rocket_rect.y -= vel
            if event.key == pygame.K_DOWN:
                rocket_rect.y += vel

    
    
    display_surface.fill(default_black)
    display_surface.blit(game_background, (0, 0))

    
    display_surface.blit(rocket, rocket_rect)
    



    pygame.display.update()
    clock.tick(fps)

pygame.quit()

