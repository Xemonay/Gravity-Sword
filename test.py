import os
from random import choice as ch
from icecream import ic
import pygame
import sys

pygame.init()
width, height = 1920, 1080
screen = pygame.display.set_mode((width, height))
FPS = 165
Clock = pygame.time.Clock()
go = True
all_sprites = pygame.sprite.Group()
surfaces = pygame.sprite.Group()




def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f'NO {fullname}')
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Player(pygame.sprite.Sprite):
    def __init__(self, group, width, height, surface):
        super().__init__(group)
        self.image = load_image('stand_pos_1.png')
        self.rect = self.image.get_rect()
        self.rect.center = (width // 2, height // 2)
        self.speed = 8
        self.last_key = 'right'
        self.slow_speed = 1
        self.jumping = 0
        self.image_cf = 0
        self.image_cs = 0
        self.image_cr = 0
        self.land = 0
        self.flipped = 0
        self.surface = surface

    def change_image_falling(self):
        match self.image_cf:
            case 0:
                self.image = load_image('fall_1.png')
                if self.flipped:
                    self.image = pygame.transform.flip(self.image, True, False)
            case 2:
                self.image = load_image('fall_2.png')
                if self.flipped:
                    self.image = pygame.transform.flip(self.image, True, False)
            case 6:
                self.image = load_image('fall_3.png')
                self.image_cf = -1
                if self.flipped:
                    self.image = pygame.transform.flip(self.image, True, False)
            case 10:
                self.image = load_image('stand_pos_1.png')
                self.image_cf = -1
                if self.flipped:
                    self.image = pygame.transform.flip(self.image, True, False)
        self.image_cf += 1

    def change_image_running(self):
        match self.image_cr:
            case 0:
                self.image = load_image('run_1.png')
                if self.flipped:
                    self.image = pygame.transform.flip(self.image, True, False)
            case 10:
                self.image = load_image('run_2.png')
                if self.flipped:
                    self.image = pygame.transform.flip(self.image, True, False)
            case 20:
                self.image = load_image('run_3.png')
                if self.flipped:
                    self.image = pygame.transform.flip(self.image, True, False)
            case 30:
                self.image = load_image('run_4.png')
                if self.flipped:
                    self.image = pygame.transform.flip(self.image, True, False)
            case 40:
                self.image = load_image('run_5.png')
                if self.flipped:
                    self.image = pygame.transform.flip(self.image, True, False)
            case 50:
                self.image = load_image('run_6.png')
                if self.flipped:
                    self.image = pygame.transform.flip(self.image, True, False)
            case 60:
                self.image = load_image('run_7.png')
                if self.flipped:
                    self.image = pygame.transform.flip(self.image, True, False)
            case 70:
                self.image = load_image('run_8.png')
                if self.flipped:
                    self.image = pygame.transform.flip(self.image, True, False)
            case 80:
                self.image = load_image('run_9.png')
                if self.flipped:
                    self.image = pygame.transform.flip(self.image, True, False)
            case 90:
                self.image = load_image('run_10.png')
                self.image_cr = -1
                if self.flipped:
                    self.image = pygame.transform.flip(self.image, True, False)

        self.image_cr += 1

    def change_image_standing(self):
        match self.image_cs:
            case 0:
                self.image = load_image('stand_pos_1.png')
                if self.flipped:
                    self.image = pygame.transform.flip(self.image, True, False)
            case 20:
                self.image = load_image('stand_pos_2.png')
                if self.flipped:
                    self.image = pygame.transform.flip(self.image, True, False)
            case 40:
                self.image = load_image('stand_pos_3.png')
                if self.flipped:
                    self.image = pygame.transform.flip(self.image, True, False)
            case 60:
                self.image = load_image('stand_pos_4.png')
                if self.flipped:
                    self.image = pygame.transform.flip(self.image, True, False)
            case 80:
                self.image = load_image('stand_pos_5.png')
                if self.flipped:
                    self.image = pygame.transform.flip(self.image, True, False)
            case 100:
                self.image = load_image('stand_pos_6.png')
                if self.flipped:
                    self.image = pygame.transform.flip(self.image, True, False)
            case 120:
                self.image = load_image('stand_pos_7.png')
                if self.flipped:
                    self.image = pygame.transform.flip(self.image, True, False)
            case 140:
                self.image = load_image('stand_pos_8.png')
                if self.flipped:
                    self.image = pygame.transform.flip(self.image, True, False)
            case 160:
                self.image = load_image('stand_pos_9.png')
                if self.flipped:
                    self.image = pygame.transform.flip(self.image, True, False)
            case 180:
                self.image = load_image('stand_pos_10.png')
                if self.flipped:
                    self.image = pygame.transform.flip(self.image, True, False)
            case 200:
                self.image = load_image('stand_pos_11.png')
                if self.flipped:
                    self.image = pygame.transform.flip(self.image, True, False)
                self.image_cs = -1
        self.image_cs += 1
        self.image_cr = 0

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
            current_speed = self.slow_speed
        else:
            current_speed = self.speed
        if keys[pygame.K_a]:  # LEFT
            self.image_cf = 0
            if self.last_key == 'right':
                self.flipped = 1
            self.last_key = 'left'
            if pygame.sprite.spritecollideany(self, self.surface) is not None:
                if pygame.sprite.spritecollideany(self, self.surface).name != 'WALL_LEFT':
                    self.rect.x -= current_speed
            else:
                self.rect.x -= current_speed
            self.image_cs = 0
            if self.land:
                self.change_image_running()
        if keys[pygame.K_d]:  # RIGHT
            self.image_cf = 0
            if self.last_key == 'left':
                self.flipped = 0
            self.last_key = 'right'
            if pygame.sprite.spritecollideany(self, self.surface) is not None:
                if pygame.sprite.spritecollideany(self, self.surface).name != 'WALL_RIGHT':
                    self.rect.x += current_speed
            else:
                self.rect.x += current_speed
            self.image_cs = 0
            if self.land:
                self.change_image_running()
        if keys[pygame.K_SPACE]:
            if self.jumping == 0 and pygame.sprite.spritecollideany(self, self.surface) is not None:
                if pygame.sprite.spritecollideany(self, self.surface).name == 'FLOOR':
                    self.land = 0
                    self.jumping = 300
            self.image_cs = 0
            self.image_cr = 0


class Floor(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color, name):
        super().__init__()
        self.name = name
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        pygame.draw.rect(self.image, color, (0, 0, width, height))
        self.rect = pygame.Rect(x, y, width, height)


floor1 = Floor(0, height - 20, 1920, 160, (125, 125, 125, 255), 'FLOOR')
wall_1 = Floor(0, 100, 20, height - 100, (125, 125, 125, 255), 'WALL_LEFT')
roof = Floor(0, 100, 1920, 20, (125, 125, 125, 255), 'ROOF')
wall_r = Floor(1900, 100, 20, 1080, (125, 125, 125, 255), 'WALL_RIGHT')
surfaces.add(floor1, wall_1, roof, wall_r)
player = Player(all_sprites, width, height, surfaces)
all_sprites.add(player)
all_sprites.add(floor1)
floor_surface = pygame.Surface((width, height), pygame.SRCALPHA)
gravity = 1
fall_speed = 0
gravity_interval = 5
frame_count = 0
while go:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            go = False
    if not any(pygame.key.get_pressed()) and player.land == 1:
        player.change_image_standing()
    if player.jumping > 0:
        player.rect = player.rect.move(0, -10)
        player.jumping -= 10
        fall_speed = 0
    elif not pygame.sprite.spritecollideany(player, surfaces):
        if frame_count % gravity_interval == 0:
            fall_speed += gravity
            player.change_image_falling()
        player.rect = player.rect.move(0, fall_speed)
    if pygame.sprite.spritecollideany(player, surfaces):
        if player.land == 0:
            player.image_cf = 10
            player.change_image_falling()
            player.land = 1
    all_sprites.update()
    screen.fill('WHITE')
    surfaces.draw(floor_surface)
    screen.blit(floor_surface, (0, 0))
    all_sprites.draw(screen)
    pygame.display.flip()
    Clock.tick(FPS)
    frame_count += 1
pygame.quit()
sys.exit()
