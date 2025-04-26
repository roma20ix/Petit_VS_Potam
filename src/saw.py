import pygame
import os
from src.settings import *


class Saw(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, all_sprites: pygame.sprite.Group) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = self.load_image(
            os.path.abspath(f'data/weapon/saw/saw_weapon.png'))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.all_sprites = all_sprites

        self.rect.x = x
        self.rect.y = y
        self.STATUS = 'WEAPON'
        self.mode = False
        self.state_pause = False
        self.saw_damage = None
        self.last_time = 0

    def update(self) -> None:
        if self.state_pause or not self.mode:
            return

        current_time = pygame.time.get_ticks()
        if current_time - self.last_time >= COOLDOWN_DISK:
            self.last_time = pygame.time.get_ticks()
            self.saw_damage.damage()

    def set_mode(self, state_mode: bool) -> None:
        self.mode = state_mode
        if self.mode:
            self.saw_damage = Saw_Damage(
                self.rect.x, self.rect.y, self.all_sprites)
            self.all_sprites.add(self.saw_damage)
        else:
            self.saw_damage.kill()

    def get_status(self) -> str:
        return self.STATUS

    def pause(self, pause: bool) -> None:
        self.state_pause = pause

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


class Saw_Damage(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, all_sprites: pygame.sprite.Group) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = self.load_image(os.path.abspath(
            f'data/weapon/saw/saw_damage_weapon.png'))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.all_sprites = all_sprites

        self.rect.x = x
        self.rect.y = y
        self.STATUS = 'SUPPORT_WEAPON'
        self.state_pause = False

    def damage(self) -> None:
        if self.state_pause:
            return

        robots = pygame.sprite.spritecollide(self, [s for s in self.all_sprites if s.get_status(
        ) == 'PLAYER'], False, pygame.sprite.collide_mask)

        if not robots:
            return

        for robot in robots:
            robot.damage(DAMAGE_SAW)

    def get_status(self) -> str:
        return self.STATUS

    def pause(self, pause: bool) -> None:
        self.state_pause = pause

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
