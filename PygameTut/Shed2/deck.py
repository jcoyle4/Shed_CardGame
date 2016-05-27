import random
import Load_Image


class DeckClass:

    # List of Cards
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,           # 2-Ace of Clubs
             14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,  # 2-Ace of Diamonds
             27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39,  # 2-Ace of Hearts
             40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]  # 2-Ace of Spades

    card_Sprites = []
    card_Sprites_rect = []
    highlighted_Card_Sprites = []
    highlighted_Card_Sprites_rect = []

    # Constructor
    def __init__(self):
        self.load_sprites()
        self.load_highlighted_sprites()

    # Load each card sprite and put it in a list
    def load_sprites(self):
        try:
            for card in self.cards:
                image_name = str(card) + '.png'
                card_image, card_image_rect = Load_Image.ImageLoad.image_load(image_name, True)
                self.card_Sprites.append(card_image)
                self.card_Sprites_rect.append(card_image_rect)
        except TypeError:  # Catching a type error as if running a unit test there won't be any, or be a need for images
            pass

    # Load each highlighted card sprite and put it in a list
    def load_highlighted_sprites(self):
        try:
            for card in self.cards:
                image_name = str(card) + 'hl.png'
                highlighted_card_image, highlighted_card_image_rect = Load_Image.ImageLoad.image_load(image_name, True)
                self.highlighted_Card_Sprites.append(highlighted_card_image)
                self.highlighted_Card_Sprites_rect.append(highlighted_card_image_rect)
        except TypeError:  # Catching a type error as if running a unit test there won't be any, or be a need for images
            pass

    # Method to draw a card from the deck
    def draw(self, hand, card_position):
        if (len(self.cards)) != 0:
            # Randomly choose a card from those that are left in the list
            card = random.choice(self.cards)
            # Remove the card from the list
            self.cards.remove(card)
            for x in range(0, 25):  # arbitrary max size of hand
                # Used the passed in position of the none slot in the hand
                # when x reaches this none slot
                if card_position == x:
                    # put the new card into this none slot
                    hand[card_position] = card

        return hand
