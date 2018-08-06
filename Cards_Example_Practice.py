
# coding: utf-8

# In[43]:


from collections import deque
from random import shuffle


# In[98]:


class Card:
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit
    
    def value(self, suit_ranking='none'):
        ranks = [str(i) for i in range(2, 11)] + list('JQKA')
        value_shift = 2 # shifting values so that a 2 card has a value of 2
        if suit_ranking == 'none':
            return value_shift + ranks.index(self._rank)
        elif type(suit_ranking) == str:
            suit_ranking = suit_ranking.split()
            suit_value = (len(suit_ranking) - suit_ranking.index(self._suit)) / 10
            return value_shift + ranks.index(self._rank) + suit_value
        
    def __str__(self):
        return "Card({0}, {1})".format(self._rank, self._suit)
    
class CardGroup:
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]
    
    def add(self, card):
        self._cards.append(card)
        
    def __str__(self):
        [print(card) for card in self._cards]
        return 'Number of cards: {0}'.format(len(self._cards))
    
class Deck(CardGroup):
    ranks = [str(i) for i in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    
    def __init__(self):
        self._cards = deque([Card(rank, suit) for suit in self.suits for rank in self.ranks])
    
    def shuffle(self):
        shuffle(self._cards)
        
    def draw(self):
        return self._cards.pop()
    
class Hand(CardGroup):
    def __init__(self, hand_max='none'):
        self._cards = []
        if type(hand_max) == int:
            self._hand_number = 0
            self._hand_max = hand_max 

    def add(self, card):
        if self._hand_number < self._hand_max:
            self._cards.append(card)
            self._hand_number += 1
        else:
            raise Exception('You cannot add a card to your hand. Max number reached.')
    
class Discard(CardGroup):
    def __init__(self):
        self._cards = []

