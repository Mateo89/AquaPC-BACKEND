from Helpers.Coordinate import Coordinate
from Helpers.Fonts import Fonts
from Helpers import Colors
from register import Register
import pygame
import os


class AirTemp:
    lcd = None
    redraw = True
    icon = None
    coordinate = None

    def __init__(self, coordinate):
        self.lcd = Register.LCD
        self.icon = pygame.image.load(os.path.join('icons', 'air-temp32.png'))
        self.coordinate = coordinate

    def getTemp(self):
        return Register.AIR_TEMP

    def draw_tile(self):
        self.coordinate.reset_slice()

        if Register.AIR_TEMP < 30:
            pygame.draw.rect(self.lcd, Colors.BLACK, pygame.Rect(self.coordinate.size_full()))
        else:
            pygame.draw.rect(self.lcd, Colors.RED, pygame.Rect(self.coordinate.size_full()))

        cord = Coordinate(*self.coordinate.get_slice(40))
        self.lcd.blit(self.icon, cord.get_center(self.icon.get_width(), self.icon.get_height()))

        cord = Coordinate(*self.coordinate.get_slice(100))
        text_surface = Fonts.font_40.render("%2.1f" % self.getTemp() + u'\u00B0' + "c", True, Colors.WHITE)
        self.lcd.blit(text_surface, cord.get_center(text_surface.get_width(), text_surface.get_height()))
