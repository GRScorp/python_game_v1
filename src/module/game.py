# здесь подключаются модули
import pygame
#import sys
from settings import Settings
from ship import Ship
from aliens import Alien
import gf

from pygame.sprite import Group
aliens = Group()
bullets = Group()

# создание объектов
pygame.init()

ai_settings = Settings()
screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))

FPS = 60
clock = pygame.time.Clock()

ship = Ship(screen, ai_settings)
alien = Alien(ai_settings, screen)

# Создание флота пришельцев.
gf.create_fleet(ai_settings, screen, ship, aliens)

# главный цикл
while True:
    # задержка
    clock.tick(FPS)
    # цикл обработки событий
    gf.check_events(ai_settings, screen, ship, bullets, alien)
    gf.update_aliens(ai_settings, aliens)
    gf.update_screen(ai_settings, screen, ship, bullets, alien, aliens)
    if (aliens.sprites() == []):
        print('gameover')
        next_game = 0
        while next_game == 0:
            for event in pygame.event.get():
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_ESCAPE:
                        aliens.empty()
                        bullets.empty()
                        next_game = 1
        gf.create_fleet(ai_settings, screen, ship, aliens)
    check_ship_hit = gf.ship_hit(aliens, ship)
    if  check_ship_hit == 1:
        print('gameover')
        next_game = 0
        while next_game == 0:
            for event in pygame.event.get():
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_ESCAPE:
                        next_game = 1
        gf.create_fleet(ai_settings, screen, ship, aliens)
