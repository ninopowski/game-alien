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

    def blitme(self):
        """ Draw the alien at its current location """
        self.screen.blit(self.image, self.rect)
