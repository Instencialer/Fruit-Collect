import pygame, random
from pygame.locals import *
pygame.init()

class apples:
    def __init__(self):
        self.x = random.randint(0, 500)
        self.y = 0
        self.img = pygame.image.load("IMG/apple.png")
        self.applerect = pygame.Rect(self.x, self.y, 32, 32)

    def calc(self, pos, speed):
        self.y += speed
        self.applerect.y = self.y
        if (self.applerect.colliderect(pygame.Rect(pos, 520, 64, 10))):
            return "POINTS"

class bombs:
    def __init__(self):
        self.x = random.randint(0, 500)
        self.y = 0
        self.img = pygame.image.load("IMG/bomb.png")
        self.bombrect = pygame.Rect(self.x, self.y, 32, 32)

    def calc(self, pos, speed):
        self.y += speed
        self.bombrect.y = self.y
        if (self.bombrect.colliderect(pygame.Rect(pos, 520, 64, 10))):
            return "OOFED"

class decor:
    def __init__(self):
        self.grass_images = [pygame.image.load("IMG/grass1.png")]
        self.grass_location = [[15, 570],[283, 600], [400, 560],[450, 670], [3300, 600]]

    def rendering(self, screen):
        for x in self.grass_location:
            screen.blit(self.grass_images[0], (x[0], x[1]))

def label(text, size):
    font = pygame.font.Font("dogica.ttf", size)
    return font.render(text,False,(255,255,255))




        
