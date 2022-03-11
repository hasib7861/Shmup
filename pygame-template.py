# Pygame template - skeleton for a new pygame project
import pygame
import random

WIDTH = 360
HEIGHT = 480
FPS = 30

# Define colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 255, 0)
GREEN = (0, 0, 255)

# Initialize pygame and create window
pygame.init()  # Initializes pygame
pygame.mixer.init()  # Initializes the audio mixer
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Creates a window
pygame.display.set_caption("My Game")  # Sets the caption of the window
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
# Game loop
running = True
while running:
    # Keep loop running at the right speed
    # (It will make the program wait till it reaches 1/30 of a second)
    # (if the program takes longer than that then it will lag)
    clock.tick(FPS)

    # Process inputs (events)
    for event in pygame.event.get():
        # Check for closing the window
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()

    # Draw / render
    screen.fill(BLACK)
    all_sprites.draw()
    # *after* drawing everything, flip the display
    pygame.display.flip()