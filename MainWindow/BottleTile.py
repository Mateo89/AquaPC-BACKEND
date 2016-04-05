from Helpers import Colors
from Helpers.Fonts import Fonts
import pygame
import os
from register import Register


class BottleTile:

    lcd = None
    coordinate = None
    icon = None
    key = None
    number = None

    def __init__(self, coordinate, key):
        self.lcd = Register.LCD
        self.coordinate = coordinate
        self.icon = pygame.image.load(os.path.join('icons', 'tube502.png'))
        self.key = key

    def draw(self):

        if Register.BOTTLE_MOD[self.key]['PERCENT'] > Register.BOTTLE_PERCENT_ALERT:
            pygame.draw.rect(self.lcd, Colors.BLACK, pygame.Rect(self.coordinate.locate(0, 0),
                             (self.coordinate.width, self.coordinate.height)))
        else:
            pygame.draw.rect(self.lcd, Colors.RED, pygame.Rect(self.coordinate.locate(0, 0),
                             (self.coordinate.width, self.coordinate.height)))

        #obliczenie wysokosci slupa
        height = int(Register.BOTTLE_MOD[self.key]['PERCENT'] / 2.63)
        height += 8

        pygame.draw.rect(self.lcd, Colors.BLUE, pygame.Rect(self.coordinate.locate(9, 53),(8,-height)))

        self.lcd.blit(self.icon, self.coordinate.locate(0, 5))

        text_surface = Fonts.font_20.render(Register.BOTTLE_MOD[self.key]['NAME'], True, Colors.WHITE)
        self.lcd.blit(text_surface, self.coordinate.locate(7, 55))