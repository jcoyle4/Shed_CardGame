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
# A transparent image the size of a card
transcard, transcard_Rect = Load_Image.ImageLoad.imageLoadfnc('back(1).png', False)


game_deck = deck.Deck()  # deck of 52 cards, sprites are also in here
# print("Starting Deck")
# print(game_deck.cards)

computer_hand = Hand.Hand()  # The hand of cards that the computer holds
player_hand = Hand.Hand()   # The hand for the player

# Object for the middle pile, holds all the cards in the middle pile and which card is on top
middle_pile = MiddlePile.Pile()

# Set up the computer hand
game_deck.cards = computer_hand.setUp(game_deck.cards)
# Set up the player hand
game_deck.cards = player_hand.setUp(game_deck.cards)

# When cx is equal to 1, this means that the image is not high-lighted
c1 = 1
c2 = 1
c3 = 1
c4 = 1
c5 = 1


clicked = 0

# if card is used, used will be equal to 'spent' and the player cannot select that card anymore.
used1 = ''
used2 = ''
used3 = ''
used4 = ''
used5 = ''

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

    # X-Coord's of each card (1st iteration)
    x_card_1 = list(range(230, 265))
    x_card_2 = list(range(270, 310))
    x_card_3 = list(range(311, 350))
    x_card_4 = list(range(351, 390))
    x_card_5 = list(range(392, 460))

    # x_card_6 = list(range(433, 467))
    # x_card_7 = list(range(474, 507))
    # x_card_8 = list(range(514, 547))
    # x_card_9 = list(range(553, 587))
    # x_card_10 = list(range(593, 627))
    # x_card_11 = list(range(633, 667))
    # x_card_12 = list(range(673, 741))

    # x_new = list(range(461, 544))
    # y_new = list(range(2, 24))


    LEFT = 1  # need these for the x's and y's clickers.
    RIGHT = 1

    player_hand_sprites = []
    # Generates sprites for player cards
    card1, card2, card3, card4, card5 = BlitPlayerCards.BlitPlayer.gen_player_blit_cards(player_hand.hand, game_deck.card_Sprites,
                                                     game_deck.highlighted_Card_Sprites, player_hand_sprites, c1, c2, c3,
                                                        c4, c5, transcard, used1, used2, used3, used4, used5)

    player_hand_sprites.append(card1)
    player_hand_sprites.append(card2)
    player_hand_sprites.append(card3)
    player_hand_sprites.append(card4)
    player_hand_sprites.append(card5)

    if turn == 0:
        game_deck.cards = middle_pile.Start_game(game_deck.cards)
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

            if x in x_mid:
                if y in y_mid:
                    this = 1
                    while this == 1:
                        if c1 == 0:  # ie clicked. This says that if a card is clicked, and therefore able to be played,
                            #  the card in the middle is now the clicked number. and etc.
                            if middle_pile.card_on_top not in middle_pile.cards_in_middle and middle_pile.card_on_top != 0:
                                middle_pile.cards_in_middle.append(middle_pile.card_on_top)
                            ComputerAI.ComputerAI.animate_Play_Card(player_hand.hand[0], screen,
                                                                    game_deck.card_Sprites, FPSCLOCK,
                                                                    player_hand_sprites, player_hand.hand,
                                                                    computer_hand.hand, back_of_card,
                                                                    middle_pile, game_deck.card_Sprites,
                                                                    deck.Deck.cards, back_of_card_Rect,
                                                                    background, background_Rect, True)
                            middle_pile.card_on_top = player_hand.hand[0]
                            used1 = 'spent'
                            c1 = 1
                            this = 0

                        elif c2 == 0:
                            if middle_pile.card_on_top not in middle_pile.cards_in_middle and middle_pile.card_on_top != 0:
                                middle_pile.cards_in_middle.append(middle_pile.card_on_top)
                            ComputerAI.ComputerAI.animate_Play_Card(player_hand.hand[1], screen,
                                                                    game_deck.card_Sprites, FPSCLOCK,
                                                                    player_hand_sprites, player_hand.hand,
                                                                    computer_hand.hand, back_of_card,
                                                                    middle_pile, game_deck.card_Sprites,
                                                                    deck.Deck.cards, back_of_card_Rect,
                                                                    background, background_Rect, True)
                            middle_pile.card_on_top = player_hand.hand[1]
                            used2 = 'spent'
                            c2 = 1
                            this = 0

                        elif c3 == 0:
                            # print(player_hand.hand)
                            if middle_pile.card_on_top not in middle_pile.cards_in_middle and middle_pile.card_on_top != 0:
                                middle_pile.cards_in_middle.append(middle_pile.card_on_top)
                            ComputerAI.ComputerAI.animate_Play_Card(player_hand.hand[2], screen,
                                                                    game_deck.card_Sprites, FPSCLOCK,
                                                                    player_hand_sprites, player_hand.hand,
                                                                    computer_hand.hand, back_of_card,
                                                                    middle_pile, game_deck.card_Sprites,
                                                                    deck.Deck.cards, back_of_card_Rect,
                                                                    background, background_Rect, True)
                            middle_pile.card_on_top = player_hand.hand[2]
                            used3 = 'spent'
                            c3 = 1
                            this = 0

                        elif c4 == 0:
                            # print(player_hand.hand)
                            if middle_pile.card_on_top not in middle_pile.cards_in_middle and middle_pile.card_on_top != 0:
                                middle_pile.cards_in_middle.append(middle_pile.card_on_top)
                            ComputerAI.ComputerAI.animate_Play_Card(player_hand.hand[3], screen,
                                                                    game_deck.card_Sprites, FPSCLOCK,
                                                                    player_hand_sprites, player_hand.hand,
                                                                    computer_hand.hand, back_of_card,
                                                                    middle_pile, game_deck.card_Sprites,
                                                                    deck.Deck.cards, back_of_card_Rect,
                                                                    background, background_Rect, True)
                            middle_pile.card_on_top = player_hand.hand[3]
                            used4 = 'spent'
                            c4 = 1
                            this = 0

                        elif c5 == 0:
                            # print(player_hand.hand)
                            if middle_pile.card_on_top not in middle_pile.cards_in_middle and middle_pile.card_on_top != 0:
                                middle_pile.cards_in_middle.append(middle_pile.card_on_top)
                            ComputerAI.ComputerAI.animate_Play_Card(player_hand.hand[4], screen,
                                                                    game_deck.card_Sprites, FPSCLOCK,
                                                                    player_hand_sprites, player_hand.hand,
                                                                    computer_hand.hand, back_of_card,
                                                                    middle_pile, game_deck.card_Sprites,
                                                                    deck.Deck.cards, back_of_card_Rect,
                                                                    background, background_Rect, True)
                            middle_pile.card_on_top = player_hand.hand[4]
                            used5 = 'spent'
                            c5 = 1
                            this = 0
                        else:
                            if len(computer_hand.hand) != 0:
                                this = 0

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

                            elif c1 == 1:
                                c1 = 0
                                c2 = 1
                                c3 = 1
                                c4 = 1
                                c5 = 1

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

                            elif c2 == 1:
                                c2 = 0
                                c1 = 1
                                c3 = 1
                                c4 = 1
                                c5 = 1

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

                            elif c3 == 1:
                                c3 = 0
                                c1 = 1
                                c2 = 1
                                c4 = 1
                                c5 = 1

            if x in x_card_4:
                if y in y_card_all:
                    print("Card 4 selected")
                    if player_hand.hand[3] in middle_pile.playable_cards_list:

                        if used4 != 'spent':
                            if c4 == 0:
                                c4 = 1
                                c1 = 1
                                c2 = 1
                                c3 = 1
                                c5 = 1

                            elif c4 == 1:
                                c4 = 0
                                c1 = 1
                                c2 = 1
                                c3 = 1
                                c5 = 1

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

                            elif c5 == 1:
                                c1 = 1
                                c2 = 1
                                c3 = 1
                                c4 = 1
                                c5 = 0

            if used1 == "spent":
                player_hand.hand[0] = None
                game_deck.draw(player_hand.hand, 0)
                # if player_hand.hand[0] is None:
                #     player_hand.hand.pop(0)
                used1 = ""
                move = False
            if used2 == "spent":
                player_hand.hand[1] = None
                game_deck.draw(player_hand.hand, 1)
                # if player_hand.hand[1] is None:
                #     player_hand.hand.pop(1)
                # if player_hand.hand[1] is not None:
                used2 = ""
                move = False
            if used3 == "spent":
                player_hand.hand[2] = None
                game_deck.draw(player_hand.hand, 2)
                # if player_hand.hand[2] is None:
                #     player_hand.hand.pop(2)
                used3 = ""
                move = False
            if used4 == "spent":
                player_hand.hand[3] = None
                game_deck.draw(player_hand.hand, 3)
                # if player_hand.hand[3] is None:
                #     player_hand.hand.pop(3)
                used4 = ""
                move = False
            if used5 == "spent":
                player_hand.hand[4] = None
                game_deck.draw(player_hand.hand, 4)
                # if player_hand.hand[4] is None:
                #     player_hand.hand.pop(4)
                used5 = ""
                move = False


    # This logic is for the computers turn
    if not move:

        middle_pile.PlayableCards()
        # print("Playable list before passed to Computer AI =", middle_pile.playable_cards_list)

        # Get the card the computer will play
        computer_move = ComputerAI.ComputerAI.play_a_card(computer_hand.hand, middle_pile.playable_cards_list)

        if computer_move is not None:
            # What position said card is in
            comp_move_position = computer_hand.hand.index(computer_move)

            # Add the card on top of the pile to a stack of cards
            middle_pile.cards_in_middle.append(middle_pile.card_on_top)

            # Play moving the card to the middle, needs lots of variables for rendering
            ComputerAI.ComputerAI.animate_Play_Card(computer_move, screen, game_deck.card_Sprites, FPSCLOCK,
                                                    player_hand_sprites, player_hand.hand, computer_hand.hand,
                                                    back_of_card, middle_pile, game_deck.card_Sprites, deck.Deck.cards,
                                                    back_of_card_Rect, background, background_Rect, False)

            # put the card in the middle to blit
            middle_pile.card_on_top = computer_move

            # remove the card from the hand
            computer_hand.hand[comp_move_position] = None

            # draw another one
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
