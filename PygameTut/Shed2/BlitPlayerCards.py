import pygame

#TRANSPARANT = (0, 0, 0)

class BlitPlayer:

    @staticmethod
    def gen_player_blit_cards(player_hand, deck_card_sprites, deck_card_hl_sprites, player_sprites,
                              c1, c2, c3, c4, c5, transcard, used1, used2, used3, used4, used5):
        global card1
        global card2
        global card3
        global card4
        global card5

        if len(player_hand) >= 1:

            for x in range(1, 53):

                if player_hand[0] == x:  # sees if a card has been clicked with the mouse. If so,
                    #  and if that card is "playable", the card in highlighted
                    if c1 == 1:
                        card1 = deck_card_sprites[x-1]

                    else:
                        card1 = deck_card_hl_sprites[x-1]

                if player_hand[0] is None:
                            card1 = transcard

                if len(player_hand) >= 2:
                    if player_hand[1] == x:
                        if c2 == 1:
                            card2 = deck_card_sprites[x-1]

                        else:
                            card2 = deck_card_hl_sprites[x-1]

                    if player_hand[1] is None:
                            card2 = transcard

                    if len(player_hand) >= 3:
                        if player_hand[2] == x:
                            if c3 == 1:
                                card3 = deck_card_sprites[x-1]
                            else:
                                card3 = deck_card_hl_sprites[x-1]

                        if player_hand[2] is None:
                            card3 = transcard

                        if len(player_hand) >= 4:
                            if player_hand[3] == x:
                                if c4 == 1:
                                    card4 = deck_card_sprites[x-1]
                                else:
                                    card4 = deck_card_hl_sprites[x-1]

                            if player_hand[3] is None:
                                card4 = transcard

                            if len(player_hand) >= 5:
                                if player_hand[4] == x:
                                    if c5 == 1:
                                        card5 = deck_card_sprites[x-1]
                                    else:
                                        card5 = deck_card_hl_sprites[x-1]

                                if player_hand[4] is None:
                                    card5 = transcard

        return card1, card2, card3, card4, card5

    @staticmethod
    def blit_Cards(player_hand_sprites, player_hand, computer_hand, back_of_card, screen, pile, card_sprites, deck, backRect):

        width = backRect.w
        height = backRect.h

        """ CODE TO GET TRANSPARANT IMAGES"""

        TRANSPARANT = pygame.Surface((width, height), pygame.SRCALPHA)
        TRANSPARANT.set_alpha(0)
        TRANSPARANT.fill((255, 255, 255, 0))

        """"""

        SEMI_TRANSPARANT = pygame.Surface((width, height), pygame.SRCALPHA)
        SEMI_TRANSPARANT.set_alpha(2)
        SEMI_TRANSPARANT.fill((255, 255, 255, 2))

        """"""

        if len(computer_hand) == 5:  # if there are 5 cards in this computers hand, blit that many "back of cards"

            screen.blit(back_of_card, (230, 5))
            screen.blit(back_of_card, (270, 5))
            screen.blit(back_of_card, (310, 5))
            screen.blit(back_of_card, (350, 5))
            screen.blit(back_of_card, (390, 5))

        if len(computer_hand) == 4:

            screen.blit(back_of_card, (230, 5))
            screen.blit(back_of_card, (270, 5))
            screen.blit(back_of_card, (310, 5))
            screen.blit(back_of_card, (350, 5))

        if len(computer_hand) == 3:

            screen.blit(back_of_card, (230, 5))
            screen.blit(back_of_card, (270, 5))
            screen.blit(back_of_card, (310, 5))

        if len(computer_hand) == 2:

            screen.blit(back_of_card, (230, 5))
            screen.blit(back_of_card, (270, 5))

        if len(computer_hand) == 1:

            screen.blit(back_of_card, (230, 5))

        if len(player_hand) == 5:
        #   may only need to do this once as there will be transparent cards
            screen.blit(player_hand_sprites[0], (230, 550))
            screen.blit(player_hand_sprites[1], (270, 550))
            screen.blit(player_hand_sprites[2], (310, 550))
            screen.blit(player_hand_sprites[3], (350, 550))
            screen.blit(player_hand_sprites[4], (390, 550))

        if len(player_hand) == 4:

            screen.blit(player_hand_sprites[0], (230, 550))
            screen.blit(player_hand_sprites[1], (270, 550))
            screen.blit(player_hand_sprites[2], (310, 550))
            screen.blit(player_hand_sprites[3], (350, 550))

        if len(player_hand) == 3:

            screen.blit(player_hand_sprites[0], (230, 550))
            screen.blit(player_hand_sprites[1], (270, 550))
            screen.blit(player_hand_sprites[2], (310, 550))

        if len(player_hand) == 2:

            screen.blit(player_hand_sprites[0], (230, 550))
            screen.blit(player_hand_sprites[1], (270, 550))

        if len(player_hand) == 1:

            screen.blit(player_hand_sprites[0], (230, 550))

        #card_in_middle = 0
        eights = [7, 20, 33, 46]
        for x in range(1, 53):
            card_under_eight = []
            # if len(pile.cards_in_middle) == 0 and pile.card_on_top is None:
            if len(pile.cards_in_middle) == 0:
                screen.blit(SEMI_TRANSPARANT, (300, 255))
            elif pile.card_on_top == x and pile.card_on_top in eights:
                card_under_eight = pile.cards_in_middle[-1:]
                print("CARD ON TOP =", pile.card_on_top)
                print("CARD UNDER THE 8 =", card_under_eight[0])
                card_under_eight_sprite = card_sprites[card_under_eight[0] - 1]
                screen.blit(card_under_eight_sprite, (300, 255))
                transparent_copy_eight = card_sprites[x-1].copy()
                transparent_copy_eight.set_alpha(100)
                # transparent_copy_eight.fill((255, 255, 255, 2), None, pygame.BLEND_RGBA_MULT)
                screen.blit(transparent_copy_eight, (325, 255))
            elif pile.card_on_top == x:
                card_in_middle = card_sprites[x-1]

                screen.blit(card_in_middle, (300, 255))
                break


        if len(deck) == 1:
            screen.blit(back_of_card, (500, 255))
        elif len(deck) == 2:
            screen.blit(back_of_card, (500, 255))
            screen.blit(back_of_card, (505, 255))
        elif len(deck) == 3:
            screen.blit(back_of_card, (500, 255))
            screen.blit(back_of_card, (505, 255))
            screen.blit(back_of_card, (510, 255))
        elif len(deck) == 4:
            screen.blit(back_of_card, (500, 255))
            screen.blit(back_of_card, (505, 255))
            screen.blit(back_of_card, (510, 255))
            screen.blit(back_of_card, (515, 255))
        elif len(deck) >= 5:
            screen.blit(back_of_card, (500, 255))
            screen.blit(back_of_card, (505, 255))
            screen.blit(back_of_card, (510, 255))
            screen.blit(back_of_card, (515, 255))
            screen.blit(back_of_card, (520, 255))

    @staticmethod
    def computer_card_move(card_sprites, card, x, y, screen):
        for cardInDeck in range(1, 53):
            if card == cardInDeck:
                card = card_sprites[cardInDeck-1]

                screen.blit(card, (x, y))


