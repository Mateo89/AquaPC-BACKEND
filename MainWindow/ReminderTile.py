import pygame

from Helpers import Colors
from Helpers.Fonts import Fonts
from register import Register


class ReminderTile:

    lcd = None
    redraw = True
    coordinate = None

    def __init__(self, coordinate):
        self.lcd = Register.LCD
        self.coordinate = coordinate

    def draw_tile(self):

        pygame.draw.rect(self.lcd, Colors.RED, pygame.Rect(self.coordinate.locate(0, 0), self.coordinate.size()))

        text_surface = Fonts.font_30.render("PODMIEN WODE", True, Colors.WHITE)
        self.lcd.blit(text_surface, self.coordinate.get_center(text_surface.get_width(), text_surface.get_height()))

