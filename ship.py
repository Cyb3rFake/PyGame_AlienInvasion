"""Модуль Корабля"""
import pygame

class Ship:
    def __init__(self, ai_game) -> None:
        """Инициализация корабля и его начальной позиции"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_react()

        # Загружает изобрадение корабля и получает его хитбокс
        self.image = pygame.image.load('./images/ship.jpg')
        self.rect = self.image.get_rect()
        # Каждый новый корабль появляется у нижнего края экрана
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Отрисовывает корабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)