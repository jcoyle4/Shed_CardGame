import unittest
from Hand import *
from MiddlePile import *
from ComputerAI import *


class PWTRSTruncationTest(unittest.TestCase):

    def setUp(self):
        self.comp_hand = HandClass()
        self.player_hand = HandClass()
        self.middle = Pile()
        self.comp_ai = ComputerAI()

    def testDescription(self):
        # Test to see if the truncation occurs correctly

        self.comp_hand.hand.append(5)   # 6 of Clubs
        self.comp_hand.hand.append(10)  # Jack of Clubs
        self.comp_hand.hand.append(15)  # 3 of Diamonds
        self.comp_hand.hand.append(14)  # 2 of Diamonds
        self.comp_hand.hand.append(25)  # King of Diamonds
        self.comp_hand.hand.append(26)  # Ace of Diamonds

        self.player_hand.hand.append(4)   # 5 of Clubs
        self.player_hand.hand.append(8)   # 9 of Clubs
        self.player_hand.hand.append(16)  # 4 of Diamonds
        self.player_hand.hand.append(17)  # 5 of Diamonds
        self.player_hand.hand.append(23)  # Jack of Diamonds

        self.comp_ai.knownCards = self.player_hand.hand

        self.middle.move_card(24)  # Queen of Diamonds

        self.middle.playable_cards()

        self.comp_ai.weights.set_total(12)

        test_move = self.comp_ai.play_a_card(self.comp_hand.hand, self.middle, len(self.player_hand.hand))

        # The ace should not be played as this violates the truncation (default 25) (12 + 13 = 25)
        self.assertNotEquals(26, test_move)
        # The king should be played (12 + 12 < 25)
        self.assertEquals(25, test_move)
