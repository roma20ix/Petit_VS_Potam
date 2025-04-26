import pygame
import os
import src.settings


class Gun(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, angl: tuple, all_sprites: pygame.sprite.Group) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = self.load_image(
            os.path.abspath(f'data/weapon/gun/gun_weapon.png'))
        rotate = {(-1, -1): 270+45+90, (1, -1): 270-45 +
                  90, (1, 1): 90+45+90, (-1, 1): 45+90}
        self.image = pygame.transform.rotate(self.image, rotate[angl])

        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.all_sprites = all_sprites

        self.rect.x = x
        self.rect.y = y
        self.STATUS = 'WEAPON'
        self.mode = False
        self.state_pause = False
        self.angl = angl
        self.last_time = 0
        self.sound_push_bullet = pygame.mixer.Sound('sounds\gun.mp3')

    def update(self) -> None:
        if self.state_pause or not self.mode:
            return
        current_time = pygame.time.get_ticks()
        if current_time - self.last_time >= src.settings.COOLDOWN_GUN:
            self.last_time = pygame.time.get_ticks()
            self.sound_push_bullet.play()
            self.all_sprites.add(
                Bullet(self.rect.x, self.rect.y, self.angl, self.all_sprites))

    def set_mode(self, state_mode: bool) -> None:
        self.mode = state_mode
        self.all_sprites.add(
            Bullet(self.rect.x, self.rect.y, self.angl, self.all_sprites))
        self.last_time = pygame.time.get_ticks()

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


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, angl: tuple, all_sprites: pygame.sprite.Group) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = self.load_image(os.path.abspath(
            f'data/weapon/gun/bullet_gun_weapon.png'))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.all_sprites = all_sprites

        self.rect.x = x
        self.rect.y = y
        self.angl = angl
        self.state_pause = False
        self.STATUS = 'SUPPORT_WEAPON'
        self.last_time = 0

    def update(self) -> None:
        if self.state_pause:
            return
        self.rect.x += self.angl[0] * src.settings.SPEED_BULLET
        self.rect.y += self.angl[1] * src.settings.SPEED_BULLET

        robots = pygame.sprite.spritecollide(self, [s for s in self.all_sprites if s.get_status(
        ) == 'PLAYER'], False, pygame.sprite.collide_mask)

        current_time = pygame.time.get_ticks()
        if current_time - self.last_time >= 100:
            self.last_time = current_time
            self.image = pygame.transform.rotate(self.image, 90)

        if not robots and 0 <= self.rect.x <= src.settings.WIDTH - self.rect.w and 0 <= self.rect.y <= src.settings.HEIGHT - self.rect.h:
            return

        for robot in robots:
            robot.damage(src.settings.DAMAGE_GUN)
        self.kill()

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
