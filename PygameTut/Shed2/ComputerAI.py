import random, pygame
import BlitPlayerCards


class ComputerAI:

    # class to hold logic for the computer players turn

    @staticmethod
    def play_a_card(hand, playable_cards):
        # This method will return a card which I will then move to the top of the pile somewhere else

        playable = []  # List of potential plays
        the_play = None  # the card that will be played

        for card in hand:
            if card in playable_cards:
                playable.append(card)

        # print("Full list of playable in Computer AI =", playable_cards)
        # print("Playable cards =", playable)

        # Basic AI, plays card with the lowest value, Aces high
        for potentialCard in range(len(playable)):
            try:
                a = playable[potentialCard] % 13
                b = playable[potentialCard + 1] % 13
                if a < b and a != 0:
                    the_play = playable[potentialCard]
                elif a < b and a == 0:
                    the_play = playable[potentialCard + 1]
                elif a > b != 0:
                    the_play = playable[potentialCard + 1]
                elif a > b == 0:
                    the_play = playable[potentialCard]
                elif a == b:
                    ran_playable = [playable[potentialCard], playable[potentialCard + 1]]
                    the_play = random.choice(ran_playable)

            except IndexError:
                continue
            except ValueError:
                return None
            finally:
                # print("a", type(the_play))
                print("The computer is playing card", the_play)
                return the_play

    @staticmethod
    def animate_Play_Card(card, screen, card_sprites, FPSCLOCK, player_hand_sprites, phand, chand, back_of_card,
                          middle_pile, card_Sprites, cards, back_of_card_Rect, background, background_Rect, player):
        moveSpeed = 0.5

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


    # # Putting this here as I am not sure where to put it
    # @staticmethod
    # def animate_play_card_player(card, screen, card_sprites, FPSCLOCK, player_hand_sprites, phand, chand, back_of_card,
    #                              middle_pile, card_Sprites, cards, back_of_card_Rect, background, background_Rect):
    #
    #     movespeed = 0.5
    #     # Middle pile has position = 300, 255
    #     # Middle of Computer hand = 310, 550
    #     ENDY = 255
    #
    #     y = 550
    #     x = 300
    #
    #     while True:
    #         y -= movespeed
    #         if y == ENDY:
    #             return
    #
    #         screen.blit(background, background_Rect)
    #         BlitPlayerCards.BlitPlayer.blit_Cards(player_hand_sprites, phand, chand, back_of_card, screen, middle_pile,
    #                                               card_Sprites, cards, back_of_card_Rect)
    #         BlitPlayerCards.BlitPlayer.computer_card_move(card_sprites, card, x, y, screen)
    #
    #         pygame.display.update()
    #         FPSCLOCK.tick()




