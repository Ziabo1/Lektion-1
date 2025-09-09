import pygame
import math

pygame.init()  # Initialize Pygame
# Create a window of 640x480 pixels
screen = pygame.display.set_mode((640, 480))
screen.fill((255, 255, 255))  # Fill the screen with white


# Draw the clock face
pygame.draw.circle(screen, (128, 128, 128), (325, 230), 175)
center_x, center_y = 325, 230
radius = 175

# Draw 60 marks (minute and hour marks)
for i in range(60):
    angle_deg = i * 6  # 360/60 = 6 degrees per minute
    angle_rad = math.radians(angle_deg)
    # For hour marks (every 5th mark)
    if i % 5 == 0:
        mark_length = 20
        mark_width = 8
        color = (0, 0, 0)
    else:
        mark_length = 10
        mark_width = 3
        color = (80, 80, 80)
    # Calculate start and end points
    x_start = int(center_x + (radius - mark_length) * math.sin(angle_rad))
    y_start = int(center_y - (radius - mark_length) * math.cos(angle_rad))
    x_end = int(center_x + radius * math.sin(angle_rad))
    y_end = int(center_y - radius * math.cos(angle_rad))
    pygame.draw.line(screen, color, (x_start, y_start),
                     (x_end, y_end), mark_width)


x_start = int(center_x + (radius - mark_length) * math.sin(angle_rad))
y_start = int(center_y - (radius - mark_length) * math.cos(angle_rad))
x_end = int(center_x + radius * math.sin(angle_rad))
y_end = int(center_y - radius * math.cos(angle_rad))
pygame.draw.line(screen, color, (x_start, y_start), (x_end, y_end), mark_width)

# Make sure the window stays open until the user closes it
run_flag = True
while run_flag is True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_flag = False
    pygame.display.flip()  # Refresh the screen so drawing appears
