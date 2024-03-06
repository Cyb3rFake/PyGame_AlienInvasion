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
            self.settings.screen_width, 
            self.settings.screen_height)
        )

        # self.ship_speed = self.settings.ship_speed
        self.bg_color = self.settings.bg_color
        self.bg_image = pygame.image.load(self.settings.bg_image)
        self.ship = Ship(self)
        

    def _check_events(self):
        """Обработка событий нажатия на клавиш и мыши"""
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    sys.exit()  
                case pygame.KEYDOWN:
                    self._check_keydown_events(event)
                case pygame.KEYUP:
                    self._check_keyup_events(event)
                
                    
            
            # if event.type == pygame.QUIT:
            #     sys.exit()
            # elif event.type == pygame.KEYDOWN:
            #     self._check_keydown_events(event)
            # elif event.type == pygame.KEYUP:
            #     self._check_keyup_events(event)
            

    def _check_keydown_events(self, event):
        """Событие  при нажатии клавиши"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_F5:
            # Развернуть на полный экран
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            self.settings.screen_width = self.screen.get_rect().width
            self.settings.screen_height = self.screen.get_rect().height
            background = pygame.image.load(self.settings.bg_image)
            self.bg_image = pygame.transform.scale(background, (self.settings.screen_width, self.settings.screen_height))
            self.ship = Ship(self)

    def _check_keyup_events(self, event):
        """Событие  при отпускании клавиши"""
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