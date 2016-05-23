import random
import Load_Image


class DeckClass:

    # change to Dictionary??
    # List of Cards
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,           # 2-Ace of Clubs
             14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,  # 2-Ace of Diamonds
             27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39,  # 2-Ace of Hearts
             40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]  # 2-Ace of Spades

    card_Sprites = []
    card_Sprites_rect = []
    highlighted_Card_Sprites = []
    highlighted_Card_Sprites_rect = []

    def __init__(self):
        self.loadSprites()
        self.loadHighlightedSprites()

    def loadSprites(self):
        try:
            for card in self.cards:
                imageName = str(card) + '.png'
                cardImage, cardImageRect = Load_Image.ImageLoad.imageLoadfnc(imageName, True)
                self.card_Sprites.append(cardImage)
                self.card_Sprites_rect.append(cardImageRect)
        except TypeError:  # Catching a type error as if running a unit test there won't be any, or be a need for images
            pass

    def loadHighlightedSprites(self):
        try:
            for card in self.cards:
                imageName = str(card) + 'hl.png'
                highlightedcardImage, highlightedcardImageRect = Load_Image.ImageLoad.imageLoadfnc(imageName, True)
                self.highlighted_Card_Sprites.append(highlightedcardImage)
                self.highlighted_Card_Sprites_rect.append(highlightedcardImageRect)
        except TypeError:  # Catching a type error as if running a unit test there won't be any, or be a need for images
            pass

    def draw(self, hand, cardPosition):
        #print(type(self.cards))
        if (len(self.cards)) != 0:
            card = random.choice(self.cards)
            self.cards.remove(card)
            for x in range(0, 25):  # arbitrary max size of hand
                if cardPosition == x:
                    hand[cardPosition] = card

        return hand
