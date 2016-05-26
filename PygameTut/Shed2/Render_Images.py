import pygame
import Load_Image


class BlitPlayer:

    @staticmethod
    def gen_face_up_table_cards(player_face_up, comp_face_up, list_of_c, deck_card_sprites, deck_card_hl_sprites, transcard):

        c1 = list_of_c[0]
        c2 = list_of_c[1]
        c3 = list_of_c[2]

        for x in range(1, 53):
            if player_face_up[0] == x:  # sees if a card has been clicked with the mouse. If so,
                #  and if that card is "playable", the card in highlighted
                if c1 == 1:
                    card1 = deck_card_sprites[x-1]

                else:
                    card1 = deck_card_hl_sprites[x-1]

            elif player_face_up[0] is None:
                card1 = transcard

            if player_face_up[1] == x:  # sees if a card has been clicked with the mouse. If so,
                #  and if that card is "playable", the card in highlighted
                if c2 == 1:
                    card2 = deck_card_sprites[x-1]

                else:
                    card2 = deck_card_hl_sprites[x-1]

            elif player_face_up[1] is None:
                card2 = transcard

            if player_face_up[2] == x:  # sees if a card has been clicked with the mouse. If so,
                #  and if that card is "playable", the card in highlighted
                if c3 == 1:
                    card3 = deck_card_sprites[x-1]

                else:
                    card3 = deck_card_hl_sprites[x-1]

            elif player_face_up[2] is None:
                card3 = transcard

            if comp_face_up[0] == x:
                comp_card1 = deck_card_sprites[x-1]

            elif comp_face_up[0] is None:
                comp_card1 = transcard

            if comp_face_up[1] == x:
                comp_card2 = deck_card_sprites[x-1]

            elif comp_face_up[1] is None:
                comp_card2 = transcard

            if comp_face_up[2] == x:
                comp_card3 = deck_card_sprites[x-1]

            elif comp_face_up[2] is None:
                comp_card3 = transcard

        return [[card1, card2, card3], [comp_card1, comp_card2, comp_card3]]

    @staticmethod
    def gen_player_blit_cards(player_hand, deck_card_sprites, deck_card_hl_sprites, list_of_c, transcard):

        c1 = list_of_c[0]
        c2 = list_of_c[1]
        c3 = list_of_c[2]
        c4 = list_of_c[3]
        c5 = list_of_c[4]
        c6 = list_of_c[5]
        c7 = list_of_c[6]
        c8 = list_of_c[7]
        c9 = list_of_c[8]
        c10 = list_of_c[9]
        c11 = list_of_c[10]
        c12 = list_of_c[11]
        c13 = list_of_c[12]
        c14 = list_of_c[13]
        c15 = list_of_c[14]
        c16 = list_of_c[15]
        c17 = list_of_c[16]
        c18 = list_of_c[17]
        c19 = list_of_c[18]
        c20 = list_of_c[19]
        c21 = list_of_c[20]
        c22 = list_of_c[21]
        c23 = list_of_c[22]
        c24 = list_of_c[23]
        c25 = list_of_c[24]

        for x in range(1, 53):

            if player_hand[0] == x:  # sees if a card has been clicked with the mouse. If so,
                #  and if that card is "playable", the card in highlighted
                if c1 == 1:
                    card1 = deck_card_sprites[x-1]

                else:
                    card1 = deck_card_hl_sprites[x-1]

            elif player_hand[0] is None:
                card1 = transcard

            if player_hand[1] == x:
                if c2 == 1:
                    card2 = deck_card_sprites[x-1]

                else:
                    card2 = deck_card_hl_sprites[x-1]

            elif player_hand[1] is None:
                card2 = transcard

            if player_hand[2] == x:
                if c3 == 1:
                    card3 = deck_card_sprites[x-1]
                else:
                    card3 = deck_card_hl_sprites[x-1]

            elif player_hand[2] is None:
                card3 = transcard

            if player_hand[3] == x:
                if c4 == 1:
                    card4 = deck_card_sprites[x-1]
                else:
                    card4 = deck_card_hl_sprites[x-1]

            elif player_hand[3] is None:
                card4 = transcard

            if player_hand[4] == x:
                if c5 == 1:
                    card5 = deck_card_sprites[x-1]
                else:
                    card5 = deck_card_hl_sprites[x-1]

            elif player_hand[4] is None:
                card5 = transcard

            if player_hand[5] == x:
                if c6 == 1:
                    card6 = deck_card_sprites[x-1]
                else:
                    card6 = deck_card_hl_sprites[x-1]

            elif player_hand[5] is None:
                card6 = transcard

            if player_hand[6] == x:
                if c7 == 1:
                    card7 = deck_card_sprites[x-1]
                else:
                    card7 = deck_card_hl_sprites[x-1]

            elif player_hand[6] is None:
                card7 = transcard

            if player_hand[7] == x:
                if c8 == 1:
                    card8 = deck_card_sprites[x-1]
                else:
                    card8 = deck_card_hl_sprites[x-1]

            elif player_hand[7] is None:
                card8 = transcard

            if player_hand[8] == x:
                if c9 == 1:
                    card9 = deck_card_sprites[x-1]
                else:
                    card9 = deck_card_hl_sprites[x-1]

            elif player_hand[8] is None:
                card9 = transcard

            if player_hand[9] == x:
                if c10 == 1:
                    card10 = deck_card_sprites[x-1]
                else:
                    card10 = deck_card_hl_sprites[x-1]

            elif player_hand[9] is None:
                card10 = transcard

            if player_hand[10] == x:
                if c11 == 1:
                    card11 = deck_card_sprites[x-1]
                else:
                    card11 = deck_card_hl_sprites[x-1]

            elif player_hand[10] is None:
                card11 = transcard

            if player_hand[11] == x:
                if c12 == 1:
                    card12 = deck_card_sprites[x-1]
                else:
                    card12 = deck_card_hl_sprites[x-1]

            elif player_hand[11] is None:
                card12 = transcard

            if player_hand[12] == x:
                if c13 == 1:
                    card13 = deck_card_sprites[x-1]
                else:
                    card13 = deck_card_hl_sprites[x-1]

            elif player_hand[12] is None:
                card13 = transcard

            if player_hand[13] == x:
                if c14 == 1:
                    card14 = deck_card_sprites[x-1]
                else:
                    card14 = deck_card_hl_sprites[x-1]

            elif player_hand[13] is None:
                card14 = transcard

            if player_hand[14] == x:
                if c15 == 1:
                    card15 = deck_card_sprites[x-1]
                else:
                    card15 = deck_card_hl_sprites[x-1]

            elif player_hand[14] is None:
                card15 = transcard

            if player_hand[15] == x:
                if c16 == 1:
                    card16 = deck_card_sprites[x-1]
                else:
                    card16 = deck_card_hl_sprites[x-1]

            elif player_hand[15] is None:
                card16 = transcard

            if player_hand[16] == x:
                if c17 == 1:
                    card17 = deck_card_sprites[x-1]
                else:
                    card17 = deck_card_hl_sprites[x-1]

            elif player_hand[16] is None:
                card17 = transcard

            if player_hand[17] == x:
                if c18 == 1:
                    card18 = deck_card_sprites[x-1]
                else:
                    card18 = deck_card_hl_sprites[x-1]

            elif player_hand[17] is None:
                card18 = transcard

            if player_hand[18] == x:
                if c19 == 1:
                    card19 = deck_card_sprites[x-1]
                else:
                    card19 = deck_card_hl_sprites[x-1]

            elif player_hand[18] is None:
                card19 = transcard

            if player_hand[19] == x:
                if c20 == 1:
                    card20 = deck_card_sprites[x-1]
                else:
                    card20 = deck_card_hl_sprites[x-1]

            elif player_hand[19] is None:
                card20 = transcard

            if player_hand[20] == x:
                if c21 == 1:
                    card21 = deck_card_sprites[x-1]
                else:
                    card21 = deck_card_hl_sprites[x-1]

            elif player_hand[20] is None:
                card21 = transcard

            if player_hand[21] == x:
                if c22 == 1:
                    card22 = deck_card_sprites[x-1]
                else:
                    card22 = deck_card_hl_sprites[x-1]

            elif player_hand[21] is None:
                card22 = transcard

            if player_hand[22] == x:
                if c23 == 1:
                    card23 = deck_card_sprites[x-1]
                else:
                    card23 = deck_card_hl_sprites[x-1]

            elif player_hand[22] is None:
                card23 = transcard

            if player_hand[23] == x:
                if c24 == 1:
                    card24 = deck_card_sprites[x-1]
                else:
                    card24 = deck_card_hl_sprites[x-1]

            elif player_hand[23] is None:
                card24 = transcard

            if player_hand[24] == x:
                if c25 == 1:
                    card25 = deck_card_sprites[x-1]
                else:
                    card25 = deck_card_hl_sprites[x-1]

            elif player_hand[24] is None:
                card25 = transcard

        return [card1, card2, card3, card4, card5, card6, card7, card8, card9, card10, card11, card12, card13, card14, card15, card16,
                card17, card18, card19, card20, card21, card22, card23, card24, card25]

    @staticmethod
    def blit_cards(player_hand_sprites, player_hand, computer_hand, back_of_card, screen, pile, card_sprites, deck, backrect, turn,
                   player_table_sprites, comp_table_sprites, player_face_down, comp_face_down):

        width = backrect.w
        height = backrect.h

        """ CODE TO GET TRANSPARENT IMAGES"""

        transparent = pygame.Surface((width, height), pygame.SRCALPHA)
        transparent.set_alpha(0)
        transparent.fill((255, 255, 255, 0))

        """"""

        semi_transparent = pygame.Surface((width, height), pygame.SRCALPHA)
        semi_transparent.set_alpha(2)
        semi_transparent.fill((255, 255, 255, 2))

        """"""
        # Region for computer cards 1 -> 25
        if len(computer_hand) == 1:     # if there are 5 cards in this computers hand, blit that many "back of cards"

            screen.blit(back_of_card, (230, 5))

        elif len(computer_hand) == 2:

            screen.blit(back_of_card, (230, 5))
            screen.blit(back_of_card, (270, 5))

        elif len(computer_hand) == 3:

            screen.blit(back_of_card, (230, 5))
            screen.blit(back_of_card, (270, 5))
            screen.blit(back_of_card, (310, 5))

        elif len(computer_hand) == 4:

            screen.blit(back_of_card, (230, 5))
            screen.blit(back_of_card, (270, 5))
            screen.blit(back_of_card, (310, 5))
            screen.blit(back_of_card, (350, 5))

        elif len(computer_hand) == 5:

            screen.blit(back_of_card, (230, 5))
            screen.blit(back_of_card, (270, 5))
            screen.blit(back_of_card, (310, 5))
            screen.blit(back_of_card, (350, 5))
            screen.blit(back_of_card, (390, 5))

        elif len(computer_hand) == 6:
            screen.blit(back_of_card, (190, 5))
            screen.blit(back_of_card, (230, 5))
            screen.blit(back_of_card, (270, 5))
            screen.blit(back_of_card, (310, 5))
            screen.blit(back_of_card, (350, 5))
            screen.blit(back_of_card, (390, 5))

        elif len(computer_hand) == 7:
            screen.blit(back_of_card, (190, 5))
            screen.blit(back_of_card, (230, 5))
            screen.blit(back_of_card, (270, 5))
            screen.blit(back_of_card, (310, 5))
            screen.blit(back_of_card, (350, 5))
            screen.blit(back_of_card, (390, 5))
            screen.blit(back_of_card, (430, 5))

        elif len(computer_hand) == 8:
            screen.blit(back_of_card, (190, 5))
            screen.blit(back_of_card, (220, 5))
            screen.blit(back_of_card, (250, 5))
            screen.blit(back_of_card, (280, 5))
            screen.blit(back_of_card, (310, 5))
            screen.blit(back_of_card, (340, 5))
            screen.blit(back_of_card, (370, 5))
            screen.blit(back_of_card, (400, 5))

        elif len(computer_hand) == 9:
            screen.blit(back_of_card, (190, 5))
            screen.blit(back_of_card, (220, 5))
            screen.blit(back_of_card, (250, 5))
            screen.blit(back_of_card, (280, 5))
            screen.blit(back_of_card, (310, 5))
            screen.blit(back_of_card, (340, 5))
            screen.blit(back_of_card, (370, 5))
            screen.blit(back_of_card, (400, 5))
            screen.blit(back_of_card, (430, 5))

        elif len(computer_hand) == 10:
            screen.blit(back_of_card, (160, 5))
            screen.blit(back_of_card, (190, 5))
            screen.blit(back_of_card, (220, 5))
            screen.blit(back_of_card, (250, 5))
            screen.blit(back_of_card, (280, 5))
            screen.blit(back_of_card, (310, 5))
            screen.blit(back_of_card, (340, 5))
            screen.blit(back_of_card, (370, 5))
            screen.blit(back_of_card, (400, 5))
            screen.blit(back_of_card, (430, 5))

        elif len(computer_hand) == 11:
            screen.blit(back_of_card, (190, 5))
            screen.blit(back_of_card, (210, 5))
            screen.blit(back_of_card, (230, 5))
            screen.blit(back_of_card, (250, 5))
            screen.blit(back_of_card, (270, 5))
            screen.blit(back_of_card, (290, 5))
            screen.blit(back_of_card, (310, 5))
            screen.blit(back_of_card, (330, 5))
            screen.blit(back_of_card, (350, 5))
            screen.blit(back_of_card, (370, 5))
            screen.blit(back_of_card, (390, 5))

        elif len(computer_hand) == 12:
            screen.blit(back_of_card, (190, 5))
            screen.blit(back_of_card, (210, 5))
            screen.blit(back_of_card, (230, 5))
            screen.blit(back_of_card, (250, 5))
            screen.blit(back_of_card, (270, 5))
            screen.blit(back_of_card, (290, 5))
            screen.blit(back_of_card, (310, 5))
            screen.blit(back_of_card, (330, 5))
            screen.blit(back_of_card, (350, 5))
            screen.blit(back_of_card, (370, 5))
            screen.blit(back_of_card, (390, 5))
            screen.blit(back_of_card, (410, 5))

        elif len(computer_hand) == 13:
            screen.blit(back_of_card, (190, 5))
            screen.blit(back_of_card, (210, 5))
            screen.blit(back_of_card, (230, 5))
            screen.blit(back_of_card, (250, 5))
            screen.blit(back_of_card, (270, 5))
            screen.blit(back_of_card, (290, 5))
            screen.blit(back_of_card, (310, 5))
            screen.blit(back_of_card, (330, 5))
            screen.blit(back_of_card, (350, 5))
            screen.blit(back_of_card, (370, 5))
            screen.blit(back_of_card, (390, 5))
            screen.blit(back_of_card, (410, 5))
            screen.blit(back_of_card, (430, 5))

        elif len(computer_hand) == 14:
            screen.blit(back_of_card, (200, 5))
            screen.blit(back_of_card, (210, 5))
            screen.blit(back_of_card, (220, 5))
            screen.blit(back_of_card, (230, 5))
            screen.blit(back_of_card, (240, 5))
            screen.blit(back_of_card, (250, 5))
            screen.blit(back_of_card, (260, 5))
            screen.blit(back_of_card, (270, 5))
            screen.blit(back_of_card, (280, 5))
            screen.blit(back_of_card, (290, 5))
            screen.blit(back_of_card, (300, 5))
            screen.blit(back_of_card, (310, 5))
            screen.blit(back_of_card, (320, 5))
            screen.blit(back_of_card, (330, 5))

        elif len(computer_hand) == 15:
            screen.blit(back_of_card, (200, 5))
            screen.blit(back_of_card, (210, 5))
            screen.blit(back_of_card, (220, 5))
            screen.blit(back_of_card, (230, 5))
            screen.blit(back_of_card, (240, 5))
            screen.blit(back_of_card, (250, 5))
            screen.blit(back_of_card, (260, 5))
            screen.blit(back_of_card, (270, 5))
            screen.blit(back_of_card, (280, 5))
            screen.blit(back_of_card, (290, 5))
            screen.blit(back_of_card, (300, 5))
            screen.blit(back_of_card, (310, 5))
            screen.blit(back_of_card, (320, 5))
            screen.blit(back_of_card, (330, 5))
            screen.blit(back_of_card, (340, 5))

        elif len(computer_hand) == 16:
            screen.blit(back_of_card, (210, 5))
            screen.blit(back_of_card, (220, 5))
            screen.blit(back_of_card, (230, 5))
            screen.blit(back_of_card, (240, 5))
            screen.blit(back_of_card, (250, 5))
            screen.blit(back_of_card, (260, 5))
            screen.blit(back_of_card, (270, 5))
            screen.blit(back_of_card, (280, 5))
            screen.blit(back_of_card, (290, 5))
            screen.blit(back_of_card, (300, 5))
            screen.blit(back_of_card, (310, 5))
            screen.blit(back_of_card, (320, 5))
            screen.blit(back_of_card, (330, 5))
            screen.blit(back_of_card, (340, 5))
            screen.blit(back_of_card, (350, 5))
            screen.blit(back_of_card, (360, 5))

        elif len(computer_hand) == 17:
            screen.blit(back_of_card, (210, 5))
            screen.blit(back_of_card, (220, 5))
            screen.blit(back_of_card, (230, 5))
            screen.blit(back_of_card, (240, 5))
            screen.blit(back_of_card, (250, 5))
            screen.blit(back_of_card, (260, 5))
            screen.blit(back_of_card, (270, 5))
            screen.blit(back_of_card, (280, 5))
            screen.blit(back_of_card, (290, 5))
            screen.blit(back_of_card, (300, 5))
            screen.blit(back_of_card, (310, 5))
            screen.blit(back_of_card, (320, 5))
            screen.blit(back_of_card, (330, 5))
            screen.blit(back_of_card, (340, 5))
            screen.blit(back_of_card, (350, 5))
            screen.blit(back_of_card, (360, 5))
            screen.blit(back_of_card, (370, 5))

        elif len(computer_hand) == 18:
            screen.blit(back_of_card, (210, 5))
            screen.blit(back_of_card, (220, 5))
            screen.blit(back_of_card, (230, 5))
            screen.blit(back_of_card, (240, 5))
            screen.blit(back_of_card, (250, 5))
            screen.blit(back_of_card, (260, 5))
            screen.blit(back_of_card, (270, 5))
            screen.blit(back_of_card, (280, 5))
            screen.blit(back_of_card, (290, 5))
            screen.blit(back_of_card, (300, 5))
            screen.blit(back_of_card, (310, 5))
            screen.blit(back_of_card, (320, 5))
            screen.blit(back_of_card, (330, 5))
            screen.blit(back_of_card, (340, 5))
            screen.blit(back_of_card, (350, 5))
            screen.blit(back_of_card, (360, 5))
            screen.blit(back_of_card, (370, 5))
            screen.blit(back_of_card, (380, 5))

        elif len(computer_hand) == 19:
            screen.blit(back_of_card, (210, 5))
            screen.blit(back_of_card, (220, 5))
            screen.blit(back_of_card, (230, 5))
            screen.blit(back_of_card, (240, 5))
            screen.blit(back_of_card, (250, 5))
            screen.blit(back_of_card, (260, 5))
            screen.blit(back_of_card, (270, 5))
            screen.blit(back_of_card, (280, 5))
            screen.blit(back_of_card, (290, 5))
            screen.blit(back_of_card, (300, 5))
            screen.blit(back_of_card, (310, 5))
            screen.blit(back_of_card, (320, 5))
            screen.blit(back_of_card, (330, 5))
            screen.blit(back_of_card, (340, 5))
            screen.blit(back_of_card, (350, 5))
            screen.blit(back_of_card, (360, 5))
            screen.blit(back_of_card, (370, 5))
            screen.blit(back_of_card, (380, 5))
            screen.blit(back_of_card, (390, 5))

        elif len(computer_hand) == 20:
            screen.blit(back_of_card, (210, 5))
            screen.blit(back_of_card, (220, 5))
            screen.blit(back_of_card, (230, 5))
            screen.blit(back_of_card, (240, 5))
            screen.blit(back_of_card, (250, 5))
            screen.blit(back_of_card, (260, 5))
            screen.blit(back_of_card, (270, 5))
            screen.blit(back_of_card, (280, 5))
            screen.blit(back_of_card, (290, 5))
            screen.blit(back_of_card, (300, 5))
            screen.blit(back_of_card, (310, 5))
            screen.blit(back_of_card, (320, 5))
            screen.blit(back_of_card, (330, 5))
            screen.blit(back_of_card, (340, 5))
            screen.blit(back_of_card, (350, 5))
            screen.blit(back_of_card, (360, 5))
            screen.blit(back_of_card, (370, 5))
            screen.blit(back_of_card, (380, 5))
            screen.blit(back_of_card, (390, 5))
            screen.blit(back_of_card, (400, 5))

        elif len(computer_hand) == 21:
            screen.blit(back_of_card, (200, 5))
            screen.blit(back_of_card, (210, 5))
            screen.blit(back_of_card, (220, 5))
            screen.blit(back_of_card, (230, 5))
            screen.blit(back_of_card, (240, 5))
            screen.blit(back_of_card, (250, 5))
            screen.blit(back_of_card, (260, 5))
            screen.blit(back_of_card, (270, 5))
            screen.blit(back_of_card, (280, 5))
            screen.blit(back_of_card, (290, 5))
            screen.blit(back_of_card, (300, 5))
            screen.blit(back_of_card, (310, 5))
            screen.blit(back_of_card, (320, 5))
            screen.blit(back_of_card, (330, 5))
            screen.blit(back_of_card, (340, 5))
            screen.blit(back_of_card, (350, 5))
            screen.blit(back_of_card, (360, 5))
            screen.blit(back_of_card, (370, 5))
            screen.blit(back_of_card, (380, 5))
            screen.blit(back_of_card, (390, 5))
            screen.blit(back_of_card, (400, 5))

        elif len(computer_hand) == 22:
            screen.blit(back_of_card, (200, 5))
            screen.blit(back_of_card, (210, 5))
            screen.blit(back_of_card, (220, 5))
            screen.blit(back_of_card, (230, 5))
            screen.blit(back_of_card, (240, 5))
            screen.blit(back_of_card, (250, 5))
            screen.blit(back_of_card, (260, 5))
            screen.blit(back_of_card, (270, 5))
            screen.blit(back_of_card, (280, 5))
            screen.blit(back_of_card, (290, 5))
            screen.blit(back_of_card, (300, 5))
            screen.blit(back_of_card, (310, 5))
            screen.blit(back_of_card, (320, 5))
            screen.blit(back_of_card, (330, 5))
            screen.blit(back_of_card, (340, 5))
            screen.blit(back_of_card, (350, 5))
            screen.blit(back_of_card, (360, 5))
            screen.blit(back_of_card, (370, 5))
            screen.blit(back_of_card, (380, 5))
            screen.blit(back_of_card, (390, 5))
            screen.blit(back_of_card, (400, 5))
            screen.blit(back_of_card, (410, 5))

        elif len(computer_hand) == 23:
            screen.blit(back_of_card, (190, 5))
            screen.blit(back_of_card, (200, 5))
            screen.blit(back_of_card, (210, 5))
            screen.blit(back_of_card, (220, 5))
            screen.blit(back_of_card, (230, 5))
            screen.blit(back_of_card, (240, 5))
            screen.blit(back_of_card, (250, 5))
            screen.blit(back_of_card, (260, 5))
            screen.blit(back_of_card, (270, 5))
            screen.blit(back_of_card, (280, 5))
            screen.blit(back_of_card, (290, 5))
            screen.blit(back_of_card, (300, 5))
            screen.blit(back_of_card, (310, 5))
            screen.blit(back_of_card, (320, 5))
            screen.blit(back_of_card, (330, 5))
            screen.blit(back_of_card, (340, 5))
            screen.blit(back_of_card, (350, 5))
            screen.blit(back_of_card, (360, 5))
            screen.blit(back_of_card, (370, 5))
            screen.blit(back_of_card, (380, 5))
            screen.blit(back_of_card, (390, 5))
            screen.blit(back_of_card, (400, 5))
            screen.blit(back_of_card, (410, 5))

        elif len(computer_hand) == 24:
            screen.blit(back_of_card, (190, 5))
            screen.blit(back_of_card, (200, 5))
            screen.blit(back_of_card, (210, 5))
            screen.blit(back_of_card, (220, 5))
            screen.blit(back_of_card, (230, 5))
            screen.blit(back_of_card, (240, 5))
            screen.blit(back_of_card, (250, 5))
            screen.blit(back_of_card, (260, 5))
            screen.blit(back_of_card, (270, 5))
            screen.blit(back_of_card, (280, 5))
            screen.blit(back_of_card, (290, 5))
            screen.blit(back_of_card, (300, 5))
            screen.blit(back_of_card, (310, 5))
            screen.blit(back_of_card, (320, 5))
            screen.blit(back_of_card, (330, 5))
            screen.blit(back_of_card, (340, 5))
            screen.blit(back_of_card, (350, 5))
            screen.blit(back_of_card, (360, 5))
            screen.blit(back_of_card, (370, 5))
            screen.blit(back_of_card, (380, 5))
            screen.blit(back_of_card, (390, 5))
            screen.blit(back_of_card, (400, 5))
            screen.blit(back_of_card, (410, 5))
            screen.blit(back_of_card, (420, 5))

        elif len(computer_hand) == 25:
            screen.blit(back_of_card, (190, 5))
            screen.blit(back_of_card, (200, 5))
            screen.blit(back_of_card, (210, 5))
            screen.blit(back_of_card, (220, 5))
            screen.blit(back_of_card, (230, 5))
            screen.blit(back_of_card, (240, 5))
            screen.blit(back_of_card, (250, 5))
            screen.blit(back_of_card, (260, 5))
            screen.blit(back_of_card, (270, 5))
            screen.blit(back_of_card, (280, 5))
            screen.blit(back_of_card, (290, 5))
            screen.blit(back_of_card, (300, 5))
            screen.blit(back_of_card, (310, 5))
            screen.blit(back_of_card, (320, 5))
            screen.blit(back_of_card, (330, 5))
            screen.blit(back_of_card, (340, 5))
            screen.blit(back_of_card, (350, 5))
            screen.blit(back_of_card, (360, 5))
            screen.blit(back_of_card, (370, 5))
            screen.blit(back_of_card, (380, 5))
            screen.blit(back_of_card, (390, 5))
            screen.blit(back_of_card, (400, 5))
            screen.blit(back_of_card, (410, 5))
            screen.blit(back_of_card, (420, 5))
            screen.blit(back_of_card, (430, 5))

        # Face down table cards for player
        if player_face_down[0] is not None:
            screen.blit(back_of_card, (210, 400))
        else:
            screen.blit(transparent, (210, 400))

        if player_face_down[1] is not None:
            screen.blit(back_of_card, (310, 400))
        else:
            screen.blit(transparent, (310, 400))

        if player_face_down[2] is not None:
            screen.blit(back_of_card, (410, 400))
        else:
            screen.blit(transparent, (410, 400))

        # Face down table cards for computer
        if comp_face_down[0] is not None:
            screen.blit(back_of_card, (210, 120))
        else:
            screen.blit(transparent, (210, 120))

        if comp_face_down[1] is not None:
            screen.blit(back_of_card, (310, 120))
        else:
            screen.blit(transparent, (310, 120))

        if comp_face_down[2] is not None:
            screen.blit(back_of_card, (410, 120))
        else:
            screen.blit(transparent, (410, 120))

        # Face up cards for player
        if player_table_sprites[0] is not None:
            screen.blit(player_table_sprites[0], (205, 400))
        else:
            screen.blit(transparent, (205, 400))

        if player_table_sprites[1] is not None:
            screen.blit(player_table_sprites[1], (305, 400))
        else:
            screen.blit(transparent, (305, 400))

        if player_table_sprites[2] is not None:
            screen.blit(player_table_sprites[2], (405, 400))
        else:
            screen.blit(transparent, (405, 400))

        # Face up cards for computer
        if comp_table_sprites[0] is not None:
            screen.blit(comp_table_sprites[0], (205, 120))
        else:
            screen.blit(transparent, (205, 120))

        if comp_table_sprites[1] is not None:
            screen.blit(comp_table_sprites[1], (305, 120))
        else:
            screen.blit(transparent, (305, 120))

        if comp_table_sprites[2] is not None:
            screen.blit(comp_table_sprites[2], (405, 120))
        else:
            screen.blit(transparent, (405, 120))



        # Player Cards
        if len(player_hand) == 25:
            screen.blit(player_hand_sprites[0], (160 - 140, 550))
            screen.blit(player_hand_sprites[1], (185 - 140, 550))
            screen.blit(player_hand_sprites[2], (210 - 140, 550))
            screen.blit(player_hand_sprites[3], (235 - 140, 550))
            screen.blit(player_hand_sprites[4], (260 - 140, 550))
            screen.blit(player_hand_sprites[5], (285 - 140, 550))
            screen.blit(player_hand_sprites[6], (310 - 140, 550))
            screen.blit(player_hand_sprites[7], (335 - 140, 550))
            screen.blit(player_hand_sprites[8], (360 - 140, 550))
            screen.blit(player_hand_sprites[9], (385 - 140, 550))
            screen.blit(player_hand_sprites[10], (410 - 140, 550))
            screen.blit(player_hand_sprites[11], (435 - 140, 550))
            screen.blit(player_hand_sprites[12], (460 - 140, 550))
            screen.blit(player_hand_sprites[13], (485 - 140, 550))
            screen.blit(player_hand_sprites[14], (510 - 140, 550))
            screen.blit(player_hand_sprites[15], (535 - 140, 550))
            screen.blit(player_hand_sprites[16], (560 - 140, 550))
            screen.blit(player_hand_sprites[17], (585 - 140, 550))
            screen.blit(player_hand_sprites[18], (610 - 140, 550))
            screen.blit(player_hand_sprites[19], (635 - 140, 550))
            screen.blit(player_hand_sprites[20], (660 - 140, 550))
            screen.blit(player_hand_sprites[21], (685 - 140, 550))
            screen.blit(player_hand_sprites[22], (710 - 140, 550))
            screen.blit(player_hand_sprites[23], (735 - 140, 550))
            screen.blit(player_hand_sprites[24], (760 - 140, 550))

        eights = [7, 20, 33, 46]
        for x in range(1, 53):
            if len(pile.cards_in_middle) == 0:
                screen.blit(semi_transparent, (300, 255))
            elif pile.card_on_top == x and pile.card_on_top in eights:
                card_under_eight = pile.cards_in_middle[-2:]
                card_under_eight_sprite = card_sprites[card_under_eight[0] - 1]
                screen.blit(card_under_eight_sprite, (300, 255))
                transparent_copy_eight = card_sprites[x-1].copy()
                transparent_copy_eight.set_alpha(100)
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

        if turn == 1:
            rules, rules_rect = Load_Image.ImageLoad.imageLoadfnc("rules.jpg", False)
            screen.blit(rules, (50, 50))


class Animation:

    @staticmethod
    def computer_card_move(card_sprites, card, x, y, screen):
        for cardInDeck in range(1, 53):
            if card == cardInDeck:
                card = card_sprites[cardInDeck-1]

                screen.blit(card, (x, y))

    @staticmethod  # used for both player and computer animations
    def animate_play_card(card, screen, card_sprites, fpsclock, player_hand_sprites, phand, chand, back_of_card,
                          middle_pile, cards, back_of_card_rect, background, background_rect, player, player_face_up_sprites,
                          computer_face_up_sprites, player_table_cards_down, computer_table_cards_down):
        move_speed = 1

        # Middle pile has position = 300, 255
        # Middle of Computer hand = 310, 5

        if not player:
            y = 5
        else:
            y = 550

        x = 300     # not exactly middle of pile but makes moving easier

        end_y = 255

        while True:
            if not player:
                y += move_speed
            else:
                y -= move_speed
            if y == end_y:
                return
            turn = 0
            # the following two functions let the other images render so the moving images do not leave black lines
            screen.blit(background, background_rect)
            BlitPlayer.blit_cards(player_hand_sprites, phand, chand, back_of_card, screen, middle_pile,
                                  card_sprites, cards, back_of_card_rect, turn, player_face_up_sprites,
                                  computer_face_up_sprites, player_table_cards_down, computer_table_cards_down)
            Animation.computer_card_move(card_sprites, card, x, y, screen)

            pygame.display.update()
            fpsclock.tick()


class Misc:
    @staticmethod
    def game_over(img, screen):
        screen.blit(img, (100, 100))

    @staticmethod
    def pick_up_deck(img, screen):
        screen.blit(img, (100, 255))

    @staticmethod
    def bg_img(bg, bgrect, screen):
        screen.blit(bg, bgrect)

    @staticmethod
    def render_font(font, screen, string):
        screen.blit(font.render(string, True, (0, 0, 0)), (475, 515))
