from settings import Settings
import pygame

class Ship():
    def __init__(self, screen, ai_settings):
        """Инициализирует корабль и задает его начальную позицию."""
        # Флаг перемещения
        self.moving_right = False
        self.moving_left = False
        #
        self.screen = screen
        self.ai_settings = ai_settings
        # Загрузка изображения корабля и получение прямоугольника.
        self.image = pygame.image.load('img/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Каждый новый корабль появляется у нижнего края экрана.
        #self.rect.centerx = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
    def update(self, ai_settings):
        """Обновляет позицию корабля с учетом флага."""
        if self.moving_right:
            self.rect.centerx += self.ai_settings.ship_speed_factor
            if self.rect.centerx > ai_settings.screen_width - 20:
                self.rect.centerx = ai_settings.screen_width - 20
        if self.moving_left:
            self.rect.centerx -= self.ai_settings.ship_speed_factor
            if self.rect.centerx < 0 + 20:
                self.rect.centerx = 0 + 20
    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)