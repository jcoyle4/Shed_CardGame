import unittest
from MiddlePile import *
from Deck import *
from Hand import *


class PickUpPileTest(unittest.TestCase):

    def setUp(self):
        self.deck = DeckClass()
        self.hand = HandClass()
        self.middle = Pile()

    def testDescription(self):

        self.deck.cards = self.hand.setUp(self.deck.cards)
        self.deck.cards = self.middle.Start_game(self.deck.cards)

        self.middle = self.hand.pick_up(self.middle, False)

        self.assertEquals(len(self.hand.hand), 6)
        self.assertEquals(len(self.middle.cards_in_middle), 0)
        self.assertEquals(self.middle.card_on_top, 0)
