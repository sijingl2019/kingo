import pygame
from pygame.sprite import Group

from alien_game.settings import Settings
from alien_game.ship import Ship
import alien_game.game_functions as gf


def run_game() :
    """
        初始化游戏
        建立屏幕对象
    """
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)
    #开始游戏主循环
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_aliens(aliens)
        # print(len(bullets))
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)
run_game()