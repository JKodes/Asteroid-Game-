import pygame, sys, os
from utility import blit_rotate_center


class Rocket(pygame.sprite.Sprite):
    def __init__(self, max_vel, rotate_vel, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join('Assets/images', 'betterquality_05.png'))
        self.rect = self.image.get_rect(center = (WINDOW_WIDTH /2, WINDOW_HEIGHT /2))
        self.max_vel = max_vel      #line 8 - 13 new code dont know if it work
        self.vel = 0
        self.rotate_vel = rotate_vel
        self.angle = 0
        self.x, self.y = (200, 250)
        self.acceleration = 0.1

    def rotate(self, left=False, right=False):
        if left:
            self.angle += self.rotate_vel
        elif right:
            self.angle -= self.rotate_vel


    def move_forward(self):
        self.vel = min(self.vel + self.acceleration, self.max_vel)
        self.move()








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
bullet_group = pygame.sprite.Group()


rocket = Rocket(rocket_group, 4,4)  
bullet = Bullets((50,100),bullet_group)


run = True
while run: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    dt = clock.tick() / 1000

    display_surface.blit(background,(0,0))

    blit_rotate_center(display, self.image, (self.x, self.y), self.angle)


    keys = pygame.key.get_pressed()
    
    if [pygame.K_LEFT]:
        rocket.rotate(left=True)
    if [pygame.K_RIGHT]:
        rocket.rotate(right=True)

    rocket_group.draw(display_surface)
    bullet_group.draw(display_surface)

    pygame.display.update()