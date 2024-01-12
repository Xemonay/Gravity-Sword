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
player = Player(all_sprites, width, height)
while go:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            go = False
    all_sprites.update()
    screen.fill('WHITE')
    all_sprites.draw(screen)
    pygame.display.flip()
    Clock.tick(FPS)
pygame.quit()
sys.exit()