import random


class Hand:

    hand = None

    def __init__(self):
        self.hand = []

    def setUp(self, deck):
        while len(self.hand) < 5:
            card = random.choice(deck)
            self.hand.append(card)
            deck.remove(card)

        return deck

    def drawACard(self, deck, cardPosition):
        if len(deck) == 0:
            card = random.choice(deck)
            deck.remove(card)
            for x in range(0, 15):
                if cardPosition == x:
                    self.hand[cardPosition] = card

        return deck

    def initialRejig(self):
        #Firstdraw = self.hand
        List_of_25 = [None] * 25

        List_of_25[11] = self.hand[2]
        List_of_25[12] = self.hand[3]
        List_of_25[10] = self.hand[1]
        List_of_25[13] = self.hand[4]
        List_of_25[9] = self.hand[0]

        self.hand = List_of_25
        # print("asjfb", List_of_25)

    def rejig(self):
        new_hand = [None] * 25
        new_hand2 = []

        for CARD in self.hand:
            if CARD is not None:
                new_hand2.append(CARD)
        new_hand2.sort()
        for card in new_hand2:
            if card is not None:
                if card not in new_hand and new_hand[11] is None:
                    new_hand[11] = card
                elif card not in new_hand and new_hand[12] is None:
                    new_hand[12] = card
                elif card not in new_hand and new_hand[10] is None:
                    new_hand[10] = card
                elif card not in new_hand and new_hand[13] is None:
                    new_hand[13] = card
                elif new_hand[9] != card and new_hand[9] is None:
                    new_hand[9] = card
                elif new_hand[14] != card and new_hand[14] is None:
                    new_hand[14] = card
                elif new_hand[8] != card and new_hand[8] is None:
                    new_hand[8] = card
                elif new_hand[15] != card and new_hand[15] is None:
                    new_hand[15] = card
                elif new_hand[7] != card and new_hand[7] is None:
                    new_hand[7] = card
                elif new_hand[16] != card and new_hand[16] is None:
                    new_hand[16] = card
                elif new_hand[6] != card and new_hand[6] is None:
                    new_hand[6] = card
                elif new_hand[17] != card and new_hand[17] is None:
                    new_hand[17] = card
                elif new_hand[5] != card and new_hand[5] is None:
                    new_hand[5] = card
                elif new_hand[18] != card and new_hand[18] is None:
                    new_hand[18] = card
                elif new_hand[4] != card and new_hand[4] is None:
                    new_hand[4] = card
                elif new_hand[19] != card and new_hand[19] is None:
                    new_hand[19] = card
                elif new_hand[3] != card and new_hand[3] is None:
                    new_hand[3] = card
                elif new_hand[20] != card and new_hand[20] is None:
                    new_hand[20] = card
                elif new_hand[21] != card and new_hand[21] is None:
                    new_hand[21] = card
                elif new_hand[2] != card and new_hand[2] is None:
                    new_hand[2] = card
                elif new_hand[22] != card and new_hand[22] is None:
                    new_hand[22] = card
                elif new_hand[1] != card and new_hand[1] is None:
                    new_hand[1] = card
                elif new_hand[23] != card and new_hand[23] is None:
                    new_hand[23] = card
                elif new_hand[0] != card and new_hand[0] is None:
                    new_hand[0] = card
                elif new_hand[24] != card and new_hand[24] is None:
                    new_hand[24] = card

        self.hand = new_hand

    #
    # @staticmethod
    # def flip(toFlip):
    #