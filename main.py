
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # Initialize the game, settings and create screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(size=(ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien invasion')

    # Initialize the ship
    ship = Ship(ai_settings, screen)

    # Set the background color
    bg_color = (230, 230, 230)

    # Start the main loop
    while True:

        # Watch for keyboard and mouse events.
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)




run_game()
