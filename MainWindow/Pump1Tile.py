__author__ = 'mateo'

from Helpers import Colors
from Helpers.Fonts import Fonts
import pygame
import os

class Pump1Tile:

    lcd = None
    coordinate = None
    icon = None

    def __init__(self, lcd, coordinate):
        self.lcd = lcd
        self.coordinate = coordinate
        self.icon = pygame.image.load(os.path.join('icons', 'feed32.png'))

    def draw(self):
        pygame.draw.rect(self.lcd, Colors.BLUE, pygame.Rect(self.coordinate.locate(0, 0),
                                                             (self.coordinate.width, self.coordinate.height)))
        self.lcd.blit(self.icon, self.coordinate.locate(8, 8))

        #text_surface = Fonts.font_30.render("1", True, Colors.WHITE)
        #self.lcd.blit(text_surface, self.coordinate.locate(35, 15))

        #text_surface = Fonts.font_20.render("LED", True, Colors.WHITE)
        #self.lcd.blit(text_surface, self.coordinate.locate(10, 35))