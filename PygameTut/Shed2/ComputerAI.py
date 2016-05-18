import random, pygame
import BlitPlayerCards


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
                if the_play == 13:
                    the_play -= 13
                print("The computer is playing card number", the_play)
                return the_play
            elif the_play is None:
                print("The computer has no play..")
                return None
        else:
            print("The computer has no play..")
            return None

    @staticmethod
    def animate_Play_Card(card, screen, card_sprites, FPSCLOCK, player_hand_sprites, phand, chand, back_of_card,
                          middle_pile, card_Sprites, cards, back_of_card_Rect, background, background_Rect, player):
        moveSpeed = 1

        # Middle pile has position = 300, 255
        # Middle of Computer hand = 310, 5

        if not player:
            y = 5
        else:
            y = 550

        x = 300     # not exactly middle of pile but makes moving easier

        ENDY = 255

        while True:
            if not player:
                y += moveSpeed
            else:
                y -= moveSpeed
            if y == ENDY:
                return

            # the following two functions let the other images render so the moving images do not leave black lines
            screen.blit(background, background_Rect)
            BlitPlayerCards.BlitPlayer.blit_Cards(player_hand_sprites, phand, chand, back_of_card, screen, middle_pile,
                                                  card_Sprites, cards, back_of_card_Rect)
            BlitPlayerCards.BlitPlayer.computer_card_move(card_sprites, card, x, y, screen)

            pygame.display.update()
            FPSCLOCK.tick()




