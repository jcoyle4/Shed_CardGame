import random, pygame
import Render_Images


class ComputerAI:

    # class to hold logic for the computer players turn

    @staticmethod
    def play_a_card(hand, playable_cards):
        # This method will return a card which I will then move to the top of the pile somewhere else

        playable = []  # List of potential plays
        playable_values = {}
        the_play = None  # the card that will be played

        for card in hand:
            if card in playable_cards:
                playable.append(card)

        # print("Full list of playable in Computer AI =", playable_cards)
        # print("Playable cards =", playable)

        # Basic AI, plays card with the lowest value, Aces high
        print("The computer has", len(playable), "playable cards")
        for potentialCard in range(len(playable)):
            a = playable[potentialCard] % 13
            if a == 0:  # need to add 13 to stop the computer playing an Ace when it shouldn't
                a += 13
            playable_values[playable[potentialCard]] = a
        if len(playable_values) > 0:
            the_play = min(playable_values, key=playable_values.get)
            print(playable_values)

            if the_play is not None:
                if playable_values[the_play] == 13:
                    playable_values[the_play] -= 13
                    the_play = min(playable_values, key=playable_values.get)
                print("The computer is playing card number", the_play)
                return the_play
            elif the_play is None:
                print("The computer has no play..")
                return None
        else:
            print("The computer has no play..")
            return None






