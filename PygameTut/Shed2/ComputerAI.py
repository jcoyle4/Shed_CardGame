import random


class Weights:

    def __init__(self):
        # Only need to track 2 and 8, as unable to play around these
        self.__magicCards = [1, 7, 14, 20, 27, 33, 40, 46]
        self.__Aces = [13, 26, 39, 52]
        self.__Kings = [12, 25, 38, 51]
        self.__Queens = [11, 24, 37, 50]
        self.__Jacks = [10, 23, 36, 49]
        self.__Tens = [9, 22, 35, 48]
        self.__Nines = [8, 21, 34, 47]
        self.__Eights = [7, 20, 33, 46]
        self.__Sevens = [6, 19, 32, 45]
        self.__Sixes = [5, 18, 31, 44]
        self.__Fives = [4, 17, 30, 43]
        self.__Fours = [3, 16, 29, 42]
        self.__Threes = [2, 15, 28, 41]
        self.__Twos = [1, 14, 27, 40]

        self.__total = 0
        self.__max_total = 25

    def calc_weight(self, card, known_cards, card_on_top):
        # card is the card that we are calculating the weight of
        # known cards are the cards that the computer knows the player has in their hand
        # card on top is the card currently on the top of the pile

        # get the weight based on the cards in the players hand, add this onto what ever card is on top
        weight = 0
        # Put into a single list, rather than a list of list, for ease or use later
        lst = [self.__Kings, self.__Queens, self.__Jacks, self.__Nines, self.__Sevens, self.__Sixes, self.__Fives, self.__Fours,
               self.__Threes]
        lst2 = []
        for x in lst:
            for y in x:
                lst2.append(y)

        # Determining the highest value card in known cards of the player
        for c in known_cards:
            # Cant play around magic cards or Aces, so return none to run the decision tree
            if c in self.__magicCards:
                return None

            elif c in self.__Aces:
                return None

            elif c in lst2:
                if card in self.__Aces:
                    weight = 11
                    break
                if card in self.__Kings:
                    weight = 10
                    break
                if card in self.__Queens:
                    weight = 9
                    break
                if card in self.__Jacks:
                    weight = 8
                    break
                if card in self.__Nines:
                    weight = 7
                    break
                if card in self.__Sevens:
                    weight = 6
                    break
                if card in self.__Sixes:
                    weight = 5
                    break
                if card in self.__Fives:
                    weight = 4
                    break
                if card in self.__Fours:
                    weight = 3
                    break
                if card in self.__Threes:
                    weight = 2
                    break
                if card in self.__Tens:
                    weight = 0.5
                    break
                if card in self.__Eights:
                    weight = 0.4
                    break
                if card in self.__Twos:
                    weight = 0.6
                    break

        # Add on the weight depending on the card on the top of the pile, with magic cards given a low weight
        if card_on_top in self.__Aces:
            if card in self.__Aces:
                weight += 1
            elif card in self.__Tens:
                weight += 0.05
            elif card in self.__Eights:
                weight += 0.05
            elif card in self.__Twos:
                weight += 0.1

        elif card_on_top in self.__Kings:
            if card in self.__Aces:
                weight += 0.9
            elif card in self.__Kings:
                weight += 1
            elif card in self.__Tens:
                weight += 0.05
            elif card in self.__Eights:
                weight += 0.05
            elif card in self.__Twos:
                weight += 0.1

        elif card_on_top in self.__Queens:
            if card in self.__Aces:
                weight += 0.8
            elif card in self.__Kings:
                weight += 0.9
            elif card in self.__Queens:
                weight += 1
            elif card in self.__Tens:
                weight += 0.05
            elif card in self.__Eights:
                weight += 0.05
            elif card in self.__Twos:
                weight += 0.1

        elif card_on_top in self.__Jacks:
            if card in self.__Aces:
                weight += 0.7
            elif card in self.__Kings:
                weight += 0.8
            elif card in self.__Queens:
                weight += 0.9
            elif card in self.__Jacks:
                weight += 1
            elif card in self.__Tens:
                weight += 0.05
            elif card in self.__Eights:
                weight += 0.05
            elif card in self.__Twos:
                weight += 0.1

        elif card_on_top in self.__Nines:
            if card in self.__Aces:
                weight += 0.6
            elif card in self.__Kings:
                weight += 0.7
            elif card in self.__Queens:
                weight += 0.8
            elif card in self.__Jacks:
                weight += 0.9
            elif card in self.__Nines:
                weight += 1
            elif card in self.__Tens:
                weight += 0.05
            elif card in self.__Eights:
                weight += 0.05
            elif card in self.__Twos:
                weight += 0.1

        elif card_on_top in self.__Sevens:
            if card in self.__Threes:
                weight += 11
            elif card in self.__Fours:
                weight += 10
            elif card in self.__Fives:
                weight += 9
            elif card in self.__Sixes:
                weight += 8
            elif card in self.__Sevens:
                weight += 7
            elif card in self.__Tens:
                weight += 0.05
            elif card in self.__Eights:
                weight += 0.05
            elif card in self.__Twos:
                weight += 0.1

        elif card_on_top in self.__Sixes:
            if card in self.__Aces:
                weight += 0.4
            elif card in self.__Kings:
                weight += 0.5
            elif card in self.__Queens:
                weight += 0.6
            elif card in self.__Jacks:
                weight += 0.7
            elif card in self.__Nines:
                weight += 0.8
            elif card in self.__Sevens:
                weight += 0.9
            elif card in self.__Sixes:
                weight += 1
            elif card in self.__Tens:
                weight += 0.05
            elif card in self.__Eights:
                weight += 0.05
            elif card in self.__Twos:
                weight += 0.1

        elif card_on_top in self.__Fives:
            if card in self.__Aces:
                weight += 0.3
            elif card in self.__Kings:
                weight += 0.4
            elif card in self.__Queens:
                weight += 0.5
            elif card in self.__Jacks:
                weight += 0.6
            elif card in self.__Nines:
                weight += 0.7
            elif card in self.__Sevens:
                weight += 0.8
            elif card in self.__Sixes:
                weight += 0.9
            elif card in self.__Fives:
                weight += 1
            elif card in self.__Tens:
                weight += 0.05
            elif card in self.__Eights:
                weight += 0.05
            elif card in self.__Twos:
                weight += 0.1

        elif card_on_top in self.__Fours:
            if card in self.__Aces:
                weight += 0.2
            elif card in self.__Kings:
                weight += 0.3
            elif card in self.__Queens:
                weight += 0.4
            elif card in self.__Jacks:
                weight += 0.5
            elif card in self.__Nines:
                weight += 0.6
            elif card in self.__Sevens:
                weight += 0.7
            elif card in self.__Sixes:
                weight += 0.8
            elif card in self.__Fives:
                weight += 0.9
            elif card in self.__Fours:
                weight += 1
            elif card in self.__Tens:
                weight += 0.05
            elif card in self.__Eights:
                weight += 0.05
            elif card in self.__Twos:
                weight += 0.1

        elif card_on_top in self.__Threes:
            if card in self.__Aces:
                weight += 0.1
            elif card in self.__Kings:
                weight += 0.2
            elif card in self.__Queens:
                weight += 0.3
            elif card in self.__Jacks:
                weight += 0.4
            elif card in self.__Nines:
                weight += 0.5
            elif card in self.__Sevens:
                weight += 0.6
            elif card in self.__Sixes:
                weight += 0.7
            elif card in self.__Fives:
                weight += 0.8
            elif card in self.__Fours:
                weight += 0.9
            elif card in self.__Threes:
                weight += 1
            elif card in self.__Tens:
                weight += 0.05
            elif card in self.__Eights:
                weight += 0.05
            elif card in self.__Twos:
                weight += 0.1

        # No Card on the top, get rid of the lowest value card in hand
        elif card_on_top == 0:
            if card in self.__Threes:
                weight += 12
            elif card in self.__Fours:
                weight += 10
            elif card in self.__Fives:
                weight += 8
            elif card in self.__Sixes:
                weight += 6
            elif card in self.__Sevens:
                weight += 4
            elif card in self.__Nines:
                weight += 2
            elif card in self.__Jacks:
                weight += 0
            elif card in self.__Queens:
                weight -= 2
            elif card in self.__Kings:
                weight -= 4
            elif card in self.__Aces:
                weight -= 6

        print("Weight =", weight)
        return weight

    def weighted_prioritized_running_sum(self,  playable_cards, known_cards, card_on_top):
        print("Running weighted_prioritized_running_sum")
        card_with_weight = {}

        if len(playable_cards) == 0:
            return None

        for card in playable_cards:
            card_with_weight[card] = self.calc_weight(card, known_cards, card_on_top)
            if card_with_weight[card] is None:
                return None  # return none to run the decision tree

        print("Card With Weight Dict =", card_with_weight)
        print("Total =", self.__total)
        print("Max Total =", self.__max_total)

        max_total_reached = False

        while True:
            highest_priority = max(card_with_weight, key=card_with_weight.get)  # gives me the card with the highest value

            if (self.__total + card_with_weight[highest_priority]) < self.__max_total:
                self.__total += card_with_weight[highest_priority]
                break
            else:
                print("MAX TOTAL REACHED")
                max_total_reached = True
                card_with_weight[highest_priority] = 0  # giving a 0 weight so skips it the next round, avoids deleting and error giving
                # del card_with_weight[highest_priority]

        print("Total before return =", self.__total)
        print("return from pwrs", highest_priority)

        if max_total_reached:
            self.__total = 0
            # max_total_reached = False

        return highest_priority


class ComputerAI:
    # class to hold logic for the computer players turn

    knownCards = None

    def __init__(self):
        self.knownCards = []
        self.weights = Weights()

    def play_a_card(self, hand, playable_cards, card_on_top):  # Playable cards is the same as middlePile.playable_cards_list
        # This method will return a card which I will then move to the top of the pile somewhere else

        if card_on_top in self.knownCards:
            self.knownCards.remove(card_on_top)

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

        if len(self.knownCards) != 0:
            the_play = self.weights.weighted_prioritized_running_sum(playable, self.knownCards, card_on_top)
            if the_play is None:
                the_play = ComputerAI.basic_decision_tree(playable_values)
        else:
            the_play = ComputerAI.basic_decision_tree(playable_values)

        return the_play

    @staticmethod
    def basic_decision_tree(playable_cards_decision_tree):
        print("Running decision tree")
        num_of_plays = len(playable_cards_decision_tree)
        magic_card_modulo = [1, 7, 9]
        playable_magic_cards = {}
        playable_normal_cards = {}

        if num_of_plays != 0:
            if num_of_plays == 1:
                return next(iter(playable_cards_decision_tree.keys()))  # Print the first key in the dictionary
            else:
                for card in playable_cards_decision_tree:
                    if playable_cards_decision_tree[card] in magic_card_modulo:
                        playable_magic_cards[card] = playable_cards_decision_tree[card]
                    else:
                        playable_normal_cards[card] = playable_cards_decision_tree[card]

                if len(playable_magic_cards) == 0:
                    the_play = min(playable_normal_cards, key=playable_normal_cards.get)
                    if playable_normal_cards[the_play] == 13:
                        playable_normal_cards[the_play] -= 13
                        the_play = min(playable_normal_cards, key=playable_normal_cards.get)

                    return the_play

                elif len(playable_magic_cards) != 0 and len(playable_normal_cards) == 0:
                    num_of_magic_cards = len(playable_magic_cards)

                    if num_of_magic_cards == 1:
                        return next(iter(playable_magic_cards.keys()))

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
# play x cards , only information gain of 50, that's how much the computer learns per move
#
# calc weighted priority of each card in hand, only limiting to one card, if more than one card, introduce truncation
# make an arbitrary threshold, keep track of the value of the weighted priority of the card that the computer plays
# when this threshold is hit, select the next card that does not cross this threshold
# then reset the threshold to 0 again
#
#
#
#
#
#
#
