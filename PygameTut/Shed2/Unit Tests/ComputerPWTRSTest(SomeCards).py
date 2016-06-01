import unittest
from Hand import *
from MiddlePile import *
from ComputerAI import *


class PWTRSSomeCardsKnownTest(unittest.TestCase):

    def setUp(self):
        self.comp_hand = HandClass()
        self.player_hand = HandClass()
        self.middle = Pile()
        self.comp_ai = ComputerAI()

    def testDescription(self):
        # Test to see if when the computer knows some of the cards in the players hand,
        # it will pick the card that has the highest probability to beat everything

        self.comp_hand.hand.append(5)   # 6 of Clubs
        self.comp_hand.hand.append(10)  # Jack of Clubs
        self.comp_hand.hand.append(15)  # 3 of Diamonds
        self.comp_hand.hand.append(14)  # 2 of Diamonds
        self.comp_hand.hand.append(25)  # King of Diamonds

        self.player_hand.hand.append(4)   # 5 of Clubs
        self.player_hand.hand.append(8)   # 9 of Clubs
        self.player_hand.hand.append(16)  # 4 of Diamonds
        self.player_hand.hand.append(17)  # 5 of Diamonds
        self.player_hand.hand.append(23)  # Jack of Diamonds

        self.comp_ai.knownCards = [4, 8, 16, 17, 23]

        self.player_hand.hand.append(26)  # Ace of Diamonds
        self.player_hand.hand.append(27)  # 2 of Hearts
        self.player_hand.hand.append(41)  # 3 of Spades
        self.player_hand.hand.append(42)  # 4 of Spades

        self.middle.move_card(24)  # Queen of Diamonds

        self.middle.playable_cards()

        test_move = self.comp_ai.play_a_card(self.comp_hand.hand, self.middle, len(self.player_hand.hand))

        self.assertEquals(test_move, 25)
