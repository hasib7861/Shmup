# Pygame template - skeleton for a new pygame project
import pygame
import random
import os

WIDTH = 800
HEIGHT = 600
FPS = 30

# Define colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# set up assets folder
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "Platformer Art Complete Pack")


class Player(pygame.sprite.Sprite):
    # Sprite for the player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, "Base pack\Player\p1_jump.png")).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.y_speed = 5

    def update(self):
        self.rect.x += 5
        self.rect.y += self.y_speed
        if self.rect.bottom > HEIGHT - 200:
            self.y_speed = -5
        if self.rect.top < 200:
            self.y_speed = 5
        if self.rect.left > WIDTH:
            self.rect.right = 0


# Initialize pygame and create window
pygame.init()  # Initializes pygame
pygame.mixer.init()  # Initializes the audio mixer
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Creates a window
pygame.display.set_caption("My Game")  # Sets the caption of the window
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
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
    screen.fill(BLUE)
    all_sprites.draw(screen)
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
