class Settings:
    """Every Setting of the Alien invasion"""

    def __init__(self):
        """Initialize the game settings"""
        #screen settings
        self.screen_width = 1200
        self.screen_height = 725
        self.bg_color = (20,20,30)

        #ship settings
        self.ship_speed = 1
        self.ship_limit = 2
        
        #Bullet Settings
        self.bullet_speed = 0.3
        self.bullet_width = 10
        self.bullet_height =15
        self.bullet_color = (0, 191, 255)
        self.bullets_allowed = 7

        #alien settings
        self.alien_speed = 0.2
        self.fleet_drop_speed = 8

        #Fleet direction of 1 represents right  -1 represents left
        self.fleet_direction = 1

        #How quickly the game speeds up
        self.speedup_scale = 0.5

        #How quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()


    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game"""
        self.ship_speed = 1
        self.bullet_speed = 1.2
        self.alien_speed = 0.2

        #Fleet direction of 1 is right and -1 is left
        self.fleet_direction = 1

        #scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and the point values"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        #points
        self.alien_points = int(self.alien_points * self.score_scale)
        #print(self.alien_points)