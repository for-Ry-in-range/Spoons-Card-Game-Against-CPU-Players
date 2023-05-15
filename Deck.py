import pygame
import random
from Card import Card

class Deck:
    def __init__(self):
        self.cards = []
        self.count = 52

    def shuffle(self): #SHUFFLES DECK
        random.shuffle(self.cards)


    def deal(self, players): #DEALS OUT 4 CARDS TO X AMOUNT OF PLAYERS
        cards_list = []
        for i in range(players):
            new_player_deck = []
            for i in range(4):
                card_index = random.randrange(0, len(self.cards))
                new_player_deck.append(self.cards[card_index])
                self.cards.pop(card_index)
                self.count-=1
            cards_list.append(new_player_deck)
        cards_list.insert(0, self.cards)
        return cards_list[1:]

    def cardcount(self): #RETURNS NUMBER OF CARDS IN DECK
        return self.count

    def top(self): #RETURNS CARD AT THE TOP OF DECK
        return self.cards[0]

    def draw(self): #returns the top card of the deck and removes it
        return self.cards.pop(0)

    def create(self, deck): #input a list of cards and it adds it to the deck
        self.cards = deck
    def addcard(self, card):
        self.cards.append(card)

    def remove_top_card(self):
        self.cards.pop(0)
