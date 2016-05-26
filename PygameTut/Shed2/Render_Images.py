import pygame
import Load_Image


class BlitPlayer:

    @staticmethod
    def gen_face_up_table_cards(player_face_up, comp_face_up, list_of_c, deck_card_sprites, deck_card_hl_sprites, transparent_card):
        # Empty Lists to store the sprites to return
        player = [None] * 3
        comp = [None] * 3
        for x in range(1, 53):
            for c in range(3):
                # Player cards
                if player_face_up[c] == x:  # If the face up card has the same values as x
                    if list_of_c[c] == 1:   # not highlighted
                        player[c] = deck_card_sprites[x-1]
                    else:                   # highlighted
                        player[c] = deck_card_hl_sprites[x-1]

                elif player_face_up[c] is None:  # if empty, render a transparant card
                    player[c] = transparent_card

                # Computer cards
                if comp_face_up[c] == x:
                    comp[c] = deck_card_sprites[x-1]

                elif comp_face_up[c] is None:
                    comp[c] = transparent_card

        return [player, comp]

    # method to take in the players hand and return the sprites that it will need
    @staticmethod
    def gen_player_blit_cards(player_hand, deck_card_sprites, deck_card_hl_sprites, list_of_c, transparent_card):

        list_to_return = [None] * 25

        for y in range(25):
            for x in range(1, 53):

                if player_hand[y] == x:
                    if list_of_c[y] == 1:
                        list_to_return[y] = deck_card_sprites[x-1]
                    else:
                        list_to_return[y] = deck_card_hl_sprites[x-1]

                elif player_hand[y] is None:
                    list_to_return[y] = transparent_card

        return list_to_return

    # Method to take lists of sprites, and position them on screen
    @staticmethod
    def blit_cards(player_hand_sprites, player_hand, computer_hand, back_of_card, screen, pile, card_sprites, deck, back_rect, turn,
                   player_table_sprites, comp_table_sprites, player_face_down, comp_face_down):

        width = back_rect.w
        height = back_rect.h

        # CODE TO GET TRANSPARENT IMAGES

        transparent = pygame.Surface((width, height), pygame.SRCALPHA)
        transparent.set_alpha(0)
        transparent.fill((255, 255, 255, 0))

        semi_transparent = pygame.Surface((width, height), pygame.SRCALPHA)
        semi_transparent.set_alpha(2)
        semi_transparent.fill((255, 255, 255, 2))

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

        # Pile in the middle, including special cases
        eights = [7, 20, 33, 46]
        for x in range(1, 53):
            # Nothing in the middle, render a semi-transparent rectangle the size of a card
            if len(pile.cards_in_middle) == 0:
                screen.blit(semi_transparent, (300, 255))
            # 8 on top, render an 'invisible' 8 just off to the side,
            # so the player knows an 8 is in the middle but can still see the card underneath
            elif pile.card_on_top == x and pile.card_on_top in eights:
                card_under_eight = pile.cards_in_middle[-2:]
                card_under_eight_sprite = card_sprites[card_under_eight[0] - 1]
                screen.blit(card_under_eight_sprite, (300, 255))
                transparent_copy_eight = card_sprites[x-1].copy()
                transparent_copy_eight.set_alpha(100)
                screen.blit(transparent_copy_eight, (325, 255))
            # Normal behaviour
            elif pile.card_on_top == x:
                card_in_middle = card_sprites[x-1]
                screen.blit(card_in_middle, (300, 255))
                break

        # Render the deck
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

        # Render the rules if it is at the beginning of the game
        if turn == 1:
            rules, rules_rect = Load_Image.ImageLoad.image_load("rules.jpg", False)
            screen.blit(rules, (50, 50))


# Class to render animations
class Animation:

    # Method to just render a card in a specific place
    @staticmethod
    def computer_card_move(card_sprites, card, x, y, screen):
        for cardInDeck in range(1, 53):
            if card == cardInDeck:
                card = card_sprites[cardInDeck-1]

                screen.blit(card, (x, y))

    # Used for both player and computer animations
    @staticmethod
    def animate_play_card(card, screen, card_sprites, fps_clock, player_hand_sprites, player_hand, computer_hand, back_of_card,
                          middle_pile, cards, back_of_card_rect, background, background_rect, player, player_face_up_sprites,
                          computer_face_up_sprites, player_table_cards_down, computer_table_cards_down):

        move_speed = 1

        # Middle pile has position = 300, 255
        # Middle of Computer hand = 310, 5

        # Start points of cards
        if not player:
            y = 5
        else:
            y = 550

        x = 300     # not exactly middle of pile but makes moving easier

        # End point
        end_y = 255

        while True:
            # Move the card
            if not player:
                y += move_speed
            else:
                y -= move_speed
            if y == end_y:
                # break if the card reaches the end point
                return
            turn = 0
            # the following two functions let the other images render so the moving images do not leave black lines
            screen.blit(background, background_rect)
            BlitPlayer.blit_cards(player_hand_sprites, player_hand, computer_hand, back_of_card, screen, middle_pile,
                                  card_sprites, cards, back_of_card_rect, turn, player_face_up_sprites,
                                  computer_face_up_sprites, player_table_cards_down, computer_table_cards_down)
            Animation.computer_card_move(card_sprites, card, x, y, screen)

            pygame.display.update()
            fps_clock.tick()


# Class to render stand alone images that are only seen once or don't need moving
class Misc:
    @staticmethod
    def game_over(img, screen):
        screen.blit(img, (100, 100))

    @staticmethod
    def pick_up_deck(img, screen):
        screen.blit(img, (100, 255))

    @staticmethod
    def background_img(bg, bg_rect, screen):
        screen.blit(bg, bg_rect)

    @staticmethod
    def render_font(font, screen, string):
        screen.blit(font.render(string, True, (0, 0, 0)), (475, 515))
