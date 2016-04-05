__author__ = 'mateo'

from Helpers import Colors
from Helpers.Fonts import Fonts
import pygame
import os
from register import Register

class O2Switch:

    lcd = None
    coordinate = None
    icon = None

    def __init__(self, coordinate):
        self.lcd = Register.LCD
        self.coordinate = coordinate
        #self.icon = pygame.image.load(os.path.join('icons', 'fan32.png'))

    def draw(self):
        if not Register.I2C_POWERMOD_O2_OVERDRIVE:
            pygame.draw.rect(self.lcd, Colors.BLACK, pygame.Rect(self.coordinate.locate(0, 0),
                                                             (self.coordinate.width, self.coordinate.height)))
        else:
            pygame.draw.rect(self.lcd, Colors.BLUE, pygame.Rect(self.coordinate.locate(0, 0),
                                                            (self.coordinate.width, self.coordinate.height)))
        #self.lcd.blit(self.icon, self.coordinate.locate(3, 3))

        if not Register.I2C_POWERMOD_O2_FLAG:
            return

        text_surface = Fonts.font_60.render("O", True, Colors.WHITE)
        self.lcd.blit(text_surface, self.coordinate.locate(5, 3))

        text_surface = Fonts.font_30.render("2", True, Colors.WHITE)
        self.lcd.blit(text_surface, self.coordinate.locate(35, 27))
