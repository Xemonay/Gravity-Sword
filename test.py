import pygame
import sys

pygame.init()

width, height = 1920, 1080
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
color1 = 'orange'

# Font settings
font = pygame.font.Font(None, 36)

# Menu options
menu_options = ["Start Game", "Options", "Quit"]
selected_option = 0

# Options menu variables
volume = 50  # Initial volume (percentage)
changing_volume = False  # Flag to indicate if the volume is being changed

# Options screen variables
options_screen_open = False

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                selected_option = (selected_option - 1) % len(menu_options)
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                selected_option = (selected_option + 1) % len(menu_options)
            elif event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                if selected_option == 0:  # Start Game
                    print("Starting Game!")
                    # Add your game start logic here
                elif selected_option == 1:  # Options
                    options_screen_open = True
                elif selected_option == 2:  # Quit
                    running = False
            elif event.key == pygame.K_LEFT:
                if changing_volume:
                    volume = max(0, volume - 10)
            elif event.key == pygame.K_RIGHT:
                if changing_volume:
                    volume = min(100, volume + 10)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                x, y = event.pos
                if 800 < x < 1120 and 450 < y < 490:  # Volume slider region
                    changing_volume = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Left mouse button
                changing_volume = False

    # Clear the screen
    screen.fill(black)

    # Display menu options
    for i, option in enumerate(menu_options):
        color = color1 if i == selected_option else white
        text = font.render(option, True, color)
        text_rect = text.get_rect(center=(width // 2, height // 2 + i * 50))
        screen.blit(text, text_rect)

    if options_screen_open:
        # Display options screen
        pygame.draw.rect(screen, white, (800, 450, 320, 40))  # Volume slider background
        pygame.draw.rect(screen, color1, (800, 450, volume * 3.2, 40))  # Volume slider fill
        # Additional options screen elements can be added here

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
