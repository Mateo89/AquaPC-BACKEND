import os
import pygame

from Display import DisplayRegister
from Display.BarTile import BarTile
from Helpers import Colors
from Helpers.Coordinate import Coordinate
from Helpers.Fonts import Fonts
from register import Register
from Helpers import LircEvents
from Logic import BottleLogic


class BottleWindow():
    lcd = None

    barTile = None
    selectedIndex = 0
    selected_bottle = 0
    bottles_on = []

    def __init__(self):
        self.lcd = Register.LCD
        self.barTile = BarTile(Coordinate(0, 0, 400, 25), "Dozownik", "home25.png")
        self.offIcon = pygame.image.load(os.path.join('icons', "tube70.png"))
        self.upIcon = pygame.image.load(os.path.join('icons', "up30.png"))
        self.downIcon = pygame.image.load(os.path.join('icons', "down30.png"))

    def event(self):
        if not Register.LIRC_EVENTS:
            return

        lirc_event = LircEvents.get_event()
        if lirc_event == LircEvents.KEY_BACK:
            DisplayRegister.set_menuWindow()

        if lirc_event == LircEvents.KEY_LEFT:
            self.selectedIndex = (self.selectedIndex - 1) % 6
        if lirc_event == LircEvents.KEY_RIGHT:
            self.selectedIndex = (self.selectedIndex + 1) % 6

        if lirc_event == LircEvents.KEY_OK:
            if self.selectedIndex == 0:
                self.selected_bottle = (self.selected_bottle - 1) % len(self.bottles_on)
            if self.selectedIndex == 1:
                self.selected_bottle = (self.selected_bottle + 1) % len(self.bottles_on)
            if self.selectedIndex == 2:
                BottleLogic.up_dose(1)
            if self.selectedIndex == 3:
                BottleLogic.down_dose(1)
            if self.selectedIndex == 4:
                BottleLogic.set_bottle(self.bottles_on[self.selected_bottle])
            if self.selectedIndex == 5:
                BottleLogic.refill_bottle(self.bottles_on[self.selected_bottle])

    def draw(self):

        self.lcd.fill(Colors.BLACK)
        self.barTile.draw_tile()

        self.bottles_on = []

        start = 0
        for x in ('bottle1', 'bottle2', 'bottle3', 'bottle4', 'bottle5', 'bottle6', 'bottle7', 'bottle8'):

            if Register.BOTTLE_MOD[x]['ON']:
                self.bottles_on.append(x)

                cord = Coordinate(10 + start, 40, 70, 120)

                height = int(Register.BOTTLE_MOD[x]['PERCENT'] / 1.85)
                height += 8

                pygame.draw.rect(self.lcd, Colors.BLUE, pygame.Rect(cord.locate(28, 65), (15, -height)))

                self.lcd.blit(self.offIcon, cord.locate(0, 0))
                text_surface = Fonts.font_30.render(Register.BOTTLE_MOD[x]['NAME'], True, Colors.WHITE)
                self.lcd.blit(text_surface, cord.locate(27, 75))
                text_surface = Fonts.font_20.render(str(Register.BOTTLE_MOD[x]['STATE']), True, Colors.WHITE)
                self.lcd.blit(text_surface, cord.locate(25, 95))

                text_surface = Fonts.font_20.render("(" + str(Register.BOTTLE_MOD[x]["PERCENT"]) + "%)",
                                                    True, Colors.WHITE)
                self.lcd.blit(text_surface, cord.locate(15, 110))
            start += 45

        # przyciski

        main_cord = Coordinate(0, 160, 400, 80)

        cord = Coordinate(*main_cord.get_slice(50))
        text_surface = Fonts.font_40.render(Register.BOTTLE_MOD[self.bottles_on[self.selected_bottle]]['NAME'],
                                                True, Colors.WHITE)
        self.lcd.blit(text_surface, cord.get_center(text_surface.get_width(), text_surface.get_height()))

        cord = Coordinate(*main_cord.get_slice(20))
        self.lcd.blit(self.upIcon, cord.get_center(self.upIcon.get_width(), self.upIcon.get_height()+20))
        if self.selectedIndex == 0:
                pygame.draw.rect(self.lcd, Colors.GRAY, pygame.Rect(cord.get_center(20, 18+26), (20, 18)), 2)

        self.lcd.blit(self.downIcon, cord.get_center(self.upIcon.get_width(), self.upIcon.get_height()-20))
        if self.selectedIndex == 1:
            pygame.draw.rect(self.lcd, Colors.GRAY, pygame.Rect(cord.get_center(20, 18-26), (20, 18)), 2)


        cord = Coordinate(*main_cord.get_slice(40))
        text_surface = Fonts.font_40.render(str(Register.BOTTLE_MANUAL_DOSE), True, Colors.WHITE)
        self.lcd.blit(text_surface, cord.get_center(text_surface.get_width(), text_surface.get_height()))

        cord = Coordinate(*main_cord.get_slice(30))
        text_surface = Fonts.font_30.render("ml", True, Colors.WHITE)
        self.lcd.blit(text_surface, cord.get_center(text_surface.get_width(), text_surface.get_height()))

        cord = Coordinate(*main_cord.get_slice(20))
        self.lcd.blit(self.upIcon, cord.get_center(self.upIcon.get_width(), self.upIcon.get_height()+20))
        if self.selectedIndex == 2:
                pygame.draw.rect(self.lcd, Colors.GRAY, pygame.Rect(cord.get_center(20, 18+26), (20, 18)), 2)

        self.lcd.blit(self.downIcon, cord.get_center(self.upIcon.get_width(), self.upIcon.get_height()-20))
        if self.selectedIndex == 3:
            pygame.draw.rect(self.lcd, Colors.GRAY, pygame.Rect(cord.get_center(20, 18-26), (20, 18)), 2)


        cord = Coordinate(*main_cord.get_slice(120))
        cord = Coordinate(*cord.get_center_surface(100, 40))
        pygame.draw.rect(self.lcd, Colors.BLUE, pygame.Rect(cord.size_full()))
        text_surface = Fonts.font_40.render("START", True, Colors.WHITE)
        self.lcd.blit(text_surface, cord.get_center(text_surface.get_width(), text_surface.get_height()))
        if self.selectedIndex == 4:
            pygame.draw.rect(self.lcd, Colors.GRAY, cord.size_full(), 2)

        cord = Coordinate(*main_cord.get_slice(120))
        cord = Coordinate(*cord.get_center_surface(100, 40))
        pygame.draw.rect(self.lcd, Colors.BLUE, pygame.Rect(cord.size_full()))
        text_surface = Fonts.font_40.render("UZUP", True, Colors.WHITE)
        self.lcd.blit(text_surface, cord.get_center(text_surface.get_width(), text_surface.get_height()))
        if self.selectedIndex == 5:
            pygame.draw.rect(self.lcd, Colors.GRAY, cord.size_full(), 2)

