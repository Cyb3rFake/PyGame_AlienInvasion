import sys
from settings import Settings
from ship import Ship
import pygame

class AlienInvasion:
    """Класс управления ресурсами и поведением приложения"""

    def __init__(self) -> None:

        pygame.init()
        pygame.display.set_caption("Alien Invasion")
        self.settings = Settings()
        self.screen = pygame.display.set_mode((
            self.settings.screen_width, self.settings.screen_height)
        )
        self.bg_color = self.settings.bg_color
        self.ship = Ship(self.screen)
        
    
    def run_game(self):
        """Инициация игры и создание ресурсов"""
        
        while True:
            """Отслеживание нажатий кнопок клавиатуры и мыши"""
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.ship.blitme()
            self.screen.fill(self.settings.bg_color)
            # Отображение экземпляра проримованного экрана.
            pygame.display.flip()

if __name__=='__main__':
    ai = AlienInvasion()
    ai.run_game()