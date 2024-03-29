"""Класс хранения всех настроек игры Alien Invansion"""

class Settings:
    def __init__(self) -> None:
        """Инициализирует настройки игры"""
        # Настрока окна игры
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        self.bg_image = 'Projects/PyGame_AlienInvasion/images/bg.jpg'

        # Настройка скорости перемещения корабля
        self.ship_speed = 3.2
        self.ship_y_position = 35

        # Настройка снарядов
        self.bullet_speed = 4
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 0, 255)
        self.bullet_allowed = 3