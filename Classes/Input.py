from pygame.locals import *
import pygame

class Input():
    def __init__(self, x, y, font) -> None:
        self.txt = ''
        self.rect = Rect(x, y, 90, 45)
        self.font = font

    '''Método que se encarga de actualizar un input'''
    def validate(self, event):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if event.key == pygame.K_BACKSPACE: self.txt = self.txt[:-1]
            else: self.txt += event.unicode

    '''Función que se encarga de dibujar en la pantalla el boton dato'''
    def draw(self, screen):
        pygame.draw.rect(screen, (17, 219, 106), self.rect, 0)
        pygame.draw.rect(screen, (7, 9, 42), self.rect, 2)
        text_surface = self.font.render(self.txt, True, (7, 9, 42))
        screen.blit(text_surface, (self.rect.x+5, self.rect.y+5))
        self.rect.w = max(100, text_surface.get_width()+10)
