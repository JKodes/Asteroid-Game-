import pygame, sys, os, math
from utility import blit_rotate_center
from random import randint, uniform 

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
        
        self.mask = pygame.mask.from_surface(self.image)

        self.can_shoot = True
        self.shoot_time = None


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

        self.rect.center = (self.x, self.y)

    def reduce_speed(self):
        self.vel = max(self.vel - self.acceleration / 2, 0)
        self.move()

    def bullet_time(self):
        if not self.can_shoot:
            current_time = pygame.time.get_ticks()
            if current_time - self.shoot_time > 500:
                self.can_shoot = True

    def bullet_launch(self):
        if pygame.key.get_pressed()[pygame.K_SPACE] and self.can_shoot:
            self.can_shoot = False 
            self.shoot_time = pygame.time.get_ticks()

            Bullets(self.rect.center, self.angle, bullet_group)
            
    def collision(self):
        if pygame.sprite.spritecollide(self, asteroid_group,False,pygame.sprite.collide_mask):
            pygame.quit()
            sys.exit()

    def update(self):
        self.bullet_time()
        self.bullet_launch()
        
        self.collision()
        


class Bullets(pygame.sprite.Sprite):
    def __init__(self, pos, angle, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join('Assets/images', 'bullets_03.png'))
        self.rect = self.image.get_rect(center = pos)
        self.mask = pygame.mask.from_surface(self.image)
        
        self.direction = pygame.math.Vector2(0, -1).rotate(-angle)
        
        offset = pygame.math.Vector2(0, -self.rect.width / 2).rotate(-angle)
        self.pos = pygame.math.Vector2(pos) + offset
        self.speed = 140
        
    def collision(self):
        if pygame.sprite.spritecollide(self,asteroid_group, True, pygame.sprite.collide_mask):
            self.kill()

    
    def update(self):
        self.pos += self.direction * self.speed * dt
        self.rect.center  = ( round(self.pos.x), round(self.pos.y))
        
        self.collision()

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join('Assets/images', 'smallasteriod2x_03.png'))
        self.rect = self.image.get_rect(center = pos)
        self.mask = pygame.mask.from_surface(self.image)

        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.direction = pygame.math.Vector2(uniform(-0.5, 0.5), 1)
        self.speed = randint(300, 400)
        
    def update(self):
        self.pos += self.direction * self.speed * dt
        self.rect.center  = ( round(self.pos.x), round(self.pos.y))
        
        if self.rect.top > WINDOW_HEIGHT:
            self.kill()

class Score:
    def __init__(self):
        font_file = 'Snubfighter.ttf'
        font_path = os.path.join(font_file)
        self.font = pygame.font.Font(font_path, 25)
        
        
    def display(self):
        score_text = f'SCORE: {pygame.time.get_ticks() // 1000}'
        text_surface = self.font.render(score_text,True, (253,216,53))
        text_rect = text_surface.get_rect(topright=(WINDOW_WIDTH - 20, 20))
        display_surface.blit(text_surface,text_rect)
        pygame.draw.rect(display_surface, (253,216,53),text_rect.inflate(30,30), width= 8, border_radius = 5)
        
        

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
asteroid_group = pygame.sprite.Group()

rocket = Rocket(2, 3, rocket_group)


asteroid_timer = pygame.event.custom_type()
pygame.time.set_timer(asteroid_timer, 300)

score = Score()

#main game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == asteroid_timer:
            asteroid_y_pos = randint(-120, -10)
            asteroid_x_pos = randint(-100, WINDOW_WIDTH + 100)
            Asteroid((asteroid_x_pos, asteroid_y_pos), groups = asteroid_group)

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

    rocket_group.update()
    bullet_group.update()
    asteroid_group.update()
    
    score.display()
    
    bullet_group.draw(display_surface)
    asteroid_group.draw(display_surface)


    pygame.display.update()
