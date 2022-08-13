from turtle import window_height, window_width
import pygame

pygame.init()

window_height = 800
window_width = 400
display_surface = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Asteriod")


run = True 


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run == False





pygame.quit()

