import pygame
import os
from src.settings import *


class Robot(pygame.sprite.Sprite):
    def __init__(self, iamgeName: str, x: int, y: int) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = self.load_image(os.path.abspath(f'data/{iamgeName}'))
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
        self.hp = HP
        
    def update(self) -> None:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        
    def move(self, coef_x: bool, coef_y: bool) -> None:
        self.rect.x += SPEED * int(coef_x)
        self.rect.y += SPEED * int(coef_y)
    
    def load_image(self, name, colorkey=None) -> pygame.image:
        image = pygame.image.load(name)

        if colorkey is not None:
            image = image.convert()
            if colorkey == -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey)
        else:
            image = image.convert_alpha()
        return image
