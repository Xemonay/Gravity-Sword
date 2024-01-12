import os
import sys
import pygame


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f'NO {fullname}')
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Player(pygame.sprite.Sprite):
    def __init__(self, group, width, height):
        super().__init__(group)
        self.image = load_image('player1.png')
        self.rect = self.image.get_rect()
        self.rect.center = (width // 2, height // 2)
        self.speed = 7
        self.last_key = 'right'
        self.slow_speed = 1

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
            current_speed = self.slow_speed
        else:
            current_speed = self.speed

        if keys[pygame.K_a]:
            if self.last_key == 'right':
                self.image = pygame.transform.flip(
                    self.image, True, False)
            self.last_key = 'left'
            self.rect.x -= current_speed
        if keys[pygame.K_d]:
            if self.last_key == 'left':
                self.image = pygame.transform.flip(
                    self.image, True, False)
            self.last_key = 'right'
            self.rect.x += current_speed
        if keys[pygame.K_w]:
            self.rect.y -= current_speed
        if keys[pygame.K_s]:
            self.rect.y += current_speed
