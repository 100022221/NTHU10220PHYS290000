# -*- coding: utf-8 -*-
"""
Created on Tue Jun 10 11:35:18 2014

@author: Administrator
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jun 09 16:15:32 2014

@author: Administrator
"""
import random

class Card(object):
    """Represents a standard playing card."""
    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7','8', '9', '10', 'Jack', 'Queen', 'King']
    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank],Card.suit_names[self.suit])
    def __cmp__(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return cmp(t1, t2)
#p=Card(3,3)
#q=Card(1,2)
#print p.__cmp__(q)

class Deck(object):
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)
    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)
    def pop_card(self):
        return self.cards.pop()
    def add_card(self, card):
        self.cards.append(card)
    def shuffle(self):
        random.shuffle(self.cards)
    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())
    def deal_hands(self,n1,n2): #n1,n2 represent:the number of hands and the number of cards per hand
        H=[]        
        for i in range(n1):
            hand=Hand()                     
            self.move_cards(hand,n2)
            print hand    
d=Deck()
print d.deal_hands(3,5)
print'\n\n\n\n\n\n\n\n'
print d


#    def sort(self):
#        for x in self.cards:
#            for y in self.cards:
#                if x.__cmp__(y)==1:
                                                       
#d=Deck()
#d.shuffle()
#d.cards.sort()
#print d
class Hand(Deck):
    """Represents a hand of playing cards."""
    def __init__(self,cards=[], label=''):
        self.cards = []
        self.label = label
    def has_pair():
        
#h=Hand()
#d.move_cards(h,3)
#print h


    