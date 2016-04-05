__author__ = 'mateo'

from Helpers import Colors
from Helpers.Fonts import Fonts
import Helpers
import pygame
import os
from register import Register


class LigthModeTile:

    lcd = None
    coordinate = None
    icon = None
    mode = 1

    def __init__(self, coordinate):
        self.lcd = Register.LCD
        self.coordinate = coordinate
        self.icon = pygame.image.load(os.path.join('icons', 'sunrise60.png'))

    def draw(self):
        pygame.draw.rect(self.lcd, Colors.BLACK, pygame.Rect(self.coordinate.locate(0, 0),
                                                             (self.coordinate.width, self.coordinate.height)))

        # 0 - night
        # 1 - sunrise/sunset
        # 2 - sunny

        if Register.LIGHT_MODE != self.mode:
            if Register.LIGHT_MODE == 0:
                self.icon = pygame.image.load(os.path.join('icons', 'moon60.png'))
            elif Register.LIGHT_MODE == 1:
                self.icon = pygame.image.load(os.path.join('icons', 'sunrise60.png'))
            elif Register.LIGHT_MODE == 2:
                self.icon = pygame.image.load(os.path.join('icons', 'sun60.png'))
            self.mode = Register.LIGHT_MODE

        self.lcd.blit(self.icon, self.coordinate.locate(5, 5))
