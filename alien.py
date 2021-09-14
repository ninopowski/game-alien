import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self, ai_settings, screen):
        """ Initialize the alien and set it on start position"""
        super().__init__()
        self.ai_settings = ai_settings
        self.screen = screen

        # Load the alien image and set its rect
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        # Start each alien at the top left corner
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien exact postion
        self.x = float(self.rect.x)

    def check_edges(self):
        """ Return true if alien is at the edge of the screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left < 0:
            return True

    def update(self):
        """ Move the alien right or left """
        self.x += self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction
        self.rect.x = self.x

    def blitme(self):
        """ Draw the alien at its current location """
        self.screen.blit(self.image, self.rect)
