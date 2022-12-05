from pygame.locals import *
import pygame

class Card:
    def __init__(self, position, value) -> None:
        self.image = pygame.transform.scale(pygame.image.load('Images/Carts/' + str(value) + '.png'), (150, 300))
        self.position = position
        self.value =  value
        self.headbox = Rect(position[0], position[1], 150, 300)