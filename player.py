import os
import sys
import pygame
from random import choice as ch
from icecream import ic


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f'NO {fullname}')
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Player(pygame.sprite.Sprite):
    def __init__(self, group, width, height, floor):
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
        self.floor = floor

    def change_image_falling(self):
        match self.image_cf:
            case 0:
                self.image = load_image('fall_1.png')
            case 1:
                self.image = load_image('fall_2.png')
            case 2:
                self.image = load_image('fall_3.png')
                self.image_cf = -1
            case 3:
                self.image = load_image('stand_pos_1.png')
                self.image_cf = -1
                self.land = 1
        self.image_cf += 1
        if self.flipped:
            self.image = pygame.transform.flip(self.image, True, False)

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
            self.rect.x -= current_speed
            self.image_cs = 0
            if self.land:
                self.change_image_running()
        if keys[pygame.K_d]:  # RIGHT
            self.image_cf = 0
            if self.last_key == 'left':
                self.flipped = 0
            self.last_key = 'right'
            self.rect.x += current_speed
            self.image_cs = 0
            if self.land:
                self.change_image_running()
        if keys[pygame.K_SPACE]:
            if self.jumping == 0 and pygame.sprite.spritecollideany(self, self.floor):
                self.land = 0
                self.jumping = 300
            self.image_cs = 0
            self.image_cr = 0
