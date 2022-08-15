from aliens import Alien
from bullet import Bullet
import pygame
import sys

#class gf():
def check_events(ai_settings, screen, ship, bullets, alien):
    """Обрабатывает нажатия клавиш и события мыши."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if len(bullets) < ai_settings.bullets_allowed:
                    # Создание новой пули и включение ее в группу bullets.
                    new_bullet = Bullet(ai_settings, screen, ship)
                    bullets.add(new_bullet)
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            if event.key == pygame.K_LEFT:
                ship.moving_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            if event.key == pygame.K_LEFT:
                ship.moving_left = False
def update_screen(ai_settings, screen, ship, bullets, alien, aliens):
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    ship.blitme()
    ship.update(ai_settings)
    aliens.draw(screen)
    bullets.update()
    check_alien_kill(alien, aliens, bullets)
    # Отображение последнего прорисованного экрана.
    pygame.display.flip()
def update_aliens(ai_settings, aliens):
    """Обновляет позиции всех пришельцев во флоте."""
    check_fleet_edges(ai_settings, aliens)
    aliens.update(ai_settings)
def get_number_aliens_x(ai_settings, alien_width):
    """Вычисляет количество пришельцев в ряду."""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x
    #return 1
def get_number_rows(ai_settings, ship_height, alien_height):
    """Определяет количество рядов, помещающихся на экране."""
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows
    #return 1
def create_fleet(ai_settings, screen, ship, aliens):
    # Создание пришельца и вычисление количества пришельцев в ряду.
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    # Создание флота пришельцев.
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)
def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """Создает пришельца и размещает его в ряду."""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)
def check_fleet_edges(ai_settings, aliens):
    """Реагирует на достижение пришельцем края экрана."""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
        break
def change_fleet_direction(ai_settings, aliens):
    """Опускает весь флот и меняет направление флота."""
    ai_settings.fleet_direction *= -1
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
def check_alien_kill(alien, aliens, bullets):
    for alien in aliens.sprites():
        for bullet in bullets.sprites():
            if (alien.rect.x) <= (bullet.rect.x + bullet.rect.width):
                if (alien.rect.x + alien.rect.width) >= (bullet.rect.x):
                    if (alien.rect.y) <= (bullet.rect.y + bullet.rect.height):
                        if (alien.rect.y + alien.rect.height) >= (bullet.rect.y):
                            aliens.remove(alien)
                            bullets.remove(bullet)
def ship_hit(aliens, ship):
    for alien in aliens.sprites():
        if (alien.rect.x) <= (ship.rect.x + ship.rect.width):
            if (alien.rect.x + alien.rect.width) >= (ship.rect.x):
                if (alien.rect.y) <= (ship.rect.y + ship.rect.height):
                    if (alien.rect.y + alien.rect.height) >= (ship.rect.y):
                        return 1
