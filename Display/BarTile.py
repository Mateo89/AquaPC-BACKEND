from Helpers.Coordinate import Coordinate
from register import Register
from Helpers import Colors
from Helpers.Fonts import Fonts
import pygame
from datetime import datetime
import os


class BarTile:
    lcd = None
    redraw = True
    coordinate = None
    icon = None
    iconName = None
    name = None

    def __init__(self, coordinate, name, iconName):
        self.lcd = Register.LCD
        self.coordinate = coordinate
        self.name = name
        self.icon = pygame.image.load(os.path.join('icons', iconName))

    def draw_tile(self):
        self.coordinate.reset_slice()
        pygame.draw.rect(self.lcd, Colors.BLUE, pygame.Rect(self.coordinate.size_full()))

        cord = Coordinate(*self.coordinate.get_slice(30))
        self.lcd.blit(self.icon, cord.get_center(self.icon.get_width(), self.icon.get_height()))

        cord = Coordinate(*self.coordinate.get_slice(300))
        text_surface = Fonts.font_30.render(self.name, True, Colors.WHITE)
        self.lcd.blit(text_surface, cord.locate_vertical_center(10, text_surface.get_height()))

        cord = Coordinate(*self.coordinate.get_slice(50))
        text_surface = Fonts.font_30.render(datetime.now().strftime('%H:%M:%S'), True, Colors.WHITE)
        self.lcd.blit(text_surface, cord.get_center(text_surface.get_width(), text_surface.get_height()))
