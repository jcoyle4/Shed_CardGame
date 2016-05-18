import pygame
import random
import os
import time
import Hand
import Load_Image
import deck
import BlitPlayerCards
import MiddlePile
import ComputerAI
import keyboard

pygame.init()

FPS = 30
# Position of the screen when it starts
startx = 200
starty = 40
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (startx, starty)

# Size of the screen and its variable
screen = pygame.display.set_mode((700, 700))
background, background_Rect = Load_Image.ImageLoad.imageLoadfnc("table.jpg", False)
back_of_card, back_of_card_Rect = Load_Image.ImageLoad.imageLoadfnc('back.png', False)

width = back_of_card_Rect.w
height = back_of_card_Rect.h

TRANSPARANT = pygame.Surface((width, height), pygame.SRCALPHA)
TRANSPARANT.set_alpha(0)
TRANSPARANT.fill((255, 255, 255, 0))


game_deck = deck.Deck()  # deck of 52 cards, sprites are also in here

computer_hand = Hand.Hand()  # The hand of cards that the computer holds
player_hand = Hand.Hand()   # The hand for the player

# Object for the middle pile, holds all the cards in the middle pile and which card is on top
middle_pile = MiddlePile.Pile()

# Set up the computer hand
game_deck.cards = computer_hand.setUp(game_deck.cards)
# Set up the player hand
game_deck.cards = player_hand.setUp(game_deck.cards)

player_hand.initialRejig()  # Use this to center the cards for playing
# print(player_hand.hand[9])
# print(player_hand.hand[10])
# print(player_hand.hand[11])
# print(player_hand.hand[12])
# print(player_hand.hand[13])

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

running = True  # Boolean for the main loop
# counter = True  #
move = True  # boolean to keep track of whose move it is True for player, False for computer
# Switch to int if more than one computer
turn = 0  # Which turn of the game we are on



while running:
    font = pygame.font.Font(None, 36)
    FPSCLOCK = pygame.time.Clock()
    # Put the background image in place
    screen.blit(background, background_Rect)

    # all of these x's and y's set up rectangular coordinates that, when clicked, perform a certain action.
    # Middle Pile
    x_mid = list(range(300, 375))
    y_mid = list(range(255, 360))

    # Y-Coord of hand
    y_card_all = list(range(550, 660))

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
    x_card_11 = list(range(271, 295))
    x_card_12 = list(range(296, 320))
    x_card_13 = list(range(321, 345))
    x_card_14 = list(range(346, 370))
    x_card_15 = list(range(371, 395))
    x_card_16 = list(range(396, 420))
    x_card_17 = list(range(421, 445))
    x_card_18 = list(range(446, 470))
    x_card_19 = list(range(471, 495))
    x_card_20 = list(range(496, 520))
    x_card_21 = list(range(521, 545))
    x_card_22 = list(range(546, 570))
    x_card_23 = list(range(571, 595))
    x_card_24 = list(range(596, 620))
    x_card_25 = list(range(621, 690))

    # x_new = list(range(461, 544))
    # y_new = list(range(2, 24))

    LEFT = 1  # need these for the x's and y's clickers.
    RIGHT = 1

    player_hand_sprites = []
    # Generates sprites for player cards
    # TODO Change the return of the function to a list
    card1, card2, card3, card4, card5, card6, card7, card8, card9, card10, card11, card12, card13, card14, card15, card16, card17, card18, card19, \
        card20, card21, card22, card23, card24, card25 = BlitPlayerCards.BlitPlayer.gen_player_blit_cards(player_hand.hand, game_deck.card_Sprites,
                                                                                                          game_deck.highlighted_Card_Sprites,
                                                                                                          player_hand_sprites, c1, c2, c3, c4, c5,
                                                                                                          c6, c7, c8, c9, c10, c11, c12, c13, c14,
                                                                                                          c15, c16, c17, c18, c19, c20, c21, c22,
                                                                                                          c23, c24, c25, TRANSPARANT, used1, used2,
                                                                                                          used3, used4, used5)

    player_hand_sprites.append(card1)
    player_hand_sprites.append(card2)
    player_hand_sprites.append(card3)
    player_hand_sprites.append(card4)
    player_hand_sprites.append(card5)
    player_hand_sprites.append(card6)
    player_hand_sprites.append(card7)
    player_hand_sprites.append(card8)
    player_hand_sprites.append(card9)
    player_hand_sprites.append(card10)
    player_hand_sprites.append(card11)
    player_hand_sprites.append(card12)
    player_hand_sprites.append(card13)
    player_hand_sprites.append(card14)
    player_hand_sprites.append(card15)
    player_hand_sprites.append(card16)
    player_hand_sprites.append(card17)
    player_hand_sprites.append(card18)
    player_hand_sprites.append(card19)
    player_hand_sprites.append(card20)
    player_hand_sprites.append(card21)
    player_hand_sprites.append(card22)
    player_hand_sprites.append(card23)
    player_hand_sprites.append(card24)
    player_hand_sprites.append(card25)

    if turn == 0:
        game_deck.cards = middle_pile.Start_game(game_deck.cards)
        #TODO Render instructions
        turn += 1

    # puts ALL (computer, player and pile) the cards on the screen, and keeps updating them during the while loop
    BlitPlayerCards.BlitPlayer.blit_Cards(player_hand_sprites, player_hand.hand, computer_hand.hand, back_of_card, screen, middle_pile,
                                          game_deck.card_Sprites, deck.Deck.cards, back_of_card_Rect)


    #print(middle_pile.playable_cards_list)
    middle_pile.PlayableCards()

    # print("Card on top =", middle_pile.card_on_top)
    # print("Playable cards =", middle_pile.playable_cards_list)
    # print("Player Hand =", player_hand.hand)

    for event in pygame.event.get():  # get user input
        if event.type == pygame.QUIT:  # if user closes
            running = False
        elif event.type == pygame.MOUSEMOTION:
            # print ("mouse at (%d, %d)" % event.pos)
            x, y = event.pos
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
            # print ("You pressed the left mouse button at (%d, %d)" % event.pos)
            print(x, y)
            print("Player Hand =", player_hand.hand)
            print("Computer Hand =", computer_hand.hand)
            print("Cards in the middle =", middle_pile.cards_in_middle)
            print("Discarded cards =", middle_pile.discarded_cards)

            # Code to move a card from the players hand to the middle
            # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            if x in x_mid:
                if y in y_mid:
                    this = 1
                    while this == 1:
                        if c1 == 0:  # ie clicked. This says that if a card is clicked, and therefore able to be played,
                            #  the card in the middle is now the clicked number. and etc.
                            ComputerAI.ComputerAI.animate_Play_Card(player_hand.hand[0], screen,
                                                                    game_deck.card_Sprites, FPSCLOCK,
                                                                    player_hand_sprites, player_hand.hand,
                                                                    computer_hand.hand, back_of_card,
                                                                    middle_pile, game_deck.card_Sprites,
                                                                    deck.Deck.cards, back_of_card_Rect,
                                                                    background, background_Rect, True)
                            middle_pile.card_on_top = player_hand.hand[0]
                            if middle_pile.card_on_top not in middle_pile.cards_in_middle and middle_pile.card_on_top != 0:
                                middle_pile.cards_in_middle.append(middle_pile.card_on_top)
                            used1 = 'spent'
                            c1 = 1
                            this = 0

                        elif c2 == 0:
                            ComputerAI.ComputerAI.animate_Play_Card(player_hand.hand[1], screen,
                                                                    game_deck.card_Sprites, FPSCLOCK,
                                                                    player_hand_sprites, player_hand.hand,
                                                                    computer_hand.hand, back_of_card,
                                                                    middle_pile, game_deck.card_Sprites,
                                                                    deck.Deck.cards, back_of_card_Rect,
                                                                    background, background_Rect, True)
                            middle_pile.card_on_top = player_hand.hand[1]
                            if middle_pile.card_on_top not in middle_pile.cards_in_middle and middle_pile.card_on_top != 0:
                                middle_pile.cards_in_middle.append(middle_pile.card_on_top)
                            used2 = 'spent'
                            c2 = 1
                            this = 0

                        elif c3 == 0:
                            # print(player_hand.hand)
                            ComputerAI.ComputerAI.animate_Play_Card(player_hand.hand[2], screen,
                                                                    game_deck.card_Sprites, FPSCLOCK,
                                                                    player_hand_sprites, player_hand.hand,
                                                                    computer_hand.hand, back_of_card,
                                                                    middle_pile, game_deck.card_Sprites,
                                                                    deck.Deck.cards, back_of_card_Rect,
                                                                    background, background_Rect, True)
                            middle_pile.card_on_top = player_hand.hand[2]
                            if middle_pile.card_on_top not in middle_pile.cards_in_middle and middle_pile.card_on_top != 0:
                                middle_pile.cards_in_middle.append(middle_pile.card_on_top)
                            used3 = 'spent'
                            c3 = 1
                            this = 0

                        elif c4 == 0:
                            # print(player_hand.hand)
                            ComputerAI.ComputerAI.animate_Play_Card(player_hand.hand[3], screen,
                                                                    game_deck.card_Sprites, FPSCLOCK,
                                                                    player_hand_sprites, player_hand.hand,
                                                                    computer_hand.hand, back_of_card,
                                                                    middle_pile, game_deck.card_Sprites,
                                                                    deck.Deck.cards, back_of_card_Rect,
                                                                    background, background_Rect, True)
                            middle_pile.card_on_top = player_hand.hand[3]
                            if middle_pile.card_on_top not in middle_pile.cards_in_middle and middle_pile.card_on_top != 0:
                                middle_pile.cards_in_middle.append(middle_pile.card_on_top)
                            used4 = 'spent'
                            c4 = 1
                            this = 0

                        elif c5 == 0:
                            # print(player_hand.hand)
                            ComputerAI.ComputerAI.animate_Play_Card(player_hand.hand[4], screen,
                                                                    game_deck.card_Sprites, FPSCLOCK,
                                                                    player_hand_sprites, player_hand.hand,
                                                                    computer_hand.hand, back_of_card,
                                                                    middle_pile, game_deck.card_Sprites,
                                                                    deck.Deck.cards, back_of_card_Rect,
                                                                    background, background_Rect, True)
                            middle_pile.card_on_top = player_hand.hand[4]
                            if middle_pile.card_on_top not in middle_pile.cards_in_middle and middle_pile.card_on_top != 0:
                                middle_pile.cards_in_middle.append(middle_pile.card_on_top)
                            used5 = 'spent'
                            c5 = 1
                            this = 0

                        elif c6 == 0:
                            # print(player_hand.hand)
                            ComputerAI.ComputerAI.animate_Play_Card(player_hand.hand[5], screen,
                                                                    game_deck.card_Sprites, FPSCLOCK,
                                                                    player_hand_sprites, player_hand.hand,
                                                                    computer_hand.hand, back_of_card,
                                                                    middle_pile, game_deck.card_Sprites,
                                                                    deck.Deck.cards, back_of_card_Rect,
                                                                    background, background_Rect, True)
                            middle_pile.card_on_top = player_hand.hand[5]
                            if middle_pile.card_on_top not in middle_pile.cards_in_middle and middle_pile.card_on_top != 0:
                                middle_pile.cards_in_middle.append(middle_pile.card_on_top)
                            used6 = 'spent'
                            c6 = 1
                            this = 0

                        elif c7 == 0:
                            # print(player_hand.hand)
                            ComputerAI.ComputerAI.animate_Play_Card(player_hand.hand[6], screen,
                                                                    game_deck.card_Sprites, FPSCLOCK,
                                                                    player_hand_sprites, player_hand.hand,
                                                                    computer_hand.hand, back_of_card,
                                                                    middle_pile, game_deck.card_Sprites,
                                                                    deck.Deck.cards, back_of_card_Rect,
                                                                    background, background_Rect, True)
                            middle_pile.card_on_top = player_hand.hand[6]
                            if middle_pile.card_on_top not in middle_pile.cards_in_middle and middle_pile.card_on_top != 0:
                                middle_pile.cards_in_middle.append(middle_pile.card_on_top)
                            used7 = 'spent'
                            c7 = 1
                            this = 0

                        elif c8 == 0:
                            # print(player_hand.hand)
                            ComputerAI.ComputerAI.animate_Play_Card(player_hand.hand[7], screen,
                                                                    game_deck.card_Sprites, FPSCLOCK,
                                                                    player_hand_sprites, player_hand.hand,
                                                                    computer_hand.hand, back_of_card,
                                                                    middle_pile, game_deck.card_Sprites,
                                                                    deck.Deck.cards, back_of_card_Rect,
                                                                    background, background_Rect, True)
                            middle_pile.card_on_top = player_hand.hand[7]
                            if middle_pile.card_on_top not in middle_pile.cards_in_middle and middle_pile.card_on_top != 0:
                                middle_pile.cards_in_middle.append(middle_pile.card_on_top)
                            used8 = 'spent'
                            c8 = 1
                            this = 0
                        elif c9 == 0:
                            # print(player_hand.hand)
                            ComputerAI.ComputerAI.animate_Play_Card(player_hand.hand[8], screen,
                                                                    game_deck.card_Sprites, FPSCLOCK,
                                                                    player_hand_sprites, player_hand.hand,
                                                                    computer_hand.hand, back_of_card,
                                                                    middle_pile, game_deck.card_Sprites,
                                                                    deck.Deck.cards, back_of_card_Rect,
                                                                    background, background_Rect, True)
                            middle_pile.card_on_top = player_hand.hand[8]
                            if middle_pile.card_on_top not in middle_pile.cards_in_middle and middle_pile.card_on_top != 0:
                                middle_pile.cards_in_middle.append(middle_pile.card_on_top)
                            used9 = 'spent'
                            c9 = 1
                            this = 0
                        elif c10 == 0:
                            # print(player_hand.hand)
                            ComputerAI.ComputerAI.animate_Play_Card(player_hand.hand[9], screen,
                                                                    game_deck.card_Sprites, FPSCLOCK,
                                                                    player_hand_sprites, player_hand.hand,
                                                                    computer_hand.hand, back_of_card,
                                                                    middle_pile, game_deck.card_Sprites,
                                                                    deck.Deck.cards, back_of_card_Rect,
                                                                    background, background_Rect, True)
                            middle_pile.card_on_top = player_hand.hand[9]
                            if middle_pile.card_on_top not in middle_pile.cards_in_middle and middle_pile.card_on_top != 0:
                                middle_pile.cards_in_middle.append(middle_pile.card_on_top)
                            used10 = 'spent'
                            c10 = 1
                            this = 0
                        elif c11 == 0:
                            # print(player_hand.hand)
                            ComputerAI.ComputerAI.animate_Play_Card(player_hand.hand[10], screen,
                                                                    game_deck.card_Sprites, FPSCLOCK,
                                                                    player_hand_sprites, player_hand.hand,
                                                                    computer_hand.hand, back_of_card,
                                                                    middle_pile, game_deck.card_Sprites,
                                                                    deck.Deck.cards, back_of_card_Rect,
                                                                    background, background_Rect, True)
                            middle_pile.card_on_top = player_hand.hand[10]
                            if middle_pile.card_on_top not in middle_pile.cards_in_middle and middle_pile.card_on_top != 0:
                                middle_pile.cards_in_middle.append(middle_pile.card_on_top)
                            used11 = 'spent'
                            c11 = 1
                            this = 0
                        elif c12 == 0:
                            # print(player_hand.hand)
                            ComputerAI.ComputerAI.animate_Play_Card(player_hand.hand[11], screen,
                                                                    game_deck.card_Sprites, FPSCLOCK,
                                                                    player_hand_sprites, player_hand.hand,
                                                                    computer_hand.hand, back_of_card,
                                                                    middle_pile, game_deck.card_Sprites,
                                                                    deck.Deck.cards, back_of_card_Rect,
                                                                    background, background_Rect, True)
                            middle_pile.card_on_top = player_hand.hand[11]
                            if middle_pile.card_on_top not in middle_pile.cards_in_middle and middle_pile.card_on_top != 0:
                                middle_pile.cards_in_middle.append(middle_pile.card_on_top)
                            used12 = 'spent'
                            c12 = 1
                            this = 0
                        elif c13 == 0:
                            # print(player_hand.hand)
                            ComputerAI.ComputerAI.animate_Play_Card(player_hand.hand[12], screen,
                                                                    game_deck.card_Sprites, FPSCLOCK,
                                                                    player_hand_sprites, player_hand.hand,
                                                                    computer_hand.hand, back_of_card,
                                                                    middle_pile, game_deck.card_Sprites,
                                                                    deck.Deck.cards, back_of_card_Rect,
                                                                    background, background_Rect, True)
                            middle_pile.card_on_top = player_hand.hand[12]
                            if middle_pile.card_on_top not in middle_pile.cards_in_middle and middle_pile.card_on_top != 0:
                                middle_pile.cards_in_middle.append(middle_pile.card_on_top)
                            used13 = 'spent'
                            c13 = 1
                            this = 0
                        elif c14 == 0:
                            # print(player_hand.hand)
                            ComputerAI.ComputerAI.animate_Play_Card(player_hand.hand[13], screen,
                                                                    game_deck.card_Sprites, FPSCLOCK,
                                                                    player_hand_sprites, player_hand.hand,
                                                                    computer_hand.hand, back_of_card,
                                                                    middle_pile, game_deck.card_Sprites,
                                                                    deck.Deck.cards, back_of_card_Rect,
                                                                    background, background_Rect, True)
                            middle_pile.card_on_top = player_hand.hand[13]
                            if middle_pile.card_on_top not in middle_pile.cards_in_middle and middle_pile.card_on_top != 0:
                                middle_pile.cards_in_middle.append(middle_pile.card_on_top)
                            used14 = 'spent'
                            c14 = 1
                            this = 0
                        elif c15 == 0:
                            # print(player_hand.hand)
                            ComputerAI.ComputerAI.animate_Play_Card(player_hand.hand[14], screen,
                                                                    game_deck.card_Sprites, FPSCLOCK,
                                                                    player_hand_sprites, player_hand.hand,
                                                                    computer_hand.hand, back_of_card,
                                                                    middle_pile, game_deck.card_Sprites,
                                                                    deck.Deck.cards, back_of_card_Rect,
                                                                    background, background_Rect, True)
                            middle_pile.card_on_top = player_hand.hand[14]
                            if middle_pile.card_on_top not in middle_pile.cards_in_middle and middle_pile.card_on_top != 0:
                                middle_pile.cards_in_middle.append(middle_pile.card_on_top)
                            used15 = 'spent'
                            c15 = 1
                            this = 0
                        elif c16 == 0:
                            # print(player_hand.hand)
                            ComputerAI.ComputerAI.animate_Play_Card(player_hand.hand[15], screen,
                                                                    game_deck.card_Sprites, FPSCLOCK,
                                                                    player_hand_sprites, player_hand.hand,
                                                                    computer_hand.hand, back_of_card,
                                                                    middle_pile, game_deck.card_Sprites,
                                                                    deck.Deck.cards, back_of_card_Rect,
                                                                    background, background_Rect, True)
                            middle_pile.card_on_top = player_hand.hand[15]
                            if middle_pile.card_on_top not in middle_pile.cards_in_middle and middle_pile.card_on_top != 0:
                                middle_pile.cards_in_middle.append(middle_pile.card_on_top)
                            used16 = 'spent'
                            c16 = 1
                            this = 0
                        elif c17 == 0:
                            # print(player_hand.hand)
                            ComputerAI.ComputerAI.animate_Play_Card(player_hand.hand[16], screen,
                                                                    game_deck.card_Sprites, FPSCLOCK,
                                                                    player_hand_sprites, player_hand.hand,
                                                                    computer_hand.hand, back_of_card,
                                                                    middle_pile, game_deck.card_Sprites,
                                                                    deck.Deck.cards, back_of_card_Rect,
                                                                    background, background_Rect, True)
                            middle_pile.card_on_top = player_hand.hand[16]
                            if middle_pile.card_on_top not in middle_pile.cards_in_middle and middle_pile.card_on_top != 0:
                                middle_pile.cards_in_middle.append(middle_pile.card_on_top)
                            used17 = 'spent'
                            c17 = 1
                            this = 0
                        elif c18 == 0:
                            # print(player_hand.hand)
                            ComputerAI.ComputerAI.animate_Play_Card(player_hand.hand[17], screen,
                                                                    game_deck.card_Sprites, FPSCLOCK,
                                                                    player_hand_sprites, player_hand.hand,
                                                                    computer_hand.hand, back_of_card,
                                                                    middle_pile, game_deck.card_Sprites,
                                                                    deck.Deck.cards, back_of_card_Rect,
                                                                    background, background_Rect, True)
                            middle_pile.card_on_top = player_hand.hand[17]
                            if middle_pile.card_on_top not in middle_pile.cards_in_middle and middle_pile.card_on_top != 0:
                                middle_pile.cards_in_middle.append(middle_pile.card_on_top)
                            used18 = 'spent'
                            c18 = 1
                            this = 0
                        elif c19 == 0:
                            # print(player_hand.hand)
                            ComputerAI.ComputerAI.animate_Play_Card(player_hand.hand[18], screen,
                                                                    game_deck.card_Sprites, FPSCLOCK,
                                                                    player_hand_sprites, player_hand.hand,
                                                                    computer_hand.hand, back_of_card,
                                                                    middle_pile, game_deck.card_Sprites,
                                                                    deck.Deck.cards, back_of_card_Rect,
                                                                    background, background_Rect, True)
                            middle_pile.card_on_top = player_hand.hand[18]
                            if middle_pile.card_on_top not in middle_pile.cards_in_middle and middle_pile.card_on_top != 0:
                                middle_pile.cards_in_middle.append(middle_pile.card_on_top)
                            used19 = 'spent'
                            c19 = 1
                            this = 0
                        elif c20 == 0:
                            # print(player_hand.hand)
                            ComputerAI.ComputerAI.animate_Play_Card(player_hand.hand[19], screen,
                                                                    game_deck.card_Sprites, FPSCLOCK,
                                                                    player_hand_sprites, player_hand.hand,
                                                                    computer_hand.hand, back_of_card,
                                                                    middle_pile, game_deck.card_Sprites,
                                                                    deck.Deck.cards, back_of_card_Rect,
                                                                    background, background_Rect, True)
                            middle_pile.card_on_top = player_hand.hand[19]
                            if middle_pile.card_on_top not in middle_pile.cards_in_middle and middle_pile.card_on_top != 0:
                                middle_pile.cards_in_middle.append(middle_pile.card_on_top)
                            used20 = 'spent'
                            c20 = 1
                            this = 0
                        elif c21 == 0:
                            # print(player_hand.hand)
                            ComputerAI.ComputerAI.animate_Play_Card(player_hand.hand[20], screen,
                                                                    game_deck.card_Sprites, FPSCLOCK,
                                                                    player_hand_sprites, player_hand.hand,
                                                                    computer_hand.hand, back_of_card,
                                                                    middle_pile, game_deck.card_Sprites,
                                                                    deck.Deck.cards, back_of_card_Rect,
                                                                    background, background_Rect, True)
                            middle_pile.card_on_top = player_hand.hand[20]
                            if middle_pile.card_on_top not in middle_pile.cards_in_middle and middle_pile.card_on_top != 0:
                                middle_pile.cards_in_middle.append(middle_pile.card_on_top)
                            used21 = 'spent'
                            c21 = 1
                            this = 0
                        elif c22 == 0:
                            # print(player_hand.hand)
                            ComputerAI.ComputerAI.animate_Play_Card(player_hand.hand[21], screen,
                                                                    game_deck.card_Sprites, FPSCLOCK,
                                                                    player_hand_sprites, player_hand.hand,
                                                                    computer_hand.hand, back_of_card,
                                                                    middle_pile, game_deck.card_Sprites,
                                                                    deck.Deck.cards, back_of_card_Rect,
                                                                    background, background_Rect, True)
                            middle_pile.card_on_top = player_hand.hand[21]
                            if middle_pile.card_on_top not in middle_pile.cards_in_middle and middle_pile.card_on_top != 0:
                                middle_pile.cards_in_middle.append(middle_pile.card_on_top)
                            used22 = 'spent'
                            c22 = 1
                            this = 0
                        elif c23 == 0:
                            # print(player_hand.hand)
                            ComputerAI.ComputerAI.animate_Play_Card(player_hand.hand[22], screen,
                                                                    game_deck.card_Sprites, FPSCLOCK,
                                                                    player_hand_sprites, player_hand.hand,
                                                                    computer_hand.hand, back_of_card,
                                                                    middle_pile, game_deck.card_Sprites,
                                                                    deck.Deck.cards, back_of_card_Rect,
                                                                    background, background_Rect, True)
                            middle_pile.card_on_top = player_hand.hand[22]
                            if middle_pile.card_on_top not in middle_pile.cards_in_middle and middle_pile.card_on_top != 0:
                                middle_pile.cards_in_middle.append(middle_pile.card_on_top)
                            used23 = 'spent'
                            c23 = 1
                            this = 0
                        elif c24 == 0:
                            # print(player_hand.hand)
                            ComputerAI.ComputerAI.animate_Play_Card(player_hand.hand[23], screen,
                                                                    game_deck.card_Sprites, FPSCLOCK,
                                                                    player_hand_sprites, player_hand.hand,
                                                                    computer_hand.hand, back_of_card,
                                                                    middle_pile, game_deck.card_Sprites,
                                                                    deck.Deck.cards, back_of_card_Rect,
                                                                    background, background_Rect, True)
                            middle_pile.card_on_top = player_hand.hand[23]
                            if middle_pile.card_on_top not in middle_pile.cards_in_middle and middle_pile.card_on_top != 0:
                                middle_pile.cards_in_middle.append(middle_pile.card_on_top)
                            used24 = 'spent'
                            c24 = 1
                            this = 0
                        elif c25 == 0:
                            # print(player_hand.hand)
                            ComputerAI.ComputerAI.animate_Play_Card(player_hand.hand[24], screen,
                                                                    game_deck.card_Sprites, FPSCLOCK,
                                                                    player_hand_sprites, player_hand.hand,
                                                                    computer_hand.hand, back_of_card,
                                                                    middle_pile, game_deck.card_Sprites,
                                                                    deck.Deck.cards, back_of_card_Rect,
                                                                    background, background_Rect, True)
                            middle_pile.card_on_top = player_hand.hand[24]
                            if middle_pile.card_on_top not in middle_pile.cards_in_middle and middle_pile.card_on_top != 0:
                                middle_pile.cards_in_middle.append(middle_pile.card_on_top)
                            used25 = 'spent'
                            c25 = 1
                            this = 0
                        else:  # when the middle pile is clicked when no card is highlighted, pick up the middle pile
                            if len(computer_hand.hand) != 0:
                                this = 0
                            if len(middle_pile.cards_in_middle) > 0:
                                for card_in_hand in range(len(player_hand.hand)):
                                    for card_in_pile in range(len(middle_pile.cards_in_middle)):
                                        if player_hand.hand[card_in_hand] is None and middle_pile.cards_in_middle[card_in_pile] not in player_hand.hand:
                                            player_hand.hand[card_in_hand] = middle_pile.cards_in_middle[card_in_pile]
                                middle_pile.cards_in_middle = []
                                middle_pile.card_on_top = 0
                                player_hand.rejig()
                                move = False

            # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            """
            # Extend this to 25 cards
            # Also put in the code to render the extra 15 cards
            """

            # Code to change a card from to and from highlighted
            # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            if x in x_card_1:  # sets up to see if a card in the players hand can be highlighted and used.
                if y in y_card_all:
                    print("Card 1 selected")

                    if player_hand.hand[0] in middle_pile.playable_cards_list:

                        if used1 != 'spent':
                            if c1 == 0:
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

                            elif c1 == 1:
                                c1 = 0
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

            if x in x_card_2:
                if y in y_card_all:
                    print("Card 2 selected")
                    if player_hand.hand[1] in middle_pile.playable_cards_list:

                        if used2 != 'spent':
                            if c2 == 0:
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

                            elif c2 == 1:
                                c1 = 1
                                c2 = 0
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

            if x in x_card_3:
                if y in y_card_all:
                    print("Card 3 selected")
                    if player_hand.hand[2] in middle_pile.playable_cards_list:

                        if used3 != 'spent':
                            if c3 == 0:
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

                            elif c3 == 1:
                                c1 = 1
                                c2 = 1
                                c3 = 0
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

            if x in x_card_4:
                if y in y_card_all:
                    print("Card 4 selected")
                    if player_hand.hand[3] in middle_pile.playable_cards_list:

                        if used4 != 'spent':
                            if c4 == 0:
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

                            elif c4 == 1:
                                c1 = 1
                                c2 = 1
                                c3 = 1
                                c4 = 0
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

            if x in x_card_5:
                if y in y_card_all:
                    print("Card 5 selected")
                    if player_hand.hand[4] in middle_pile.playable_cards_list:

                        if used5 != 'spent':
                            if c5 == 0:
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

                            elif c5 == 1:
                                c1 = 1
                                c2 = 1
                                c3 = 1
                                c4 = 1
                                c5 = 0
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

            if x in x_card_6:
                if y in y_card_all:
                    print("Card 6 selected")
                    if player_hand.hand[5] in middle_pile.playable_cards_list:

                        if used6 != 'spent':
                            if c6 == 0:
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

                            elif c6 == 1:
                                c1 = 1
                                c2 = 1
                                c3 = 1
                                c4 = 1
                                c5 = 1
                                c6 = 0
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

            if x in x_card_7:
                if y in y_card_all:
                    print("Card 7 selected")
                    if player_hand.hand[6] in middle_pile.playable_cards_list:

                        if used7 != 'spent':
                            if c7 == 0:
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

                            elif c7 == 1:
                                c1 = 1
                                c2 = 1
                                c3 = 1
                                c4 = 1
                                c5 = 1
                                c6 = 1
                                c7 = 0
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

            if x in x_card_8:
                if y in y_card_all:
                    print("Card 8 selected")
                    if player_hand.hand[7] in middle_pile.playable_cards_list:

                        if used8 != 'spent':
                            if c8 == 0:
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

                            elif c8 == 1:
                                c1 = 1
                                c2 = 1
                                c3 = 1
                                c4 = 1
                                c5 = 1
                                c6 = 1
                                c7 = 1
                                c8 = 0
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

            if x in x_card_9:
                if y in y_card_all:
                    print("Card 9 selected")
                    if player_hand.hand[8] in middle_pile.playable_cards_list:

                        if used9 != 'spent':
                            if c9 == 0:
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

                            elif c9 == 1:
                                c1 = 1
                                c2 = 1
                                c3 = 1
                                c4 = 1
                                c5 = 1
                                c6 = 1
                                c7 = 1
                                c8 = 1
                                c9 = 0
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

            if x in x_card_10:
                if y in y_card_all:
                    print("Card 10 selected")
                    if player_hand.hand[9] in middle_pile.playable_cards_list:

                        if used10 != 'spent':
                            if c10 == 0:
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

                            elif c10 == 1:
                                c1 = 1
                                c2 = 1
                                c3 = 1
                                c4 = 1
                                c5 = 1
                                c6 = 1
                                c7 = 1
                                c8 = 1
                                c9 = 1
                                c10 = 0
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

            if x in x_card_11:
                if y in y_card_all:
                    print("Card 11 selected")
                    if player_hand.hand[10] in middle_pile.playable_cards_list:

                        if used11 != 'spent':
                            if c11 == 0:
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

                            elif c11 == 1:
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
                                c11 = 0
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

            if x in x_card_12:
                if y in y_card_all:
                    print("Card 12 selected")
                    if player_hand.hand[11] in middle_pile.playable_cards_list:

                        if used12 != 'spent':
                            if c12 == 0:
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

                            elif c12 == 1:
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
                                c12 = 0
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

            if x in x_card_13:
                if y in y_card_all:
                    print("Card 13 selected")
                    if player_hand.hand[12] in middle_pile.playable_cards_list:

                        if used13 != 'spent':
                            if c13 == 0:
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

                            elif c13 == 1:
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
                                c13 = 0
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

            if x in x_card_14:
                if y in y_card_all:
                    print("Card 14 selected")
                    if player_hand.hand[13] in middle_pile.playable_cards_list:

                        if used14 != 'spent':
                            if c14 == 0:
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

                            elif c14 == 1:
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
                                c14 = 0
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
            if x in x_card_15:
                if y in y_card_all:
                    print("Card 15 selected")
                    if player_hand.hand[15] in middle_pile.playable_cards_list:

                        if used15 != 'spent':
                            if c15 == 0:
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

                            elif c15 == 1:
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
                                c15 = 0
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
            if x in x_card_16:
                if y in y_card_all:
                    print("Card 16 selected")
                    if player_hand.hand[15] in middle_pile.playable_cards_list:

                        if used16 != 'spent':
                            if c16 == 0:
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

                            elif c16 == 1:
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
                                c16 = 0
                                c17 = 1
                                c18 = 1
                                c19 = 1
                                c20 = 1
                                c21 = 1
                                c22 = 1
                                c23 = 1
                                c24 = 1
                                c25 = 1

            if x in x_card_17:
                if y in y_card_all:
                    print("Card 17 selected")
                    if player_hand.hand[16] in middle_pile.playable_cards_list:

                        if used17 != 'spent':
                            if c17 == 0:
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

                            elif c17 == 1:
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
                                c17 = 0
                                c18 = 1
                                c19 = 1
                                c20 = 1
                                c21 = 1
                                c22 = 1
                                c23 = 1
                                c24 = 1
                                c25 = 1
            if x in x_card_18:
                if y in y_card_all:
                    print("Card 18 selected")
                    if player_hand.hand[17] in middle_pile.playable_cards_list:

                        if used18 != 'spent':
                            if c18 == 0:
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

                            elif c18 == 1:
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
                                c18 = 0
                                c19 = 1
                                c20 = 1
                                c21 = 1
                                c22 = 1
                                c23 = 1
                                c24 = 1
                                c25 = 1

            if x in x_card_19:
                if y in y_card_all:
                    print("Card 19 selected")
                    if player_hand.hand[18] in middle_pile.playable_cards_list:

                        if used19 != 'spent':
                            if c19 == 0:
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

                            elif c19 == 1:
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
                                c19 = 0
                                c20 = 1
                                c21 = 1
                                c22 = 1
                                c23 = 1
                                c24 = 1
                                c25 = 1

            if x in x_card_20:
                if y in y_card_all:
                    print("Card 20 selected")
                    if player_hand.hand[19] in middle_pile.playable_cards_list:

                        if used20 != 'spent':
                            if c20 == 0:
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

                            elif c20 == 1:
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
                                c20 = 0
                                c21 = 1
                                c22 = 1
                                c23 = 1
                                c24 = 1
                                c25 = 1

            if x in x_card_21:
                if y in y_card_all:
                    print("Card 21 selected")
                    if player_hand.hand[20] in middle_pile.playable_cards_list:

                        if used21 != 'spent':
                            if c21 == 0:
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

                            elif c21 == 1:
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
                                c21 = 0
                                c22 = 1
                                c23 = 1
                                c24 = 1
                                c25 = 1
            if x in x_card_22:
                if y in y_card_all:
                    print("Card 22 selected")
                    if player_hand.hand[21] in middle_pile.playable_cards_list:

                        if used22 != 'spent':
                            if c22 == 0:
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

                            elif c22 == 1:
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
                                c22 = 0
                                c23 = 1
                                c24 = 1
                                c25 = 1

            if x in x_card_23:
                if y in y_card_all:
                    print("Card 23 selected")
                    if player_hand.hand[22] in middle_pile.playable_cards_list:

                        if used23 != 'spent':
                            if c23 == 0:
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

                            elif c23 == 1:
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
                                c23 = 0
                                c24 = 1
                                c25 = 1
            if x in x_card_24:
                if y in y_card_all:
                    print("Card 24 selected")
                    if player_hand.hand[23] in middle_pile.playable_cards_list:

                        if used24 != 'spent':
                            if c24 == 0:
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

                            elif c24 == 1:
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
                                c24 = 0
                                c25 = 1
            if x in x_card_25:
                if y in y_card_all:
                    print("Card 25 selected")
                    if player_hand.hand[24] in middle_pile.playable_cards_list:

                        if used25 != 'spent':
                            if c25 == 0:
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

                            elif c25 == 1:
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
                                c25 = 0
            # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

            # Code to draw a card and end move
            # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            number_of_player_cards = sum(x is not None for x in player_hand.hand)
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
            # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


    # This logic is for the computers turn
    if not move:

        middle_pile.PlayableCards()
        # print("Playable list before passed to Computer AI =", middle_pile.playable_cards_list)

        # Get the card the computer will play
        computer_move = ComputerAI.ComputerAI.play_a_card(computer_hand.hand, middle_pile.playable_cards_list)

        if computer_move is not None:
            # What position said card is in
            comp_move_position = computer_hand.hand.index(computer_move)


            # Play moving the card to the middle, needs lots of variables for rendering
            ComputerAI.ComputerAI.animate_Play_Card(computer_move, screen, game_deck.card_Sprites, FPSCLOCK,
                                                    player_hand_sprites, player_hand.hand, computer_hand.hand,
                                                    back_of_card, middle_pile, game_deck.card_Sprites, deck.Deck.cards,
                                                    back_of_card_Rect, background, background_Rect, False)

            # put the card in the middle to blit
            middle_pile.card_on_top = computer_move

            # Add the card on top of the pile to a stack of cards
            middle_pile.cards_in_middle.append(middle_pile.card_on_top)

            # remove the card from the hand
            computer_hand.hand[comp_move_position] = None

            if len(computer_hand.hand) <= 5:
                # draw another one
                print("The computer is drawing a card")
                game_deck.draw(computer_hand.hand, comp_move_position)

            # if no cards can be added
            if computer_hand.hand[comp_move_position] is None:
                computer_hand.hand.pop(comp_move_position)

        # if the computer has no move
        elif computer_move is None:
            computer_hand.hand.extend(middle_pile.cards_in_middle)
            middle_pile.cards_in_middle = []
            middle_pile.card_on_top = 0
            print("No Computer move")
        move = True

    # Closes the game if all cards in the hand are gone
    if all(card is None for card in player_hand.hand):
        running = False

    pygame.display.flip()



# END
