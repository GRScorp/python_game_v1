class Settings():
    def __init__(self):
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255, 255, 255)
        #
        self.ship_speed_factor = 2
        # Параметры пули
        self.bullet_speed_factor = 5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 30
        # Настройки пришельцев
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 3
        self.fleet_direction = 1 # 1 обозначает движение вправо  -1 обозначает влево
