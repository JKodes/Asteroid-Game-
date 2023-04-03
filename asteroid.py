import pygame, sys, os


class Rocket(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load("Assets/station_rocket.png").convert_alpha()
        self.rect = self.image.get_rect(center = (WINDOW_WIDTH /2, WINDOW_HEIGHT /2))


pygame.init()

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 500
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Asteriod")

clock = pygame.time.Clock()

background = pygame.image.load("Assets/images/asteriod_galaxy.png").convert_alpha()  #this line needs to be fixed


rocket_group = pygame.sprite.Group()


rocket = Rocket(rocket_group)

run = True
while run: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    dt = clock.tick() / 1000

    rocket_group.draw(display_surface)

    pygame.display.update()