import os
import sys
import pygame
from icecream import ic


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f'NO {fullname}')
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Player(pygame.sprite.Sprite):
    def __init__(self, group, width, height, floor, wall1, wall2, roof):
        super().__init__(group)
        self.image = load_image('stand_pos_1.png')
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = (width // 2 - 200, height - 161)
        self.speed = 8
        self.last_key = 'right'
        self.slow_speed = 4
        self.jumping = 0
        self.image_cf = 0
        self.image_cs = 0
        self.image_cr = 0
        self.image_cd = 0
        self.image_cg = 0
        self.land = 0
        self.flipped = 0
        self.floor = floor
        self.wall1 = wall1
        self.wall2 = wall2
        self.roof = roof
        self.dance = False
        self.standp = False

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

    def change_image_standup(self):
        match self.image_cg:
            case 0:
                self.image = load_image('stand_up_10.png')
            case 10:
                self.image = load_image('stand_up_20.png')
            case 20:
                self.image = load_image('stand_up_30.png')
            case 30:
                self.image = load_image('stand_up_40.png')
            case 40:
                self.image = load_image('stand_up_50.png')
            case 50:
                self.image = load_image('stand_up_60.png')
            case 60:
                self.image = load_image('stand_up_70.png')
            case 70:
                self.image = load_image('stand_up_80.png')
            case 80:
                self.image = load_image('stand_up_90.png')
        self.image_cg += 1
        if self.image_cg == 100:
            self.image = load_image('stand_pos_1.png')
            self.rect.x, self.rect.y = (1920 // 2 - 100, 1080 - 130)
            self.standp = True

    def change_image_dance(self):
        match self.image_cd:
            case 0:
                self.image = load_image('dance_1.png')
            case 10:
                self.image = load_image('dance_2.png')
            case 20:
                self.image = load_image('dance_3.png')
            case 30:
                self.image = load_image('dance_4.png')
            case 40:
                self.image = load_image('dance_5.png')
            case 50:
                self.image = load_image('dance_6.png')
            case 60:
                self.image = load_image('dance_7.png')
            case 70:
                self.image = load_image('dance_8.png')
            case 80:
                self.image = load_image('dance_9.png')
            case 90:
                self.image = load_image('dance_10.png')
            case 100:
                self.image = load_image('dance_11.png')
            case 110:
                self.image = load_image('dance_12.png')
                self.image_cd = -1
        self.image_cd += 1

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

    def change_image_attack(self):
        pass

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
            self.dance = False
            current_speed = self.slow_speed
        else:
            current_speed = self.speed
        if keys[pygame.K_a]:  # LEFT
            self.dance = False
            self.image_cf = 0
            if self.last_key == 'right':
                self.flipped = 1
            self.last_key = 'left'
            if not pygame.sprite.spritecollideany(self, self.wall1):
                self.rect.x -= current_speed
            self.image_cs = 0
            if self.land:
                self.change_image_running()
        if keys[pygame.K_d]:  # RIGHT
            self.image_cf = 0
            self.dance = False
            if self.last_key == 'left':
                self.flipped = 0
            self.last_key = 'right'
            if not pygame.sprite.spritecollideany(self, self.wall2):
                self.rect.x += current_speed
            self.image_cs = 0
            if self.land:
                self.change_image_running()
        if keys[pygame.K_SPACE]:
            self.dance = False
            if self.jumping == 0 and pygame.sprite.spritecollideany(self, self.floor):
                self.land = 0
                self.jumping = 300
            self.image_cs = 0
            self.image_cr = 0
