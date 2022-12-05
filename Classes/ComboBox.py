from pygame.locals import *
import pygame
from Classes.Botton import Botton

class ComboBox():
    def __init__(self, x, y, txt, font, options) -> None:
        self.box = Rect(x, y, 140, 45)
        self.txt = pygame.font.SysFont('Corbel', 35, False, True).render(txt, True, (7, 9, 42))
        self.active = False
        self.options = []
        self.init_options(options, font)

    '''Método que se encarga de inciar las opciones del comboBox'''
    def init_options(self, options, font):
        y = self.box.y + 45
        for option in options:
            botton = Botton(self.box.x, y, option, font)
            botton.box = Rect(self.box.x, y, 140, 32)
            self.options.append(botton)
            y += 32
    
    '''Método que se encarga de revisar si una de las opciones ha sido seleccionada'''
    def check(self):
        for option in self.options:
            if option.box.collidepoint(pygame.mouse.get_pos()): option.active = True
            else: option.active = False
        self.active = False

    '''Método que se encarga de dibujar el comboBox en la pantalla'''
    def draw(self, screen):
        if self.box.collidepoint(pygame.mouse.get_pos()): 
            pygame.draw.rect(screen, (16, 142, 72), self.box, 0)
            pygame.draw.rect(screen, (7, 9, 42), self.box, 2)
        else: 
            pygame.draw.rect(screen, (17, 219, 106), self.box, 0)
            pygame.draw.rect(screen, (7, 9, 42), self.box, 2)
        screen.blit(self.txt, (self.box.x + (self.box.width - self.txt.get_width()) / 2, 
                                self.box.y + (self.box.height - self.txt.get_height()) / 2))

        if self.active: 
            for option in self.options: option.draw(screen)
