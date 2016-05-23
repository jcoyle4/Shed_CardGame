# Core Unit Test
import unittest
from MiddlePile import *
from Deck import *
from Hand import *


class HandToMiddleTest(unittest.TestCase):

    def setUp(self):
        self.deck = DeckClass()
        self.hand = HandClass()
        self.middle = Pile()

    def testDescription(self):

        self.deck.cards = self.hand.setUp(self.deck.cards)
        self.deck.cards = self.middle.Start_game(self.deck.cards)

        self.middle.PlayableCards()

        self.assertEquals(len(self.middle.cards_in_middle), 1)

        # Need a boolean here on the chance that there is no possible move
        card_moved = False

        for card in self.hand.hand:
            if card in self.middle.playable_cards_list:
                card_moved = True
                self.middle.moveCard(card)
                # need to break as only one card at a time should be moved
                break

        if card_moved:
            self.assertEquals(len(self.middle.cards_in_middle), 2)
