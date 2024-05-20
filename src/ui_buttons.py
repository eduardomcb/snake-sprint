import time

import pygame


class Button:
    def __init__(self, text, font, text_color, box_color, surface, x, y):
        self.text = text
        self.font = font
        self.text_color = text_color
        self.box_color = box_color
        self.surface = surface
        self.x = x
        self.y = y
        self.clicked = False
        self.rect = pygame.Rect(x, y, 200, 50)  # Define as dimensões do retângulo do botão

    def draw(self):
        pygame.draw.rect(self.surface, self.box_color, self.rect)  # Desenha o retângulo preto como fundo do botão
        text_obj = self.font.render(self.text, True, self.text_color)
        text_rect = text_obj.get_rect(center=self.rect.center)
        self.surface.blit(text_obj, text_rect)

    def is_clicked(self):
        action = False
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()

        if self.rect.collidepoint(mouse_pos):
            if mouse_pressed[0] == 1 and not self.clicked:
                self.clicked = True
                action = True
                time.sleep(0.2)

        if mouse_pressed[0] == 0:
            self.clicked = False

        return action
