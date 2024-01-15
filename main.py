import sys
from random import choice as ch

import pygame

from player import Player

pygame.init()
width, height = 1920, 1080
screen = pygame.display.set_mode((width, height))
FPS = 165
Clock = pygame.time.Clock()
go = True
all_sprites = pygame.sprite.Group()
surfaces = pygame.sprite.Group()
count = 0
font = pygame.font.Font(None, 56)
loading_image = pygame.image.load('data//Xemonay.png')
loading_rect = loading_image.get_rect(center=(width // 2, height // 2))
screen.fill('black')
screen.blit(loading_image, loading_rect)
pygame.display.flip()
pygame.time.delay(2000)
loading_image = pygame.image.load('data//ChatGPT.png')
loading_rect = loading_image.get_rect(center=(width // 2, height // 2))
screen.fill('black')
screen.blit(loading_image, loading_rect)
pause_font = pygame.font.Font(None, 120)
pause_text = pause_font.render("Pause", True, (255, 255, 255))
end_text = pause_font.render("End", True, (255, 255, 255))
end_text_rect = end_text.get_rect(center=(width // 2, height // 2 - 200))
pause_text_rect = pause_text.get_rect(center=(width // 2, height // 2 - 200))
s_text = pygame.font.Font(None, 120)
s_text = pause_font.render("Gravity Sword", True, 'pink')
s_text_rect = pause_text.get_rect(center=(width // 2 - 160, height // 2 - 200))
pygame.display.flip()
pygame.time.delay(2000)
clock = pygame.time.Clock()
black = (0, 0, 0)
white = (255, 255, 255)
color1 = 'orange'
font = pygame.font.Font(None, 36)
menu_options = ["Start Game", "Options", "Quit"]
selected_option = 0
volume = 1


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


class Floor(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color, name):
        super().__init__(surfaces)
        self.name = name
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        pygame.draw.rect(self.image, color, (0, 0, width, height))
        self.rect = pygame.Rect(x, y, width, height)


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


changing_volume = False
options_screen_open = False
bg2 = pygame.sprite.Sprite()
bg2.image = pygame.image.load('data//bg1.png').convert_alpha()
bg2.rect = bg2.image.get_rect()
bg_end = pygame.sprite.Sprite()
bg_end.image = pygame.image.load('data//end.png')
bg_end.rect = bg_end.image.get_rect()
bg0 = pygame.sprite.Group()
bg0.add(bg2)
running = True
start = False
pygame.mouse.set_visible(False)
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
floor.add(floor1)
wall1.add(wall_1)
wall2.add(wall_r)
roof1.add(roof)
all_sprites.add(floor1)
floor_surface = pygame.Surface((width, height), pygame.SRCALPHA)
pygame.mixer.music.load('data//Bayonetta_Lets_Dance_Boys!.mp3')
sound = pygame.mixer.Sound('data//lost.wav')
sound1 = pygame.mixer.Sound('data//hit.wav')
end = False
pygame.mixer.music.set_volume(volume)
pygame.mixer.music.load('data//banana.mp3')
player = Player(all_sprites, width, height, floor, wall1, wall2, roof1)
all_sprites.add(player)
pygame.mixer.music.play(-1)
while running:
    if not start:
        menu_options = ["Start Game", "Options", "Quit"]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                go = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    selected_option = (selected_option - 1) % len(menu_options)
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    selected_option = (selected_option + 1) % len(menu_options)
                elif event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    if selected_option == 0:
                        print("Starting Game!")
                        start = True
                        go = True
                        pygame.mixer.music.unload()
                    elif selected_option == 1:
                        options_screen_open = True if options_screen_open is False else False
                        changing_volume = True
                    elif selected_option == 2:
                        running = False
                        go = False
                elif event.key == pygame.K_LEFT:
                    if changing_volume:
                        volume = max(0, volume - 0.1)
                elif event.key == pygame.K_RIGHT:
                    if changing_volume:
                        volume = min(1, volume + 0.1)
        pygame.mixer.music.set_volume(volume)
        screen.fill(black)
        screen.blit(bg2.image, bg2.rect)
        for i, option in enumerate(menu_options):
            color = color1 if i == selected_option else white
            text = font.render(option, True, color)
            text_rect = text.get_rect(center=(width // 2, height // 2 + i * 50))
            screen.blit(text, text_rect)
        if options_screen_open:
            pygame.draw.rect(screen, white, (800, 450, 320, 40))
            pygame.draw.rect(screen, color1, (800, 450, volume * 100 * 3.2, 40))
        screen.blit(s_text, s_text_rect)
        pygame.display.flip()
        clock.tick(165)
    else:
        start_time = pygame.time.get_ticks()
        gravity = 1
        fall_speed = 0
        gravity_interval = 5
        frame_count = 0
        diifer = 0
        bhc = 0
        p_bhc = 0
        if go:
            player.rect.x, player.rect.y = (width // 2 - 200, height - 161)
            pygame.mixer.music.set_volume(0.4 * volume)
            sound.set_volume(volume * 0.6)
            sound1.set_volume(volume)
            pygame.mixer.music.load('data//Bayonetta_Lets_Dance_Boys!.mp3')
            pygame.mixer.music.play(-1)
            player.image_cg = 0
            while not player.standp:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        go = False
                        running = False
                        end = False
                        break
                elapsed_time = pygame.time.get_ticks() - start_time
                stopwatch_text = font.render(
                    f"{elapsed_time // 60000}:{elapsed_time // 1000}:{str(elapsed_time)[len(str(elapsed_time)) - 3:]}",
                    True,
                    (0, 0, 0))
                bhc_text = font.render(f"Score: {bhc}", True, (0, 0, 0))
                screen.fill('WHITE')
                surfaces.draw(floor_surface)
                screen.blit(floor_surface, (0, 0))
                bg1.update()
                player.change_image_standup()
                screen.blit(stopwatch_text, (width // 2 - 210, 25))
                screen.blit(bhc_text, (width - 891, 25))
                all_sprites.draw(screen)
                pygame.display.flip()
                Clock.tick(FPS)
                frame_count += 1
        sound_is_playing = False
        pygame.mixer.set_num_channels(3)
        p_bhc = 0
        esc = False
        end = False
        while go:
            if esc:
                menu_options = ["Continue", "Options", 'End Game', "Main Menu"]
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        go = False
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP or event.key == pygame.K_w:
                            selected_option = (selected_option - 1) % len(menu_options)
                        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                            selected_option = (selected_option + 1) % len(menu_options)
                        elif event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                            if selected_option == 0:
                                esc = False
                                diifer += pygame.time.get_ticks() - start_time - was_to
                                pygame.mixer.music.unpause()
                            elif selected_option == 1:
                                options_screen_open = True if options_screen_open is False else False
                                changing_volume = True
                            elif selected_option == 2:
                                end = True
                                go = False
                                pygame.mixer.music.unload()
                                pygame.mixer.music.set_volume(volume)
                                pygame.mixer.music.load('data//banana.mp3')
                                pygame.mixer.music.play(-1)
                            elif selected_option == 3:
                                start = False
                                go = False
                                pygame.mixer.music.unload()
                                pygame.mixer.music.set_volume(volume)
                                pygame.mixer.music.load('data//banana.mp3')
                                pygame.mixer.music.play(-1)
                        elif event.key == pygame.K_LEFT:
                            if changing_volume:
                                volume = max(0, volume - 0.1)
                        elif event.key == pygame.K_RIGHT:
                            if changing_volume:
                                volume = min(1, volume + 0.1)
                for i, option in enumerate(menu_options):
                    color = color1 if i == selected_option else white
                    text = font.render(option, True, color)
                    text_rect = text.get_rect(center=(width // 2, height // 2 + i * 50))
                    screen.blit(text, text_rect)
                screen.blit(pause_text, pause_text_rect)
                if options_screen_open:
                    pygame.draw.rect(screen, white, (800, 450, 320, 40))
                    pygame.draw.rect(screen, color1, (800, 450, volume * 100 * 3.2, 40))
                pygame.display.flip()
                sound.set_volume(volume * 0.6)
                sound1.set_volume(volume)
                clock.tick(165)
                continue
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    go = False
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        was_to = pygame.time.get_ticks() - start_time
                        esc = True
                        pygame.mixer.music.pause()

            elapsed_time = pygame.time.get_ticks() - start_time - diifer
            stopwatch_text = font.render(
                f"{elapsed_time // 60000}:{elapsed_time // 1000}:{str(elapsed_time)[len(str(elapsed_time)) - 3:]}",
                True,
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
    while end:
        menu_options = ['Try again', 'Main Menu']
        balls_count_text = pygame.font.Font(None, 36).render(f"Balls: {bhc}", True, white)
        time_text = pygame.font.Font(None, 36).render(f"Time: {elapsed_time / 1000} s", True, white)
        avg_time_text = pygame.font.Font(None, 36).render(
            f"Avg Time/Ball: {round(elapsed_time / 1000 / (bhc + 1 if bhc == 0 else bhc), 6)} s", True, white)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                go = False
                end = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    selected_option = (selected_option - 1) % len(menu_options)
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    selected_option = (selected_option + 1) % len(menu_options)
                elif event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    if selected_option == 0:
                        start = True
                        end = False
                        go = True
                    elif selected_option == 1:
                        end = False
                        start = False
                elif event.key == pygame.K_LEFT:
                    if changing_volume:
                        volume = max(0, volume - 0.1)
                elif event.key == pygame.K_RIGHT:
                    if changing_volume:
                        volume = min(1, volume + 0.1)

        # Display elements
        screen.blit(bg_end.image, bg_end.rect)
        for i, option in enumerate(menu_options):
            color = color1 if i == selected_option else 'white'
            text = font.render(option, True, color)
            text_rect = text.get_rect(center=(width // 2, height // 2 + i * 50))
            screen.blit(text, text_rect)

        screen.blit(end_text, end_text_rect)
        screen.blit(balls_count_text, (width // 2 - 80, height // 2 + 150))
        screen.blit(time_text, (width // 2 - 80, height // 2 + 200))
        screen.blit(avg_time_text, (width // 2 - 120, height // 2 + 250))

        if options_screen_open:
            pygame.draw.rect(screen, white, (800, 450, 320, 40))
            pygame.draw.rect(screen, color1, (800, 450, volume * 100 * 3.2, 40))

        pygame.display.flip()
        pygame.mixer.music.set_volume(volume)
        clock.tick(165)
pygame.quit()
sys.exit()
