import os

import settings
from Display import DisplayRegister
from Display.BarTile import BarTile
from Helpers import Colors
from Helpers.Coordinate import Coordinate
from Helpers.Fonts import Fonts
from register import Register
from Helpers import LircEvents
import pygame


class Light2SettingWindow():

    lcd = None

    barTile =None
    selectedIndex = 0
    tiles = []

    def __init__(self):
        self.lcd = Register.LCD
        self.barTile = BarTile(Coordinate(0, 0, 400, 25), "Lampa 2", "settings25.png")
        self.upIcon = pygame.image.load(os.path.join('icons', "up30.png"))
        self.downIcon = pygame.image.load(os.path.join('icons', "down30.png"))
        self.switch_on_icon = pygame.image.load(os.path.join("icons", "switchon50.png"))
        self.switch_off_icon = pygame.image.load(os.path.join("icons", "switchoff50.png"))
        self.on_hour = Register.LIGHT2_ON_HOUR
        self.on_min = Register.LIGHT2_ON_MINUTE
        self.off_hour = Register.LIGHT2_OFF_HOUR
        self.off_min = Register.LIGHT2_OFF_MINUTE
        self.change_water = Register.LIGHT2_CHANGE_WATER_ON_FLAG

    def event(self):
        if not Register.LIRC_EVENTS:
            return

        lirc_event = LircEvents.get_event()
        if lirc_event == LircEvents.KEY_BACK:
            DisplayRegister.set_settingsWindow()

        if lirc_event == LircEvents.KEY_RIGHT:
            self.selectedIndex = (self.selectedIndex + 1) % 11

        if lirc_event == LircEvents.KEY_LEFT:
            self.selectedIndex = (self.selectedIndex - 1) % 11

        if lirc_event == LircEvents.KEY_UP:
            self.selectedIndex = (self.selectedIndex - 4) % 11

        if lirc_event == LircEvents.KEY_DOWN:
            self.selectedIndex = (self.selectedIndex + 4) % 11

        if lirc_event == LircEvents.KEY_OK:
            if self.selectedIndex == 0:
                self.on_hour = (self.on_hour + 1) % 24
            if self.selectedIndex == 1:
                self.on_hour = (self.on_hour - 1) % 24
            if self.selectedIndex == 2:
                self.on_min = (self.on_min + 1) % 60
            if self.selectedIndex == 3:
                self.on_min = (self.on_min - 1) % 60
            if self.selectedIndex == 4:
                self.off_hour = (self.off_hour + 1) % 24
            if self.selectedIndex == 5:
                self.off_hour = (self.off_hour - 1) % 24
            if self.selectedIndex == 6:
                self.off_min = (self.off_min + 1) % 60
            if self.selectedIndex == 7:
                self.off_min = (self.off_min - 1) % 60
            if self.selectedIndex == 8:  #change_water flag
                self.change_water = not self.change_water
            if self.selectedIndex == 9:  #reset
                self.reset()
            if self.selectedIndex == 10:  #zapisz
                self.save()
                self.reset()

    def reset(self):
        self.on_hour = Register.LIGHT2_ON_HOUR
        self.on_min = Register.LIGHT2_ON_MINUTE
        self.off_hour = Register.LIGHT2_OFF_HOUR
        self.off_min = Register.LIGHT2_OFF_MINUTE
        self.change_water = Register.LIGHT2_CHANGE_WATER_ON_FLAG

    def save(self):
        Register.LIGHT2_ON_HOUR = self.on_hour
        Register.LIGHT2_ON_MINUTE = self.on_min
        Register.LIGHT2_OFF_HOUR = self.off_hour
        Register.LIGHT2_OFF_MINUTE = self.off_min
        Register.LIGHT2_CHANGE_WATER_ON_FLAG = self.change_water
        settings.save_settings()

    def draw(self):

        self.lcd.fill(Colors.BLACK)
        self.barTile.draw_tile()

        main_cord = Coordinate(0, 30, 400, 30)

        cord = Coordinate(*main_cord.get_slice(200))
        text_surface = Fonts.font_40.render("ON",
                                            True, Colors.WHITE)
        self.lcd.blit(text_surface, cord.get_center(text_surface.get_width(), text_surface.get_height()))

        cord = Coordinate(*main_cord.get_slice(30))
        if Register.LIGHT2_ON_HOUR != self.on_hour:
            pygame.draw.rect(self.lcd, Colors.RED, pygame.Rect(cord.locate(0, 0), cord.size()))
        text_surface = Fonts.font_40.render(str(self.on_hour),
                                            True, Colors.WHITE)
        self.lcd.blit(text_surface, cord.get_center(text_surface.get_width(), text_surface.get_height()))

        cord = Coordinate(*main_cord.get_slice(30))
        self.lcd.blit(self.upIcon, cord.get_center(self.upIcon.get_width(), self.upIcon.get_height()+20))
        if self.selectedIndex == 0:
            pygame.draw.rect(self.lcd, Colors.GRAY, pygame.Rect(cord.get_center(30, 18+26), (30, 18)), 2)
        self.lcd.blit(self.downIcon, cord.get_center(self.upIcon.get_width(), self.upIcon.get_height()-20))
        if self.selectedIndex == 1:
            pygame.draw.rect(self.lcd, Colors.GRAY, pygame.Rect(cord.get_center(30, 18-26), (30, 18)), 2)

        cord = Coordinate(*main_cord.get_slice(30))
        text_surface = Fonts.font_30.render(":", True, Colors.WHITE)
        self.lcd.blit(text_surface, cord.get_center(text_surface.get_width(), text_surface.get_height()))

        cord = Coordinate(*main_cord.get_slice(30))
        if Register.LIGHT2_ON_MINUTE != self.on_min:
            pygame.draw.rect(self.lcd, Colors.RED, pygame.Rect(cord.locate(0, 0), cord.size()))
        text_surface = Fonts.font_40.render(str(self.on_min), True, Colors.WHITE)
        self.lcd.blit(text_surface, cord.get_center(text_surface.get_width(), text_surface.get_height()))

        cord = Coordinate(*main_cord.get_slice(30))
        self.lcd.blit(self.upIcon, cord.get_center(self.upIcon.get_width(), self.upIcon.get_height()+20))
        if self.selectedIndex == 2:
            pygame.draw.rect(self.lcd, Colors.GRAY, pygame.Rect(cord.get_center(30, 18+26), (30, 18)), 2)
        self.lcd.blit(self.downIcon, cord.get_center(self.upIcon.get_width(), self.upIcon.get_height()-20))
        if self.selectedIndex == 3:
            pygame.draw.rect(self.lcd, Colors.GRAY, pygame.Rect(cord.get_center(30, 18-26), (30, 18)), 2)

        main_cord = Coordinate(0, 70, 400, 30)

        cord = Coordinate(*main_cord.get_slice(200))
        text_surface = Fonts.font_40.render("OFF",
                                            True, Colors.WHITE)
        self.lcd.blit(text_surface, cord.get_center(text_surface.get_width(), text_surface.get_height()))

        cord = Coordinate(*main_cord.get_slice(30))
        if Register.LIGHT2_OFF_HOUR != self.off_hour:
            pygame.draw.rect(self.lcd, Colors.RED, pygame.Rect(cord.locate(0, 0), cord.size()))
        text_surface = Fonts.font_40.render(str(self.off_hour),
                                            True, Colors.WHITE)
        self.lcd.blit(text_surface, cord.get_center(text_surface.get_width(), text_surface.get_height()))

        cord = Coordinate(*main_cord.get_slice(30))
        self.lcd.blit(self.upIcon, cord.get_center(self.upIcon.get_width(), self.upIcon.get_height()+20))
        if self.selectedIndex == 4:
            pygame.draw.rect(self.lcd, Colors.GRAY, pygame.Rect(cord.get_center(30, 18+26), (30, 18)), 2)
        self.lcd.blit(self.downIcon, cord.get_center(self.downIcon.get_width(), self.downIcon.get_height()-20))
        if self.selectedIndex == 5:
            pygame.draw.rect(self.lcd, Colors.GRAY, pygame.Rect(cord.get_center(30, 18-26), (30, 18)), 2)

        cord = Coordinate(*main_cord.get_slice(30))
        text_surface = Fonts.font_30.render(":", True, Colors.WHITE)
        self.lcd.blit(text_surface, cord.get_center(text_surface.get_width(), text_surface.get_height()))

        cord = Coordinate(*main_cord.get_slice(30))
        if Register.LIGHT2_OFF_MINUTE != self.off_min:
            pygame.draw.rect(self.lcd, Colors.RED, pygame.Rect(cord.locate(0, 0), cord.size()))
        text_surface = Fonts.font_40.render(str(self.off_min), True, Colors.WHITE)
        self.lcd.blit(text_surface, cord.get_center(text_surface.get_width(), text_surface.get_height()))

        cord = Coordinate(*main_cord.get_slice(30))
        self.lcd.blit(self.upIcon, cord.get_center(self.upIcon.get_width(), self.upIcon.get_height()+20))
        if self.selectedIndex == 6:
            pygame.draw.rect(self.lcd, Colors.GRAY, pygame.Rect(cord.get_center(30, 18+26), (30, 18)), 2)
        self.lcd.blit(self.downIcon, cord.get_center(self.upIcon.get_width(), self.upIcon.get_height()-20))
        if self.selectedIndex == 7:
            pygame.draw.rect(self.lcd, Colors.GRAY, pygame.Rect(cord.get_center(30, 18-26), (30, 18)), 2)

        main_cord = Coordinate(0, 150, 400, 30)
        cord = Coordinate(*main_cord.get_slice(320))
        text_surface = Fonts.font_30.render("WL. PODCZAS ZMIANY WODY", True, Colors.WHITE)
        self.lcd.blit(text_surface, cord.get_center(text_surface.get_width(), text_surface.get_height()))

        cord = Coordinate(*main_cord.get_slice(60))

        if Register.LIGHT2_CHANGE_WATER_ON_FLAG != self.change_water:
            pygame.draw.rect(self.lcd, Colors.RED, pygame.Rect(cord.size_full()))
        if self.change_water:
            self.lcd.blit(self.switch_on_icon, cord.get_center(self.switch_on_icon.get_width(), self.switch_on_icon.get_height()))
        else:
            self.lcd.blit(self.switch_off_icon, cord.get_center(self.switch_off_icon.get_width(), self.switch_off_icon.get_height()))
        if self.selectedIndex == 8:
            pygame.draw.rect(self.lcd, Colors.GRAY, cord.size_full(), 2)

        main_cord = Coordinate(0, 190, 400, 40)
        cord = Coordinate(*main_cord.get_slice(200))
        cord = Coordinate(*cord.get_center_surface(150, 40))
        pygame.draw.rect(self.lcd, Colors.BLUE, pygame.Rect(cord.size_full()))
        text_surface = Fonts.font_30.render("RESET", True, Colors.WHITE)
        self.lcd.blit(text_surface, cord.get_center(text_surface.get_width(), text_surface.get_height()))
        if self.selectedIndex == 9:
            pygame.draw.rect(self.lcd, Colors.GRAY, cord.size_full(), 2)

        cord = Coordinate(*main_cord.get_slice(200))
        cord = Coordinate(*cord.get_center_surface(150, 40))
        pygame.draw.rect(self.lcd, Colors.BLUE, pygame.Rect(cord.size_full()))
        text_surface = Fonts.font_30.render("ZAPISZ", True, Colors.WHITE)
        self.lcd.blit(text_surface, cord.get_center(text_surface.get_width(), text_surface.get_height()))
        if self.selectedIndex == 10:
            pygame.draw.rect(self.lcd, Colors.GRAY, cord.size_full(), 2)
