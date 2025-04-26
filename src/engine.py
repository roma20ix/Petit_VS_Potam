"""

"""


import pygame
import os

from src.settings import *
from src.button import Button


class Engine:
    """
    ...
    
    Args:
        __init__(self, width, height, fps)
            ...
            Args: ...
            Returns: ...

        __del__(self)
            ...
            Args: ...
            Returns: ...

        __check_events(self):
            ...
            Args: ...
            Returns: ...

        __check_logic(self):
            ...
            Args: ...
            Returns: ...
        
        __draw(self):
            ...
            Args: ...
            Returns: ...

        run(self):
            ...
            Args: ...
            Returns: ...
    """

    def __init__(self) -> None:
        """"""
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()

        self.title = "PetitPotam"
        self.game_end = False
        self.main_game = False
        
        self.background = pygame.image.load(os.path.abspath('data/background.png'))
        self.field_game = pygame.image.load(os.path.abspath('data/field_game.png'))
        
        # инцилизация всех кнопок
        self.play_button = Button('button_play.png', 0, HEIGHT // 6)
        self.rule_button = Button('button_rule.png', WIDTH, HEIGHT // 3)
        self.setting_button = Button('setting_button.png', 0,  HEIGHT // 2)
        self.credit_button = Button('credits_button.png', WIDTH, 2 * HEIGHT // 3)
        self.out_button = Button('out_button.png', 0, 5 * HEIGHT // 6)
        self.exit_button = Button('exit_button.png', 0, 5 * HEIGHT // 6)
        
        self.play_in_one_PC_button = Button('play_in_one_PC_button.png', -self.play_button.original_size[0], HEIGHT // 3)
        self.play_local_inter_burron = Button('play_local_inter_burron.png', WIDTH, 2 * HEIGHT // 3)
        self.play_in_one_PC_button.target_coor = -self.play_button.original_size[0]
        self.play_local_inter_burron.target_coor = WIDTH + self.play_button.original_size[0]
        
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.play_button)
        self.all_sprites.add(self.rule_button)
        self.all_sprites.add(self.setting_button)
        self.all_sprites.add(self.credit_button)
        self.all_sprites.add(self.out_button)
        
        self.all_sprites.add(self.play_in_one_PC_button)
        self.all_sprites.add(self.play_local_inter_burron)
        
        self.screen_game = 0   # текущий экран 0 - начальный, 1 - настройки, 2 - правила, 3 - выбрать как играть, 4 - сама игра, 5 - пауза
        
    def __del__(self) -> None:
        """"""
        pygame.quit()

    def __check_events(self) -> None:
        """"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_end = True
            
            # =========== начало обработок кнопок ============
            if self.play_button.handle_event(event):
                self.play_button.target_coor = -self.play_button.original_size[0]
                self.rule_button.target_coor = WIDTH + self.rule_button.original_size[0]
                self.setting_button.target_coor = -self.setting_button.original_size[0]
                self.credit_button.target_coor = WIDTH + self.credit_button.original_size[0]
                self.out_button.target_coor = -self.out_button.original_size[0]
                
                self.play_in_one_PC_button.target_coor = WIDTH // 2
                self.play_local_inter_burron.target_coor = WIDTH // 2
                
            if self.rule_button.handle_event(event):
                self.play_button.target_coor = -self.play_button.original_size[0]
                self.rule_button.target_coor = WIDTH + self.rule_button.original_size[0]
                self.setting_button.target_coor = -self.setting_button.original_size[0]
                self.credit_button.target_coor = WIDTH + self.credit_button.original_size[0]
                self.out_button.target_coor = -self.out_button.original_size[0]
            
            if self.setting_button.handle_event(event):
                self.play_button.target_coor = -self.play_button.original_size[0]
                self.rule_button.target_coor = WIDTH + self.rule_button.original_size[0]
                self.setting_button.target_coor = -self.setting_button.original_size[0]
                self.credit_button.target_coor = WIDTH + self.credit_button.original_size[0]
                self.out_button.target_coor = -self.out_button.original_size[0]
            
            if self.credit_button.handle_event(event):
                self.play_button.target_coor = -self.play_button.original_size[0]
                self.rule_button.target_coor = WIDTH + self.rule_button.original_size[0]
                self.setting_button.target_coor = -self.setting_button.original_size[0]
                self.credit_button.target_coor = WIDTH + self.credit_button.original_size[0]
                self.out_button.target_coor = -self.out_button.original_size[0]
            
            if self.out_button.handle_event(event):
                self.game_end = True
                
            if self.play_in_one_PC_button.handle_event(event):
                self.main_game = True
                self.play_in_one_PC_button.target_coor = -self.play_button.original_size[0]
                self.play_local_inter_burron.target_coor = WIDTH + self.rule_button.original_size[0]
            # ==========================================================
    
    def __check_logic(self) -> None:
        """"""
        ...

    def __draw(self) -> None:
        """"""
        if self.main_game:
            self.screen.blit(self.field_game, (0, 0))
        else:
            self.screen.blit(self.background, (0, 0))

        self.all_sprites.update()
        self.all_sprites.draw(self.screen)
        
        pygame.display.flip()

    def run(self) -> None:
        pygame.init()
        pygame.display.set_caption(self.title)

        while not self.game_end:
            self.__check_events()
            self.__check_logic()
            self.__draw()
            self.clock.tick(FPS)
