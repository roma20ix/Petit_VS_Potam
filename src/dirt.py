import pygame
import os


class Dirt(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = self.load_image(
            os.path.abspath(f'data/dirt/dirt_weapon.png'))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

        self.rect.x = x
        self.rect.y = y
        self.STATUS = 'SUPPORT'

    def get_status(self) -> str:
        return self.STATUS

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
