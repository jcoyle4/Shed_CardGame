import random


class Pile:

    cards_in_middle = None
    card_on_top = None
    discarded_cards = None

    playable_cards_list = None

    def __init__(self):
        self.cards_in_middle = []
        self.discarded_cards = []
        self.playable_cards_list = []
        #self.PlayableCards()

    def add_Twos(self):
        self.playable_cards_list.append(1)
        self.playable_cards_list.append(14)
        self.playable_cards_list.append(27)
        self.playable_cards_list.append(40)

    def add_Threes(self):
        self.playable_cards_list.append(2)
        self.playable_cards_list.append(15)
        self.playable_cards_list.append(28)
        self.playable_cards_list.append(41)

    def add_Fours(self):
        self.playable_cards_list.append(3)
        self.playable_cards_list.append(16)
        self.playable_cards_list.append(29)
        self.playable_cards_list.append(42)

    def add_Fives(self):
        self.playable_cards_list.append(4)
        self.playable_cards_list.append(17)
        self.playable_cards_list.append(30)
        self.playable_cards_list.append(43)

    def add_Sixes(self):
        self.playable_cards_list.append(5)
        self.playable_cards_list.append(18)
        self.playable_cards_list.append(31)
        self.playable_cards_list.append(44)

    def add_Sevens(self):
        self.playable_cards_list.append(6)
        self.playable_cards_list.append(19)
        self.playable_cards_list.append(32)
        self.playable_cards_list.append(45)

    def add_Eights(self):
        self.playable_cards_list.append(7)
        self.playable_cards_list.append(20)
        self.playable_cards_list.append(33)
        self.playable_cards_list.append(46)

    def add_Nines(self):
        self.playable_cards_list.append(8)
        self.playable_cards_list.append(21)
        self.playable_cards_list.append(34)
        self.playable_cards_list.append(47)

    def add_Tens(self):
        self.playable_cards_list.append(9)
        self.playable_cards_list.append(22)
        self.playable_cards_list.append(35)
        self.playable_cards_list.append(48)

    def add_Jacks(self):
        self.playable_cards_list.append(10)
        self.playable_cards_list.append(23)
        self.playable_cards_list.append(36)
        self.playable_cards_list.append(49)

    def add_Queens(self):
        self.playable_cards_list.append(11)
        self.playable_cards_list.append(24)
        self.playable_cards_list.append(37)
        self.playable_cards_list.append(50)

    def add_Kings(self):
        self.playable_cards_list.append(12)
        self.playable_cards_list.append(25)
        self.playable_cards_list.append(38)
        self.playable_cards_list.append(51)

    def add_Aces(self):
        self.playable_cards_list.append(13)
        self.playable_cards_list.append(26)
        self.playable_cards_list.append(39)
        self.playable_cards_list.append(52)

    def PlayableCards(self):
        # MAGIC
        # 2 on top
        self.playable_cards_list = []
        if self.card_on_top in [1, 14, 27, 40]:
            # resets the value of the pile
            self.add_Twos()
            self.add_Threes()
            self.add_Fours()
            self.add_Fives()
            self.add_Sixes()
            self.add_Sevens()
            self.add_Eights()
            self.add_Nines()
            self.add_Tens()
            self.add_Jacks()
            self.add_Queens()
            self.add_Kings()
            self.add_Aces()

        # 3 on top
        elif self.card_on_top in [2, 15, 28, 41]:
            self.add_Twos()
            self.add_Threes()
            self.add_Fours()
            self.add_Fives()
            self.add_Sixes()
            self.add_Sevens()
            self.add_Eights()
            self.add_Nines()
            self.add_Tens()
            self.add_Jacks()
            self.add_Queens()
            self.add_Kings()
            self.add_Aces()

        # 4 on top
        elif self.card_on_top in [3, 16, 29, 42]:
            self.add_Twos()
            self.add_Fours()
            self.add_Fives()
            self.add_Sixes()
            self.add_Sevens()
            self.add_Eights()
            self.add_Nines()
            self.add_Tens()
            self.add_Jacks()
            self.add_Queens()
            self.add_Kings()
            self.add_Aces()

        # 5 on top
        elif self.card_on_top in [4, 17, 30, 43]:
            self.add_Twos()
            self.add_Fives()
            self.add_Sixes()
            self.add_Sevens()
            self.add_Eights()
            self.add_Nines()
            self.add_Tens()
            self.add_Jacks()
            self.add_Queens()
            self.add_Kings()
            self.add_Aces()

        # 6 on top
        elif self.card_on_top in [5, 18, 31, 44]:
            self.add_Twos()
            self.add_Sixes()
            self.add_Sevens()
            self.add_Eights()
            self.add_Nines()
            self.add_Tens()
            self.add_Jacks()
            self.add_Queens()
            self.add_Kings()
            self.add_Aces()

        # MAGIC
        # 7 on top
        elif self.card_on_top in [6, 19, 32, 45]:
            # next card played must be valued <= 7
            self.add_Twos()
            self.add_Threes()
            self.add_Fours()
            self.add_Fives()
            self.add_Sixes()
            self.add_Sevens()
            self.add_Eights()

        # MAGIC
        # 8 on top
        elif self.card_on_top in [7, 20, 33, 46]:
            # change value of card on top to card played before the 8
            # then re-run this method

            card_under_8 = self.cards_in_middle[-1]
            if card_under_8 in [1, 14, 27, 40]:
                # resets the value of the pile
                self.add_Twos()
                self.add_Threes()
                self.add_Fours()
                self.add_Fives()
                self.add_Sixes()
                self.add_Sevens()
                self.add_Eights()
                self.add_Nines()
                self.add_Tens()
                self.add_Jacks()
                self.add_Queens()
                self.add_Kings()
                self.add_Aces()

        # 3 on top
            elif card_under_8 in [2, 15, 28, 41]:
                self.add_Twos()
                self.add_Threes()
                self.add_Fours()
                self.add_Fives()
                self.add_Sixes()
                self.add_Sevens()
                self.add_Eights()
                self.add_Nines()
                self.add_Tens()
                self.add_Jacks()
                self.add_Queens()
                self.add_Kings()
                self.add_Aces()

            elif card_under_8 in [3, 16, 29, 42]:
                self.add_Twos()
                self.add_Fours()
                self.add_Fives()
                self.add_Sixes()
                self.add_Sevens()
                self.add_Eights()
                self.add_Nines()
                self.add_Tens()
                self.add_Jacks()
                self.add_Queens()
                self.add_Kings()
                self.add_Aces()

        # 5 on top
            elif card_under_8 in [4, 17, 30, 43]:
                self.add_Twos()
                self.add_Fives()
                self.add_Sixes()
                self.add_Sevens()
                self.add_Eights()
                self.add_Nines()
                self.add_Tens()
                self.add_Jacks()
                self.add_Queens()
                self.add_Kings()
                self.add_Aces()

            # 6 on top
            elif card_under_8 in [5, 18, 31, 44]:
                self.add_Twos()
                self.add_Sixes()
                self.add_Sevens()
                self.add_Eights()
                self.add_Nines()
                self.add_Tens()
                self.add_Jacks()
                self.add_Queens()
                self.add_Kings()
                self.add_Aces()

            # MAGIC
            # 7 on top
            elif card_under_8 in [6, 19, 32, 45]:
                # next card played must be valued <= 7
                self.add_Twos()
                self.add_Threes()
                self.add_Fours()
                self.add_Fives()
                self.add_Sixes()
                self.add_Sevens()
                self.add_Eights()

            # two eights on top of each other, let them play anything
            elif card_under_8 in [7, 20, 33, 46]:
                self.add_Twos()
                self.add_Threes()
                self.add_Fours()
                self.add_Fives()
                self.add_Sixes()
                self.add_Sevens()
                self.add_Eights()
                self.add_Nines()
                self.add_Tens()
                self.add_Jacks()
                self.add_Queens()
                self.add_Kings()
                self.add_Aces()

            # 9
            elif card_under_8 in [8, 21, 34, 47]:
                self.add_Twos()
                self.add_Eights()
                self.add_Nines()
                self.add_Tens()
                self.add_Jacks()
                self.add_Queens()
                self.add_Kings()
                self.add_Aces()
            # # 10 there will never be a 10 under an 8
            # elif card_under_8 in [9, 22, 35, 48]:
            #     self.add_Twos()
            #     self.add_Threes()
            #     self.add_Fours()
            #     self.add_Fives()
            #     self.add_Sixes()
            #     self.add_Sevens()
            #     self.add_Eights()
            #     self.add_Nines()
            #     self.add_Tens()
            #     self.add_Jacks()
            #     self.add_Queens()
            #     self.add_Kings()
            #     self.add_Aces()
            # J
            elif card_under_8 in [10, 23, 36, 49]:
                self.add_Twos()
                self.add_Eights()
                self.add_Jacks()
                self.add_Queens()
                self.add_Kings()
                self.add_Tens()
                self.add_Aces()

            # Queen on top
            elif card_under_8 in [11, 24, 37, 50]:
                self.add_Twos()
                self.add_Eights()
                self.add_Queens()
                self.add_Kings()
                self.add_Tens()
                self.add_Aces()

            # King on top
            elif card_under_8 in [12, 25, 38, 51]:
                self.add_Twos()
                self.add_Eights()
                self.add_Kings()
                self.add_Tens()
                self.add_Aces()

            # Ace on top
            elif card_under_8 in [13, 26, 39, 52]:
                self.add_Twos()
                self.add_Eights()
                self.add_Tens()
                self.add_Aces()


        # 9 on top
        elif self.card_on_top in [8, 21, 34, 47]:
            self.add_Twos()
            self.add_Eights()
            self.add_Nines()
            self.add_Tens()
            self.add_Jacks()
            self.add_Queens()
            self.add_Kings()
            self.add_Aces()

        # MAGIC
        # 10 on top
        elif self.card_on_top in [9, 22, 35, 48]:
            # discard the pile
            self.discarded_cards += self.cards_in_middle
            # If a 10 is on top is also need to be added to the pile of discarded cards

            # self.discarded_cards.append(self.card_on_top)
            # reset the pile
            self.cards_in_middle = []
            # self.card_on_top = None
            # any card may be played
            self.add_Twos()
            self.add_Threes()
            self.add_Fours()
            self.add_Fives()
            self.add_Sixes()
            self.add_Sevens()
            self.add_Eights()
            self.add_Nines()
            self.add_Tens()
            self.add_Jacks()
            self.add_Queens()
            self.add_Kings()
            self.add_Aces()
            print("THE CARD IN THE MIDDLE IS A 10 (9, 22, 35, 48)")
            # print("10 - Discarded cards =", self.discarded_cards)
            # print("10 - Cards in the middle =", self.cards_in_middle)

        # Jack on top
        elif self.card_on_top in [10, 23, 36, 49]:
            self.add_Twos()
            self.add_Eights()
            self.add_Jacks()
            self.add_Queens()
            self.add_Kings()
            self.add_Tens()
            self.add_Aces()

        # Queen on top
        elif self.card_on_top in [11, 24, 37, 50]:
            self.add_Twos()
            self.add_Eights()
            self.add_Queens()
            self.add_Kings()
            self.add_Tens()
            self.add_Aces()

        # King on top
        elif self.card_on_top in [12, 25, 38, 51]:
            self.add_Twos()
            self.add_Eights()
            self.add_Kings()
            self.add_Tens()
            self.add_Aces()

        # Ace on top
        elif self.card_on_top in [13, 26, 39, 52]:
            self.add_Twos()
            self.add_Eights()
            self.add_Tens()
            self.add_Aces()

        elif self.card_on_top == 0:
            self.add_Twos()
            self.add_Threes()
            self.add_Fours()
            self.add_Fives()
            self.add_Sixes()
            self.add_Sevens()
            self.add_Eights()
            self.add_Nines()
            self.add_Tens()
            self.add_Jacks()
            self.add_Queens()
            self.add_Kings()
            self.add_Aces()

        # elif self.card_on_top is None:
        #     self.add_Twos()
        #     self.add_Threes()
        #     self.add_Fours()
        #     self.add_Fives()
        #     self.add_Sixes()
        #     self.add_Sevens()
        #     self.add_Eights()
        #     self.add_Nines()
        #     self.add_Tens()
        #     self.add_Jacks()
        #     self.add_Queens()
        #     self.add_Kings()
        #     self.add_Aces()

        print("Discarded cards =", self.discarded_cards)
        print("Cards in the middle =", self.cards_in_middle)
        print("Card on top =", self.card_on_top)
        self.playable_cards_list.sort()





    def Start_game(self, deck):
        card = random.choice(deck)
        deck.remove(card)
        self.card_on_top = card
        self.cards_in_middle.append(card)
        return deck

