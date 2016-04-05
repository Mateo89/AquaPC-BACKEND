from Helpers.Coordinate import Coordinate
from Helpers.Fonts import Fonts
from Helpers import Colors
from register import Register
import pygame
import os
import math


class WaterTemp:

    lcd = None
    i = 20.0
    redraw = True
    icon = None
    coordinate = None

    def __init__(self, coordinate):
        self.lcd = Register.LCD
        self.icon = pygame.image.load(os.path.join('icons', 'water-temp32.png'))
        self.coordinate = coordinate

    def getTemp(self):
        return Register.WATER_TEMP

    def draw_tile(self):

        if math.fabs(Register.WATER_TEMP_SET - Register.WATER_TEMP) < Register.WATER_TEMP_ALERT_DELTA:
            pygame.draw.rect(self.lcd, Colors.BLACK, pygame.Rect(self.coordinate.size_full()))
        else:
            pygame.draw.rect(self.lcd, Colors.RED, pygame.Rect(self.coordinate.size_full()))

        cord = Coordinate(*self.coordinate.get_slice(40))
        self.lcd.blit(self.icon, cord.get_center(self.icon.get_width(), self.icon.get_height()))

        cord = Coordinate(*self.coordinate.get_slice(100))
        text_surface = Fonts.font_40.render("%.1f" % self.getTemp() + u'\u00B0'+"c", True, Colors.WHITE)
        self.lcd.blit(text_surface, cord.get_center(text_surface.get_width(), text_surface.get_height()))

        self.coordinate.reset_slice()
