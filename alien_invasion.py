import sys
from settings import Settings
from ship import Ship
import pygame

class AlienInvasion:
    """Класс управления ресурсами и поведением приложения"""

    def __init__(self) -> None:
        
        pygame.init()
        pygame.display.set_caption("Alien Invasion")

        self.ai_settings = Settings()
        self.screen = pygame.display.set_mode((
            self.ai_settings.screen_width, 
            self.ai_settings.screen_height)
        )
        
        self.bg_color = self.ai_settings.bg_color
        self.bg_image = pygame.image.load(self.ai_settings.bg_image)
        self.ship = Ship(self.screen)
        

    def _check_events(self):
        """Обработка событий нажатия на клавиш и мыши"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            #Перемещение вправо
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False

            



    def _update_screen(self):
        """Отображение изображения на экране"""
        # self.screen.fill(self.bg_color)
        self.screen.blit(self.bg_image, (0, 0))
        self.ship.blitme()
        pygame.display.flip()


    def run_game(self):
        """Инициация игры и создание ресурсов"""
        
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            

if __name__=='__main__':
    ai = AlienInvasion()
    ai.run_game()