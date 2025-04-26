import pygame
import os
import src.settings


class Disk(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, all_sprites: pygame.sprite.Group) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = self.load_image(os.path.abspath(
            f'data/weapon/disk/disk_weapon.png'))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.all_sprites = all_sprites

        self.rect.center = (x, y)
        self.STATUS = 'WEAPON'
        self.mode = False
        self.state_pause = False
        self.saw_disk = None
        self.last_time = 0

    def update(self) -> None:
        if self.state_pause or not self.mode:
            return

        current_time = pygame.time.get_ticks()
        if current_time - self.last_time >= src.settings.COOLDOWN_DISK:
            self.last_time = pygame.time.get_ticks()
            self.saw_disk.damage()

    def set_mode(self, state_mode: bool) -> None:
        self.mode = state_mode
        if self.mode:
            self.saw_disk = Saw_Disk(self.rect.center, self.all_sprites)
            self.all_sprites.add(self.saw_disk)
        else:
            self.saw_disk.kill()

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


class Saw_Disk(pygame.sprite.Sprite):
    def __init__(self, center: int, all_sprites: pygame.sprite.Group) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = self.load_image(os.path.abspath(
            f'data/weapon/disk/saw_disk_weapon.png'))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.all_sprites = all_sprites

        self.rect.center = center
        self.STATUS = 'SUPPORT_WEAPON'
        self.state_pause = False
        self.last_time = 0

    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_time >= 100:
            self.last_time = current_time
            self.image = pygame.transform.rotate(self.image, 90)

    def damage(self) -> None:
        if self.state_pause:
            return
        robots = pygame.sprite.spritecollide(self, [s for s in self.all_sprites if s.get_status(
        ) == 'PLAYER'], False, pygame.sprite.collide_mask)

        if not robots:
            return

        for robot in robots:
            robot.damage(src.settings.DAMAGE_DISK)

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
