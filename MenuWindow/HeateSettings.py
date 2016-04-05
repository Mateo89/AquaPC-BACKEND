import os
from Display import DisplayRegister
from Display.BarTile import BarTile
from Helpers import Colors
from Helpers.Coordinate import Coordinate
from Helpers.Fonts import Fonts
from register import Register
from Helpers import LircEvents
import pygame
import settings

class HeaterSettingWindow():

    lcd = None

    barTile =None
    selectedIndex = 0
    tiles = []

    def __init__(self):
        self.lcd = Register.LCD
        self.barTile = BarTile(Coordinate(0, 0, 400, 25), "GRZALKA", "settings25.png")
        self.upIcon = pygame.image.load(os.path.join('icons', "up30.png"))
        self.downIcon = pygame.image.load(os.path.join('icons', "down30.png"))
        self.temp_set = Register.WATER_TEMP_SET
        self.temp_alert_delta = Register.WATER_TEMP_ALERT_DELTA
        self.temp_on_off_delta = Register.WATER_TEMP_ONOFF_DELTA

    def event(self):
        if not Register.LIRC_EVENTS:
            return

        lirc_event = LircEvents.get_event()
        if lirc_event == LircEvents.KEY_BACK:
            DisplayRegister.set_settingsWindow()

        if lirc_event == LircEvents.KEY_RIGHT:
            self.selectedIndex = (self.selectedIndex + 1) % 8

        if lirc_event == LircEvents.KEY_LEFT:
            self.selectedIndex = (self.selectedIndex - 2) % 8

        if lirc_event == LircEvents.KEY_UP:
            self.selectedIndex = (self.selectedIndex - 2) % 8

        if lirc_event == LircEvents.KEY_DOWN:
            self.selectedIndex = (self.selectedIndex + 2) % 8

        if lirc_event == LircEvents.KEY_OK:
            if self.selectedIndex == 0:
                self.temp_set = (self.temp_set + 0.1) % 30
            if self.selectedIndex == 1:
                self.temp_set = (self.temp_set - 0.1) % 30
            if self.selectedIndex == 2:
                self.temp_alert_delta = (self.temp_alert_delta + 0.1) % 20
            if self.selectedIndex == 3:
                self.temp_alert_delta = (self.temp_alert_delta - 0.1) % 20
            if self.selectedIndex == 4:
                self.temp_on_off_delta = (self.temp_on_off_delta + 0.1) % 3
            if self.selectedIndex == 5:
                self.temp_on_off_delta = (self.temp_on_off_delta - 0.1) % 3
            if self.selectedIndex == 6:  #reset
                self.reset()
            if self.selectedIndex == 7:  #zapisz
                self.save()
                self.reset()

    def reset(self):
        self.temp_set = Register.WATER_TEMP_SET
        self.temp_alert_delta = Register.WATER_TEMP_ALERT_DELTA
        self.temp_on_off_delta = Register.WATER_TEMP_ONOFF_DELTA

    def save(self):
        Register.WATER_TEMP_SET = self.temp_set
        Register.WATER_TEMP_ALERT_DELTA = self.temp_alert_delta
        Register.WATER_TEMP_ONOFF_DELTA = self.temp_on_off_delta
        settings.save_settings()

    def draw(self):

        self.lcd.fill(Colors.BLACK)
        self.barTile.draw_tile()

        main_cord = Coordinate(0, 50, 400, 30)

        cord = Coordinate(*main_cord.get_slice(300))
        text_surface = Fonts.font_40.render("TEMP WODY",
                                            True, Colors.WHITE)
        self.lcd.blit(text_surface, cord.get_center(text_surface.get_width(), text_surface.get_height()))

        cord = Coordinate(*main_cord.get_slice(60))
        if Register.WATER_TEMP_SET != self.temp_set:
            pygame.draw.rect(self.lcd, Colors.RED, pygame.Rect(cord.locate(0, 0), cord.size()))
        text_surface = Fonts.font_40.render(str(self.temp_set), True, Colors.WHITE)
        self.lcd.blit(text_surface, cord.get_center(text_surface.get_width(), text_surface.get_height()))

        cord = Coordinate(*main_cord.get_slice(30))
        self.lcd.blit(self.upIcon, cord.get_center(self.upIcon.get_width(), self.upIcon.get_height()+20))
        if self.selectedIndex == 0:
            pygame.draw.rect(self.lcd, Colors.GRAY, pygame.Rect(cord.get_center(30, 18+26), (30, 18)), 2)
        self.lcd.blit(self.downIcon, cord.get_center(self.upIcon.get_width(), self.upIcon.get_height()-20))
        if self.selectedIndex == 1:
            pygame.draw.rect(self.lcd, Colors.GRAY, pygame.Rect(cord.get_center(30, 18-26), (30, 18)), 2)

        main_cord = Coordinate(0, 90, 400, 30)

        cord = Coordinate(*main_cord.get_slice(300))
        text_surface = Fonts.font_40.render("TEMP ALERT DELTA",
                                            True, Colors.WHITE)
        self.lcd.blit(text_surface, cord.get_center(text_surface.get_width(), text_surface.get_height()))

        cord = Coordinate(*main_cord.get_slice(60))
        if Register.WATER_TEMP_ALERT_DELTA != self.temp_alert_delta:
            pygame.draw.rect(self.lcd, Colors.RED, pygame.Rect(cord.locate(0, 0), cord.size()))
        text_surface = Fonts.font_40.render(str(self.temp_alert_delta), True, Colors.WHITE)
        self.lcd.blit(text_surface, cord.get_center(text_surface.get_width(), text_surface.get_height()))

        cord = Coordinate(*main_cord.get_slice(30))
        self.lcd.blit(self.upIcon, cord.get_center(self.upIcon.get_width(), self.upIcon.get_height()+20))
        if self.selectedIndex == 2:
            pygame.draw.rect(self.lcd, Colors.GRAY, pygame.Rect(cord.get_center(30, 18+26), (30, 18)), 2)
        self.lcd.blit(self.downIcon, cord.get_center(self.upIcon.get_width(), self.upIcon.get_height()-20))
        if self.selectedIndex == 3:
            pygame.draw.rect(self.lcd, Colors.GRAY, pygame.Rect(cord.get_center(30, 18-26), (30, 18)), 2)

        main_cord = Coordinate(0, 130, 400, 30)

        cord = Coordinate(*main_cord.get_slice(300))
        text_surface = Fonts.font_40.render("ON/OFF DELTA",
                                            True, Colors.WHITE)
        self.lcd.blit(text_surface, cord.get_center(text_surface.get_width(), text_surface.get_height()))

        cord = Coordinate(*main_cord.get_slice(60))
        if Register.WATER_TEMP_ONOFF_DELTA != self.temp_on_off_delta:
            pygame.draw.rect(self.lcd, Colors.RED, pygame.Rect(cord.locate(0, 0), cord.size()))
        text_surface = Fonts.font_40.render(str(self.temp_on_off_delta), True, Colors.WHITE)
        self.lcd.blit(text_surface, cord.get_center(text_surface.get_width(), text_surface.get_height()))

        cord = Coordinate(*main_cord.get_slice(30))
        self.lcd.blit(self.upIcon, cord.get_center(self.upIcon.get_width(), self.upIcon.get_height()+20))
        if self.selectedIndex == 4:
            pygame.draw.rect(self.lcd, Colors.GRAY, pygame.Rect(cord.get_center(30, 18+26), (30, 18)), 2)
        self.lcd.blit(self.downIcon, cord.get_center(self.upIcon.get_width(), self.upIcon.get_height()-20))
        if self.selectedIndex == 5:
            pygame.draw.rect(self.lcd, Colors.GRAY, pygame.Rect(cord.get_center(30, 18-26), (30, 18)), 2)

        main_cord = Coordinate(0, 190, 400, 40)
        cord = Coordinate(*main_cord.get_slice(200))
        cord = Coordinate(*cord.get_center_surface(150, 40))
        pygame.draw.rect(self.lcd, Colors.BLUE, pygame.Rect(cord.size_full()))
        text_surface = Fonts.font_30.render("RESET", True, Colors.WHITE)
        self.lcd.blit(text_surface, cord.get_center(text_surface.get_width(), text_surface.get_height()))
        if self.selectedIndex == 6:
            pygame.draw.rect(self.lcd, Colors.GRAY, cord.size_full(), 2)

        cord = Coordinate(*main_cord.get_slice(200))
        cord = Coordinate(*cord.get_center_surface(150, 40))
        pygame.draw.rect(self.lcd, Colors.BLUE, pygame.Rect(cord.size_full()))
        text_surface = Fonts.font_30.render("ZAPISZ", True, Colors.WHITE)
        self.lcd.blit(text_surface, cord.get_center(text_surface.get_width(), text_surface.get_height()))
        if self.selectedIndex == 7:
            pygame.draw.rect(self.lcd, Colors.GRAY, cord.size_full(), 2)
