from Helpers import Colors
from Helpers.Coordinate import Coordinate
from Helpers.Fonts import Fonts
from register import Register
import pygame
import os


class MenuTile():

    lcd = None
    coordinate = None
    icon = None
    name = None
    selected = False

    def __init__(self, coordinate, iconName, name):
        self.lcd = Register.LCD
        self.coordinate = coordinate
        self.name = name
        self.icon = pygame.image.load(os.path.join('icons', iconName))

    def select(self):
        self.selected = True

    def unselect(self):
        self.selected = False

    def draw(self):
        self.coordinate.reset_slice()

        pygame.draw.rect(self.lcd, Colors.BLUE, pygame.Rect(self.coordinate.size_full()))
        if self.selected:
            pygame.draw.rect(self.lcd, Colors.WHITE,  pygame.Rect(self.coordinate.size_full()), 5)

        cord = Coordinate(*self.coordinate.get_slice(40))
        self.lcd.blit(self.icon, cord.get_center(self.icon.get_width(), self.icon.get_height()))

        cord = Coordinate(*self.coordinate.get_slice(100))
        text_surface = Fonts.font_30.render(self.name, True, Colors.WHITE)
        self.lcd.blit(text_surface,  cord.locate_vertical_center(0, text_surface.get_height()))
