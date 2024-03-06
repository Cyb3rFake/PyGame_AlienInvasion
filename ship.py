import pygame
from time import sleep
class Ship:
    """Класс отрисовки корабля"""
    def __init__(self, ai_game) -> None:
        """Инициализация корабля и его начальной позиции"""
        self.screen = ai_game.screen
        # Флаг перемещения вправо
        self.moving_right = False
        self.moving_left = False
        
        # Загружает скорость корабля из настроке Settings
        self.settings = ai_game.settings

        
        # Загружает изображение корабля и получает его хитбокс
        self.image = pygame.image.load('Projects/PyGame_AlienInvasion/images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = ai_game.screen.get_rect()
        

        # Каждый новый корабль появляется у нижнего края экрана
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom - self.settings.ship_y_position
        
        # Сохранение координаты центра корабля
        self.x = float(self.rect.x)
        print(f"Current coords: {str(self.x)}")


    def update(self):
        """Обновление позиции корабля ч учетом флагов"""
        #  Обновление атрибутов x, не rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.ship_speed
            print(f"rect.x: {str(self.rect.x)}",end=' ')
            print(f"self.x: {str(self.x)}")
            
            # sleep(1)

        if self.moving_left and self.rect.left > 0:
            self.rect.x -= self.settings.ship_speed+0.1
            print(f"rect.x: {str(self.rect.x)}",end=' ')
            print(f"self.x: {str(self.x)}")
            # sleep(1)

        # Обновление атрибута rect на основании self.x            
        self.x = self.rect.x
        # self.rect.x = self.x



    def blitme(self):
        """Отрисовывает корабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)
    