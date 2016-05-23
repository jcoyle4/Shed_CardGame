import random


class HandClass:

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
        list_of_25 = [None] * 25

        list_of_25[11] = self.hand[2]
        list_of_25[12] = self.hand[3]
        list_of_25[10] = self.hand[1]
        list_of_25[13] = self.hand[4]
        list_of_25[9] = self.hand[0]

        self.hand = list_of_25

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


    @staticmethod
    def flipC(C_To_Flip):

        if C_To_Flip == 1:
            C_To_Flip = 0

        return C_To_Flip

    @staticmethod
    def unflipAll(cList):

         for x in range(len(cList)):
            cList[x] = 1

         return cList

    def pickUp(self, pile, player):

        if not player:
            self.hand.extend(pile.cards_in_middle)
            # pile.cards_in_middle = []
            # pile.card_on_top = 0

        else:
            for card_in_hand in range(len(self.hand)):
                for card_in_pile in range(len(pile.cards_in_middle)):
                    if self.hand[card_in_hand] is None and pile.cards_in_middle[card_in_pile] not in self.hand:
                        self.hand[card_in_hand] = pile.cards_in_middle[card_in_pile]
            self.rejig()

        pile.cards_in_middle = []
        pile.card_on_top = 0

        return pile
