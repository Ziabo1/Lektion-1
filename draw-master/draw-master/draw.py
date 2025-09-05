import pygame

pygame.init() # Initialize Pygame
screen = pygame.display.set_mode((640, 480)) # Create a window of 640x480 pixels
screen.fill((255, 255, 255)) # Fill the screen with white

pygame.draw.line(screen, (0, 0, 0), (100, 380), (540, 380)) # Draw a black line


# Draw the ground
pygame.draw.rect(screen, (0, 255, 0), (0, 380, 640, 100))
# draw dirt
pygame.draw.rect(screen, (139, 69, 19), (0, 420, 640, 90))

# Draw the bottom of the house
pygame.draw.rect(screen, (255, 0, 0), (200, 250, 240, 130))
# Draw two walls
pygame.draw.rect(screen, (255, 255, 0), (220, 280, 80, 100))   
pygame.draw.rect(screen, (255, 255, 0), (340, 280, 80, 100))
# draw door knob
pygame.draw.circle(screen, (0, 0, 0), (290, 330), 5)    

# Draw the windows
pygame.draw.rect(screen, (0, 0, 255), (350, 290, 60, 60))



pygame.draw.polygon(screen, (0, 0, 255), [(190, 250), (320, 150), (450, 250)])
# Draw the sun
pygame.draw.circle(screen, (255, 255, 0), (500, 80), 40)
pygame.draw. line(screen, (255, 255, 0), (500, 10), (500, 50), 5) # Sun ray
pygame.draw. line(screen, (255, 255, 0), (500,      150), (500, 110), 5) # Sun ray
pygame.draw. line(screen, (255, 255, 0), (430, 80), (470, 80), 5) # Sun ray
pygame.draw. line(screen, (255, 255, 0), (570, 80), (530, 80), 5) # Sun ray
pygame.draw. line(screen, (255, 255, 0), (450, 30), (480, 60), 5) # Sun ray
pygame.draw. line(screen, (255, 255, 0), (550, 130), (520, 100), 5) # Sun ray
pygame.draw. line(screen, (255, 255, 0), (450,  130), (480, 100), 5) # Sun ray
pygame.draw. line(screen, (255, 255, 0), (550, 30), (520, 60), 5) # Sun ray

# draw cloud 
pygame.draw.circle(screen, (200, 200, 200), (150, 80), 30)
pygame.draw.circle(screen, (200, 200, 200), (180, 80), 30)
pygame.draw.circle(screen, (200, 200, 200), (210, 80), 30)
pygame.draw.circle(screen, (200, 200, 200), (165, 60), 30)
pygame.draw.circle(screen, (200, 200, 200), (195, 60), 30)

# draw a tree
pygame.draw.rect(screen, (139, 69, 19), (100, 300, 20, 80)) # Tree trunk
pygame.draw.polygon(screen, (0, 100, 0), [(90, 300), (110, 220), (130, 300)]) # Tree leaves 
pygame.draw.polygon(screen, (0, 100, 0), [(80, 250), (110, 180), (140, 250)]) # More leaves
pygame.draw.polygon(screen, (0, 100, 0), [(90, 300), (110, 220), (130, 300)]) # Even more leaves    
pygame.draw.polygon(screen, (0, 100, 0), [(70, 200), (110, 140), (150, 200)]) # Even more leaves    

# Make sure the window stays open until the user closes it
run_flag = True
while run_flag is True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_flag = False
    pygame.display.flip() # Refresh the screen so drawing appears