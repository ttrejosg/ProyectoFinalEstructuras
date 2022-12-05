from pygame.locals import *
import pygame

class Botton():
    def __init__(self, x, y, txt, font) -> None:
        self.box = Rect(x, y, 140, 45)
        self.txt_surface = font.render(txt, True, (7, 9, 42))
        self.txt = txt
        self.active = False
    
    '''Función que se encarga de dibujar en la pantalla el boton dato'''
    def draw(self, screen):
        #Valida si el mouse esta en la zona del botton
        if self.box.collidepoint(pygame.mouse.get_pos()): 
            pygame.draw.rect(screen, (16, 142, 72), self.box, 0)
            pygame.draw.rect(screen, (7, 9, 42), self.box, 2)
        else: 
            pygame.draw.rect(screen, (17, 219, 106), self.box, 0)
            pygame.draw.rect(screen, (7, 9, 42), self.box, 2)
        screen.blit(self.txt_surface, (self.box.x + (self.box.width - self.txt_surface.get_width()) / 2, 
                                self.box.y + (self.box.height - self.txt_surface.get_height()) / 2))