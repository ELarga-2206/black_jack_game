    # WELCOME TO BLACKJACK GAME CODE, IF YOU HAVE NO IDEA WHAT IS A BLACKJACK GAME, PLEASE CHECK IT OUT IN GOOGLE
# let's import Random library
import random

# Let's give the info of the card's suits, ranks and values

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
          'Queen':10, 'King':10, 'Ace':11}  # these are basically tuples defining possible values for card attributes.

playing = True

# Following below is the Card Class which will initiate a card with the given suit and rank

class Card: 

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit

