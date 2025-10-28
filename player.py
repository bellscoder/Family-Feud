class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.strikes = 0

    def add_score(self, points):
        self.score += points

    def add_strike(self):
        self.strikes += 1

    def reset_strikes(self):
        self.strikes = 0
