import random


# Class to store data and functionality for the table cards
class TableCardsClass:

    face_down = None
    face_up = None

    def __init__(self):
        self.face_down = []
        self.face_up = []

    # Draw the card from the deck
    def setup(self, deck):
        deck = self.draw_face_up(deck)
        deck = self.draw_face_down(deck)

        return deck

    def draw_face_up(self, deck):

        while len(self.face_up) < 3:
            card = random.choice(deck)
            self.face_up.append(card)
            deck.remove(card)

        return deck

    def draw_face_down(self, deck):

        while len(self.face_down) < 3:
            card = random.choice(deck)
            self.face_down.append(card)
            deck.remove(card)

        return deck

    # Method used by the player when playing their face down cards
    def play_face_down_card(self, index, hand, pile):

        pile.move_card(self.face_down[index])

        if self.face_down[index] not in pile.playable_cards_list:

            pile = hand.pick_up(pile, True)

        self.face_down[index] = None

        return [hand, pile]
