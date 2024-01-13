import pygame
import sys
from player import Player
from random import choice as ch

pygame.init()
width, height = 1920, 1080
screen = pygame.display.set_mode((width, height))
FPS = 165
Clock = pygame.time.Clock()
go = True
all_sprites = pygame.sprite.Group()
surfaces = pygame.sprite.Group()

start_time = pygame.time.get_ticks()
font = pygame.font.Font(None, 56)


class Background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(surfaces)
        self.image = pygame.image.load('data//bg_1.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.x = 1
        self.y = 10

    def update(self):
        if frame_count % self.y == 0:
            self.image = pygame.image.load(f'data//bg_{self.x}.png')
            self.x += 1
            if self.x == 55:
                self.x = 1


class Floor(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color, name):
        super().__init__(surfaces)
        self.name = name
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        pygame.draw.rect(self.image, color, (0, 0, width, height))
        self.rect = pygame.Rect(x, y, width, height)


bg1 = Background()
floor1 = Floor(0, height - 20, 1920, 160, (255, 255, 255, 255), 'FLOOR')
wall_1 = Floor(0, 90, 20, height - 90, (255, 255, 255, 255), 'WALL_LEFT')
roof = Floor(0, 80, 1920, 18, (255, 255, 255, 255), 'ROOF')
wall_r = Floor(1900, 90, 20, 1080, (255, 255, 255, 255), 'WALL_RIGHT')
surfaces.add(floor1, wall_1, roof, wall_r)
wall1 = pygame.sprite.Group()
wall2 = pygame.sprite.Group()
roof1 = pygame.sprite.Group()
floor = pygame.sprite.Group()
floor.add(floor1)
wall1.add(wall_1)
wall2.add(wall_r)
roof1.add(roof)
player = Player(all_sprites, width, height, floor, wall1, wall2, roof1)
all_sprites.add(floor1)
all_sprites.add(player)
floor_surface = pygame.Surface((width, height), pygame.SRCALPHA)
gravity = 1
fall_speed = 0
gravity_interval = 5
frame_count = 0
x = 0
while not player.standp:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            go = False
            break
    elapsed_time = pygame.time.get_ticks() - start_time
    stopwatch_text = font.render(
        f"{elapsed_time // 60000}:{elapsed_time // 1000}:{str(elapsed_time)[len(str(elapsed_time)) - 3:]}", True,
        (0, 0, 0))
    screen.fill('WHITE')
    surfaces.draw(floor_surface)
    screen.blit(floor_surface, (0, 0))
    bg1.update()
    player.change_image_standup()
    screen.blit(stopwatch_text, (width // 2 - 210, 25))
    all_sprites.draw(screen)
    pygame.display.flip()
    Clock.tick(FPS)
    frame_count += 1
while go:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            go = False
    elapsed_time = pygame.time.get_ticks() - start_time
    stopwatch_text = font.render(
        f"{elapsed_time // 60000}:{elapsed_time // 1000}:{str(elapsed_time)[len(str(elapsed_time)) - 3:]}", True,
        (0, 0, 0))
    if not any(pygame.key.get_pressed()) and player.land == 1 and not player.dance:
        player.change_image_standing()
    if player.dance or ch(range(0, 1560)) == 1:
        player.image_cs = 0
        player.dance = True
        player.change_image_dance()
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
            player.image_cf = 10
            player.change_image_falling()
            player.land = 1

    screen.fill('WHITE')
    surfaces.draw(floor_surface)
    screen.blit(floor_surface, (0, 0))
    all_sprites.update()
    all_sprites.draw(screen)
    screen.blit(stopwatch_text, (width // 2 - 210, 25))
    bg1.update()
    pygame.display.flip()
    Clock.tick(FPS)
    frame_count += 1
pygame.quit()
sys.exit()
