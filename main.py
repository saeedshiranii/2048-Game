import pygame


# initialize pygame
pygame.init()

# Display
screen_width = 900
screen_height = 400
screen = pygame.display.set_mode(size=(screen_width, screen_height))

# Title and images
pygame.display.set_caption('2048 made by Saeed')
icon = pygame.image.load('number_blocks.png')
pygame.display.set_icon(icon)

# Game loop
run_game = True
while run_game:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run_game = False

    screen.fill((179, 255, 174))
    pygame.display.update()


