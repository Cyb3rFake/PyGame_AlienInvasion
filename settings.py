"""Класс хранения всех настроек игры Alien Invansion"""

class Settings:
    def __init__(self) -> None:
        """Инициализирует настройки игры"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        self.bg_image = 'Projects/PyGame_AlienInvasion/images/bg.jpg'
        # Настройка скорости перемещения корабля
        self.ship_speed = 1.5