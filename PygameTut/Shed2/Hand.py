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
