import os
import pygame


class WalkForwardImages:
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

    def scale(self, Width, Height):
        for i in self.WalkForward:
            pygame.transform.scale(i, (Width, Height))


class Environment:
    Background = pygame.image.load(os.path.join("venv", "background.jpg"))
    
    def getBackground(self):
        return self.Background
