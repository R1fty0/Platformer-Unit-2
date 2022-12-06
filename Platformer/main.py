# Time left to work on Project: 24h

# Imports
import pygame
import os

# Refresh Rate of Program
FPS = 60

# Dimensions of Game Window
Width, Height = 800, 600

# Player Dimensions
PlayerWidth, PlayerHeight = 144, 194
# Player Speed
Speed = 1


# Scales Images
def ScaleImages(List, Width, Height):
    for i in List:
        pygame.transform.scale(i, (Width, Height))


# Walking Forward Images
WalkForward = [pygame.image.load(os.path.join("venv", "p1_walk01.png")),
               pygame.image.load(os.path.join("venv", "p1_walk02.png")),
               pygame.image.load(os.path.join("venv", "p1_walk03.png")),
               pygame.image.load(os.path.join("venv", "p1_walk04.png")),
               pygame.image.load(os.path.join("venv", "p1_walk05.png")),
               pygame.image.load(os.path.join("venv", "p1_walk06.png")),
               pygame.image.load(os.path.join("venv", "p1_walk07.png")),
               pygame.image.load(os.path.join("venv", "p1_walk08.png")),
               pygame.image.load(os.path.join("venv", "p1_walk09.png")),
               pygame.image.load(os.path.join("venv", "p1_walk10.png")),
               pygame.image.load(os.path.join("venv", "p1_walk11.png"))]

# Walking Backwards Images
WalkBackward = []

# Flips the Images of the WalkForward List, and adds them to be used as the images for the WalkBackwards List.
for i in WalkForward:
    image = pygame.transform.flip(i, False, True)
    WalkBackward.append(image)

# Prints the length of both lists.
print("The length of the WalkBackward List is " f"{len(WalkBackward)} frames.")
print("The length of the WalkForward List is " f"{len(WalkForward)} frames.")


# Background
Background = pygame.image.load(os.path.join("venv", "background.png"))
# Idle
Idle = pygame.image.load(os.path.join("venv", "p1_stand.png"))
# Jumping
Jumping = pygame.image.load(os.path.join("venv", "p1_jump.png"))

# Scales Images to a desired size.
ScaleImages(WalkForward, PlayerWidth, PlayerHeight)

# Creates Window and Name of the Game
Window = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Platformer")


"""

This is a border between the functions and the other pieces of code. Realistically, the code above should be implemented into various data structures.

"""

# Updates the Visuals on the Screen.
def Canvas(Player):

    # Draws Background
    Window.blit(Background, (0, 0))
    # Draws Player in the idle state
    Window.blit(Idle, (Player.x, Player.y))

    # Updates the Screen with the changes made by this function.
    pygame.display.update()


def Movement(Player):
    KeyPressed = pygame.key.get_pressed()

    if KeyPressed[pygame.K_a]:
        # Moves Player to the Right, or Forward relative to the game's perspective.
        Player.x -= Speed
    if KeyPressed[pygame.K_d]:
        # Moves Player to the Left, or Backwards relative to the game's perspective.
        Player.x += Speed
    if KeyPressed[pygame.K_w]:
        # Allows the Player to jump
        Player.y -= Speed


def Update():
    # Player spawn position.
    PlayerSpawnX = Width / 4
    PlayerSpawnY = Height / 2

    # Displays the Player at the location listed above.
    Player = pygame.Rect(PlayerSpawnX, PlayerSpawnY, PlayerWidth, PlayerHeight)

    # Clock that maintains FPS
    clock = pygame.time.Clock()
    # If this boolean is true, then the program runs.
    run = True
    while run:
        clock.tick(FPS)
        # Terminates Program if the User Closes the Application
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            Movement(Player)
            Canvas(Player)
    pygame.quit()


# Similar to the Update Call in Unity
if __name__ == "__main__":
    Update()
