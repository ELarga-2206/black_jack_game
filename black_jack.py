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

class Deck:

    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))  # build Card objects and add them to the list

    def __str__(self):
        deck_comp = ''  # start with an empty string
        for card in self.deck:
            deck_comp += '\n '+card.__str__() # add each Card object's print string
        return 'The deck has:' + deck_comp

    def shuffle(self):          # shuffle function will shuffle the whole deck
        random.shuffle(self.deck)

    def deal(self):             # deal function will take one card from the deck
        single_card = self.deck.pop()
        return single_card

class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces

# add_card function will add a card to the player's hand
# abstraction
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]


# since ace can have two values as 1 or 11, adjust_for_ace will adjust the value of ace

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1