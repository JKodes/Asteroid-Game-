import pygame, sys


class RocketShip(pygame.sprite.Sprite):
    def __init__(self, groups):
        super.__init__(groups)

        self.image = pygame.image.load("/Assets/station_rocket.png").convert.alpha()
        self.rect = self.image.get_rect(center = (WINDOW_WIDTH /2, WINDOW_HEIGHT /2))


pygame.init()

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 500

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Asteriod")

clock = pygame.time.Clock()


rocket_group =pygame.sprite.Group()


space_craft = RocketShip(rocket_group)

run = True
while run: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    dt = clock.tick() / 1000

    pygame.display.update()