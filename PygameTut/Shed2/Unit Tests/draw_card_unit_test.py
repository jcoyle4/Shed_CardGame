# Core Unit Test

import unittest
from Hand import HandClass
from Deck import DeckClass


class DrawACardTest(unittest.TestCase):

    def setUp(self):

        self.deck = DeckClass()
        self.hand = HandClass()

        self.snapShotOfHand = []
        for card in self.hand.hand:
            self.snapShotOfHand.append(card)

    def testDescription(self):

        self.deck.cards = self.hand.setUp(self.deck.cards)

        self.hand.hand[0] = None
        self.assertTrue(any(card is None for card in self.hand.hand))
        self.hand.hand = self.deck.draw(self.hand.hand, 0)

        self.assertNotEquals(self.hand.hand, self.snapShotOfHand)
        self.assertFalse(any(card is None for card in self.hand.hand))


if __name__ == '__main__':
    unittest.main()

