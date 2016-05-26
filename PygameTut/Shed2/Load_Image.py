import os
import pygame


class ImageLoad:

    @staticmethod
    def image_load(name, card):
        # Function for loading an image. Makes sure the game is compatible across multiple OS'es, as it
        # uses the os.path.join function to get he full filename. It then tries to load the image,
        # and raises an exception if it can't, so the user will know specifically what's going if the image loading
        # does not work.

        if card:
            fullname = os.path.join("Images/Cards/", name)
        else:
            fullname = os.path.join('Images', name)

        try:
            image = pygame.image.load(fullname)
            image = image.convert()

            return image, image.get_rect()
        except FileNotFoundError:
            print('Cannot load image:', name)
        except pygame.error:
            pass
