__author__ = 'mateo'

from Helpers import Colors
from Helpers.Fonts import Fonts
import pygame
import os
from register import Register

class HeaterSwitch:

    lcd = None
    coordinate = None
    icon = None

    def __init__(self, coordinate):
        self.lcd = Register.LCD
        self.coordinate = coordinate
        self.icon = pygame.image.load(os.path.join('icons', 'heater40.png'))

    def draw(self):
        if not Register.I2C_POWERMOD_HEATER_OVERDRIVE:
            pygame.draw.rect(self.lcd, Colors.BLACK, pygame.Rect(self.coordinate.locate(0, 0),
                                                             (self.coordinate.width, self.coordinate.height)))
        else:
            pygame.draw.rect(self.lcd, Colors.BLUE, pygame.Rect(self.coordinate.locate(0, 0),
                                                            (self.coordinate.width, self.coordinate.height)))

        if not Register.I2C_POWERMOD_HEATER_FLAG:
            return

        self.lcd.blit(self.icon, self.coordinate.locate(5, 3))

        

        #text_surface = Fonts.font_30.render("1", True, Colors.WHITE)
        #self.lcd.blit(text_surface, self.coordinate.locate(35, 15))

        #text_surface = Fonts.font_20.render("LED", True, Colors.WHITE)
        #self.lcd.blit(text_surface, self.coordinate.locate(10, 35))
