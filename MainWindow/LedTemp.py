from Helpers.Fonts import Fonts
from Helpers import Colors
import pygame
import os
from register import Register
from Helpers.Coordinate import Coordinate

class LedTemp:

    lcd = None
    redraw = True
    icon = None
    coordinate = None

    def __init__(self, coordinate):
        self.lcd = Register.LCD
        self.icon = pygame.image.load(os.path.join('icons', 'light32.png'))
        self.coordinate = coordinate

    def get_temp(self):
        return Register.LIGHT1_TEMP

    def draw_tile(self):

        if Register.LIGHT1_TEMP_ALERT:
            pygame.draw.rect(self.lcd, Colors.BLACK, pygame.Rect(self.coordinate.locate(0, 0), self.coordinate.size()))
        else:
            pygame.draw.rect(self.lcd, Colors.RED, pygame.Rect(self.coordinate.locate(0, 0), self.coordinate.size()))

        cord = Coordinate(*self.coordinate.get_slice(40))
        self.lcd.blit(self.icon, cord.get_center(self.icon.get_width(), self.icon.get_height()))

        cord = Coordinate(*self.coordinate.get_slice(100))
        text_surface = Fonts.font_40.render("%2.1f" % self.get_temp() + u'\u00B0'+"c", True, Colors.WHITE)
        self.lcd.blit(text_surface, cord.get_center(text_surface.get_width(), text_surface.get_height()))

        self.coordinate.reset_slice()
