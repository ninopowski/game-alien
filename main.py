
import pygame
from settings import Settings
from ship import Ship
from pygame.sprite import Group
import game_functions as gf


def run_game():
    # Initialize the game, settings and create screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(size=(ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien invasion')

    # Make a ship, group of bullets and group of aliens
    # Initialize the ship
    ship = Ship(ai_settings, screen)
    # Make a group to store the bullets in
    bullets = Group()
    aliens = Group()


    # Create the fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Set the background color
    bg_color = (230, 230, 230)

    # Start the main loop
    while True:

        # Watch for keyboard and mouse events.
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_buletts(bullets)
        gf.update_aliens(ai_settings, aliens)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)




run_game()
