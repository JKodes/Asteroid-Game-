import pygame
from sys import exit 

pygame.init()

screen = pygame.display.set_mode((1270,800))
pygame.display.set_caption('Asteroids')
mainclock = pygame.time.Clock()

bg_image = pygame.image.load('images/asteriod_galaxy.png')

fix_bg_image = pygame.transform.scale(bg_image, (50,200))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    screen.blit(bg_image,(0,0))




    pygame.display.update()
    mainclock.tick(60)