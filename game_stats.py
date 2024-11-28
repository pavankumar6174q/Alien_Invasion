class GameStats:
    """Track statistics for Alien Invasion"""

    def __init__(self, ai_game):
        """Initialize stats"""
        self.settings = ai_game.settings
        self.reset_stats()
        #Start alien invasion in an inactive state
        self.game_active = False

        #High score should never reset
        self.high_score = 0
        


    def reset_stats(self):
        """"Initialize statistics that can change during the game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def _load_high_score(self):
        """Load the high score from a file if available"""
        try:
            with open("high_score.txt", "r") as f:
                return int(f.read())
        except (FileNotFoundError, ValueError):
            return 0  # Start at 0 if the file doesn't exist or there's an error

    def save_high_score(self):
        """Save the high score to a file"""
        with open("high_score.txt", "w") as f:
            f.write(str(self.high_score))