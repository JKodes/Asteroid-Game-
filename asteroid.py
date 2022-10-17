import pygame
import os

pygame.init()

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600


game_bg = pygame.image.load(os.path.join('Assets', 'asteroid_bg.jpg'))

display_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Asteriod")






FPS = 60
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display_window.fill((0,0,0))
    display_window.blit(game_bg,(0,0))
    pygame.display.update()
    clock.tick(FPS)


pygame.quit()