import pygame

class Ship:
    """Класс отрисовки корабля"""
    def __init__(self, screen) -> None:
        """Инициализация корабля и его начальной позиции"""
        self.screen = screen
        # Флаг перемещения вправо
        self.moving_right = False
        self.moving_left = False

        # Загружает изобрадение корабля и получает его хитбокс
        self.image = pygame.image.load('Projects/PyGame_AlienInvasion/images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Каждый новый корабль появляется у нижнего края экрана
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom


    def blitme(self):
        """Отрисовывает корабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)
    
    def update(self):
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1