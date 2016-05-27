# Core Unit Test

import unittest
from Hand import *
from MiddlePile import *
from ComputerAI import *


class ComputerMoveTest(unittest.TestCase):

    def setUp(self):
        self.test_hand = HandClass()
        self.middle = Pile()

    # this test will need to change/ get more advanced when more AI rules are added
    def testDescription(self):

        # self.deck.cards = self.hand.setUp(self.deck.cards)
        self.test_hand.hand.append(5)   # 6 of Clubs
        self.test_hand.hand.append(10)  # Jack of Clubs
        self.test_hand.hand.append(15)  # 3 of Diamonds
        self.test_hand.hand.append(14)  # 2 of Diamonds
        self.test_hand.hand.append(25)  # King of Diamonds

        self.middle.move_card(17)  # five of Diamonds

        self.middle.playable_cards()

        test_move = ComputerAI.play_a_card(self.test_hand.hand, self.middle.playable_cards_list)

        self.assertEquals(test_move, 5)

