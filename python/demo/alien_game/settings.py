"""
设置模块
"""
class Settings():
    """设置类"""
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 130, 230)
        self.ship_speed_factor = 1.5

        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 5

        self.alien_speed_factor = 1

        self.fleet_drop_speed = 10
        self.fleet_direction = 1