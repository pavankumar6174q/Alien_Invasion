import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """A class to manage ship"""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position"""
        super().__init__()
        self.screen = ai_game.screen #1
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect() #2

        #load the ship image and get its rect
        self.image = pygame.image.load('images/spaceship_image.bmp') 
        self.image = pygame.transform.scale(self.image, (50, 50))#3
        self.rect = self.image.get_rect()


        #Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom #4


        #Store a decimal value for the ship's horizontal position
        self.x = float(self.rect.x)


        #movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update ship's position based on the movement flag"""
    # Move right if the flag is set and the ship is within screen bounds
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        # Move left if the flag is set and the ship is within screen bounds
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update rect.x to the new value of self.x
        self.rect.x = self.x


    def blitme(self):
     """Draw the ship at its current location"""
     self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)