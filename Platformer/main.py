# Time left to work on Project: 26h 00m

# Imports
import pygame
from images import WalkForwardImages
from images import Environment


# Instantiation of Classes
WalkImagesList = WalkForwardImages()
Background = Environment()

# Refresh Rate of Program
FPS = 60

# Dimensions of Game Window
Width, Height = 1000, 500

# Player Dimensions
PlayerWidth, PlayerHeight = 144, 194

# Scales all images to the correct dimensions
WalkImagesList.scale(PlayerWidth, PlayerHeight)

# Creates Window and Name of the Game
Window = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Platformer")


def Update():
    # Gets the Background from the Environment Class
    image = Background.getBackground
    # Draws Background on Screen
    Window.blit(image, (0, 0))
    # Clock that maintains FPS
    clock = pygame.time.Clock()
    # If this boolean is true, then the program runs.
    run = True
    while run:
        clock.tick(FPS)
        # Loops through this check until the user decides to quit the program, then the code in the loop will run
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    pygame.quit()


# Similar to the Update Call in Unity
if __name__ == "__main__":
    Update()
