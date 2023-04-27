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

# Other Code

# When You Are Done
server.stop_server()
Creating A Client

from vidstream import CameraClient
from vidstream import VideoClient
from vidstream import ScreenShareClient

# Choose One
client1 = CameraClient('127.0.0.1', 9999)
client2 = VideoClient('127.0.0.1', 9999, 'video.mp4')
client3 = ScreenShareClient('127.0.0.1', 9999)

client1.start_stream()
client2.start_stream()
client3.start_stream()
Check out: https://www.youtube.com/c/NeuralNine
