import pygame, sys, os, math
from utility import blit_rotate_center

class Rocket(pygame.sprite.Sprite):
    def __init__(self, max_vel, rotate_vel, groups):
        super().__init__(groups)
        pygame.image.get_extended()  # Disable cache for all images loaded afterwards
        self.image = pygame.image.load(os.path.join('Assets/images', 'betterquality_05.png'))
        self.rect = self.image.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
        self.max_vel = max_vel
        self.vel = 0
        self.rotate_vel = rotate_vel
        self.angle = 0
        self.x, self.y = (200, 250)
        self.acceleration = 0.1


        self.bullet_group = pygame.sprite.Group()

    

    def rotate(self, left=False, right=False):
        if left:
            self.angle += self.rotate_vel
        elif right:
            self.angle -= self.rotate_vel

    def move_forward(self):
        self.vel = min(self.vel + self.acceleration, self.max_vel)
        self.move()

    def move(self):
        radians = math.radians(self.angle)
        vertical_vel = math.cos(radians) * self.vel
        horizontal_vel = math.sin(radians) * self.vel

        self.y -= vertical_vel
        self.x -= horizontal_vel

    def reduce_speed(self):
        self.vel = max(self.vel - self.acceleration / 2, 0)
        self.move()


class Bullets(pygame.sprite.Sprite):
    def __init__(self, pos, direction, groups):
        super().__init__(groups)
        pygame.image.get_extended()  # Disable cache for all images loaded afterwards
        self.image = pygame.image.load(os.path.join('Assets/images', 'bullets_03.png'))


#initalize pygame
pygame.init()

#create pygame window 
WINDOW_WIDTH = 1300
WINDOW_HEIGHT = 800
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Asteriod")

clock = pygame.time.Clock()

#background display
background = pygame.image.load(os.path.join('Assets/images', 'bryan-goff-f7YQo-eYHdM-unsplash.jpg'))

rocket_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()

rocket = Rocket(2, 3, rocket_group)


#main game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    dt = clock.tick() / 1000

    display_surface.blit(background, (0, 0))

    blit_rotate_center(display_surface, rocket.image, (rocket.x, rocket.y), rocket.angle)

    keys = pygame.key.get_pressed()
    moved = False

    if keys[pygame.K_LEFT]:
        rocket.rotate(left=True)
    if keys[pygame.K_RIGHT]:
        rocket.rotate(right=True)
    if keys[pygame.K_UP]:
        moved = True
        rocket.move_forward()

    if not moved:
        rocket.reduce_speed()

    

    rocket_group.draw(display_surface)
    bullet_group.draw(display_surface)

    pygame.display.update()
