import pygame
import math

pygame.init()  # Initialize Pygame
# Create a window of 640x480 pixels
screen = pygame.display.set_mode((640, 480))
screen.fill((255, 255, 255))  # Fill the screen with white


# Draw the 3, 6, 9, and 12 o'clock marks on a clock face
pygame.draw.circle(screen, (128, 128, 128), (325, 230), 175)
pygame.draw.rect(screen, (0, 0, 0), (320, 60, 5, 8))
pygame.draw.rect(screen, (0, 0, 0), (320, 395, 5, 8))
pygame.draw.rect(screen, (0, 0, 0), (155, 230, 8, 5))
pygame.draw.rect(screen, (0, 0, 0), (490, 230, 8, 5))

pygame.draw.rect(screen, (0, 0, 0), (490, 230, 80, 50), 2)

# Make sure the window stays open until the user closes it
run_flag = True
while run_flag is True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_flag = False
    pygame.display.flip()  # Refresh the screen so drawing appears
