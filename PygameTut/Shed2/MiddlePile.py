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

    def add_twos(self):
        self.playable_cards_list.append(1)
        self.playable_cards_list.append(14)
        self.playable_cards_list.append(27)
        self.playable_cards_list.append(40)

    def add_threes(self):
        self.playable_cards_list.append(2)
        self.playable_cards_list.append(15)
        self.playable_cards_list.append(28)
        self.playable_cards_list.append(41)

    def add_fours(self):
        self.playable_cards_list.append(3)
        self.playable_cards_list.append(16)
        self.playable_cards_list.append(29)
        self.playable_cards_list.append(42)

    def add_fives(self):
        self.playable_cards_list.append(4)
        self.playable_cards_list.append(17)
        self.playable_cards_list.append(30)
        self.playable_cards_list.append(43)

    def add_sixes(self):
        self.playable_cards_list.append(5)
        self.playable_cards_list.append(18)
        self.playable_cards_list.append(31)
        self.playable_cards_list.append(44)

    def add_sevens(self):
        self.playable_cards_list.append(6)
        self.playable_cards_list.append(19)
        self.playable_cards_list.append(32)
        self.playable_cards_list.append(45)

    def add_eights(self):
        self.playable_cards_list.append(7)
        self.playable_cards_list.append(20)
        self.playable_cards_list.append(33)
        self.playable_cards_list.append(46)

    def add_nines(self):
        self.playable_cards_list.append(8)
        self.playable_cards_list.append(21)
        self.playable_cards_list.append(34)
        self.playable_cards_list.append(47)

    def add_tens(self):
        self.playable_cards_list.append(9)
        self.playable_cards_list.append(22)
        self.playable_cards_list.append(35)
        self.playable_cards_list.append(48)

    def add_jacks(self):
        self.playable_cards_list.append(10)
        self.playable_cards_list.append(23)
        self.playable_cards_list.append(36)
        self.playable_cards_list.append(49)

    def add_queens(self):
        self.playable_cards_list.append(11)
        self.playable_cards_list.append(24)
        self.playable_cards_list.append(37)
        self.playable_cards_list.append(50)

    def add_kings(self):
        self.playable_cards_list.append(12)
        self.playable_cards_list.append(25)
        self.playable_cards_list.append(38)
        self.playable_cards_list.append(51)

    def add_aces(self):
        self.playable_cards_list.append(13)
        self.playable_cards_list.append(26)
        self.playable_cards_list.append(39)
        self.playable_cards_list.append(52)

    def playable_cards(self):
        # MAGIC
        # 2 on top
        self.playable_cards_list = []
        if self.card_on_top in [1, 14, 27, 40]:
            # resets the value of the pile
            self.add_twos()
            self.add_threes()
            self.add_fours()
            self.add_fives()
            self.add_sixes()
            self.add_sevens()
            self.add_eights()
            self.add_nines()
            self.add_tens()
            self.add_jacks()
            self.add_queens()
            self.add_kings()
            self.add_aces()

        # 3 on top
        elif self.card_on_top in [2, 15, 28, 41]:
            self.add_twos()
            self.add_threes()
            self.add_fours()
            self.add_fives()
            self.add_sixes()
            self.add_sevens()
            self.add_eights()
            self.add_nines()
            self.add_tens()
            self.add_jacks()
            self.add_queens()
            self.add_kings()
            self.add_aces()

        # 4 on top
        elif self.card_on_top in [3, 16, 29, 42]:
            self.add_twos()
            self.add_fours()
            self.add_fives()
            self.add_sixes()
            self.add_sevens()
            self.add_eights()
            self.add_nines()
            self.add_tens()
            self.add_jacks()
            self.add_queens()
            self.add_kings()
            self.add_aces()

        # 5 on top
        elif self.card_on_top in [4, 17, 30, 43]:
            self.add_twos()
            self.add_fives()
            self.add_sixes()
            self.add_sevens()
            self.add_eights()
            self.add_nines()
            self.add_tens()
            self.add_jacks()
            self.add_queens()
            self.add_kings()
            self.add_aces()

        # 6 on top
        elif self.card_on_top in [5, 18, 31, 44]:
            self.add_twos()
            self.add_sixes()
            self.add_sevens()
            self.add_eights()
            self.add_nines()
            self.add_tens()
            self.add_jacks()
            self.add_queens()
            self.add_kings()
            self.add_aces()

        # MAGIC
        # 7 on top
        elif self.card_on_top in [6, 19, 32, 45]:
            # next card played must be valued <= 7
            self.add_twos()
            self.add_threes()
            self.add_fours()
            self.add_fives()
            self.add_sixes()
            self.add_sevens()
            self.add_eights()
            self.add_tens()

        # MAGIC
        # 8 on top
        elif self.card_on_top in [7, 20, 33, 46]:
            # change value of card on top to card played before the 8

            # If an 8 comes out of the deck first, let any card be played
            if len(self.cards_in_middle) <= 1:
                card_under_8 = 1
            # Otherwise, get the value of the card underneath the 8, which is the second last index, hence -2
            else:
                card_under_8 = self.cards_in_middle[-2]
            if card_under_8 in [1, 14, 27, 40]:
                # resets the value of the pile
                self.add_twos()
                self.add_threes()
                self.add_fours()
                self.add_fives()
                self.add_sixes()
                self.add_sevens()
                self.add_eights()
                self.add_nines()
                self.add_tens()
                self.add_jacks()
                self.add_queens()
                self.add_kings()
                self.add_aces()

        # 3 on top
            elif card_under_8 in [2, 15, 28, 41]:
                self.add_twos()
                self.add_threes()
                self.add_fours()
                self.add_fives()
                self.add_sixes()
                self.add_sevens()
                self.add_eights()
                self.add_nines()
                self.add_tens()
                self.add_jacks()
                self.add_queens()
                self.add_kings()
                self.add_aces()

            elif card_under_8 in [3, 16, 29, 42]:
                self.add_twos()
                self.add_fours()
                self.add_fives()
                self.add_sixes()
                self.add_sevens()
                self.add_eights()
                self.add_nines()
                self.add_tens()
                self.add_jacks()
                self.add_queens()
                self.add_kings()
                self.add_aces()

        # 5 on top
            elif card_under_8 in [4, 17, 30, 43]:
                self.add_twos()
                self.add_fives()
                self.add_sixes()
                self.add_sevens()
                self.add_eights()
                self.add_nines()
                self.add_tens()
                self.add_jacks()
                self.add_queens()
                self.add_kings()
                self.add_aces()

            # 6 on top
            elif card_under_8 in [5, 18, 31, 44]:
                self.add_twos()
                self.add_sixes()
                self.add_sevens()
                self.add_eights()
                self.add_nines()
                self.add_tens()
                self.add_jacks()
                self.add_queens()
                self.add_kings()
                self.add_aces()

            # MAGIC
            # 7 on top
            elif card_under_8 in [6, 19, 32, 45]:
                # next card played must be valued <= 7
                self.add_twos()
                self.add_threes()
                self.add_fours()
                self.add_fives()
                self.add_sixes()
                self.add_sevens()
                self.add_eights()
                self.add_tens()

            # two eights on top of each other, let them play anything
            elif card_under_8 in [7, 20, 33, 46]:
                self.add_twos()
                self.add_threes()
                self.add_fours()
                self.add_fives()
                self.add_sixes()
                self.add_sevens()
                self.add_eights()
                self.add_nines()
                self.add_tens()
                self.add_jacks()
                self.add_queens()
                self.add_kings()
                self.add_aces()

            # 9
            elif card_under_8 in [8, 21, 34, 47]:
                self.add_twos()
                self.add_eights()
                self.add_nines()
                self.add_tens()
                self.add_jacks()
                self.add_queens()
                self.add_kings()
                self.add_aces()

            # 10 there will never be a 10 under an 8

            elif card_under_8 in [10, 23, 36, 49]:
                self.add_twos()
                self.add_eights()
                self.add_jacks()
                self.add_queens()
                self.add_kings()
                self.add_tens()
                self.add_aces()

            # Queen on top
            elif card_under_8 in [11, 24, 37, 50]:
                self.add_twos()
                self.add_eights()
                self.add_queens()
                self.add_kings()
                self.add_tens()
                self.add_aces()

            # King on top
            elif card_under_8 in [12, 25, 38, 51]:
                self.add_twos()
                self.add_eights()
                self.add_kings()
                self.add_tens()
                self.add_aces()

            # Ace on top
            elif card_under_8 in [13, 26, 39, 52]:
                self.add_twos()
                self.add_eights()
                self.add_tens()
                self.add_aces()

        # 9 on top
        elif self.card_on_top in [8, 21, 34, 47]:
            self.add_twos()
            self.add_eights()
            self.add_nines()
            self.add_tens()
            self.add_jacks()
            self.add_queens()
            self.add_kings()
            self.add_aces()

        # MAGIC
        # 10 on top
        elif self.card_on_top in [9, 22, 35, 48]:
            # discard the pile
            self.discarded_cards += self.cards_in_middle
            # reset the pile
            self.cards_in_middle = []
            # any card may be played
            self.add_twos()
            self.add_threes()
            self.add_fours()
            self.add_fives()
            self.add_sixes()
            self.add_sevens()
            self.add_eights()
            self.add_nines()
            self.add_tens()
            self.add_jacks()
            self.add_queens()
            self.add_kings()
            self.add_aces()

        # Jack on top
        elif self.card_on_top in [10, 23, 36, 49]:
            self.add_twos()
            self.add_eights()
            self.add_jacks()
            self.add_queens()
            self.add_kings()
            self.add_tens()
            self.add_aces()

        # Queen on top
        elif self.card_on_top in [11, 24, 37, 50]:
            self.add_twos()
            self.add_eights()
            self.add_queens()
            self.add_kings()
            self.add_tens()
            self.add_aces()

        # King on top
        elif self.card_on_top in [12, 25, 38, 51]:
            self.add_twos()
            self.add_eights()
            self.add_kings()
            self.add_tens()
            self.add_aces()

        # Ace on top
        elif self.card_on_top in [13, 26, 39, 52]:
            self.add_twos()
            self.add_eights()
            self.add_tens()
            self.add_aces()

        elif self.card_on_top == 0:
            self.add_twos()
            self.add_threes()
            self.add_fours()
            self.add_fives()
            self.add_sixes()
            self.add_sevens()
            self.add_eights()
            self.add_nines()
            self.add_tens()
            self.add_jacks()
            self.add_queens()
            self.add_kings()
            self.add_aces()

        self.playable_cards_list.sort()

    # Method run at game start
    def start_game(self, deck):
        # Choose a random card left in the deck
        card = random.choice(deck)
        # Ensures that the starting card is less than a 7
        while True:
            if card % 13 >= 6 or card % 13 == 0:
                card = random.choice(deck)
            else:
                break
        # Remove from the deck
        deck.remove(card)
        # Move onto the pile
        self.move_card(card)
        return deck

    # Method to move a card from somewhere to the pile
    def move_card(self, card):
        # The card given will be on top
        self.card_on_top = card
        # If it is not already in the list of cards that are in the middle, add it to that list
        if self.card_on_top not in self.cards_in_middle and self.card_on_top != 0:
            self.cards_in_middle.append(self.card_on_top)

