
from turtle import window_height, window_width
import pygame
import os


pygame.init()

window_width = 1200
window_height = 700
display_surface = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Asteriod")

default_black =(105, 105, 105)

fps = 60
clock = pygame.time.Clock()

vel = 5

rocket = pygame.image.load(os.path.join('Assets', 'station_rocket.png')).convert_alpha()
rocket_rect = rocket.get_rect()
rocket_rect.center = pygame.math.Vector2((window_width//2, window_height//2))
direction = pygame.math.Vector2(5, 0)

rocket_move =[pygame.image.load(os.path.join('Assets', 'moving_rocket.png'))]

game_background = pygame.transform.scale(pygame.image.load('Assets/asteroid_bg.jpg'), (window_width, window_height))



run = True 


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        direction.rotate_ip(-1)
    if keys[pygame.K_RIGHT]:
        direction.rotate_ip(1)
    if keys[pygame.K_UP]:
        rocket_rect.center += direction   
    if keys[pygame.K_DOWN]:
        rocket_rect.center -= direction

    angle = direction.angle_to((1, 0))
    rotated_car = pygame.transform.rotate(rocket, angle)
    display_surface.blit(rotated_car, rotated_car.get_rect(center = (round(rocket_rect.center), round(rocket_rect.center.y))))
    
    
    display_surface.fill((default_black))
    display_surface.blit(game_background, (0, 0))

    
    display_surface.blit(rocket, rocket_rect)
    



    pygame.display.update()
    clock.tick(fps)

pygame.quit()

