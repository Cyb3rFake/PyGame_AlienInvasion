import pygame
from pygame.sprite import Group, Sprite

class Alien(Sprite):
    """Класс, представляющий одного пришельца."""
    def __init__(self,ai_game):
        """Иницализация пришельца и его изначальной позиции"""
        super().__init__()
        self.screen = ai_game.screen

        # Загрузка изображения пришельца и назначение арибута rect
        self.image = pygame.image.load('Projects/PyGame_AlienInvasion/images/alien_invader.png')
        self.rect = self.image.get_rect()

        # Каждый новый пришелец появляется в левом верхнем углу экрана.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Сохранение точной горизонтальной позиции пришельца.
        self.x = float(self.rect.x)