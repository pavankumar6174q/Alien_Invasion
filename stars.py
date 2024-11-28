import pygame
import random
from pygame.sprite import Sprite

class Star(Sprite):
    """A class to represent a single star."""

    def __init__(self, ai_game):
        """Initialize the star and set its random position."""
        super().__init__()
        self.screen = ai_game.screen
        self.image = pygame.image.load('images/star.bmp')
        self.image = pygame.transform.scale(self.image, (10, 10))  # Load your star image here
        self.rect = self.image.get_rect()

        # Randomize the position of the star within screen boundaries
        self.rect.x = random.randint(0, ai_game.settings.screen_width - self.rect.width)
        self.rect.y = random.randint(0, ai_game.settings.screen_height - self.rect.height)