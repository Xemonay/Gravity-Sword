import pygame
import sys
from player import Player

pygame.init()
width, height = 1920, 1080
screen = pygame.display.set_mode((width, height))
FPS = 165
Clock = pygame.time.Clock()
go = True
all_sprites = pygame.sprite.Group()
floor = pygame.sprite.Group()


class Floor(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        super().__init__()
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        pygame.draw.rect(self.image, color, (0, 0, width, height))
        self.rect = self.image.get_rect(topleft=(x, y))


floor1 = Floor(0, height - 20, 1920, 10, (125, 125, 125, 255))
floor.add(floor1)
player = Player(all_sprites, width, height, floor)
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
    if not player.landing:
        if not any(pygame.key.get_pressed()):
            player.change_image_standing()
        if player.jumping > 0:
            player.rect = player.rect.move(0, -10)
            player.jumping -= 10
            fall_speed = 0
        elif not pygame.sprite.spritecollideany(player, floor):
            if frame_count % gravity_interval == 0:
                fall_speed += gravity
                player.change_image_falling()
            player.rect = player.rect.move(0, fall_speed)
        if pygame.sprite.spritecollideany(player, floor):
            if player.land == 0:
                player.image_cf = 3
                if player.fall_t >= 100000:
                    player.change_image_landing()
                    player.landing = True
                player.fall_t = 0
                player.change_image_falling()
    else:
        player.change_image_landing()
        if player.image_cl >= 21:
            player.image_cl = 0
            player.landing = False
    all_sprites.update()
    screen.fill('WHITE')
    screen.blit(floor_surface, (0, 0))
    all_sprites.draw(screen)
    pygame.display.flip()
    Clock.tick(FPS)
    frame_count += 1
pygame.quit()
sys.exit()
