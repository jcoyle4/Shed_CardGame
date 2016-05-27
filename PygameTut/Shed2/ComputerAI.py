import random


class ComputerAI:
    # class to hold logic for the computer players turn

    @staticmethod
    def play_a_card(hand, playable_cards):
        # This method will return a card which I will then move to the top of the pile somewhere else

        playable = []  # List of potential plays
        # Dictionary to store plays and their values, the card is the key and the value is the card % 13
        playable_values = {}

        for card in hand:
            if card in playable_cards:
                playable.append(card)

        # print("Full list of playable in Computer AI =", playable_cards)
        # print("Playable cards =", playable)

        # Basic AI, plays card with the lowest value, Aces high
        for potentialCard in range(len(playable)):
            a = playable[potentialCard] % 13
            if a == 0:  # need to add 13 to stop the computer playing an Ace when it shouldn't
                a += 13
            playable_values[playable[potentialCard]] = a

        return ComputerAI.basic_decision_tree(playable_values)
        # if len(playable_values) > 0:
        #     the_play = min(playable_values, key=playable_values.get)
        #     print(playable_values)
        #
        #     if the_play is not None:
        #         if playable_values[the_play] == 13:
        #             playable_values[the_play] -= 13
        #             the_play = min(playable_values, key=playable_values.get)
        #         return the_play
        #     elif the_play is None:
        #         return None
        # else:
        #     return None

    @staticmethod
    def basic_decision_tree(playable_cards):
        num_of_plays = len(playable_cards)
        magic_card_modulo = [1, 7, 9]
        playable_magic_cards = {}
        playable_normal_cards = {}

        if num_of_plays != 0:
            if num_of_plays == 1:
                return next(iter(playable_cards.values()))  # Print the first value in the dictionary
            else:
                for card in playable_cards:
                    if playable_cards[card] in magic_card_modulo:
                        playable_magic_cards[card] = playable_cards[card]
                    else:
                        playable_normal_cards[card] = playable_cards[card]

                if len(playable_magic_cards) == 0:
                    the_play = min(playable_normal_cards, key=playable_normal_cards.get)
                    if playable_normal_cards[the_play] == 13:
                        playable_normal_cards[the_play] -= 13
                        the_play = min(playable_normal_cards, key=playable_normal_cards.get)

                    return the_play

                elif len(playable_magic_cards) != 0 and len(playable_normal_cards) == 0:
                    num_of_magic_cards = len(playable_magic_cards)

                    if num_of_magic_cards == 1:
                        return next(iter(playable_magic_cards.values()))

                    else:
                        for key in playable_magic_cards:
                            # Play a 7 first
                            if playable_magic_cards[key] == 1:
                                return key
                            elif playable_magic_cards[key] == 7:
                                return key
                            elif playable_magic_cards[key] == 9:
                                return key

                elif len(playable_magic_cards) != 0 and len(playable_normal_cards) != 0:

                    the_play = min(playable_normal_cards, key=playable_normal_cards.get)

                    if playable_normal_cards[the_play] == 13:
                        playable_normal_cards[the_play] -= 13
                        the_play = min(playable_normal_cards, key=playable_normal_cards.get)

                    return the_play

        else:
            return None

    @staticmethod
    def play_face_down_card(face_down_cards):
        # need to avoid None
        list_of_cards_to_choose_from = []

        for card in face_down_cards:
            if card is not None:
                list_of_cards_to_choose_from.append(card)

        return random.choice(list_of_cards_to_choose_from)

""" Aaron notes on weighted truncated running sum"""
#
#
#
#
#
#
#
#
#
#
#
#
