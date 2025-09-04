import pygame

pygame.init() # Initialize Pygame
screen = pygame.display.set_mode((640, 480)) # Create a window of 640x480 pixels
screen.fill((255, 255, 255)) # Fill the screen with white

pygame.draw.line(screen, (0, 0, 0), (100, 380), (540, 380)) # Draw a black line

# Draw the ground
pygame.draw.rect(screen, (0, 255, 0), (0, 380, 640, 100))
# Draw the bottom of the house
pygame.draw.rect(screen, (255, 0, 0), (200, 250, 240, 130))
# Draw two walls
pygame.draw.rect(screen, (255, 255, 0), (220, 280, 80, 100))
pygame.draw.rect(screen, (255, 255, 0), (340, 280
# Draw the roof
, 80, 100))
pygame.draw.polygon(screen, (0, 0, 255), [(190, 250), (320, 150), (450, 250)])
# Draw the sun
pygame.draw.circle(screen, (255, 255, 0), (500, 80), 40)

# draw a tree
pygame.draw.rect(screen, (139, 69, 19), (100, 300, 20, 80)) # Tree trunk


# Make sure the window stays open until the user closes it
run_flag = True
while run_flag is True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_flag = False
    pygame.display.flip() # Refresh the screen so drawing appears