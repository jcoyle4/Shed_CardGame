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

    # Method to set the starting total (Only for testing purposes)
    def set_total(self, number):
        self.__total = number

    # Method to set max total (Used in later iteration for difficulty purposes)
    def set_max_total(self, level):

        if level == 1:
            self.__max_total = 15
        if level == 2:
            self.__max_total = 25
        if level == 3:
            self.__max_total = 35

    def fill_beaten_by(self, card):
        beaten_by = []
        # If there is nothing on the top of the pile, make it seem as if there is a one, as everything should be allowed on it
        if card == 0:
            card = 1

        if card in self.__Aces:
            for x in self.__Aces:
                beaten_by.append(x)
            for x in self.__Tens:
                beaten_by.append(x)
            for x in self.__Eights:
                beaten_by.append(x)
            for x in self.__Twos:
                beaten_by.append(x)

        elif card in self.__Kings:
            for x in self.__Aces:
                beaten_by.append(x)
            for x in self.__Kings:
                beaten_by.append(x)
            for x in self.__Tens:
                beaten_by.append(x)
            for x in self.__Eights:
                beaten_by.append(x)
            for x in self.__Twos:
                beaten_by.append(x)

        elif card in self.__Queens:
            for x in self.__Aces:
                beaten_by.append(x)
            for x in self.__Kings:
                beaten_by.append(x)
            for x in self.__Queens:
                beaten_by.append(x)
            for x in self.__Tens:
                beaten_by.append(x)
            for x in self.__Eights:
                beaten_by.append(x)
            for x in self.__Twos:
                beaten_by.append(x)

        elif card in self.__Jacks:
            for x in self.__Aces:
                beaten_by.append(x)
            for x in self.__Kings:
                beaten_by.append(x)
            for x in self.__Queens:
                beaten_by.append(x)
            for x in self.__Jacks:
                beaten_by.append(x)
            for x in self.__Tens:
                beaten_by.append(x)
            for x in self.__Eights:
                beaten_by.append(x)
            for x in self.__Twos:
                beaten_by.append(x)

        elif card in self.__Tens:
            for x in self.__Aces:
                beaten_by.append(x)
            for x in self.__Kings:
                beaten_by.append(x)
            for x in self.__Queens:
                beaten_by.append(x)
            for x in self.__Jacks:
                beaten_by.append(x)
            for x in self.__Tens:
                beaten_by.append(x)
            for x in self.__Nines:
                beaten_by.append(x)
            for x in self.__Eights:
                beaten_by.append(x)
            for x in self.__Sevens:
                beaten_by.append(x)
            for x in self.__Sixes:
                beaten_by.append(x)
            for x in self.__Fives:
                beaten_by.append(x)
            for x in self.__Fours:
                beaten_by.append(x)
            for x in self.__Threes:
                beaten_by.append(x)
            for x in self.__Twos:
                beaten_by.append(x)

        elif card in self.__Nines:
            for x in self.__Aces:
                beaten_by.append(x)
            for x in self.__Kings:
                beaten_by.append(x)
            for x in self.__Queens:
                beaten_by.append(x)
            for x in self.__Jacks:
                beaten_by.append(x)
            for x in self.__Tens:
                beaten_by.append(x)
            for x in self.__Nines:
                beaten_by.append(x)
            for x in self.__Eights:
                beaten_by.append(x)
            for x in self.__Twos:
                beaten_by.append(x)

        elif card in self.__Eights:
            for x in self.__Aces:
                beaten_by.append(x)
            for x in self.__Kings:
                beaten_by.append(x)
            for x in self.__Queens:
                beaten_by.append(x)
            for x in self.__Jacks:
                beaten_by.append(x)
            for x in self.__Tens:
                beaten_by.append(x)
            for x in self.__Nines:
                beaten_by.append(x)
            for x in self.__Eights:
                beaten_by.append(x)
            for x in self.__Sevens:
                beaten_by.append(x)
            for x in self.__Sixes:
                beaten_by.append(x)
            for x in self.__Fives:
                beaten_by.append(x)
            for x in self.__Fours:
                beaten_by.append(x)
            for x in self.__Threes:
                beaten_by.append(x)
            for x in self.__Twos:
                beaten_by.append(x)

        elif card in self.__Sevens:
            for x in self.__Tens:
                beaten_by.append(x)
            for x in self.__Eights:
                beaten_by.append(x)
            for x in self.__Sevens:
                beaten_by.append(x)
            for x in self.__Sixes:
                beaten_by.append(x)
            for x in self.__Fives:
                beaten_by.append(x)
            for x in self.__Fours:
                beaten_by.append(x)
            for x in self.__Threes:
                beaten_by.append(x)
            for x in self.__Twos:
                beaten_by.append(x)

        elif card in self.__Sixes:
            for x in self.__Aces:
                beaten_by.append(x)
            for x in self.__Kings:
                beaten_by.append(x)
            for x in self.__Queens:
                beaten_by.append(x)
            for x in self.__Jacks:
                beaten_by.append(x)
            for x in self.__Tens:
                beaten_by.append(x)
            for x in self.__Nines:
                beaten_by.append(x)
            for x in self.__Eights:
                beaten_by.append(x)
            for x in self.__Sevens:
                beaten_by.append(x)
            for x in self.__Sixes:
                beaten_by.append(x)
            for x in self.__Twos:
                beaten_by.append(x)

        elif card in self.__Fives:
            for x in self.__Aces:
                beaten_by.append(x)
            for x in self.__Kings:
                beaten_by.append(x)
            for x in self.__Queens:
                beaten_by.append(x)
            for x in self.__Jacks:
                beaten_by.append(x)
            for x in self.__Tens:
                beaten_by.append(x)
            for x in self.__Nines:
                beaten_by.append(x)
            for x in self.__Eights:
                beaten_by.append(x)
            for x in self.__Sevens:
                beaten_by.append(x)
            for x in self.__Sixes:
                beaten_by.append(x)
            for x in self.__Fives:
                beaten_by.append(x)
            for x in self.__Twos:
                beaten_by.append(x)

        elif card in self.__Fours:
            for x in self.__Aces:
                beaten_by.append(x)
            for x in self.__Kings:
                beaten_by.append(x)
            for x in self.__Queens:
                beaten_by.append(x)
            for x in self.__Jacks:
                beaten_by.append(x)
            for x in self.__Tens:
                beaten_by.append(x)
            for x in self.__Nines:
                beaten_by.append(x)
            for x in self.__Eights:
                beaten_by.append(x)
            for x in self.__Sevens:
                beaten_by.append(x)
            for x in self.__Sixes:
                beaten_by.append(x)
            for x in self.__Fives:
                beaten_by.append(x)
            for x in self.__Fours:
                beaten_by.append(x)
            for x in self.__Twos:
                beaten_by.append(x)

        elif card in self.__Threes:
            for x in self.__Aces:
                beaten_by.append(x)
            for x in self.__Kings:
                beaten_by.append(x)
            for x in self.__Queens:
                beaten_by.append(x)
            for x in self.__Jacks:
                beaten_by.append(x)
            for x in self.__Tens:
                beaten_by.append(x)
            for x in self.__Nines:
                beaten_by.append(x)
            for x in self.__Eights:
                beaten_by.append(x)
            for x in self.__Sevens:
                beaten_by.append(x)
            for x in self.__Sixes:
                beaten_by.append(x)
            for x in self.__Fives:
                beaten_by.append(x)
            for x in self.__Fours:
                beaten_by.append(x)
            for x in self.__Threes:
                beaten_by.append(x)
            for x in self.__Twos:
                beaten_by.append(x)

        elif card in self.__Twos:
            for x in self.__Aces:
                beaten_by.append(x)
            for x in self.__Kings:
                beaten_by.append(x)
            for x in self.__Queens:
                beaten_by.append(x)
            for x in self.__Jacks:
                beaten_by.append(x)
            for x in self.__Tens:
                beaten_by.append(x)
            for x in self.__Nines:
                beaten_by.append(x)
            for x in self.__Eights:
                beaten_by.append(x)
            for x in self.__Sevens:
                beaten_by.append(x)
            for x in self.__Sixes:
                beaten_by.append(x)
            for x in self.__Fives:
                beaten_by.append(x)
            for x in self.__Fours:
                beaten_by.append(x)
            for x in self.__Threes:
                beaten_by.append(x)
            for x in self.__Twos:
                beaten_by.append(x)

        return beaten_by

    def calc_weight(self, card, known_cards, pile, comp_hand, length_of_player_hand, comp_table_cards, player_table_cards):
        # card is the card that we are calculating the weight of
        # known cards are the cards that the computer knows the player has in their hand
        # card on top is the card currently on the top of the pile

        max_length_of_deck = 52
        # The length of the deck minus any known cards
        cards_left = max_length_of_deck - len(comp_hand) - len(pile.cards_in_middle) - len(pile.discarded_cards)

        # list of cards that will beat the card handed in
        if card not in self.__Eights:
            beaten_by = self.fill_beaten_by(card)
        else:  # If an 8 is on top, look at the card beneath it
            beaten_by = self.fill_beaten_by(pile.card_on_top)

        # if some of the cards in the players hand are unknown
        if len(known_cards) != length_of_player_hand:
            # remove cards from the beaten by list that we know aren't available

            # Remove cards from the beaten by list if they are in the middle
            for b in pile.cards_in_middle:
                if b in beaten_by:
                    beaten_by.remove(b)

            # Remove cards from the beaten by list if they are in the computers hand
            for c in comp_hand:
                if c in beaten_by:
                    beaten_by.remove(c)

            # Remove cards from the beaten by list if they are in the discarded cards
            for d in pile.discarded_cards:
                if d in beaten_by:
                    beaten_by.remove(d)

            # Remove Table Cards
            for e in comp_table_cards:
                if e in beaten_by:
                    beaten_by.remove(e)

            for f in player_table_cards:
                if f in beaten_by:
                    beaten_by.remove(f)

            # If the player has a card that can beat the card in hand, give the card a 0 weight so the decision tree runs if all values 0
            # No point playing around something that you know will beat you
            if any(card in beaten_by for card in known_cards):
                weight = 0
            else:
                # Remove cards from the beaten by list if they are in the known cards, as need this to calc the correct odds (DO I??)
                for a in known_cards:
                    if a in beaten_by:
                        beaten_by.remove(a)

                num_of_better_cards = len(beaten_by)
                num_of_unknown_cards = length_of_player_hand - len(known_cards)

                cards_left -= (length_of_player_hand - num_of_unknown_cards)

                # Calculate the probability that the card will be beaten
                probability_to_beat = 1
                denominator = cards_left
                for x in range(num_of_unknown_cards):
                    probability_to_beat *= (num_of_better_cards/denominator)
                    denominator -= 1

                probability_to_not_beat = 1 - probability_to_beat

                # Cannot have Aces as the lowest value
                mod = (card % 13)
                if mod == 0:
                    mod = 13
                if mod in [1, 7, 9]:  # Give the magic cards low, but non-zero, probability to reduce priority in picking
                    weight = mod * (probability_to_not_beat/2)
                else:
                    weight = mod * probability_to_not_beat

        # Know all the cards in the players hand, so each card has a weight of its value, ensuring that the highest card will be played
        elif length_of_player_hand == len(known_cards):
            if all(card not in beaten_by for card in known_cards):
                weight = (card % 13)
                if weight == 0:
                    weight = 13
            # The cards cannot be beaten, return 0, if all are 0, it will just run the decision tree
            else:
                weight = 0

        return weight

    def weighted_prioritized_running_sum(self,  playable_cards, known_cards, pile, comp_hand, len_of_player_hand, comp_table_cards,
                                         player_table_cards):
        card_with_weight = {}

        if len(playable_cards) == 0:
            return None

        # If the player has an Ace, Two or Eight, return None to run the decision tree
        highest_value = [self.__Aces, self.__Twos, self.__Eights]

        for lst in highest_value:
            for x in lst:
                for y in known_cards:
                    if y == x:
                        return None

        for card in playable_cards:
            card_with_weight[card] = self.calc_weight(card, known_cards, pile, comp_hand, len_of_player_hand, comp_table_cards, player_table_cards)

        # If all weights returned 0 (not 0.0), return None to run the decision tree
        if all(value == 0 and type(value) == int for value in card_with_weight.values()):
            return None  # return none to run the decision tree

        max_total_reached = False

        while True:
            highest_priority = max(card_with_weight, key=card_with_weight.get)  # gives me the card with the highest value

            if (self.__total + card_with_weight[highest_priority]) < self.__max_total:
                self.__total += card_with_weight[highest_priority]
                break
            else:
                max_total_reached = True
                card_with_weight[highest_priority] *= -1  # giving a negative weight so skips it the next round, avoids deleting and error giving

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

    def play_a_card(self, hand, pile, length_of_player_hand, comp_table_cards, player_table_cards):  # Playable cards is the same as
        # middlePile.playable_cards_list
        # This method will return a card which I will then move to the top of the pile somewhere else

        if pile.card_on_top in self.knownCards and len(self.knownCards) != 0:
            self.knownCards.remove(pile.card_on_top)

        playable = []  # List of potential plays
        # Dictionary to store plays and their values, the card is the key and the value is the card % 13
        playable_values = {}

        for card in hand:
            if card in pile.playable_cards_list:
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
            the_play = self.weights.weighted_prioritized_running_sum(playable, self.knownCards, pile, hand, length_of_player_hand, comp_table_cards,
                                                                     player_table_cards)
            if the_play is None:
                the_play = ComputerAI.basic_decision_tree(playable_values)
        else:
            the_play = ComputerAI.basic_decision_tree(playable_values)

        return the_play

    @staticmethod
    def basic_decision_tree(playable_cards_decision_tree):
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
