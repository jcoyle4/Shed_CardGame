import pygame
import os
from Hand import HandClass
import Load_Image
import Deck
from TableCards import TableCardsClass
import MiddlePile
from ComputerAI import ComputerAI
from Render_Images import *

pygame.init()

FPS = 30
# Position of the screen when it starts
startx = 200
starty = 40
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (startx, starty)
font = pygame.font.Font(None, 25)


# Size of the screen and its variable
screen = pygame.display.set_mode((700, 700))
background, background_Rect = Load_Image.ImageLoad.imageLoadfnc("table.jpg", False)
back_of_card, back_of_card_Rect = Load_Image.ImageLoad.imageLoadfnc('back.png', False)

width = back_of_card_Rect.w
height = back_of_card_Rect.h

transparent = pygame.Surface((width, height), pygame.SRCALPHA)
transparent.set_alpha(0)
transparent.fill((255, 255, 255, 0))

playerWinnerIMG, playerWinnerIMG_Rect = Load_Image.ImageLoad.imageLoadfnc("win.jpg", False)
computerWinnerIMG, computerWinnerIMG_Rect = Load_Image.ImageLoad.imageLoadfnc("lose.jpg", False)
pickUpDeckIMG, pickUpDeckIMG_Rect = Load_Image.ImageLoad.imageLoadfnc("PickUpTheDeck.jpg", False)

game_deck = Deck.DeckClass()  # deck of 52 cards, sprites are also in here

computer_hand = HandClass()  # The hand of cards that the computer holds
player_hand = HandClass()   # The hand for the player

# Object for the middle pile, holds all the cards in the middle pile and which card is on top
middle_pile = MiddlePile.Pile()

computer_table_cards = TableCardsClass()
player_table_cards = TableCardsClass()

game_deck.cards = computer_table_cards.setup(game_deck.cards)
game_deck.cards = player_table_cards.setup(game_deck.cards)


# Set up the computer hand
game_deck.cards = computer_hand.setUp(game_deck.cards)
# Set up the player hand
game_deck.cards = player_hand.setUp(game_deck.cards)

player_hand.initialRejig()  # Use this to center the cards for playing

# When cx is equal to 1, this means that the image is not high-lighted
c1 = 1
c2 = 1
c3 = 1
c4 = 1
c5 = 1
c6 = 1
c7 = 1
c8 = 1
c9 = 1
c10 = 1
c11 = 1
c12 = 1
c13 = 1
c14 = 1
c15 = 1
c16 = 1
c17 = 1
c18 = 1
c19 = 1
c20 = 1
c21 = 1
c22 = 1
c23 = 1
c24 = 1
c25 = 1

list_of_c = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20, c21, c22, c23, c24, c25]

c_table1 = 1
c_table2 = 1
c_table3 = 1

list_of_c_table = [c_table1, c_table2, c_table3]

clicked = 0

# if card is used, used will be equal to 'spent' and the player cannot select that card anymore.
used1 = ''
used2 = ''
used3 = ''
used4 = ''
used5 = ''
used6 = ''
used7 = ''
used8 = ''
used9 = ''
used10 = ''
used11 = ''
used12 = ''
used13 = ''
used14 = ''
used15 = ''
used16 = ''
used17 = ''
used18 = ''
used19 = ''
used20 = ''
used21 = ''
used22 = ''
used23 = ''
used24 = ''
used25 = ''

table1 = ''
table2 = ''
table3 = ''

running = True  # Boolean for the main loop
# counter = True  #
move = True  # boolean to keep track of whose move it is True for player, False for computer
# Switch to int if more than one computer
turn = 0  # Which turn of the game we are on

dblClickGlobal = None

dblClick1 = None
dblClick2 = None
dblClick3 = None
dblClick4 = None
dblClick5 = None
dblClick6 = None
dblClick7 = None
dblClick8 = None
dblClick9 = None
dblClick10 = None
dblClick11 = None
dblClick12 = None
dblClick13 = None
dblClick14 = None
dblClick15 = None
dblClick16 = None
dblClick17 = None
dblClick18 = None
dblClick19 = None
dblClick20 = None
dblClick21 = None
dblClick22 = None
dblClick23 = None
dblClick24 = None
dblClick25 = None


while running:
    listOfDblClicks = [dblClickGlobal, dblClick1, dblClick2, dblClick3, dblClick4, dblClick5, dblClick6, dblClick7, dblClick8,
                       dblClick9, dblClick10, dblClick11, dblClick12, dblClick13, dblClick14, dblClick15, dblClick16,
                       dblClick17, dblClick18, dblClick19, dblClick20, dblClick21, dblClick22, dblClick23, dblClick24, dblClick25]

    FPSCLOCK = pygame.time.Clock()
    # Put the background image in place
    Misc.bg_img(background, background_Rect, screen)
    Misc.pick_up_deck(pickUpDeckIMG, screen)

    # all of these x's and y's set up rectangular coordinates that, when clicked, perform a certain action.
    # Middle Pile
    x_mid = list(range(300, 375))
    y_mid = list(range(255, 360))

    y_table_cards = list(range(400, 500))

    x_table_1 = list(range(205, 275))
    x_table_2 = list(range(305, 375))
    x_table_3 = list(range(405, 475))

    x_pick_up = list(range(100, 250))
    y_pick_up = list(range(255, 355))

    # Y-Coord of hand
    y_card_all = list(range(550, 660))
    x_all = list(range(0, 700))
    y_all = list(range(0, 700))

    player_hand_sprites = BlitPlayer.gen_player_blit_cards(player_hand.hand, game_deck.card_Sprites,
                                                           game_deck.highlighted_Card_Sprites, list_of_c, transparent)

    list_to_alter = BlitPlayer.gen_face_up_table_cards(player_table_cards.face_up, computer_table_cards.face_up, list_of_c_table,
                                                       game_deck.card_Sprites, game_deck.highlighted_Card_Sprites, transparent)

    player_face_up_sprites = list_to_alter[0]
    computer_face_up_sprites = list_to_alter[1]

    # X-Coord's of each card
    x_card_1 = list(range(20, 44))
    x_card_2 = list(range(45, 69))
    x_card_3 = list(range(70, 95))
    x_card_4 = list(range(96, 119))
    x_card_5 = list(range(120, 144))
    x_card_6 = list(range(145, 170))
    x_card_7 = list(range(171, 194))
    x_card_8 = list(range(195, 219))
    x_card_9 = list(range(220, 244))
    x_card_10 = list(range(245, 270))
    if player_hand.hand[11] is None:
        x_card_11 = list(range(271, 310))
        x_card_12 = list(range(296, 320))
        x_card_13 = list(range(321, 345))
        x_card_14 = list(range(346, 417))
        x_card_15 = list(range(420, 440))
        x_card_16 = list(range(441, 460))
        x_card_17 = list(range(461, 480))
        x_card_18 = list(range(481, 500))
        x_card_19 = list(range(501, 520))
        x_card_20 = list(range(521, 540))
        x_card_21 = list(range(541, 560))
        x_card_22 = list(range(561, 580))
        x_card_23 = list(range(581, 600))
        x_card_24 = list(range(601, 620))
    else:
        x_card_11 = list(range(271, 295))

        if player_hand.hand[12] is None:
            x_card_12 = list(range(296, 365))
            x_card_13 = list(range(321, 345))
            x_card_14 = list(range(346, 417))
            x_card_15 = list(range(420, 440))
            x_card_16 = list(range(441, 460))
            x_card_17 = list(range(461, 480))
            x_card_18 = list(range(481, 500))
            x_card_19 = list(range(501, 520))
            x_card_20 = list(range(521, 540))
            x_card_21 = list(range(541, 560))
            x_card_22 = list(range(561, 580))
            x_card_23 = list(range(581, 600))
            x_card_24 = list(range(601, 620))
        else:
            x_card_12 = list(range(296, 320))

            if player_hand.hand[13] is None:
                x_card_13 = list(range(321, 395))
                x_card_14 = list(range(346, 417))
                x_card_15 = list(range(420, 440))
                x_card_16 = list(range(441, 460))
                x_card_17 = list(range(461, 480))
                x_card_18 = list(range(481, 500))
                x_card_19 = list(range(501, 520))
                x_card_20 = list(range(521, 540))
                x_card_21 = list(range(541, 560))
                x_card_22 = list(range(561, 580))
                x_card_23 = list(range(581, 600))
                x_card_24 = list(range(601, 620))
            else:
                x_card_13 = list(range(321, 345))

                if player_hand.hand[14] is None:
                    x_card_14 = list(range(346, 417))
                    x_card_15 = list(range(420, 440))
                    x_card_16 = list(range(441, 460))
                    x_card_17 = list(range(461, 480))
                    x_card_18 = list(range(481, 500))
                    x_card_19 = list(range(501, 520))
                    x_card_20 = list(range(521, 540))
                    x_card_21 = list(range(541, 560))
                    x_card_22 = list(range(561, 580))
                    x_card_23 = list(range(581, 600))
                    x_card_24 = list(range(601, 620))
                else:
                    x_card_14 = list(range(346, 370))

                    if player_hand.hand[15] is None:
                        x_card_15 = list(range(371, 440))
                        x_card_16 = list(range(441, 460))
                        x_card_17 = list(range(461, 480))
                        x_card_18 = list(range(481, 500))
                        x_card_19 = list(range(501, 520))
                        x_card_20 = list(range(521, 540))
                        x_card_21 = list(range(541, 560))
                        x_card_22 = list(range(561, 580))
                        x_card_23 = list(range(581, 600))
                        x_card_24 = list(range(601, 620))
                    else:
                        x_card_15 = list(range(371, 395))

                        if player_hand.hand[16] is None:
                            x_card_16 = list(range(396, 466))
                            x_card_17 = list(range(461 + 10, 480 + 10))
                            x_card_18 = list(range(481 + 10, 500 + 10))
                            x_card_19 = list(range(501 + 10, 520 + 10))
                            x_card_20 = list(range(521 + 10, 540 + 10))
                            x_card_21 = list(range(541 + 10, 560 + 10))
                            x_card_22 = list(range(561 + 10, 580 + 10))
                            x_card_23 = list(range(581 + 10, 600 + 10))
                            x_card_24 = list(range(601 + 10, 620 + 10))
                        else:
                            x_card_16 = list(range(396, 420))

                            if player_hand.hand[17] is None:
                                x_card_17 = list(range(421, 490))
                                x_card_18 = list(range(481 + 10, 500 + 10))
                                x_card_19 = list(range(501 + 10, 520 + 10))
                                x_card_20 = list(range(521 + 10, 540 + 10))
                                x_card_21 = list(range(541 + 10, 560 + 10))
                                x_card_22 = list(range(561 + 10, 580 + 10))
                                x_card_23 = list(range(581 + 10, 600 + 10))
                                x_card_24 = list(range(601 + 10, 620 + 10))
                            else:
                                x_card_17 = list(range(421, 445))

                                if player_hand.hand[18] is None:
                                    x_card_18 = list(range(446, 518))
                                    x_card_19 = list(range(501 + 20, 520 + 20))
                                    x_card_20 = list(range(521 + 20, 540 + 20))
                                    x_card_21 = list(range(541 + 20, 560 + 20))
                                    x_card_22 = list(range(561 + 20, 580 + 20))
                                    x_card_23 = list(range(581 + 20, 600 + 20))
                                    x_card_24 = list(range(601 + 20, 620 + 20))
                                else:
                                    x_card_18 = list(range(446, 470))

                                    if player_hand.hand[19] is None:
                                        x_card_19 = list(range(471, 542))
                                        x_card_20 = list(range(521 + 25, 540 + 25))
                                        x_card_21 = list(range(541 + 25, 560 + 25))
                                        x_card_22 = list(range(561 + 25, 580 + 25))
                                        x_card_23 = list(range(581 + 25, 600 + 25))
                                        x_card_24 = list(range(601 + 25, 620 + 25))
                                    else:
                                        x_card_19 = list(range(471, 495))

                                        if player_hand.hand[20] is None:
                                            x_card_20 = list(range(496, 566))
                                            x_card_21 = list(range(541 + 25, 560 + 25))
                                            x_card_22 = list(range(561 + 25, 580 + 25))
                                            x_card_23 = list(range(581 + 25, 600 + 25))
                                            x_card_24 = list(range(601 + 25, 620 + 25))
                                        else:
                                            x_card_20 = list(range(496, 520))

                                            if player_hand.hand[21] is None:
                                                x_card_21 = list(range(521, 586))
                                                x_card_22 = list(range(561 + 30, 580 + 30))
                                                x_card_23 = list(range(581 + 30, 600 + 30))
                                                x_card_24 = list(range(601 + 30, 620 + 30))
                                            else:
                                                x_card_21 = list(range(521, 545))

                                                if player_hand.hand[22] is None:
                                                    x_card_22 = list(range(546, 611))
                                                    x_card_23 = list(range(581 + 31, 600 + 31))
                                                    x_card_24 = list(range(601 + 31, 620 + 31))
                                                else:
                                                    x_card_22 = list(range(546, 570))

                                                    if player_hand.hand[23] is None:
                                                        x_card_23 = list(range(571, 636))
                                                        x_card_24 = list(range(601 + 41, 620 + 41))
                                                    else:
                                                        x_card_23 = list(range(571, 595))

                                                        if player_hand.hand[24] is None:
                                                            x_card_24 = list(range(596, 661))
                                                        else:
                                                            x_card_24 = list(range(596, 620))

    x_card_25 = list(range(621, 690))

    if turn == 0:
        game_deck.cards = middle_pile.Start_game(game_deck.cards)
        turn += 1  # counter to show the rules

    # puts ALL (computer, player and pile) the cards on the screen, and keeps updating them during the while loop
    BlitPlayer.blit_cards(player_hand_sprites, player_hand.hand, computer_hand.hand, back_of_card, screen, middle_pile,
                          game_deck.card_Sprites, Deck.DeckClass.cards, back_of_card_Rect, turn, player_face_up_sprites,
                          computer_face_up_sprites, player_table_cards.face_down, computer_table_cards.face_down)

    middle_pile.PlayableCards()

    # Text Notification for when the player need to pick up the pile
    if any(card is not None for card in player_hand.hand):
        if all(card not in middle_pile.playable_cards_list for card in player_hand.hand):
            Misc.render_font(font, screen, "You must pick up the deck")
    if all(card is None for card in player_hand.hand) and any(card is not None for card in player_table_cards.face_up):
        if all(card not in middle_pile.playable_cards_list for card in player_table_cards.face_up):
            Misc.render_font(font, screen, "You must pick up the deck")

    number_of_player_cards = sum(x is not None for x in player_hand.hand)

    for event in pygame.event.get():  # get user input
        # if dblClick and pygame.time.get_ticks() - dblClick > 600:
        #     dblClick = None
        for item in listOfDblClicks:
            if item is not None and pygame.time.get_ticks() - item > 600:
                item = None

        if event.type == pygame.QUIT:  # if user closes
            running = False
        elif event.type == pygame.MOUSEMOTION:
            # print ("mouse at (%d, %d)" % event.pos)
            x, y = event.pos
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # print ("You pressed the left mouse button at (%d, %d)" % event.pos)
            print(x, y)
            # print("Time between clicks =", pygame.time.get_ticks() - int(dblClick))
            if dblClickGlobal and pygame.time.get_ticks() - dblClickGlobal < 600:
                turn += 1
                print("Time between clicks =", pygame.time.get_ticks() - dblClickGlobal)
                print("Player Hand =", player_hand.hand)
                print("Computer Hand =", computer_hand.hand)
                print("Cards in the middle =", middle_pile.cards_in_middle)
                print("Discarded cards =", middle_pile.discarded_cards)
                print("Player Table Cards =", player_table_cards.face_up, "&", player_table_cards.face_down)
                print("Computer Table Cards =", computer_table_cards.face_up, "&", computer_table_cards.face_down)
                dblClickGlobal = None
            else:
                dblClickGlobal = pygame.time.get_ticks()

            # Closes the game if all cards in the hand are gone
            if all(card is None for card in player_hand.hand) and all(card is None for card in player_table_cards.face_down):
                Misc.game_over(playerWinnerIMG, screen)
                pygame.display.flip()
                if x in x_all and y in y_all:
                    running = False
                    pygame.time.delay(3000)

            if len(computer_hand.hand) == 0 and all(card is None for card in computer_table_cards.face_down):
                Misc.game_over(computerWinnerIMG, screen)
                pygame.display.flip()
                if x in x_all and y in y_all:
                    # print("QUITTING")
                    running = False
                    pygame.time.delay(3000)

            # Code to move a card from the players hand to the middle
            # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            if x in x_mid:
                if y in y_mid:
                    this = 1
                    while this == 1:
                        # C1
                        if list_of_c[0] == 0:  # ie clicked. This says that if a card is clicked, and therefore able to be played,
                            #  the card in the middle is now the clicked number. and etc.
                            Animation.animate_play_card(player_hand.hand[0], screen, game_deck.card_Sprites, FPSCLOCK,
                                                        player_hand_sprites, player_hand.hand, computer_hand.hand, back_of_card,
                                                        middle_pile, Deck.DeckClass.cards, back_of_card_Rect,
                                                        background, background_Rect, True, player_face_up_sprites,
                                                        computer_face_up_sprites, player_table_cards.face_down,
                                                        computer_table_cards.face_down)
                            middle_pile.moveCard(player_hand.hand[0])
                            used1 = 'spent'
                            list_of_c = HandClass.un_flip_all(list_of_c)
                            this = 0

                        # C2
                        elif list_of_c[1] == 0:
                            Animation.animate_play_card(player_hand.hand[1], screen, game_deck.card_Sprites, FPSCLOCK,
                                                        player_hand_sprites, player_hand.hand, computer_hand.hand, back_of_card,
                                                        middle_pile, Deck.DeckClass.cards, back_of_card_Rect,
                                                        background, background_Rect, True, player_face_up_sprites,
                                                        computer_face_up_sprites, player_table_cards.face_down,
                                                        computer_table_cards.face_down)
                            middle_pile.moveCard(player_hand.hand[1])
                            used2 = 'spent'
                            list_of_c = HandClass.un_flip_all(list_of_c)
                            this = 0

                        elif list_of_c[2] == 0:
                            Animation.animate_play_card(player_hand.hand[2], screen, game_deck.card_Sprites, FPSCLOCK,
                                                        player_hand_sprites, player_hand.hand, computer_hand.hand, back_of_card,
                                                        middle_pile, Deck.DeckClass.cards, back_of_card_Rect,
                                                        background, background_Rect, True, player_face_up_sprites,
                                                        computer_face_up_sprites, player_table_cards.face_down,
                                                        computer_table_cards.face_down)
                            middle_pile.moveCard(player_hand.hand[2])
                            used3 = 'spent'
                            list_of_c = HandClass.un_flip_all(list_of_c)
                            this = 0

                        elif list_of_c[3] == 0:
                            Animation.animate_play_card(player_hand.hand[3], screen, game_deck.card_Sprites, FPSCLOCK,
                                                        player_hand_sprites, player_hand.hand, computer_hand.hand, back_of_card,
                                                        middle_pile, Deck.DeckClass.cards, back_of_card_Rect,
                                                        background, background_Rect, True, player_face_up_sprites,
                                                        computer_face_up_sprites, player_table_cards.face_down,
                                                        computer_table_cards.face_down)
                            middle_pile.moveCard(player_hand.hand[3])
                            used4 = 'spent'
                            list_of_c = HandClass.un_flip_all(list_of_c)
                            this = 0

                        elif list_of_c[4] == 0:
                            Animation.animate_play_card(player_hand.hand[4], screen, game_deck.card_Sprites, FPSCLOCK,
                                                        player_hand_sprites, player_hand.hand, computer_hand.hand, back_of_card,
                                                        middle_pile, Deck.DeckClass.cards, back_of_card_Rect,
                                                        background, background_Rect, True, player_face_up_sprites,
                                                        computer_face_up_sprites, player_table_cards.face_down,
                                                        computer_table_cards.face_down)
                            middle_pile.moveCard(player_hand.hand[4])
                            used5 = 'spent'
                            list_of_c = HandClass.un_flip_all(list_of_c)
                            this = 0

                        elif list_of_c[5] == 0:
                            Animation.animate_play_card(player_hand.hand[5], screen, game_deck.card_Sprites, FPSCLOCK,
                                                        player_hand_sprites, player_hand.hand, computer_hand.hand, back_of_card,
                                                        middle_pile, Deck.DeckClass.cards, back_of_card_Rect,
                                                        background, background_Rect, True, player_face_up_sprites,
                                                        computer_face_up_sprites, player_table_cards.face_down,
                                                        computer_table_cards.face_down)
                            middle_pile.moveCard(player_hand.hand[5])
                            used6 = 'spent'
                            list_of_c = HandClass.un_flip_all(list_of_c)
                            this = 0

                        elif list_of_c[6] == 0:
                            Animation.animate_play_card(player_hand.hand[6], screen, game_deck.card_Sprites, FPSCLOCK,
                                                        player_hand_sprites, player_hand.hand, computer_hand.hand, back_of_card,
                                                        middle_pile, Deck.DeckClass.cards, back_of_card_Rect,
                                                        background, background_Rect, True, player_face_up_sprites,
                                                        computer_face_up_sprites, player_table_cards.face_down,
                                                        computer_table_cards.face_down)
                            middle_pile.moveCard(player_hand.hand[6])
                            used7 = 'spent'
                            list_of_c = HandClass.un_flip_all(list_of_c)
                            this = 0

                        elif list_of_c[7] == 0:
                            Animation.animate_play_card(player_hand.hand[7], screen, game_deck.card_Sprites, FPSCLOCK,
                                                        player_hand_sprites, player_hand.hand, computer_hand.hand, back_of_card,
                                                        middle_pile, Deck.DeckClass.cards, back_of_card_Rect,
                                                        background, background_Rect, True, player_face_up_sprites,
                                                        computer_face_up_sprites, player_table_cards.face_down,
                                                        computer_table_cards.face_down)
                            middle_pile.moveCard(player_hand.hand[7])
                            used8 = 'spent'
                            list_of_c = HandClass.un_flip_all(list_of_c)
                            this = 0

                        elif list_of_c[8] == 0:
                            Animation.animate_play_card(player_hand.hand[8], screen, game_deck.card_Sprites, FPSCLOCK,
                                                        player_hand_sprites, player_hand.hand, computer_hand.hand, back_of_card,
                                                        middle_pile, Deck.DeckClass.cards, back_of_card_Rect,
                                                        background, background_Rect, True, player_face_up_sprites,
                                                        computer_face_up_sprites, player_table_cards.face_down,
                                                        computer_table_cards.face_down)
                            middle_pile.moveCard(player_hand.hand[8])
                            used9 = 'spent'
                            list_of_c = HandClass.un_flip_all(list_of_c)
                            this = 0

                        elif list_of_c[9] == 0:
                            Animation.animate_play_card(player_hand.hand[9], screen, game_deck.card_Sprites, FPSCLOCK,
                                                        player_hand_sprites, player_hand.hand, computer_hand.hand, back_of_card,
                                                        middle_pile, Deck.DeckClass.cards, back_of_card_Rect,
                                                        background, background_Rect, True, player_face_up_sprites,
                                                        computer_face_up_sprites, player_table_cards.face_down,
                                                        computer_table_cards.face_down)
                            middle_pile.moveCard(player_hand.hand[9])
                            used10 = 'spent'
                            list_of_c = HandClass.un_flip_all(list_of_c)
                            this = 0

                        elif list_of_c[10] == 0:
                            Animation.animate_play_card(player_hand.hand[10], screen, game_deck.card_Sprites, FPSCLOCK,
                                                        player_hand_sprites, player_hand.hand, computer_hand.hand, back_of_card,
                                                        middle_pile, Deck.DeckClass.cards, back_of_card_Rect,
                                                        background, background_Rect, True, player_face_up_sprites,
                                                        computer_face_up_sprites, player_table_cards.face_down,
                                                        computer_table_cards.face_down)
                            middle_pile.moveCard(player_hand.hand[10])
                            used11 = 'spent'
                            list_of_c = HandClass.un_flip_all(list_of_c)
                            this = 0

                        elif list_of_c[11] == 0:
                            Animation.animate_play_card(player_hand.hand[11], screen, game_deck.card_Sprites, FPSCLOCK,
                                                        player_hand_sprites, player_hand.hand, computer_hand.hand, back_of_card,
                                                        middle_pile, Deck.DeckClass.cards, back_of_card_Rect,
                                                        background, background_Rect, True, player_face_up_sprites,
                                                        computer_face_up_sprites, player_table_cards.face_down,
                                                        computer_table_cards.face_down)
                            middle_pile.moveCard(player_hand.hand[11])
                            used12 = 'spent'
                            list_of_c = HandClass.un_flip_all(list_of_c)
                            this = 0

                        elif list_of_c[12] == 0:
                            Animation.animate_play_card(player_hand.hand[12], screen, game_deck.card_Sprites, FPSCLOCK,
                                                        player_hand_sprites, player_hand.hand, computer_hand.hand, back_of_card,
                                                        middle_pile, Deck.DeckClass.cards, back_of_card_Rect,
                                                        background, background_Rect, True, player_face_up_sprites,
                                                        computer_face_up_sprites, player_table_cards.face_down,
                                                        computer_table_cards.face_down)
                            middle_pile.moveCard(player_hand.hand[12])
                            used13 = 'spent'
                            list_of_c = HandClass.un_flip_all(list_of_c)
                            this = 0

                        elif list_of_c[13] == 0:
                            Animation.animate_play_card(player_hand.hand[13], screen, game_deck.card_Sprites, FPSCLOCK,
                                                        player_hand_sprites, player_hand.hand, computer_hand.hand, back_of_card,
                                                        middle_pile, Deck.DeckClass.cards, back_of_card_Rect,
                                                        background, background_Rect, True, player_face_up_sprites,
                                                        computer_face_up_sprites, player_table_cards.face_down,
                                                        computer_table_cards.face_down)
                            middle_pile.moveCard(player_hand.hand[13])
                            used14 = 'spent'
                            list_of_c = HandClass.un_flip_all(list_of_c)
                            this = 0

                        elif list_of_c[14] == 0:
                            Animation.animate_play_card(player_hand.hand[14], screen, game_deck.card_Sprites, FPSCLOCK,
                                                        player_hand_sprites, player_hand.hand, computer_hand.hand, back_of_card,
                                                        middle_pile, Deck.DeckClass.cards, back_of_card_Rect,
                                                        background, background_Rect, True, player_face_up_sprites,
                                                        computer_face_up_sprites, player_table_cards.face_down,
                                                        computer_table_cards.face_down)
                            middle_pile.moveCard(player_hand.hand[14])
                            used15 = 'spent'
                            list_of_c = HandClass.un_flip_all(list_of_c)
                            this = 0

                        elif list_of_c[15] == 0:
                            Animation.animate_play_card(player_hand.hand[15], screen, game_deck.card_Sprites, FPSCLOCK,
                                                        player_hand_sprites, player_hand.hand, computer_hand.hand, back_of_card,
                                                        middle_pile, Deck.DeckClass.cards, back_of_card_Rect,
                                                        background, background_Rect, True, player_face_up_sprites,
                                                        computer_face_up_sprites, player_table_cards.face_down,
                                                        computer_table_cards.face_down)
                            middle_pile.moveCard(player_hand.hand[15])
                            used16 = 'spent'
                            list_of_c = HandClass.un_flip_all(list_of_c)
                            this = 0

                        elif list_of_c[16] == 0:
                            Animation.animate_play_card(player_hand.hand[16], screen, game_deck.card_Sprites, FPSCLOCK,
                                                        player_hand_sprites, player_hand.hand, computer_hand.hand, back_of_card,
                                                        middle_pile, Deck.DeckClass.cards, back_of_card_Rect,
                                                        background, background_Rect, True, player_face_up_sprites,
                                                        computer_face_up_sprites, player_table_cards.face_down,
                                                        computer_table_cards.face_down)
                            middle_pile.moveCard(player_hand.hand[16])
                            used17 = 'spent'
                            list_of_c = HandClass.un_flip_all(list_of_c)
                            this = 0

                        elif list_of_c[17] == 0:
                            Animation.animate_play_card(player_hand.hand[17], screen, game_deck.card_Sprites, FPSCLOCK,
                                                        player_hand_sprites, player_hand.hand, computer_hand.hand, back_of_card,
                                                        middle_pile, Deck.DeckClass.cards, back_of_card_Rect,
                                                        background, background_Rect, True, player_face_up_sprites,
                                                        computer_face_up_sprites, player_table_cards.face_down,
                                                        computer_table_cards.face_down)
                            middle_pile.moveCard(player_hand.hand[17])
                            used18 = 'spent'
                            list_of_c = HandClass.un_flip_all(list_of_c)
                            this = 0

                        elif list_of_c[18] == 0:
                            Animation.animate_play_card(player_hand.hand[18], screen, game_deck.card_Sprites, FPSCLOCK,
                                                        player_hand_sprites, player_hand.hand, computer_hand.hand, back_of_card,
                                                        middle_pile, Deck.DeckClass.cards, back_of_card_Rect,
                                                        background, background_Rect, True, player_face_up_sprites,
                                                        computer_face_up_sprites, player_table_cards.face_down,
                                                        computer_table_cards.face_down)
                            middle_pile.moveCard(player_hand.hand[18])
                            used19 = 'spent'
                            list_of_c = HandClass.un_flip_all(list_of_c)
                            this = 0

                        elif list_of_c[19] == 0:
                            Animation.animate_play_card(player_hand.hand[19], screen, game_deck.card_Sprites, FPSCLOCK,
                                                        player_hand_sprites, player_hand.hand, computer_hand.hand, back_of_card,
                                                        middle_pile, Deck.DeckClass.cards, back_of_card_Rect,
                                                        background, background_Rect, True, player_face_up_sprites,
                                                        computer_face_up_sprites, player_table_cards.face_down,
                                                        computer_table_cards.face_down)
                            middle_pile.moveCard(player_hand.hand[19])
                            used20 = 'spent'
                            list_of_c = HandClass.un_flip_all(list_of_c)
                            this = 0

                        elif list_of_c[20] == 0:
                            Animation.animate_play_card(player_hand.hand[20], screen, game_deck.card_Sprites, FPSCLOCK,
                                                        player_hand_sprites, player_hand.hand, computer_hand.hand, back_of_card,
                                                        middle_pile, Deck.DeckClass.cards, back_of_card_Rect,
                                                        background, background_Rect, True, player_face_up_sprites,
                                                        computer_face_up_sprites, player_table_cards.face_down,
                                                        computer_table_cards.face_down)
                            middle_pile.moveCard(player_hand.hand[20])
                            used21 = 'spent'
                            list_of_c = HandClass.un_flip_all(list_of_c)
                            this = 0

                        elif list_of_c[21] == 0:
                            Animation.animate_play_card(player_hand.hand[21], screen, game_deck.card_Sprites, FPSCLOCK,
                                                        player_hand_sprites, player_hand.hand, computer_hand.hand, back_of_card,
                                                        middle_pile, Deck.DeckClass.cards, back_of_card_Rect,
                                                        background, background_Rect, True, player_face_up_sprites,
                                                        computer_face_up_sprites, player_table_cards.face_down,
                                                        computer_table_cards.face_down)
                            middle_pile.moveCard(player_hand.hand[21])
                            used22 = 'spent'
                            list_of_c = HandClass.un_flip_all(list_of_c)
                            this = 0

                        elif list_of_c[22] == 0:
                            Animation.animate_play_card(player_hand.hand[22], screen, game_deck.card_Sprites, FPSCLOCK,
                                                        player_hand_sprites, player_hand.hand, computer_hand.hand, back_of_card,
                                                        middle_pile, Deck.DeckClass.cards, back_of_card_Rect,
                                                        background, background_Rect, True, player_face_up_sprites,
                                                        computer_face_up_sprites, player_table_cards.face_down,
                                                        computer_table_cards.face_down)
                            middle_pile.moveCard(player_hand.hand[22])
                            used23 = 'spent'
                            list_of_c = HandClass.un_flip_all(list_of_c)
                            this = 0

                        elif list_of_c[23] == 0:
                            Animation.animate_play_card(player_hand.hand[23], screen, game_deck.card_Sprites, FPSCLOCK,
                                                        player_hand_sprites, player_hand.hand, computer_hand.hand, back_of_card,
                                                        middle_pile, Deck.DeckClass.cards, back_of_card_Rect,
                                                        background, background_Rect, True, player_face_up_sprites,
                                                        computer_face_up_sprites, player_table_cards.face_down,
                                                        computer_table_cards.face_down)
                            middle_pile.moveCard(player_hand.hand[23])
                            used24 = 'spent'
                            list_of_c = HandClass.un_flip_all(list_of_c)
                            this = 0

                        elif list_of_c[24] == 0:
                            Animation.animate_play_card(player_hand.hand[24], screen, game_deck.card_Sprites, FPSCLOCK,
                                                        player_hand_sprites, player_hand.hand, computer_hand.hand, back_of_card,
                                                        middle_pile, Deck.DeckClass.cards, back_of_card_Rect,
                                                        background, background_Rect, True, player_face_up_sprites,
                                                        computer_face_up_sprites, player_table_cards.face_down,
                                                        computer_table_cards.face_down)
                            middle_pile.moveCard(player_hand.hand[24])
                            used25 = 'spent'
                            list_of_c = HandClass.un_flip_all(list_of_c)
                            this = 0
                        # Table Cards for player
                        elif list_of_c_table[0] == 0:
                            Animation.animate_play_card(player_table_cards.face_up[0], screen, game_deck.card_Sprites, FPSCLOCK,
                                                        player_hand_sprites, player_hand.hand, computer_hand.hand, back_of_card,
                                                        middle_pile, Deck.DeckClass.cards, back_of_card_Rect,
                                                        background, background_Rect, True, player_face_up_sprites,
                                                        computer_face_up_sprites, player_table_cards.face_down,
                                                        computer_table_cards.face_down)
                            middle_pile.moveCard(player_table_cards.face_up[0])
                            table1 = 'spent'
                            list_of_c_table = HandClass.un_flip_all(list_of_c_table)
                            this = 0
                        elif list_of_c_table[1] == 0:
                            Animation.animate_play_card(player_table_cards.face_up[1], screen, game_deck.card_Sprites, FPSCLOCK,
                                                        player_hand_sprites, player_hand.hand, computer_hand.hand, back_of_card,
                                                        middle_pile, Deck.DeckClass.cards, back_of_card_Rect,
                                                        background, background_Rect, True, player_face_up_sprites,
                                                        computer_face_up_sprites, player_table_cards.face_down,
                                                        computer_table_cards.face_down)
                            middle_pile.moveCard(player_table_cards.face_up[1])
                            table2 = 'spent'
                            list_of_c_table = HandClass.un_flip_all(list_of_c_table)
                            this = 0
                        elif list_of_c_table[2] == 0:
                            Animation.animate_play_card(player_table_cards.face_up[2], screen, game_deck.card_Sprites, FPSCLOCK,
                                                        player_hand_sprites, player_hand.hand, computer_hand.hand, back_of_card,
                                                        middle_pile, Deck.DeckClass.cards, back_of_card_Rect,
                                                        background, background_Rect, True, player_face_up_sprites,
                                                        computer_face_up_sprites, player_table_cards.face_down,
                                                        computer_table_cards.face_down)
                            middle_pile.moveCard(player_table_cards.face_up[2])
                            table3 = 'spent'
                            list_of_c_table = HandClass.un_flip_all(list_of_c_table)
                            this = 0
                        else:
                            this = 0
                            # continue

            if x in x_pick_up:
                if y in y_pick_up:
                    if len(computer_hand.hand) != 0:
                        this = 0
                    if len(middle_pile.cards_in_middle) > 0:
                        middle_pile = player_hand.pick_up(middle_pile, True)
                        player_hand.rejig()
                        move = False

            # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            # Code to change a card from to and from highlighted
            # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            if x in x_card_1:  # sets up to see if a card in the players hand can be highlighted and used.
                if y in y_card_all:
                    print("Card 1 selected")

                    if player_hand.hand[0] in middle_pile.playable_cards_list:
                        if dblClick1 and pygame.time.get_ticks() - dblClick1 < 600:
                            Animation.animate_play_card(player_hand.hand[0], screen, game_deck.card_Sprites, FPSCLOCK,
                                                        player_hand_sprites, player_hand.hand, computer_hand.hand, back_of_card,
                                                        middle_pile, Deck.DeckClass.cards, back_of_card_Rect,
                                                        background, background_Rect, True, player_face_up_sprites,
                                                        computer_face_up_sprites, player_table_cards.face_down,
                                                        computer_table_cards.face_down)
                            middle_pile.moveCard(player_hand.hand[0])
                            player_hand.hand[0] = None
                            if number_of_player_cards <= 5:
                                game_deck.draw(player_hand.hand, 0)
                            player_hand.rejig()
                            move = False
                        else:
                            dblClick1 = pygame.time.get_ticks()

                        if used1 != 'spent':
                            # C1
                            if list_of_c[0] == 0:
                                list_of_c = HandClass.un_flip_all(list_of_c)

                            elif list_of_c[0] == 1:
                                list_of_c = HandClass.un_flip_all(list_of_c)
                                list_of_c[0] = HandClass.flip_c(list_of_c[0])

            if x in x_card_2:
                if y in y_card_all:
                    print("Card 2 selected")
                    if player_hand.hand[1] in middle_pile.playable_cards_list:
                        if dblClick2 and pygame.time.get_ticks() - dblClick2 < 600:
                            Animation.animate_play_card(player_hand.hand[1], screen, game_deck.card_Sprites, FPSCLOCK,
                                                        player_hand_sprites, player_hand.hand, computer_hand.hand, back_of_card,
                                                        middle_pile, Deck.DeckClass.cards, back_of_card_Rect,
                                                        background, background_Rect, True, player_face_up_sprites,
                                                        computer_face_up_sprites, player_table_cards.face_down,
                                                        computer_table_cards.face_down)
                            middle_pile.moveCard(player_hand.hand[1])
                            player_hand.hand[1] = None
                            if number_of_player_cards <= 5:
                                game_deck.draw(player_hand.hand, 1)
                            player_hand.rejig()
                            move = False
                        else:
                            dblClick2 = pygame.time.get_ticks()

                        if used2 != 'spent':
                            # C2
                            if list_of_c[1] == 0:
                                list_of_c = HandClass.un_flip_all(list_of_c)

                            elif list_of_c[1] == 1:
                                list_of_c = HandClass.un_flip_all(list_of_c)
                                list_of_c[1] = HandClass.flip_c(list_of_c[1])

            if x in x_card_3:
                if y in y_card_all:
                    print("Card 3 selected")
                    if player_hand.hand[2] in middle_pile.playable_cards_list:
                        if dblClick3 and pygame.time.get_ticks() - dblClick3 < 600:
                            Animation.animate_play_card(player_hand.hand[2], screen, game_deck.card_Sprites, FPSCLOCK,
                                                        player_hand_sprites, player_hand.hand, computer_hand.hand, back_of_card,
                                                        middle_pile, Deck.DeckClass.cards, back_of_card_Rect,
                                                        background, background_Rect, True, player_face_up_sprites,
                                                        computer_face_up_sprites, player_table_cards.face_down,
                                                        computer_table_cards.face_down)
                            middle_pile.moveCard(player_hand.hand[2])
                            player_hand.hand[2] = None
                            if number_of_player_cards <= 5:
                                game_deck.draw(player_hand.hand, 2)
                            player_hand.rejig()
                            move = False
                        else:
                            dblClick3 = pygame.time.get_ticks()

                        if used3 != 'spent':
                            # C3
                            if list_of_c[2] == 0:
                                list_of_c = HandClass.un_flip_all(list_of_c)

                            elif list_of_c[2] == 1:
                                list_of_c = HandClass.un_flip_all(list_of_c)
                                list_of_c[2] = HandClass.flip_c(list_of_c[2])

            if x in x_card_4:
                if y in y_card_all:
                    print("Card 4 selected")
                    if player_hand.hand[3] in middle_pile.playable_cards_list:
                        if dblClick4 and pygame.time.get_ticks() - dblClick4 < 600:
                            Animation.animate_play_card(player_hand.hand[3], screen, game_deck.card_Sprites, FPSCLOCK,
                                                        player_hand_sprites, player_hand.hand, computer_hand.hand, back_of_card,
                                                        middle_pile, Deck.DeckClass.cards, back_of_card_Rect,
                                                        background, background_Rect, True, player_face_up_sprites,
                                                        computer_face_up_sprites, player_table_cards.face_down,
                                                        computer_table_cards.face_down)
                            middle_pile.moveCard(player_hand.hand[3])
                            player_hand.hand[3] = None
                            if number_of_player_cards <= 5:
                                game_deck.draw(player_hand.hand, 3)
                            player_hand.rejig()
                            move = False
                        else:
                            dblClick4 = pygame.time.get_ticks()

                        if used4 != 'spent':
                            # C4
                            if list_of_c[3] == 0:
                                list_of_c = HandClass.un_flip_all(list_of_c)

                            elif list_of_c[3] == 1:
                                list_of_c = HandClass.un_flip_all(list_of_c)
                                list_of_c[3] = HandClass.flip_c(list_of_c[3])

            if x in x_card_5:
                if y in y_card_all:
                    print("Card 5 selected")
                    if player_hand.hand[4] in middle_pile.playable_cards_list:
                        if dblClick5 and pygame.time.get_ticks() - dblClick5 < 600:
                            Animation.animate_play_card(player_hand.hand[4], screen, game_deck.card_Sprites, FPSCLOCK,
                                                        player_hand_sprites, player_hand.hand, computer_hand.hand, back_of_card,
                                                        middle_pile, Deck.DeckClass.cards, back_of_card_Rect,
                                                        background, background_Rect, True, player_face_up_sprites,
                                                        computer_face_up_sprites, player_table_cards.face_down,
                                                        computer_table_cards.face_down)
                            middle_pile.moveCard(player_hand.hand[4])
                            player_hand.hand[4] = None
                            if number_of_player_cards <= 5:
                                game_deck.draw(player_hand.hand, 4)
                            player_hand.rejig()
                            move = False
                        else:
                            dblClick5 = pygame.time.get_ticks()
                        if used5 != 'spent':
                            # C5
                            if list_of_c[4] == 0:
                                list_of_c = HandClass.un_flip_all(list_of_c)

                            elif list_of_c[4] == 1:
                                list_of_c = HandClass.un_flip_all(list_of_c)
                                list_of_c[4] = HandClass.flip_c(list_of_c[4])

            if x in x_card_6:
                if y in y_card_all:
                    print("Card 6 selected")
                    if player_hand.hand[5] in middle_pile.playable_cards_list:
                        if dblClick6 and pygame.time.get_ticks() - dblClick6 < 600:
                            Animation.animate_play_card(player_hand.hand[0], screen, game_deck.card_Sprites, FPSCLOCK,
                                                        player_hand_sprites, player_hand.hand, computer_hand.hand, back_of_card,
                                                        middle_pile, Deck.DeckClass.cards, back_of_card_Rect,
                                                        background, background_Rect, True, player_face_up_sprites,
                                                        computer_face_up_sprites, player_table_cards.face_down,
                                                        computer_table_cards.face_down)
                            middle_pile.moveCard(player_hand.hand[5])
                            player_hand.hand[5] = None
                            if number_of_player_cards <= 5:
                                game_deck.draw(player_hand.hand, 5)
                            player_hand.rejig()
                            move = False
                        else:
                            dblClick6 = pygame.time.get_ticks()

                        if used6 != 'spent':
                            # C6
                            if list_of_c[5] == 0:
                                list_of_c = HandClass.un_flip_all(list_of_c)

                            elif list_of_c[5] == 1:
                                list_of_c = HandClass.un_flip_all(list_of_c)
                                list_of_c[5] = HandClass.flip_c(list_of_c[5])

            if x in x_card_7:
                if y in y_card_all:
                    print("Card 7 selected")
                    if player_hand.hand[6] in middle_pile.playable_cards_list:
                        if dblClick7 and pygame.time.get_ticks() - dblClick7 < 600:
                            Animation.animate_play_card(player_hand.hand[6], screen, game_deck.card_Sprites, FPSCLOCK,
                                                        player_hand_sprites, player_hand.hand, computer_hand.hand, back_of_card,
                                                        middle_pile, Deck.DeckClass.cards, back_of_card_Rect,
                                                        background, background_Rect, True, player_face_up_sprites,
                                                        computer_face_up_sprites, player_table_cards.face_down,
                                                        computer_table_cards.face_down)
                            middle_pile.moveCard(player_hand.hand[6])
                            player_hand.hand[6] = None
                            if number_of_player_cards <= 5:
                                game_deck.draw(player_hand.hand, 6)
                            player_hand.rejig()
                            move = False
                        else:
                            dblClick7 = pygame.time.get_ticks()

                        if used7 != 'spent':
                            # C7
                            if list_of_c[6] == 0:
                                list_of_c = HandClass.un_flip_all(list_of_c)

                            elif list_of_c[6] == 1:
                                list_of_c = HandClass.un_flip_all(list_of_c)
                                list_of_c[6] = HandClass.flip_c(list_of_c[6])

            if x in x_card_8:
                if y in y_card_all:
                    print("Card 8 selected")
                    if player_hand.hand[7] in middle_pile.playable_cards_list:
                        if dblClick8 and pygame.time.get_ticks() - dblClick8 < 600:
                            Animation.animate_play_card(player_hand.hand[7], screen, game_deck.card_Sprites, FPSCLOCK,
                                                        player_hand_sprites, player_hand.hand, computer_hand.hand, back_of_card,
                                                        middle_pile, Deck.DeckClass.cards, back_of_card_Rect,
                                                        background, background_Rect, True, player_face_up_sprites,
                                                        computer_face_up_sprites, player_table_cards.face_down,
                                                        computer_table_cards.face_down)
                            middle_pile.moveCard(player_hand.hand[7])
                            player_hand.hand[7] = None
                            if number_of_player_cards <= 5:
                                game_deck.draw(player_hand.hand, 7)
                            player_hand.rejig()
                            move = False
                        else:
                            dblClick8 = pygame.time.get_ticks()

                        if used8 != 'spent':
                            # C8
                            if list_of_c[7] == 0:
                                list_of_c = HandClass.un_flip_all(list_of_c)
                            elif list_of_c[7] == 1:
                                list_of_c = HandClass.un_flip_all(list_of_c)
                                list_of_c[7] = HandClass.flip_c(list_of_c[7])

            if x in x_card_9:
                if y in y_card_all:
                    # Not needed to move turn on, just needed to remove rules from the screen
                    turn += 1
                    print("Card 9 selected")
                    if player_hand.hand[8] in middle_pile.playable_cards_list:
                        if dblClick9 and pygame.time.get_ticks() - dblClick9 < 600:
                            Animation.animate_play_card(player_hand.hand[8], screen, game_deck.card_Sprites, FPSCLOCK,
                                                        player_hand_sprites, player_hand.hand, computer_hand.hand, back_of_card,
                                                        middle_pile, Deck.DeckClass.cards, back_of_card_Rect,
                                                        background, background_Rect, True, player_face_up_sprites,
                                                        computer_face_up_sprites, player_table_cards.face_down,
                                                        computer_table_cards.face_down)
                            middle_pile.moveCard(player_hand.hand[8])
                            player_hand.hand[8] = None
                            if number_of_player_cards <= 5:
                                game_deck.draw(player_hand.hand, 8)
                            player_hand.rejig()
                            move = False
                        else:
                            dblClick9 = pygame.time.get_ticks()

                        if used9 != 'spent':
                            # C9
                            if list_of_c[8] == 0:
                                list_of_c = HandClass.un_flip_all(list_of_c)

                            elif list_of_c[8] == 1:
                                list_of_c = HandClass.un_flip_all(list_of_c)
                                list_of_c[8] = HandClass.flip_c(list_of_c[8])

            if x in x_card_10:
                if y in y_card_all:
                    # turn += 1
                    print("Card 10 selected")
                    if player_hand.hand[9] in middle_pile.playable_cards_list:
                        if dblClick9 and pygame.time.get_ticks() - dblClick9 < 600:
                            Animation.animate_play_card(player_hand.hand[9], screen, game_deck.card_Sprites, FPSCLOCK,
                                                        player_hand_sprites, player_hand.hand, computer_hand.hand, back_of_card,
                                                        middle_pile, Deck.DeckClass.cards, back_of_card_Rect,
                                                        background, background_Rect, True, player_face_up_sprites,
                                                        computer_face_up_sprites, player_table_cards.face_down,
                                                        computer_table_cards.face_down)
                            middle_pile.moveCard(player_hand.hand[9])
                            used14 = 'spent'
                            player_hand.hand[13] = None
                            if number_of_player_cards <= 5:
                                game_deck.draw(player_hand.hand, 9)
                            player_hand.rejig()
                            used14 = ""
                            move = False
                        else:
                            dblClick9 = pygame.time.get_ticks()
                            print("10 here")

                        if used10 != 'spent':
                            # C10
                            if list_of_c[9] == 0:
                                list_of_c = HandClass.un_flip_all(list_of_c)

                            elif list_of_c[9] == 1:
                                list_of_c = HandClass.un_flip_all(list_of_c)
                                list_of_c[9] = HandClass.flip_c(list_of_c[9])

            if x in x_card_11:
                if y in y_card_all:
                    # turn += 1
                    print("Card 11 selected")
                    if player_hand.hand[10] in middle_pile.playable_cards_list:
                        if dblClick10 and pygame.time.get_ticks() - dblClick10 < 600:
                            Animation.animate_play_card(player_hand.hand[10], screen, game_deck.card_Sprites, FPSCLOCK,
                                                        player_hand_sprites, player_hand.hand, computer_hand.hand, back_of_card,
                                                        middle_pile, Deck.DeckClass.cards, back_of_card_Rect,
                                                        background, background_Rect, True, player_face_up_sprites,
                                                        computer_face_up_sprites, player_table_cards.face_down,
                                                        computer_table_cards.face_down)
                            middle_pile.moveCard(player_hand.hand[10])
                            used14 = 'spent'
                            player_hand.hand[13] = None
                            if number_of_player_cards <= 5:
                                game_deck.draw(player_hand.hand, 10)
                            player_hand.rejig()
                            used14 = ""
                            move = False
                        else:
                            dblClick10 = pygame.time.get_ticks()
                            print("11 here")

                        if used11 != 'spent':
                            # C11
                            if list_of_c[10] == 0:
                                list_of_c = HandClass.un_flip_all(list_of_c)

                            elif list_of_c[10] == 1:
                                list_of_c = HandClass.un_flip_all(list_of_c)
                                list_of_c[10] = HandClass.flip_c(list_of_c[10])

            if x in x_card_12:
                if y in y_card_all:
                    # turn += 1
                    print("Card 12 selected")
                    if player_hand.hand[11] in middle_pile.playable_cards_list:
                        if dblClick11 and pygame.time.get_ticks() - dblClick11 < 600:
                            Animation.animate_play_card(player_hand.hand[11], screen, game_deck.card_Sprites, FPSCLOCK,
                                                        player_hand_sprites, player_hand.hand, computer_hand.hand, back_of_card,
                                                        middle_pile, Deck.DeckClass.cards, back_of_card_Rect,
                                                        background, background_Rect, True, player_face_up_sprites,
                                                        computer_face_up_sprites, player_table_cards.face_down,
                                                        computer_table_cards.face_down)
                            middle_pile.moveCard(player_hand.hand[11])
                            used14 = 'spent'
                            player_hand.hand[13] = None
                            if number_of_player_cards <= 5:
                                game_deck.draw(player_hand.hand, 11)
                            player_hand.rejig()
                            used14 = ""
                            move = False
                        else:
                            dblClick11 = pygame.time.get_ticks()
                            print("12 here")

                        if used12 != 'spent':
                            # C12
                            if list_of_c[11] == 0:
                                list_of_c = HandClass.un_flip_all(list_of_c)

                            elif list_of_c[11] == 1:
                                list_of_c = HandClass.un_flip_all(list_of_c)
                                list_of_c[11] = HandClass.flip_c(list_of_c[11])

            if x in x_card_13:
                if y in y_card_all:
                    # turn += 1
                    print("Card 13 selected")
                    if player_hand.hand[12] in middle_pile.playable_cards_list:
                        if dblClick12 and pygame.time.get_ticks() - dblClick12 < 600:
                            Animation.animate_play_card(player_hand.hand[12], screen, game_deck.card_Sprites, FPSCLOCK,
                                                        player_hand_sprites, player_hand.hand, computer_hand.hand, back_of_card,
                                                        middle_pile, Deck.DeckClass.cards, back_of_card_Rect,
                                                        background, background_Rect, True, player_face_up_sprites,
                                                        computer_face_up_sprites, player_table_cards.face_down,
                                                        computer_table_cards.face_down)
                            middle_pile.moveCard(player_hand.hand[12])
                            used14 = 'spent'
                            player_hand.hand[13] = None
                            if number_of_player_cards <= 5:
                                game_deck.draw(player_hand.hand, 12)
                            player_hand.rejig()
                            used14 = ""
                            move = False
                        else:
                            print("13 here")
                            dblClick12 = pygame.time.get_ticks()

                        if used13 != 'spent':
                            # C13
                            if list_of_c[12] == 0:
                                list_of_c = HandClass.un_flip_all(list_of_c)

                            elif list_of_c[12] == 1:
                                list_of_c = HandClass.un_flip_all(list_of_c)
                                list_of_c[12] = HandClass.flip_c(list_of_c[12])

            if x in x_card_14:
                if y in y_card_all:
                    # turn += 1
                    print("Card 14 selected")
                    if player_hand.hand[13] in middle_pile.playable_cards_list:
                        if dblClick14 and pygame.time.get_ticks() - dblClick14 < 600:
                            Animation.animate_play_card(player_hand.hand[13], screen, game_deck.card_Sprites, FPSCLOCK,
                                                        player_hand_sprites, player_hand.hand, computer_hand.hand, back_of_card,
                                                        middle_pile, Deck.DeckClass.cards, back_of_card_Rect,
                                                        background, background_Rect, True, player_face_up_sprites,
                                                        computer_face_up_sprites, player_table_cards.face_down,
                                                        computer_table_cards.face_down)
                            middle_pile.moveCard(player_hand.hand[13])
                            used14 = 'spent'
                            player_hand.hand[13] = None
                            if number_of_player_cards <= 5:
                                game_deck.draw(player_hand.hand, 13)
                            player_hand.rejig()
                            used14 = ""
                            move = False
                        else:
                            dblClick14 = pygame.time.get_ticks()
                            print("14 here")

                        if used14 != 'spent':
                            # C14
                            if list_of_c[13] == 0:
                                list_of_c = HandClass.un_flip_all(list_of_c)

                            elif list_of_c[13] == 1:
                                list_of_c = HandClass.un_flip_all(list_of_c)
                                list_of_c[13] = HandClass.flip_c(list_of_c[13])
            if x in x_card_15:
                if y in y_card_all:
                    print("Card 15 selected")
                    if player_hand.hand[14] in middle_pile.playable_cards_list:
                        if dblClick15 and pygame.time.get_ticks() - dblClick15 < 600:
                            Animation.animate_play_card(player_hand.hand[14], screen, game_deck.card_Sprites, FPSCLOCK,
                                                        player_hand_sprites, player_hand.hand, computer_hand.hand, back_of_card,
                                                        middle_pile, Deck.DeckClass.cards, back_of_card_Rect,
                                                        background, background_Rect, True, player_face_up_sprites,
                                                        computer_face_up_sprites, player_table_cards.face_down,
                                                        computer_table_cards.face_down)
                            middle_pile.moveCard(player_hand.hand[14])
                            player_hand.hand[14] = None
                            if number_of_player_cards <= 5:
                                game_deck.draw(player_hand.hand, 14)
                            player_hand.rejig()
                            move = False
                        else:
                            dblClick15 = pygame.time.get_ticks()
                            print("14 here")

                        if used15 != 'spent':
                            # C15
                            if list_of_c[14] == 0:
                                list_of_c = HandClass.un_flip_all(list_of_c)

                            elif list_of_c[14] == 1:
                                list_of_c = HandClass.un_flip_all(list_of_c)
                                list_of_c[14] = HandClass.flip_c(list_of_c[14])
            if x in x_card_16:
                if y in y_card_all:
                    print("Card 16 selected")
                    if player_hand.hand[15] in middle_pile.playable_cards_list:
                        if dblClick16 and pygame.time.get_ticks() - dblClick16 < 600:
                            Animation.animate_play_card(player_hand.hand[15], screen, game_deck.card_Sprites, FPSCLOCK,
                                                        player_hand_sprites, player_hand.hand, computer_hand.hand, back_of_card,
                                                        middle_pile, Deck.DeckClass.cards, back_of_card_Rect,
                                                        background, background_Rect, True, player_face_up_sprites,
                                                        computer_face_up_sprites, player_table_cards.face_down,
                                                        computer_table_cards.face_down)
                            middle_pile.moveCard(player_hand.hand[15])
                            player_hand.hand[15] = None
                            if number_of_player_cards <= 5:
                                game_deck.draw(player_hand.hand, 15)
                            player_hand.rejig()
                            move = False
                        else:
                            dblClick16 = pygame.time.get_ticks()
                            print("14 here")

                        if used16 != 'spent':
                            # C16
                            if list_of_c[15] == 0:
                                list_of_c = HandClass.un_flip_all(list_of_c)

                            elif list_of_c[15] == 1:
                                list_of_c = HandClass.un_flip_all(list_of_c)
                                list_of_c[15] = HandClass.flip_c(list_of_c[15])

            if x in x_card_17:
                if y in y_card_all:
                    print("Card 17 selected")
                    if player_hand.hand[16] in middle_pile.playable_cards_list:
                        if dblClick17 and pygame.time.get_ticks() - dblClick17 < 600:
                            Animation.animate_play_card(player_hand.hand[16], screen, game_deck.card_Sprites, FPSCLOCK,
                                                        player_hand_sprites, player_hand.hand, computer_hand.hand, back_of_card,
                                                        middle_pile, Deck.DeckClass.cards, back_of_card_Rect,
                                                        background, background_Rect, True, player_face_up_sprites,
                                                        computer_face_up_sprites, player_table_cards.face_down,
                                                        computer_table_cards.face_down)
                            middle_pile.moveCard(player_hand.hand[16])
                            player_hand.hand[16] = None
                            if number_of_player_cards <= 5:
                                game_deck.draw(player_hand.hand, 16)
                            player_hand.rejig()
                            move = False
                        else:
                            dblClick17 = pygame.time.get_ticks()
                            print("14 here")

                        if used17 != 'spent':
                            # C17
                            if list_of_c[16] == 0:
                                list_of_c = HandClass.un_flip_all(list_of_c)

                            elif list_of_c[16] == 1:
                                list_of_c = HandClass.un_flip_all(list_of_c)
                                list_of_c[16] = HandClass.flip_c(list_of_c[16])
            if x in x_card_18:
                if y in y_card_all:
                    print("Card 18 selected")
                    if player_hand.hand[17] in middle_pile.playable_cards_list:
                        if dblClick18 and pygame.time.get_ticks() - dblClick18 < 600:
                            Animation.animate_play_card(player_hand.hand[17], screen, game_deck.card_Sprites, FPSCLOCK,
                                                        player_hand_sprites, player_hand.hand, computer_hand.hand, back_of_card,
                                                        middle_pile, Deck.DeckClass.cards, back_of_card_Rect,
                                                        background, background_Rect, True, player_face_up_sprites,
                                                        computer_face_up_sprites, player_table_cards.face_down,
                                                        computer_table_cards.face_down)
                            middle_pile.moveCard(player_hand.hand[17])
                            player_hand.hand[17] = None
                            if number_of_player_cards <= 5:
                                game_deck.draw(player_hand.hand, 17)
                            player_hand.rejig()
                            move = False
                        else:
                            dblClick18 = pygame.time.get_ticks()
                            print("14 here")

                        if used18 != 'spent':
                            # C18
                            if list_of_c[17] == 0:
                                list_of_c = HandClass.un_flip_all(list_of_c)

                            elif list_of_c[17] == 1:
                                list_of_c = HandClass.un_flip_all(list_of_c)
                                list_of_c[17] = HandClass.flip_c(list_of_c[17])

            if x in x_card_19:
                if y in y_card_all:
                    print("Card 19 selected")
                    if player_hand.hand[18] in middle_pile.playable_cards_list:
                        if dblClick19 and pygame.time.get_ticks() - dblClick19 < 600:
                            Animation.animate_play_card(player_hand.hand[18], screen, game_deck.card_Sprites, FPSCLOCK,
                                                        player_hand_sprites, player_hand.hand, computer_hand.hand, back_of_card,
                                                        middle_pile, Deck.DeckClass.cards, back_of_card_Rect,
                                                        background, background_Rect, True, player_face_up_sprites,
                                                        computer_face_up_sprites, player_table_cards.face_down,
                                                        computer_table_cards.face_down)
                            middle_pile.moveCard(player_hand.hand[18])
                            player_hand.hand[18] = None
                            if number_of_player_cards <= 5:
                                game_deck.draw(player_hand.hand, 18)
                            player_hand.rejig()
                            move = False
                        else:
                            dblClick19 = pygame.time.get_ticks()
                            print("14 here")

                        if used19 != 'spent':
                            # C19
                            if list_of_c[18] == 0:
                                list_of_c = HandClass.un_flip_all(list_of_c)

                            elif list_of_c[18] == 1:
                                list_of_c = HandClass.un_flip_all(list_of_c)
                                list_of_c[18] = HandClass.flip_c(list_of_c[18])

            if x in x_card_20:
                if y in y_card_all:
                    print("Card 20 selected")
                    if player_hand.hand[19] in middle_pile.playable_cards_list:
                        if dblClick20 and pygame.time.get_ticks() - dblClick20 < 600:
                            Animation.animate_play_card(player_hand.hand[19], screen, game_deck.card_Sprites, FPSCLOCK,
                                                        player_hand_sprites, player_hand.hand, computer_hand.hand, back_of_card,
                                                        middle_pile, Deck.DeckClass.cards, back_of_card_Rect,
                                                        background, background_Rect, True, player_face_up_sprites,
                                                        computer_face_up_sprites, player_table_cards.face_down,
                                                        computer_table_cards.face_down)
                            middle_pile.moveCard(player_hand.hand[19])
                            player_hand.hand[19] = None
                            if number_of_player_cards <= 5:
                                game_deck.draw(player_hand.hand, 19)
                            player_hand.rejig()
                            move = False
                        else:
                            dblClick20 = pygame.time.get_ticks()
                            print("14 here")

                        if used20 != 'spent':
                            # C20
                            if list_of_c[19] == 0:
                                list_of_c = HandClass.un_flip_all(list_of_c)

                            elif list_of_c[19] == 1:
                                list_of_c = HandClass.un_flip_all(list_of_c)
                                list_of_c[19] = HandClass.flip_c(list_of_c[19])

            if x in x_card_21:
                if y in y_card_all:
                    print("Card 21 selected")
                    if player_hand.hand[20] in middle_pile.playable_cards_list:
                        if dblClick21 and pygame.time.get_ticks() - dblClick21 < 600:
                            Animation.animate_play_card(player_hand.hand[20], screen, game_deck.card_Sprites, FPSCLOCK,
                                                        player_hand_sprites, player_hand.hand, computer_hand.hand, back_of_card,
                                                        middle_pile, Deck.DeckClass.cards, back_of_card_Rect,
                                                        background, background_Rect, True, player_face_up_sprites,
                                                        computer_face_up_sprites, player_table_cards.face_down,
                                                        computer_table_cards.face_down)
                            middle_pile.moveCard(player_hand.hand[20])
                            player_hand.hand[20] = None
                            if number_of_player_cards <= 5:
                                game_deck.draw(player_hand.hand, 20)
                            player_hand.rejig()
                            move = False
                        else:
                            dblClick21 = pygame.time.get_ticks()
                            print("14 here")

                        if used21 != 'spent':
                            # C21
                            if list_of_c[20] == 0:
                                list_of_c = HandClass.un_flip_all(list_of_c)

                            elif list_of_c[20] == 1:
                                list_of_c = HandClass.un_flip_all(list_of_c)
                                list_of_c[20] = HandClass.flip_c(list_of_c[20])
            if x in x_card_22:
                if y in y_card_all:
                    print("Card 22 selected")
                    if player_hand.hand[21] in middle_pile.playable_cards_list:
                        if dblClick22 and pygame.time.get_ticks() - dblClick22 < 600:
                            Animation.animate_play_card(player_hand.hand[21], screen, game_deck.card_Sprites, FPSCLOCK,
                                                        player_hand_sprites, player_hand.hand, computer_hand.hand, back_of_card,
                                                        middle_pile, Deck.DeckClass.cards, back_of_card_Rect,
                                                        background, background_Rect, True, player_face_up_sprites,
                                                        computer_face_up_sprites, player_table_cards.face_down,
                                                        computer_table_cards.face_down)
                            middle_pile.moveCard(player_hand.hand[21])
                            player_hand.hand[21] = None
                            if number_of_player_cards <= 5:
                                game_deck.draw(player_hand.hand, 21)
                            player_hand.rejig()
                            move = False
                        else:
                            dblClick22 = pygame.time.get_ticks()

                        if used22 != 'spent':
                            # C22
                            if list_of_c[21] == 0:
                                list_of_c = HandClass.un_flip_all(list_of_c)

                            elif list_of_c[21] == 1:
                                list_of_c = HandClass.un_flip_all(list_of_c)
                                list_of_c[21] = HandClass.flip_c(list_of_c[21])

            if x in x_card_23:
                if y in y_card_all:
                    print("Card 23 selected")
                    if player_hand.hand[22] in middle_pile.playable_cards_list:
                        if dblClick23 and pygame.time.get_ticks() - dblClick23 < 600:
                            Animation.animate_play_card(player_hand.hand[22], screen, game_deck.card_Sprites, FPSCLOCK,
                                                        player_hand_sprites, player_hand.hand, computer_hand.hand, back_of_card,
                                                        middle_pile, Deck.DeckClass.cards, back_of_card_Rect,
                                                        background, background_Rect, True, player_face_up_sprites,
                                                        computer_face_up_sprites, player_table_cards.face_down,
                                                        computer_table_cards.face_down)
                            middle_pile.moveCard(player_hand.hand[22])
                            player_hand.hand[22] = None
                            if number_of_player_cards <= 5:
                                game_deck.draw(player_hand.hand, 22)
                            player_hand.rejig()
                            move = False
                        else:
                            dblClick23 = pygame.time.get_ticks()

                        if used23 != 'spent':
                            # C23
                            if list_of_c[22] == 0:
                                list_of_c = HandClass.un_flip_all(list_of_c)

                            elif list_of_c[22] == 1:
                                list_of_c = HandClass.un_flip_all(list_of_c)
                                list_of_c[22] = HandClass.flip_c(list_of_c[22])
            if x in x_card_24:
                if y in y_card_all:
                    print("Card 24 selected")
                    if player_hand.hand[23] in middle_pile.playable_cards_list:
                        if dblClick24 and pygame.time.get_ticks() - dblClick24 < 600:
                            Animation.animate_play_card(player_hand.hand[23], screen, game_deck.card_Sprites, FPSCLOCK,
                                                        player_hand_sprites, player_hand.hand, computer_hand.hand, back_of_card,
                                                        middle_pile, Deck.DeckClass.cards, back_of_card_Rect,
                                                        background, background_Rect, True, player_face_up_sprites,
                                                        computer_face_up_sprites, player_table_cards.face_down,
                                                        computer_table_cards.face_down)
                            middle_pile.moveCard(player_hand.hand[23])
                            player_hand.hand[23] = None
                            if number_of_player_cards <= 5:
                                game_deck.draw(player_hand.hand, 23)
                            player_hand.rejig()
                            move = False
                        else:
                            dblClick24 = pygame.time.get_ticks()

                        if used24 != 'spent':
                            # C21
                            if list_of_c[23] == 0:
                                list_of_c = HandClass.un_flip_all(list_of_c)

                            elif list_of_c[23] == 1:
                                list_of_c = HandClass.un_flip_all(list_of_c)
                                list_of_c[23] = HandClass.flip_c(list_of_c[23])
            if x in x_card_25:
                if y in y_card_all:
                    print("Card 25 selected")
                    if player_hand.hand[24] in middle_pile.playable_cards_list:
                        if dblClick25 and pygame.time.get_ticks() - dblClick25 < 600:
                            Animation.animate_play_card(player_hand.hand[24], screen, game_deck.card_Sprites, FPSCLOCK,
                                                        player_hand_sprites, player_hand.hand, computer_hand.hand, back_of_card,
                                                        middle_pile, Deck.DeckClass.cards, back_of_card_Rect,
                                                        background, background_Rect, True, player_face_up_sprites,
                                                        computer_face_up_sprites, player_table_cards.face_down,
                                                        computer_table_cards.face_down)
                            middle_pile.moveCard(player_hand.hand[24])
                            player_hand.hand[24] = None
                            if number_of_player_cards <= 5:
                                game_deck.draw(player_hand.hand, 24)
                            player_hand.rejig()
                            move = False
                        else:
                            dblClick25 = pygame.time.get_ticks()

                        if used25 != 'spent':
                            # C25
                            if list_of_c[24] == 0:
                                list_of_c = HandClass.un_flip_all(list_of_c)

                            elif list_of_c[24] == 1:
                                list_of_c = HandClass.un_flip_all(list_of_c)
                                list_of_c[24] = HandClass.flip_c(list_of_c[24])

            # Player Table Cards
            # Face Up
            if all(card is None for card in player_hand.hand):
                if any(card is not None for card in player_table_cards.face_up):
                    if x in x_table_1:
                        if y in y_table_cards:
                            print("Table card 1 selected")
                            if player_table_cards.face_up[0] in middle_pile.playable_cards_list:
                                if table1 != 'spent':
                                    if list_of_c_table[0] == 0:
                                        list_of_c_table = HandClass.un_flip_all(list_of_c_table)

                                    elif list_of_c_table[0] == 1:
                                        list_of_c_table = HandClass.un_flip_all(list_of_c_table)
                                        list_of_c_table[0] = HandClass.flip_c(list_of_c_table[0])

                    if x in x_table_2:
                        if y in y_table_cards:
                            print("Table card 2 selected")
                            if player_table_cards.face_up[1] in middle_pile.playable_cards_list:
                                if table2 != 'spent':
                                    if list_of_c_table[1] == 0:
                                        list_of_c_table = HandClass.un_flip_all(list_of_c_table)

                                    elif list_of_c_table[1] == 1:
                                        list_of_c_table = HandClass.un_flip_all(list_of_c_table)
                                        list_of_c_table[1] = HandClass.flip_c(list_of_c_table[1])

                    if x in x_table_3:
                        if y in y_table_cards:
                            print("Table card 3 selected")
                            if player_table_cards.face_up[2] in middle_pile.playable_cards_list:
                                if table3 != 'spent':
                                    if list_of_c_table[2] == 0:
                                        list_of_c_table = HandClass.un_flip_all(list_of_c_table)

                                    elif list_of_c_table[2] == 1:
                                        list_of_c_table = HandClass.un_flip_all(list_of_c_table)
                                        list_of_c_table[2] = HandClass.flip_c(list_of_c_table[2])

                # Face Down
                elif any(card is not None for card in player_table_cards.face_down):
                    if x in x_table_1:
                        if y in y_table_cards:
                            Animation.animate_play_card(player_table_cards.face_down[0], screen, game_deck.card_Sprites, FPSCLOCK,
                                                        player_hand_sprites, player_hand.hand, computer_hand.hand, back_of_card,
                                                        middle_pile, Deck.DeckClass.cards, back_of_card_Rect,
                                                        background, background_Rect, True, player_face_up_sprites,
                                                        computer_face_up_sprites, player_table_cards.face_down,
                                                        computer_table_cards.face_down)
                            returnList = player_table_cards.play_face_down_card(0, player_hand, middle_pile)
                            player_hand = returnList[0]
                            if any(card is not None for card in player_hand.hand):
                                Misc.render_font(font, screen, "Your card was not a valid move, you picked up the pile")
                                pygame.time.delay(2000)
                            middle_pile = returnList[1]
                            move = False
                    if x in x_table_2:
                        if y in y_table_cards:
                            Animation.animate_play_card(player_table_cards.face_down[1], screen, game_deck.card_Sprites, FPSCLOCK,
                                                        player_hand_sprites, player_hand.hand, computer_hand.hand, back_of_card,
                                                        middle_pile, Deck.DeckClass.cards, back_of_card_Rect,
                                                        background, background_Rect, True, player_face_up_sprites,
                                                        computer_face_up_sprites, player_table_cards.face_down,
                                                        computer_table_cards.face_down)
                            returnList = player_table_cards.play_face_down_card(1, player_hand, middle_pile)
                            player_hand = returnList[0]
                            if any(card is not None for card in player_hand.hand):
                                Misc.render_font(font, screen, "Your card was not a valid move, you picked up the pile")
                                pygame.time.delay(2000)
                            middle_pile = returnList[1]
                            move = False
                    if x in x_table_3:
                        if y in y_table_cards:
                            Animation.animate_play_card(player_table_cards.face_down[2], screen, game_deck.card_Sprites, FPSCLOCK,
                                                        player_hand_sprites, player_hand.hand, computer_hand.hand, back_of_card,
                                                        middle_pile, Deck.DeckClass.cards, back_of_card_Rect,
                                                        background, background_Rect, True, player_face_up_sprites,
                                                        computer_face_up_sprites, player_table_cards.face_down,
                                                        computer_table_cards.face_down)
                            returnList = player_table_cards.play_face_down_card(2, player_hand, middle_pile)
                            player_hand = returnList[0]
                            if any(card is not None for card in player_hand.hand):
                                Misc.render_font(font, screen, "Your card was not a valid move, you picked up the pile")
                                pygame.time.delay(2000)
                            middle_pile = returnList[1]
                            move = False

            # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

            # Code to draw a card and end move
            # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

            if used1 == "spent":
                player_hand.hand[0] = None
                if number_of_player_cards <= 5:
                    game_deck.draw(player_hand.hand, 0)
                player_hand.rejig()
                used1 = ""
                move = False
            if used2 == "spent":
                player_hand.hand[1] = None
                if number_of_player_cards <= 5:
                    game_deck.draw(player_hand.hand, 1)
                player_hand.rejig()
                used2 = ""
                move = False
            if used3 == "spent":
                player_hand.hand[2] = None
                if number_of_player_cards <= 5:
                    game_deck.draw(player_hand.hand, 2)
                player_hand.rejig()
                used3 = ""
                move = False
            if used4 == "spent":
                player_hand.hand[3] = None
                if number_of_player_cards <= 5:
                    game_deck.draw(player_hand.hand, 3)
                player_hand.rejig()
                used4 = ""
                move = False
            if used5 == "spent":
                player_hand.hand[4] = None
                if number_of_player_cards <= 5:
                    game_deck.draw(player_hand.hand, 4)
                player_hand.rejig()
                used5 = ""
                move = False
            if used6 == "spent":
                player_hand.hand[5] = None
                if number_of_player_cards <= 5:
                    game_deck.draw(player_hand.hand, 5)
                player_hand.rejig()
                used6 = ""
                move = False
            if used7 == "spent":
                player_hand.hand[6] = None
                if number_of_player_cards <= 5:
                    game_deck.draw(player_hand.hand, 6)
                player_hand.rejig()
                used7 = ""
                move = False
            if used8 == "spent":
                player_hand.hand[7] = None
                if number_of_player_cards <= 5:
                    game_deck.draw(player_hand.hand, 7)
                player_hand.rejig()
                used8 = ""
                move = False
            if used9 == "spent":
                player_hand.hand[8] = None
                if number_of_player_cards <= 5:
                    game_deck.draw(player_hand.hand, 8)
                player_hand.rejig()
                used9 = ""
                move = False
            if used10 == "spent":
                player_hand.hand[9] = None
                if number_of_player_cards <= 5:
                    game_deck.draw(player_hand.hand, 9)
                player_hand.rejig()
                used10 = ""
                move = False
            if used11 == "spent":
                player_hand.hand[10] = None
                if number_of_player_cards <= 5:
                    game_deck.draw(player_hand.hand, 10)
                player_hand.rejig()
                used11 = ""
                move = False
            if used12 == "spent":
                player_hand.hand[11] = None
                if number_of_player_cards <= 5:
                    game_deck.draw(player_hand.hand, 11)
                player_hand.rejig()
                used12 = ""
                move = False
            if used13 == "spent":
                player_hand.hand[12] = None
                if number_of_player_cards <= 5:
                    game_deck.draw(player_hand.hand, 12)
                player_hand.rejig()
                used13 = ""
                move = False
            if used14 == "spent":
                player_hand.hand[13] = None
                if number_of_player_cards <= 5:
                    game_deck.draw(player_hand.hand, 13)
                player_hand.rejig()
                used14 = ""
                move = False
            if used15 == "spent":
                player_hand.hand[14] = None
                if number_of_player_cards <= 5:
                    game_deck.draw(player_hand.hand, 14)
                player_hand.rejig()
                used15 = ""
                move = False
            if used16 == "spent":
                player_hand.hand[15] = None
                if number_of_player_cards <= 5:
                    game_deck.draw(player_hand.hand, 15)
                player_hand.rejig()
                used16 = ""
                move = False
            if used17 == "spent":
                player_hand.hand[16] = None
                if number_of_player_cards <= 5:
                    game_deck.draw(player_hand.hand, 16)
                player_hand.rejig()
                used17 = ""
                move = False
            if used18 == "spent":
                player_hand.hand[17] = None
                if number_of_player_cards <= 5:
                    game_deck.draw(player_hand.hand, 17)
                player_hand.rejig()
                used18 = ""
                move = False
            if used19 == "spent":
                player_hand.hand[18] = None
                if number_of_player_cards <= 5:
                    game_deck.draw(player_hand.hand, 18)
                player_hand.rejig()
                used19 = ""
                move = False
            if used20 == "spent":
                player_hand.hand[19] = None
                if number_of_player_cards <= 5:
                    game_deck.draw(player_hand.hand, 19)
                player_hand.rejig()
                used20 = ""
                move = False
            if used21 == "spent":
                player_hand.hand[20] = None
                if number_of_player_cards <= 5:
                    game_deck.draw(player_hand.hand, 20)
                player_hand.rejig()
                used21 = ""
                move = False
            if used22 == "spent":
                player_hand.hand[21] = None
                if number_of_player_cards <= 5:
                    game_deck.draw(player_hand.hand, 21)
                player_hand.rejig()
                used22 = ""
                move = False
            if used23 == "spent":
                player_hand.hand[22] = None
                if number_of_player_cards <= 5:
                    game_deck.draw(player_hand.hand, 22)
                player_hand.rejig()
                used23 = ""
                move = False
            if used24 == "spent":
                player_hand.hand[23] = None
                if number_of_player_cards <= 5:
                    game_deck.draw(player_hand.hand, 23)
                player_hand.rejig()
                used24 = ""
                move = False
            if used25 == "spent":
                player_hand.hand[24] = None
                if number_of_player_cards <= 5:
                    game_deck.draw(player_hand.hand, 24)
                player_hand.rejig()
                used25 = ""
                move = False

            if table1 == "spent":
                player_table_cards.face_up[0] = None
                table1 = "used"
                move = False
            if table2 == "spent":
                player_table_cards.face_up[1] = None
                table2 = "used"
                move = False
            if table3 == "spent":
                player_table_cards.face_up[2] = None
                table3 = "used"
                move = False

            # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # This logic is for the computers turn
    if not move:
        fromHand = False
        fromTableFaceUp = False
        fromTableFaceDown = False
        middle_pile.PlayableCards()
        # print("Playable list before passed to Computer AI =", middle_pile.playable_cards_list)

        # Get the card the computer will play
        if len(computer_hand.hand) != 0:
            computer_move = ComputerAI.play_a_card(computer_hand.hand, middle_pile.playable_cards_list)
            fromHand = True

        elif any(card is not None for card in computer_table_cards.face_up):
            computer_move = ComputerAI.play_a_card(computer_table_cards.face_up, middle_pile.playable_cards_list)
            fromTableFaceUp = True

        elif any(card is not None for card in computer_table_cards.face_down):
            computer_move = ComputerAI.play_face_down_card(computer_table_cards.face_down)
            fromTableFaceDown = True

        if computer_move is not None:

            # Play moving the card to the middle, needs lots of variables for rendering
            Animation.animate_play_card(computer_move, screen, game_deck.card_Sprites, FPSCLOCK,
                                        player_hand_sprites, player_hand.hand, computer_hand.hand,
                                        back_of_card, middle_pile, Deck.DeckClass.cards,
                                        back_of_card_Rect, background, background_Rect, False, player_face_up_sprites,
                                        computer_face_up_sprites, player_table_cards.face_down, computer_table_cards.face_down)
            # Put the card on the pile of cards
            middle_pile.moveCard(computer_move)
            if fromHand:
                # What position said card is in
                comp_move_position = computer_hand.hand.index(computer_move)
                # remove the card from the hand
                computer_hand.hand[comp_move_position] = None

                if len(computer_hand.hand) <= 5:
                    # draw another card
                    print("The computer is drawing a card")
                    game_deck.draw(computer_hand.hand, comp_move_position)

                # if no cards can be added
                if computer_hand.hand[comp_move_position] is None:
                    computer_hand.hand.pop(comp_move_position)

            if fromTableFaceUp:
                comp_move_position = computer_table_cards.face_up.index(computer_move)
                computer_table_cards.face_up[comp_move_position] = None

            if fromTableFaceDown:
                comp_move_position = computer_table_cards.face_down.index(computer_move)
                computer_table_cards.face_down[comp_move_position] = None

                if computer_move not in middle_pile.playable_cards_list:
                    print("The computers random choice was incorrect, picking up the pile")
                    middle_pile = computer_hand.pick_up(middle_pile, False)

        # if the computer has no move
        elif computer_move is None:

            middle_pile = computer_hand.pick_up(middle_pile, False)
            print("No Computer move")
        move = True
        turn += 1

    pygame.display.flip()

# END
