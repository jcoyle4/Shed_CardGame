# Core Unit Test

import unittest
from Deck import DeckClass
from Hand import HandClass


class FillHandTest(unittest.TestCase):

    def setUp(self):
        self.deck = DeckClass()
        self.computer_hand = HandClass()
        self.player_hand = HandClass()

        self.expected_values = [5, 5, 42]

    def testDescription(self):

        self.deck.cards = self.computer_hand.set_up(self.deck.cards)
        self.deck.cards = self.player_hand.set_up(self.deck.cards)

        self.assertEquals(self.expected_values[2], len(self.deck.cards))
        self.assertEquals(self.expected_values[1], len(self.computer_hand.hand))
        self.assertEquals(self.expected_values[0], len(self.player_hand.hand))

if __name__ == '__main__':
    unittest.main()
