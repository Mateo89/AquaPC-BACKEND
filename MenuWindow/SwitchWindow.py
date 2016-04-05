import os

from Display import DisplayRegister
from Display.BarTile import BarTile
import pygame
from Helpers import Colors
from Helpers.Coordinate import Coordinate
from Helpers.Fonts import Fonts
from Logic import Light1Logic
from register import Register
from Helpers import LircEvents
from Logic import Filter1Logic
from Logic import Filter2Logic
from Logic import O2Logic
from Logic import Co2Logic
from Logic import WaterTempLogic

class SwitchWindow():

    lcd = None

    barTile =None
    selectedIndex = 0

    def __init__(self):
        self.lcd = Register.LCD
        self.barTile = BarTile(Coordinate(0, 0, 400, 25),"Wlacznik","switch25.png")
        self.filter1 = pygame.image.load(os.path.join('icons', 'fan32.png'))
        self.filter2 = pygame.image.load(os.path.join('icons', 'fan32.png'))
        self.heater = pygame.image.load(os.path.join('icons', 'heater32.png'))
        self.switch_on = pygame.image.load(os.path.join('icons', 'switchon50.png'))
        self.switch_off = pygame.image.load(os.path.join('icons', 'switchoff50.png'))

    def event(self):
        if not Register.LIRC_EVENTS:
            return

        lirc_event = LircEvents.get_event()
        if lirc_event == LircEvents.KEY_BACK:
            DisplayRegister.set_menuWindow()

        if lirc_event == LircEvents.KEY_RIGHT:
            self.selectedIndex = (self.selectedIndex + 1) % 7
        if lirc_event == LircEvents.KEY_DOWN:

            if self.selectedIndex == 3 or self.selectedIndex == 4 or self.selectedIndex == 5:
                self.selectedIndex = 6
            else:
                self.selectedIndex = (self.selectedIndex + 3) % 7

        if lirc_event == LircEvents.KEY_LEFT:
            self.selectedIndex = (self.selectedIndex - 1) % 7
        if lirc_event == LircEvents.KEY_UP:
            if self.selectedIndex == 6:
                self.selectedIndex = 3
            else:
                self.selectedIndex = (self.selectedIndex - 3) % 7

        if lirc_event == LircEvents.KEY_OK:
            if self.selectedIndex == 0:
                Filter1Logic.block_filter()
                Filter1Logic.toggle_filter()

            if self.selectedIndex == 1: # podniesienie procentow o 5%
                O2Logic.block_o2()
                O2Logic.toggle_o2()

            if self.selectedIndex == 2:
                WaterTempLogic.block_heater()
                WaterTempLogic.toggle_heater()

            if self.selectedIndex == 3:
                Filter2Logic.block_filter()
                Filter2Logic.toggle_filter()

            if self.selectedIndex == 4:
                Co2Logic.block_co2()
                Co2Logic.toggle_co2()

            if self.selectedIndex == 5:
                WaterTempLogic.block_heater_led()
                WaterTempLogic.toggle_heater_led()

            if self.selectedIndex == 6:
                Filter1Logic.unblock_filter()
                Filter2Logic.unblock_filter()
                O2Logic.unblock_o2()
                Co2Logic.unblock_co2()
                WaterTempLogic.unblock_heater()
                WaterTempLogic.unblock_heater_led()

    def draw(self):

        self.lcd.fill(Colors.BLACK)
        self.barTile.draw_tile()

        cord = Coordinate(20, 40, 110, 60)
        if Register.I2C_POWERMOD_FILTER1_OVERDRIVE:
            pygame.draw.rect(self.lcd, Colors.RED, pygame.Rect(cord.locate(0,0),cord.size()))
        else:
            pygame.draw.rect(self.lcd, Colors.BLUE, pygame.Rect(cord.locate(0,0),cord.size()))

        self.lcd.blit(self.filter1, cord.locate(3, 3))

        if Register.I2C_POWERMOD_FILTER1_FLAG:
            self.lcd.blit(self.switch_on, cord.locate(55,20))
        else:
            self.lcd.blit(self.switch_off, cord.locate(55,20))
        text_surface = Fonts.font_30.render("1", True, Colors.WHITE)
        self.lcd.blit(text_surface, cord.locate(35, 20))
        if self.selectedIndex == 0:
            pygame.draw.rect(self.lcd, Colors.GRAY, pygame.Rect(cord.locate(0,0),
                                                                 cord.size()),2)

        cord = Coordinate(145, 40, 110, 60)
        if Register.I2C_POWERMOD_O2_OVERDRIVE:
            pygame.draw.rect(self.lcd, Colors.RED, pygame.Rect(cord.locate(0,0),cord.size()))
        else:
            pygame.draw.rect(self.lcd, Colors.BLUE, pygame.Rect(cord.locate(0,0),cord.size()))
        text_surface = Fonts.font_40.render("O2", True, Colors.WHITE)
        self.lcd.blit(text_surface, cord.locate(5, 5))

        if Register.I2C_POWERMOD_O2_FLAG:
            self.lcd.blit(self.switch_on, cord.locate(55,20))
        else:
            self.lcd.blit(self.switch_off, cord.locate(55,20))
        if self.selectedIndex == 1:
            pygame.draw.rect(self.lcd, Colors.GRAY, pygame.Rect(cord.locate(0,0),
                                                                 cord.size()),2)

        cord = Coordinate(270, 40, 110, 60)
        if Register.I2C_POWERMOD_HEATER_OVERDRIVE:
            pygame.draw.rect(self.lcd, Colors.RED, pygame.Rect(cord.locate(0,0),cord.size()))
        else:
            pygame.draw.rect(self.lcd, Colors.BLUE, pygame.Rect(cord.locate(0,0),cord.size()))
        self.lcd.blit(self.heater, cord.locate(3, 3))

        if Register.I2C_POWERMOD_HEATER_FLAG:
            self.lcd.blit(self.switch_on, cord.locate(55,20))
        else:
            self.lcd.blit(self.switch_off, cord.locate(55,20))

        if self.selectedIndex == 2:
            pygame.draw.rect(self.lcd, Colors.GRAY, pygame.Rect(cord.locate(0,0),
                                                                 cord.size()),2)

        ### 2 linia

        cord = Coordinate(20, 110, 110, 60)
        if Register.I2C_POWERMOD_FILTER2_OVERDRIVE:
            pygame.draw.rect(self.lcd, Colors.RED, pygame.Rect(cord.locate(0,0),cord.size()))
        else:
            pygame.draw.rect(self.lcd, Colors.BLUE, pygame.Rect(cord.locate(0,0),cord.size()))
        self.lcd.blit(self.filter2, cord.locate(3, 3))
        if Register.I2C_POWERMOD_FILTER2_FLAG:
            self.lcd.blit(self.switch_on, cord.locate(55,20))
        else:
            self.lcd.blit(self.switch_off, cord.locate(55,20))
        text_surface = Fonts.font_30.render("2", True, Colors.WHITE)
        self.lcd.blit(text_surface, cord.locate(35, 20))
        if self.selectedIndex == 3:
            pygame.draw.rect(self.lcd, Colors.GRAY, pygame.Rect(cord.locate(0,0),
                                                                 cord.size()),2)

        cord = Coordinate(145, 110, 110, 60)
        if Register.I2C_POWERMOD_CO2_OVERDRIVE:
            pygame.draw.rect(self.lcd, Colors.RED, pygame.Rect(cord.locate(0,0),cord.size()))
        else:
            pygame.draw.rect(self.lcd, Colors.BLUE, pygame.Rect(cord.locate(0,0),cord.size()))
        text_surface = Fonts.font_40.render("CO2", True, Colors.WHITE)
        self.lcd.blit(text_surface, cord.locate(5, 5))
        if Register.I2C_POWERMOD_CO2_FLAG:
            self.lcd.blit(self.switch_on, cord.locate(55,20))
        else:
            self.lcd.blit(self.switch_off, cord.locate(55,20))
        if self.selectedIndex == 4:
            pygame.draw.rect(self.lcd, Colors.GRAY, pygame.Rect(cord.locate(0,0),
                                                                 cord.size()),2)

        cord = Coordinate(270, 110, 110, 60)
        if Register.I2C_POWERMOD_HEATER_LED_OVERDRIVE:
            pygame.draw.rect(self.lcd, Colors.RED, pygame.Rect(cord.locate(0,0),cord.size()))
        else:
            pygame.draw.rect(self.lcd, Colors.BLUE, pygame.Rect(cord.locate(0,0),cord.size()))
        self.lcd.blit(self.heater, cord.locate(3, 3))

        if Register.I2C_POWERMOD_HEATER_LED_FLAG:
            self.lcd.blit(self.switch_on, cord.locate(55,20))
        else:
            self.lcd.blit(self.switch_off, cord.locate(55,20))
        text_surface = Fonts.font_20.render("LED", True, Colors.WHITE)
        self.lcd.blit(text_surface, cord.locate(8, 35))
        if self.selectedIndex == 5:
            pygame.draw.rect(self.lcd, Colors.GRAY, pygame.Rect(cord.locate(0,0),
                                                                 cord.size()),2)

        # AUTO
        cord = Coordinate(100, 190, 200, 40)
        pygame.draw.rect(self.lcd, Colors.BLUE, pygame.Rect(cord.locate(0,0),cord.size()))
        text_surface = Fonts.font_40.render("AUTO", True, Colors.WHITE)
        self.lcd.blit(text_surface, cord.locate(60, 5))
        if self.selectedIndex == 6:
            pygame.draw.rect(self.lcd, Colors.GRAY, pygame.Rect(cord.locate(0,0),
                                                                 cord.size()),2)


