from Helpers.Coordinate import Coordinate
from register import Register
from Helpers.Fonts import Fonts
from Helpers import Colors
import pygame
import os

class PhTile:

    lcd = None
    i = 6.0
    redraw = True
    icon = None
    coordinate = None

    def __init__(self, coordinate):
        self.lcd = Register.LCD
        self.icon = pygame.image.load(os.path.join('icons', 'ph32.png'))
        self.coordinate = coordinate

    def get_ph(self):
        return self.i

    def draw_tile(self):

        pygame.draw.rect(self.lcd, Colors.BLACK, pygame.Rect(self.coordinate.locate(0, 0), self.coordinate.size()))

        cord = Coordinate(*self.coordinate.get_slice(40))
        self.lcd.blit(self.icon, cord.get_center(self.icon.get_width(),self.icon.get_height()))

        cord = Coordinate(*self.coordinate.get_slice(60))
        text_surface = Fonts.font_40.render("%.1f" % self.get_ph(), True, Colors.WHITE)
        self.lcd.blit(text_surface, cord.get_center(text_surface.get_width(), text_surface.get_height()))

        cord = Coordinate(*self.coordinate.get_slice(40))
        text_surface = Fonts.font_30.render("pH ", True, Colors.WHITE)
        self.lcd.blit(text_surface, cord.get_center(text_surface.get_width(), text_surface.get_height()))

        self.coordinate.reset_slice()
