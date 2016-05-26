import unittest
from Deck import *
from Hand import *
from MiddlePile import *


class MagicCardTest(unittest.TestCase):

    def setUp(self):
        # self.deck = DeckClass()
        # self.hand = HandClass()
        self.middle = Pile()

    def testDescription(self):
        # two on top, every card playable
        self.middle.card_on_top = 1
        self.middle.playable_cards()

        self.assertEquals(len(self.middle.playable_cards_list), 52)

        # 7 on top, a 2,3,4,5,6,7,8 or 10 maybe played
        self.middle.card_on_top = 32
        self.middle.playable_cards()
        seven_counter = 0
        for card in self.middle.playable_cards_list:
            if card == 1:
                seven_counter += 1
            elif card == 2:
                seven_counter += 1
            elif card == 3:
                seven_counter += 1
            elif card == 4:
                seven_counter += 1
            elif card == 5:
                seven_counter += 1
            elif card == 6:
                seven_counter += 1
            elif card == 7:
                seven_counter += 1
            elif card == 9:
                seven_counter += 1

        self.assertEquals(seven_counter, 8)

        # 8 on top and 7 below, a 2,3,4,5,6,7,8 or 10 maybe played

        self.middle.card_on_top = 33
        self.middle.cards_in_middle = [32, 33]
        self.middle.playable_cards()
        eight_counter = 0
        for card in self.middle.playable_cards_list:
            if card == 1:
                eight_counter += 1
            elif card == 2:
                eight_counter += 1
            elif card == 3:
                eight_counter += 1
            elif card == 4:
                eight_counter += 1
            elif card == 5:
                eight_counter += 1
            elif card == 6:
                eight_counter += 1
            elif card == 7:
                eight_counter += 1
            elif card == 9:
                eight_counter += 1

        self.assertEquals(eight_counter, 8)

        # 10 on top, cards in the discarded pile, no cards in the middle, every card may be played
        self.middle.card_on_top = 35
        self.middle.cards_in_middle = [32, 33, 35]
        self.middle.playable_cards()

        self.assertEquals(len(self.middle.discarded_cards), 3)
        self.assertEquals(len(self.middle.cards_in_middle), 0)
        self.assertEquals(len(self.middle.playable_cards_list), 52)

