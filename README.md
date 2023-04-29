# NOTE: Not uploaded.

# Pygame Functions
Currently in development. Please DM me on Discord if you have advice. DL#6569

Developed by DL#6569.

# How to use Pygame Functions 
Creating A New Python File.

```py
from pygame_functions import *
import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
WINDOW_SIZE = (400, 300)
screen = pygame.display.set_mode(WINDOW_SIZE)

# Set the caption of the window
pygame.display.set_caption("Open YouTube")

# Hello function
def hello():
  print("Hello!")

# Create the button
myButton = WordButton(200, 100, "Hey!", (12, 182, 29), (40, 220, 58), 40)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
      
    # Draw the button
    nextButton.displayText(screen, None, hello)
    screen.blit(button_text, button_rect)

    # Update the display
    pygame.display.update()
```

# Next
Thanks for using my pygame function really appriciate it.
DL.
