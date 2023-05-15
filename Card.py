import pygame

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.image = pygame.image.load(self.value + self.suit + '.png')  # pngs of cards should be named in format “2c.png” or “kd.png”
    def __repr__(self):
        return f"{self.value} of {self.suit}"
