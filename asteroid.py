import pygame

pygame.init()

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600

display_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Asteriod")

FPS = 60
clock = pygame.time.clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False





pygame.quit()