"""
    Code for the card game Shed/Palace
    One player versus computer
    Images created in Microsoft Paint or from https://pixabay.com/
    Ideas for some solutions adapted from
    http://www.pygame.org/project-Pyhole-2010-.html
    and
    Making Games with Python & Pygame, Al Sweigart, 2012
"""

# ----------------- Imports ---------
import os
from Hand import HandClass
import Deck
from TableCards import TableCardsClass
import MiddlePile
from ComputerAI import ComputerAI
from Render_Images import *

# ----------------- Set Up ----------------------
# Initialize the Pygame Library
pygame.init()

FPS = 30
# Position of the screen when it starts
start_x = 200
start_y = 40
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (start_x, start_y)

# Load font, 25 is the font size
font = pygame.font.Font(None, 25)

# Size of the screen and its variable
screen = pygame.display.set_mode((700, 700))

# Loading Images ~~~~~~~~~~~~~~~~~~~~~~~~~~~
background, backgroundRect = Load_Image.ImageLoad.image_load("table.jpg", False)
backOfCard, backOfCardRect = Load_Image.ImageLoad.image_load('cardback.png', False)


width = backOfCardRect.w
height = backOfCardRect.h

transparent = pygame.Surface((width, height), pygame.SRCALPHA)
transparent.set_alpha(0)
transparent.fill((255, 255, 255, 0))

playerWinnerIMG, playerWinnerImgRect = Load_Image.ImageLoad.image_load("win.png", False)
computerWinnerIMG, computerWinnerImgRect = Load_Image.ImageLoad.image_load("lose.png", False)
pickUpDeckIMG, pickUpDeckImgRect = Load_Image.ImageLoad.image_load("PickUpTheDeck.png", False)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# deck of 52 cards, sprites are also in here
gameDeck = Deck.DeckClass()

# The hand of cards that the computer holds
computerHand = HandClass()
# The hand for the player
playerHand = HandClass()
# the class so can store data the computer needs to remember
computerAI = ComputerAI()

# Object for the middle pile, holds all the cards in the middle pile and which card is on top
middlePile = MiddlePile.Pile()

# Objects for the Table Cards
computerTableCards = TableCardsClass()
playerTableCards = TableCardsClass()

# Draw the 6 table cards for each players
computerTableCards.setup(gameDeck)
playerTableCards.setup(gameDeck)

# Set up the computer hand
computerHand.hand = gameDeck.draw_hand(computerHand.hand)
# Set up the player hand
playerHand.hand = gameDeck.draw_hand(playerHand.hand)

# Use this to center the cards for playing, and make the hand a list of 25 entries, mostly None
playerHand.initial_rejig()

# When listOfC[x] is equal to 1, this means that the image is not high-lighted, each x corresponds to the player hand
# i.e. listOfC[x] <=> player_hand.hand[x]
listOfC = [1] * 25
# Same as above, but for the 3 face up table cards
listOfCTable = [1] * 3

# if card is used, used will be equal to 'spent' and the player cannot select that card anymore.
# Similar one to one mapping
listOfUsedValues = [""] * 25

# this list follows the same rules as the table above, with the one to one mapping
listOfTableUsed = [""] * 3

# Boolean for the main loop
running = True
# boolean to keep track of whose move it is True for player, False for computer
move = True
# Which turn of the game we are on (only used to map the first move for the instructions)
turn = 0

# Double Click variables, no functionality to track double clicks in Pygame, so have to measure the time between clicks
dblClickGlobal = None
listOfDblClicks = [None] * 25
listOfDblClicksTable = [None] * 3


# --------------------- Main Game Loop -------------------
while running:

    FpsClock = pygame.time.Clock()
    # Put the background image in place
    Misc.background_img(background, backgroundRect, screen)
    # Put the pick up deck button in place
    Misc.pick_up_deck(pickUpDeckIMG, screen)

    # ~~~~~~~ all of these x's and y's set up rectangular coordinates that, when clicked, perform a certain action. ~~~~~~~~
    # Middle Pile
    xMid = list(range(300, 375))
    yMid = list(range(255, 360))

    # Shared y-coord of player table cards
    yTableCards = list(range(400, 500))

    # x coord of the player table cards
    xTable_1 = list(range(205, 275))
    xTable_2 = list(range(305, 375))
    xTable_3 = list(range(405, 475))

    # Put into a list for a loop
    listOfXTable = [xTable_1, xTable_2, xTable_3]

    # Coord's of pick up deck button
    xPickUp = list(range(100, 250))
    yPickUp = list(range(255, 355))

    # Y-Coord of hand
    yCardAll = list(range(550, 660))

    # Coord's of the full screen
    xAll = list(range(0, 700))
    yAll = list(range(0, 700))

    # X-Coord's of each card
    xCard_1 = list(range(20, 44))
    xCard_2 = list(range(45, 69))
    xCard_3 = list(range(70, 95))
    xCard_4 = list(range(96, 119))
    xCard_5 = list(range(120, 144))
    xCard_6 = list(range(145, 170))
    xCard_7 = list(range(171, 194))
    xCard_8 = list(range(195, 219))
    xCard_9 = list(range(220, 244))
    xCard_10 = list(range(245, 270))
    if playerHand.hand[11] is None:
        xCard_11 = list(range(271, 310))
        xCard_12 = list(range(0))
        xCard_13 = list(range(0))
        xCard_14 = list(range(0))
        xCard_15 = list(range(0))
        xCard_16 = list(range(0))
        xCard_17 = list(range(0))
        xCard_18 = list(range(0))
        xCard_19 = list(range(0))
        xCard_20 = list(range(0))
        xCard_21 = list(range(0))
        xCard_22 = list(range(0))
        xCard_23 = list(range(0))
        xCard_24 = list(range(0))
    else:
        xCard_11 = list(range(271, 295))

        if playerHand.hand[12] is None:
            xCard_12 = list(range(296, 365))
            xCard_13 = list(range(0))
            xCard_14 = list(range(0))
            xCard_15 = list(range(0))
            xCard_16 = list(range(0))
            xCard_17 = list(range(0))
            xCard_18 = list(range(0))
            xCard_19 = list(range(0))
            xCard_20 = list(range(0))
            xCard_21 = list(range(0))
            xCard_22 = list(range(0))
            xCard_23 = list(range(0))
            xCard_24 = list(range(0))
        else:
            xCard_12 = list(range(296, 320))

            if playerHand.hand[13] is None:
                xCard_13 = list(range(321, 395))
                xCard_14 = list(range(0))
                xCard_15 = list(range(0))
                xCard_16 = list(range(0))
                xCard_17 = list(range(0))
                xCard_18 = list(range(0))
                xCard_19 = list(range(0))
                xCard_20 = list(range(0))
                xCard_21 = list(range(0))
                xCard_22 = list(range(0))
                xCard_23 = list(range(0))
                xCard_24 = list(range(0))
            else:
                xCard_13 = list(range(321, 345))

                if playerHand.hand[14] is None:
                    xCard_14 = list(range(346, 417))
                    xCard_15 = list(range(0))
                    xCard_16 = list(range(0))
                    xCard_17 = list(range(0))
                    xCard_18 = list(range(0))
                    xCard_19 = list(range(0))
                    xCard_20 = list(range(0))
                    xCard_21 = list(range(0))
                    xCard_22 = list(range(0))
                    xCard_23 = list(range(0))
                    xCard_24 = list(range(0))
                else:
                    xCard_14 = list(range(346, 370))

                    if playerHand.hand[15] is None:
                        xCard_15 = list(range(371, 440))
                        xCard_16 = list(range(0))
                        xCard_17 = list(range(0))
                        xCard_18 = list(range(0))
                        xCard_19 = list(range(0))
                        xCard_20 = list(range(0))
                        xCard_21 = list(range(0))
                        xCard_22 = list(range(0))
                        xCard_23 = list(range(0))
                        xCard_24 = list(range(0))
                    else:
                        xCard_15 = list(range(371, 395))

                        if playerHand.hand[16] is None:
                            xCard_16 = list(range(396, 466))
                            xCard_17 = list(range(0))
                            xCard_18 = list(range(0))
                            xCard_19 = list(range(0))
                            xCard_20 = list(range(0))
                            xCard_21 = list(range(0))
                            xCard_22 = list(range(0))
                            xCard_23 = list(range(0))
                            xCard_24 = list(range(0))
                        else:
                            xCard_16 = list(range(396, 420))

                            if playerHand.hand[17] is None:
                                xCard_17 = list(range(421, 490))
                                xCard_18 = list(range(0))
                                xCard_19 = list(range(0))
                                xCard_20 = list(range(0))
                                xCard_21 = list(range(0))
                                xCard_22 = list(range(0))
                                xCard_23 = list(range(0))
                                xCard_24 = list(range(0))
                            else:
                                xCard_17 = list(range(421, 445))

                                if playerHand.hand[18] is None:
                                    xCard_18 = list(range(446, 518))
                                    xCard_19 = list(range(0))
                                    xCard_20 = list(range(0))
                                    xCard_21 = list(range(0))
                                    xCard_22 = list(range(0))
                                    xCard_23 = list(range(0))
                                    xCard_24 = list(range(0))
                                else:
                                    xCard_18 = list(range(446, 470))

                                    if playerHand.hand[19] is None:
                                        xCard_19 = list(range(471, 542))
                                        xCard_20 = list(range(0))
                                        xCard_21 = list(range(0))
                                        xCard_22 = list(range(0))
                                        xCard_23 = list(range(0))
                                        xCard_24 = list(range(0))
                                    else:
                                        xCard_19 = list(range(471, 495))

                                        if playerHand.hand[20] is None:
                                            xCard_20 = list(range(496, 566))
                                            xCard_21 = list(range(0))
                                            xCard_22 = list(range(0))
                                            xCard_23 = list(range(0))
                                            xCard_24 = list(range(0))
                                        else:
                                            xCard_20 = list(range(496, 520))

                                            if playerHand.hand[21] is None:
                                                xCard_21 = list(range(521, 586))
                                                xCard_22 = list(range(0))
                                                xCard_23 = list(range(0))
                                                xCard_24 = list(range(0))
                                            else:
                                                xCard_21 = list(range(521, 545))

                                                if playerHand.hand[22] is None:
                                                    xCard_22 = list(range(546, 611))
                                                    xCard_23 = list(range(0))
                                                    xCard_24 = list(range(0))
                                                else:
                                                    xCard_22 = list(range(546, 570))

                                                    if playerHand.hand[23] is None:
                                                        xCard_23 = list(range(571, 636))
                                                        xCard_24 = list(range(0))
                                                    else:
                                                        xCard_23 = list(range(571, 595))

                                                        if playerHand.hand[24] is None:
                                                            xCard_24 = list(range(596, 661))
                                                        else:
                                                            xCard_24 = list(range(596, 620))

    x_card_25 = list(range(621, 690))

    # X Coord's into a list for easy looping
    listOfXHand = [xCard_1, xCard_2, xCard_3, xCard_4, xCard_5, xCard_6, xCard_7, xCard_8, xCard_9, xCard_10, xCard_11, xCard_12, xCard_13,
                   xCard_14, xCard_15, xCard_16, xCard_17, xCard_18, xCard_19, xCard_20, xCard_21, xCard_22, xCard_23, xCard_24, x_card_25]
    # ~~~~~~~~~~~~~~~~~~~~~~~~ End Coord Set Up ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # ~~~~~~~~~~~~~~~~~~~~~~~~ Get and Load the Images ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Load up the images that will be needed for the players hand of cards
    playerHandSprites = BlitPlayer.gen_player_blit_cards(playerHand.hand, gameDeck.card_Sprites,
                                                         gameDeck.highlighted_Card_Sprites, listOfC, transparent)

    # Load the images that will be needed for the face up cards
    faceUpSprites = BlitPlayer.gen_face_up_table_cards(playerTableCards.face_up, computerTableCards.face_up, listOfCTable,
                                                       gameDeck.card_Sprites, gameDeck.highlighted_Card_Sprites, transparent)

    # Split the return of the above function into their proper places
    playerFaceUpSprites = faceUpSprites[0]
    computerFaceUpSprites = faceUpSprites[1]

    # puts ALL (computer, player and pile) the cards on the screen, and keeps updating them during the while loop
    BlitPlayer.blit_cards(playerHandSprites, playerHand.hand, computerHand.hand, backOfCard, screen, middlePile,
                          gameDeck.card_Sprites, Deck.DeckClass.cards, backOfCardRect, turn, playerFaceUpSprites,
                          computerFaceUpSprites, playerTableCards.face_down, computerTableCards.face_down)

    # ~~~~~~~~~~~~~~~~~~~~~~~~ End Get and Load Images ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # If it is the first turn, draw a random card from the deck to start
    if turn == 0:
        gameDeck.cards = middlePile.start_game(gameDeck.cards)
        turn += 1  # counter to show the rules

    # Gets a list of cards that are allowed to be played and stores that list in the middle pile object
    middlePile.playable_cards()

    # Text Notification for when the player need to pick up the pile
    if any(card is not None for card in playerHand.hand):
        if all(card not in middlePile.playable_cards_list for card in playerHand.hand):
            Misc.render_font(font, screen, "You must pick up the deck")
    if all(card is None for card in playerHand.hand) and any(card is not None for card in playerTableCards.face_up):
        if all(card not in middlePile.playable_cards_list for card in playerTableCards.face_up):
            Misc.render_font(font, screen, "You must pick up the deck")

    # Count how many cards the player has, used to draw a card
    number_of_player_cards = sum(x is not None for x in playerHand.hand)

    # add the table cards to the list of computers known cards
    if sum(x is not None for x in playerTableCards.face_up) != 0:
        for card in playerTableCards.face_up:
            if card not in computerAI.knownCards:
                computerAI.knownCards.append(card)

    # Anything in this For Loop depends on Whether and Where the mouse was clicked
    for event in pygame.event.get():

        # Reset Double Click variables if it goes too long without an action
        for item in listOfDblClicks:
            if item is not None and pygame.time.get_ticks() - item > 600:
                item = None

        # If User closes
        if event.type == pygame.QUIT:
            running = False
        # If User clicks
        elif event.type == pygame.MOUSEMOTION:
            # Keep track of WHERE the mouse position is
            x, y = event.pos
        # If User clicks and something needs to happen
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Double click anywhere to clear the rules
            if dblClickGlobal and pygame.time.get_ticks() - dblClickGlobal < 600:
                turn += 1
                dblClickGlobal = None
            else:
                dblClickGlobal = pygame.time.get_ticks()

            # Closes the game if all cards in the hand are gone
            # Player Winner
            if all(card is None for card in playerHand.hand) and all(card is None for card in playerTableCards.face_down):
                Misc.game_over(playerWinnerIMG, screen)
                pygame.display.flip()
                if x in xAll and y in yAll:
                    running = False
                    pygame.time.delay(3000)
            # Computer Winner
            if len(computerHand.hand) == 0 and all(card is None for card in computerTableCards.face_down):
                Misc.game_over(computerWinnerIMG, screen)
                pygame.display.flip()
                if x in xAll and y in yAll:
                    running = False
                    pygame.time.delay(3000)

            # Code to move a card from the players hand to the middle, the card must be highlighted
            # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            if x in xMid:
                if y in yMid:
                    for index_for_mid in range(25):
                        # If a C is 0 that means the corresponding card is highlighted
                        if listOfC[index_for_mid] == 0:
                            # Play the Animation
                            Animation.animate_play_card(playerHand.hand[index_for_mid], screen, gameDeck.card_Sprites, FpsClock,
                                                        playerHandSprites, playerHand.hand, computerHand.hand, backOfCard,
                                                        middlePile, Deck.DeckClass.cards, backOfCardRect,
                                                        background, backgroundRect, True, playerFaceUpSprites,
                                                        computerFaceUpSprites, playerTableCards.face_down,
                                                        computerTableCards.face_down)
                            # Move the card to the middle
                            middlePile.move_card(playerHand.hand[index_for_mid])
                            # List the card as spent
                            listOfUsedValues[index_for_mid] = 'spent'
                            # Un flip the c values so cards won't be highlighted
                            listOfC = HandClass.un_flip_all(listOfC)
                    # Similar for the table cards
                    for indexTableForMid in range(3):
                        if listOfCTable[indexTableForMid] == 0:
                            Animation.animate_play_card(playerTableCards.face_up[indexTableForMid], screen, gameDeck.card_Sprites, FpsClock,
                                                        playerHandSprites, playerHand.hand, computerHand.hand, backOfCard,
                                                        middlePile, Deck.DeckClass.cards, backOfCardRect,
                                                        background, backgroundRect, True, playerFaceUpSprites,
                                                        computerFaceUpSprites, playerTableCards.face_down,
                                                        computerTableCards.face_down)
                            middlePile.move_card(playerTableCards.face_up[indexTableForMid])
                            listOfTableUsed[indexTableForMid] = "spent"
                            listOfCTable = HandClass.un_flip_all(listOfCTable)

            # ~~~~~~~~~~~~~~~~ End of moving card from hand to the middle ~~~~~~~~~~~~~~~

            # When the pick up deck button is pressed
            if x in xPickUp:
                if y in yPickUp:
                    if len(middlePile.cards_in_middle) > 0:
                        computerAI.knownCards = middlePile.cards_in_middle
                        middlePile = playerHand.pick_up(middlePile, True)
                        playerHand.rejig()
                        move = False

            # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            # Code to change a card from to and from highlighted, double click functionality is here too

            for indexToPlay in range(25):
                if x in listOfXHand[indexToPlay]:
                    if y in yCardAll:
                        # The following will only trigger if the clicked card is allowed to be played
                        if playerHand.hand[indexToPlay] in middlePile.playable_cards_list:
                            # Double Click If statement, similar to lines 396-405
                            if listOfDblClicks[indexToPlay] and pygame.time.get_ticks() - listOfDblClicks[indexToPlay] < 600:
                                Animation.animate_play_card(playerHand.hand[indexToPlay], screen, gameDeck.card_Sprites, FpsClock,
                                                            playerHandSprites, playerHand.hand, computerHand.hand, backOfCard,
                                                            middlePile, Deck.DeckClass.cards, backOfCardRect,
                                                            background, backgroundRect, True, playerFaceUpSprites,
                                                            computerFaceUpSprites, playerTableCards.face_down,
                                                            computerTableCards.face_down)
                                middlePile.move_card(playerHand.hand[indexToPlay])
                                # Set the card to None
                                playerHand.hand[indexToPlay] = None
                                # Draw a card if needed
                                if number_of_player_cards <= 5:
                                    gameDeck.draw(playerHand.hand, indexToPlay)
                                playerHand.rejig()
                                listOfC = HandClass.un_flip_all(listOfC)
                                move = False
                            # Single click else statement
                            else:
                                # Start the double click timer
                                listOfDblClicks[indexToPlay] = pygame.time.get_ticks()

                                # If the card is in the hand
                                if listOfUsedValues[indexToPlay] != "spent":
                                    # Card highlighted
                                    if listOfC[indexToPlay] == 0:
                                        listOfC = HandClass.un_flip_all(listOfC)
                                    # Card un-highlighted
                                    elif listOfC[indexToPlay] == 1:
                                        listOfC = HandClass.un_flip_all(listOfC)
                                        listOfC[indexToPlay] = HandClass.flip(listOfC[indexToPlay])

            # Player Table Cards
            # Only allowed to interact if hand is empty
            if all(card is None for card in playerHand.hand):
                # If statement to interact with FACE UP CARDS
                if any(card is not None for card in playerTableCards.face_up):
                    for indexFaceUp in range(3):
                        if x in listOfXTable[indexFaceUp]:
                            if y in yTableCards:
                                # If the face up card is able to be played
                                if playerTableCards.face_up[indexFaceUp] in middlePile.playable_cards_list:
                                    # Double click functionality, similar to before
                                    if listOfDblClicksTable[indexFaceUp] and pygame.time.get_ticks() - listOfDblClicksTable[indexFaceUp] < 600:
                                        Animation.animate_play_card(playerTableCards.face_up[indexFaceUp], screen, gameDeck.card_Sprites,
                                                                    FpsClock, playerHandSprites, playerHand.hand, computerHand.hand,
                                                                    backOfCard, middlePile, Deck.DeckClass.cards, backOfCardRect,
                                                                    background, backgroundRect, True, playerFaceUpSprites,
                                                                    computerFaceUpSprites, playerTableCards.face_down,
                                                                    computerTableCards.face_down)
                                        middlePile.move_card(playerHand.hand[indexFaceUp])
                                        playerHand.hand[indexFaceUp] = None
                                        middlePile.move_card(playerTableCards.face_up[indexFaceUp])
                                        listOfTableUsed[indexFaceUp] = "spent"
                                        move = False
                                    # Single click functionality, same as before
                                    else:
                                        listOfDblClicksTable[indexFaceUp] = pygame.time.get_ticks()

                                        if listOfTableUsed[indexFaceUp] != "spent":
                                            if listOfCTable[indexFaceUp] == 0:
                                                listOfCTable = HandClass.un_flip_all(listOfCTable)

                                            elif listOfCTable[indexFaceUp] == 1:
                                                listOfCTable = HandClass.un_flip_all(listOfCTable)
                                                listOfCTable[indexFaceUp] = HandClass.flip(listOfCTable[indexFaceUp])

                # Else If statement to interact with FACE DOWN CARDS
                elif any(card is not None for card in playerTableCards.face_down):
                    for indexFaceDown in range(3):
                        if x in listOfXTable[indexFaceDown]:
                            if y in yTableCards:
                                Animation.animate_play_card(playerTableCards.face_down[indexFaceDown], screen, gameDeck.card_Sprites,
                                                            FpsClock, playerHandSprites, playerHand.hand, computerHand.hand, backOfCard,
                                                            middlePile, Deck.DeckClass.cards, backOfCardRect, background,
                                                            backgroundRect, True, playerFaceUpSprites, computerFaceUpSprites,
                                                            playerTableCards.face_down, computerTableCards.face_down)
                                # Send to player table cards object to deal with if the move is illegal
                                returnList = playerTableCards.play_face_down_card(indexFaceDown, playerHand, middlePile)
                                # Pulling the hand from the return list
                                playerHand = returnList[0]
                                # Message to explain if pile had to be picked up
                                if any(card is not None for card in playerHand.hand):
                                    Misc.render_font(font, screen, "Your card was not a valid move, you picked up the pile")
                                    pygame.time.delay(2000)
                                # Pulling the middle pile from the return list
                                middlePile = returnList[1]
                                # End the Move
                                move = False

            # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

            # Code to draw a card and end move, used only if a card was not double clicked and move to the middle
            # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            # From Hand
            for indexToDraw in range(25):
                # Was this position of hand used as the card to go to the middle
                if listOfUsedValues[indexToDraw] == "spent":
                    # Make the index none, effectively removing the card from the hand
                    playerHand.hand[indexToDraw] = None
                    # If there are less than 5 cards in hand, draw a card
                    if number_of_player_cards <= 5:
                        gameDeck.draw(playerHand.hand, indexToDraw)
                    playerHand.rejig()
                    # reset the spent variable so the card can be used again
                    listOfUsedValues[indexToDraw] = ""
                    # End the move
                    move = False
            # From Table
            for indexTableForMid1 in range(3):
                if listOfTableUsed[indexTableForMid1] == "spent":
                    playerTableCards.face_up[indexTableForMid1] = None
                    listOfTableUsed[indexTableForMid1] = "used"
                    move = False

            # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # This logic is for the computers turn
    if not move:
        # Boolean's to see where the card came from
        fromHand = False
        fromTableFaceUp = False
        fromTableFaceDown = False
        middlePile.playable_cards()

        # Get the card the computer will play, and where it came from
        if len(computerHand.hand) != 0:
            computer_move = computerAI.play_a_card(computerHand.hand, middlePile, number_of_player_cards, computerTableCards.face_up,
                                                   playerTableCards.face_up)
            fromHand = True

        elif any(card is not None for card in computerTableCards.face_up):
            computer_move = computerAI.play_a_card(computerHand.hand, middlePile, number_of_player_cards, computerTableCards.face_up,
                                                   playerTableCards.face_up)
            fromTableFaceUp = True

        elif any(card is not None for card in computerTableCards.face_down):
            computer_move = ComputerAI.play_face_down_card(computerTableCards.face_down)
            fromTableFaceDown = True

        if computer_move is not None:

            # Play moving the card to the middle, needs lots of variables for rendering
            Animation.animate_play_card(computer_move, screen, gameDeck.card_Sprites, FpsClock,
                                        playerHandSprites, playerHand.hand, computerHand.hand,
                                        backOfCard, middlePile, Deck.DeckClass.cards,
                                        backOfCardRect, background, backgroundRect, False, playerFaceUpSprites,
                                        computerFaceUpSprites, playerTableCards.face_down, computerTableCards.face_down)
            # Put the card on the pile of cards
            middlePile.move_card(computer_move)
            if fromHand:
                # What position said card is in
                comp_move_position = computerHand.hand.index(computer_move)
                # remove the card from the hand
                computerHand.hand[comp_move_position] = None

                if len(computerHand.hand) <= 5:
                    # draw another card
                    gameDeck.draw(computerHand.hand, comp_move_position)

                # if no cards can be added
                if computerHand.hand[comp_move_position] is None:
                    computerHand.hand.pop(comp_move_position)

            if fromTableFaceUp:
                # Position of where the card came from
                comp_move_position = computerTableCards.face_up.index(computer_move)
                # Remove the card from the list of face up cards
                computerTableCards.face_up[comp_move_position] = None

            if fromTableFaceDown:
                # Position of where the card came from
                comp_move_position = computerTableCards.face_down.index(computer_move)
                # Remove the card from the list of face down cards
                computerTableCards.face_down[comp_move_position] = None
                # If the randomly selected move from the computer is illegal
                if computer_move not in middlePile.playable_cards_list:
                    middlePile = computerHand.pick_up(middlePile, False)

        # if the computer has no move
        elif computer_move is None:
            # The computer must pick up the pile
            middlePile = computerHand.pick_up(middlePile, False)
        # Back to the player
        move = True

    # Throw all the images onto the screen
    pygame.display.flip()

# END
