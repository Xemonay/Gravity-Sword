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
count = 0
start_time = pygame.time.get_ticks()
font = pygame.font.Font(None, 56)
loading_image = pygame.image.load('data//Xemonay.png')  # Replace 'loading_screen.png' with your PNG image file
loading_rect = loading_image.get_rect(center=(width // 2, height // 2))
screen.fill('black')
screen.blit(loading_image, loading_rect)
pygame.display.flip()
pygame.time.delay(2000)
loading_image = pygame.image.load('data//ChatGPT.png')  # Replace 'loading_screen.png' with your PNG image file
loading_rect = loading_image.get_rect(center=(width // 2, height // 2))
screen.fill('black')
screen.blit(loading_image, loading_rect)
pygame.display.flip()
pygame.time.delay(2000)

class Ball(pygame.sprite.Sprite):
    def __init__(self, initial_x, initial_y):
        super().__init__(all_sprites)
        self.image = pygame.image.load('data//ball2.png')
        self.rect = self.image.get_rect()
        self.rect.x = initial_x
        self.rect.y = initial_y
        self.rotate = False
        self.x = 1
        self.coo = 0

    def update(self):
        if frame_count % 6 == 0:
            if not self.rotate:
                self.rect = self.rect.move(-1, 1 * self.x)
                if self.coo == 10:
                    self.rotate = True
                    self.coo = -1
                if self.coo == 5:
                    self.x = -1
                self.coo += 1
            else:
                self.rect = self.rect.move(1, 1 * self.x)
                if self.coo == 5:
                    self.x = 1
                if self.coo == 10:
                    self.rotate = False
                    self.coo = -1
                    self.x = 1
                self.coo += 1


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


pygame.mouse.set_visible(False)


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
ball = pygame.sprite.Group()
ball1 = Ball(ch(range(100, 1775)), ch(range(100, 960)))
ball.add(ball1)
player = Player(all_sprites, width, height, floor, wall1, wall2, roof1)
floor.add(floor1)
wall1.add(wall_1)
wall2.add(wall_r)
roof1.add(roof)
all_sprites.add(floor1)
all_sprites.add(player)
floor_surface = pygame.Surface((width, height), pygame.SRCALPHA)
gravity = 1
fall_speed = 0
gravity_interval = 5
frame_count = 0
bhc = 0
while not player.standp:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            go = False
            break
    elapsed_time = pygame.time.get_ticks() - start_time
    stopwatch_text = font.render(
        f"{elapsed_time // 60000}:{elapsed_time // 1000}:{str(elapsed_time)[len(str(elapsed_time)) - 3:]}", True,
        (0, 0, 0))
    bhc_text = font.render(f"Score: {bhc}", True, (0, 0, 0))
    screen.fill('WHITE')
    surfaces.draw(floor_surface)
    screen.blit(floor_surface, (0, 0))
    bg1.update()
    player.change_image_standup()
    screen.blit(stopwatch_text, (width // 2 - 210, 25))
    screen.blit(bhc_text, (width // 2 - 60, 10))
    all_sprites.draw(screen)
    pygame.display.flip()
    Clock.tick(FPS)
    frame_count += 1
pygame.mixer.music.load('data//Bayonetta_Lets_Dance_Boys!.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)
sound = pygame.mixer.Sound('data//lost.wav')
sound1 = pygame.mixer.Sound('data//hit.wav')
sound.set_volume(0.1)
sound1.set_volume(0.45)
sound_is_playing = False
pygame.mixer.set_num_channels(3)
p_bhc = 0
while go:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            go = False
    elapsed_time = pygame.time.get_ticks() - start_time
    stopwatch_text = font.render(
        f"{elapsed_time // 60000}:{elapsed_time // 1000}:{str(elapsed_time)[len(str(elapsed_time)) - 3:]}", True,
        (0, 0, 0))
    if not player.attack:
        if not any(pygame.key.get_pressed()) and player.land == 1 and not player.dance:
            player.change_image_standing()
        if player.dance or ch(range(0, 1560)) == 1:
            player.image_cs = 0
            player.dance = True
            player.change_image_dance()
        sound_is_playing = False
    else:
        player.change_image_attack()
        if not sound_is_playing:
            sound.play()
            sound_is_playing = True
        if pygame.sprite.spritecollideany(player, ball):
            bhc += 1
            ball1.rect.x, ball1.rect.y = ch(range(100, 1775)), ch(range(100, 960))
    if player.jumping > 0:
        player.rect = player.rect.move(0, -10 if player.gravity == 1 else 10)
        player.jumping -= 10
        fall_speed = 0
    elif (not pygame.sprite.spritecollideany(player, floor) and player.gravity == 1) or (
            not pygame.sprite.spritecollideany(player, roof1) and player.gravity == 0):
        if frame_count % gravity_interval == 0:
            fall_speed += gravity
            if not player.attack:
                player.change_image_falling()
        player.rect = player.rect.move(0, fall_speed if player.gravity == 1 else -fall_speed)
    if pygame.sprite.spritecollideany(player, floor) or pygame.sprite.spritecollideany(player, roof1):
        if player.land == 0 and not player.attack:
            player.image_cf = 10
            player.change_image_falling()
            player.land = 1
    if p_bhc < bhc:
        sound1.play()
    bhc_text = font.render(f"Score: {bhc}", True, (0, 0, 0))
    screen.fill('WHITE')
    surfaces.draw(floor_surface)
    screen.blit(floor_surface, (0, 0))
    all_sprites.update()
    all_sprites.draw(screen)
    screen.blit(stopwatch_text, (width // 2 - 210, 25))
    screen.blit(bhc_text, (width - 891, 25))
    bg1.update()
    pygame.display.flip()
    Clock.tick(FPS)
    frame_count += 1
    p_bhc = bhc
pygame.quit()
sys.exit()
