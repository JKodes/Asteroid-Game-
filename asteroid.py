import pygame, sys, os


class Rocket(pygame.sprite.Sprite):
    def __init__(self,groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join('Assets/images', 'betterquality_05.png'))
        self.rect = self.image.get_rect(center = (WINDOW_WIDTH /2, WINDOW_HEIGHT /2))





class Bullets(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join('Assets/images', 'bullets_03.png'))
        self.rect = self.image.get_rect(midbottom = pos)



pygame.init()

WINDOW_WIDTH = 1800
WINDOW_HEIGHT = 900
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Asteriod")

clock = pygame.time.Clock()

#background = pygame.image.load("Assets/images/asteriod_galaxy.png").convert_alpha()  #this line needs to be fixed
background = pygame.image.load(os.path.join('Assets/images', 'bryan-goff-f7YQo-eYHdM-unsplash.jpg'))


rocket_group = pygame.sprite.Group()
bullet_groups = pygame.sprite.Group()


rocket = Rocket(rocket_group) # class being called  



run = True
while run: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    dt = clock.tick() / 1000

    display_surface.blit(background,(0,0))

    rocket_group.draw(display_surface)

    pygame.display.update()