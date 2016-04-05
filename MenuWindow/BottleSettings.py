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


class BottleSettingWindow:

    lcd = None

    barTile =None
    selectedIndex = 0
    tiles = []
    bottles = None
    bottles_names = ['bottle1', 'bottle2', 'bottle3', 'bottle4']

    def __init__(self):
        self.lcd = Register.LCD
        self.barTile = BarTile(Coordinate(0, 0, 400, 25), "Dozownik", "settings25.png")
        self.upIcon = pygame.image.load(os.path.join('icons', "up30.png"))
        self.downIcon = pygame.image.load(os.path.join('icons', "down30.png"))
        self.switch_on_icon = pygame.image.load(os.path.join("icons", "switchon50.png"))
        self.switch_off_icon = pygame.image.load(os.path.join("icons", "switchoff50.png"))
        self.reset()

    def reset(self):
        self.bottles = dict(bottle1={
            'ON': Register.BOTTLE_MOD['bottle1']['ON'],
            'HOUR': Register.BOTTLE_MOD['bottle1']['HOUR'],
            'MIN': Register.BOTTLE_MOD['bottle1']['MIN'],
            'DOSE': Register.BOTTLE_MOD['bottle1']['DOSE'],
            'SEC_PER_ML': Register.BOTTLE_MOD['bottle1']['SEC_PER_ML']
        }, bottle2={
            'ON': Register.BOTTLE_MOD['bottle2']['ON'],
            'HOUR': Register.BOTTLE_MOD['bottle2']['HOUR'],
            'MIN': Register.BOTTLE_MOD['bottle2']['MIN'],
            'DOSE': Register.BOTTLE_MOD['bottle2']['DOSE'],
            'SEC_PER_ML': Register.BOTTLE_MOD['bottle2']['SEC_PER_ML']
        }, bottle3={
            'ON': Register.BOTTLE_MOD['bottle3']['ON'],
            'HOUR': Register.BOTTLE_MOD['bottle3']['HOUR'],
            'MIN': Register.BOTTLE_MOD['bottle3']['MIN'],
            'DOSE': Register.BOTTLE_MOD['bottle3']['DOSE'],
            'SEC_PER_ML': Register.BOTTLE_MOD['bottle3']['SEC_PER_ML']
        }, bottle4={
            'ON': Register.BOTTLE_MOD['bottle4']['ON'],
            'HOUR': Register.BOTTLE_MOD['bottle4']['HOUR'],
            'MIN': Register.BOTTLE_MOD['bottle4']['MIN'],
            'DOSE': Register.BOTTLE_MOD['bottle4']['DOSE'],
            'SEC_PER_ML': Register.BOTTLE_MOD['bottle4']['SEC_PER_ML']
        })

    def save(self):
        for bottle in self.bottles_names:
            Register.BOTTLE_MOD[bottle]['ON'] = self.bottles[bottle]['ON']
            Register.BOTTLE_MOD[bottle]['HOUR'] = self.bottles[bottle]['HOUR']
            Register.BOTTLE_MOD[bottle]['MIN'] = self.bottles[bottle]['MIN']
            Register.BOTTLE_MOD[bottle]['DOSE'] = self.bottles[bottle]['DOSE']
            Register.BOTTLE_MOD[bottle]['SEC_PER_ML'] = self.bottles[bottle]['SEC_PER_ML']
        settings.save_settings()

    def event(self):
        if not Register.LIRC_EVENTS:
            return

        lirc_event = LircEvents.get_event()
        if lirc_event == LircEvents.KEY_BACK:
            DisplayRegister.set_settingsWindow()

        if lirc_event == LircEvents.KEY_RIGHT:
            self.selectedIndex = (self.selectedIndex + 1) % 38

        if lirc_event == LircEvents.KEY_LEFT:
            self.selectedIndex = (self.selectedIndex - 1) % 38

        if lirc_event == LircEvents.KEY_UP:
            self.selectedIndex = (self.selectedIndex - 9) % 38

        if lirc_event == LircEvents.KEY_DOWN:
            self.selectedIndex = (self.selectedIndex + 9) % 38

        if lirc_event == LircEvents.KEY_OK:

            if self.selectedIndex == 36:  #reset
                self.reset()
                return
            if self.selectedIndex == 37:  #zapisz
                self.save()
                self.reset()
                return

            i = 0
            if self.selectedIndex in range(0, 9):
                i = 0
            elif self.selectedIndex in range(9, 18):
                i = 1
            elif self.selectedIndex in range(18, 27):
                i = 2
            else:
                i = 3

            method = self.selectedIndex - (i * 9)

            if method == 0:
                self.bottles[self.bottles_names[i]]['ON'] = not self.bottles[self.bottles_names[i]]['ON']
            elif method == 1:
                self.bottles[self.bottles_names[i]]['DOSE'] += 1
            elif method == 2:
                self.bottles[self.bottles_names[i]]['DOSE'] -= 1
                if self.bottles[self.bottles_names[i]]['DOSE'] < 0:
                    self.bottles[self.bottles_names[i]]['DOSE'] = 0
            elif method == 3:
                self.bottles[self.bottles_names[i]]['SEC_PER_ML'] += 0.1
            elif method == 4:
                self.bottles[self.bottles_names[i]]['SEC_PER_ML'] -= 0.1
                if self.bottles[self.bottles_names[i]]['SEC_PER_ML'] < 0:
                    self.bottles[self.bottles_names[i]]['SEC_PER_ML'] = 0
            elif method == 5:
                self.bottles[self.bottles_names[i]]['HOUR'] = (self.bottles[self.bottles_names[i]]['HOUR'] + 1) % 24
            elif method == 6:
                self.bottles[self.bottles_names[i]]['HOUR'] = (self.bottles[self.bottles_names[i]]['HOUR'] - 1) % 24
            elif method == 7:
                self.bottles[self.bottles_names[i]]['MIN'] = (self.bottles[self.bottles_names[i]]['MIN'] + 1) % 60
            elif method == 8:
                self.bottles[self.bottles_names[i]]['MIN'] = (self.bottles[self.bottles_names[i]]['MIN'] - 1) % 60

    def draw(self):

        self.lcd.fill(Colors.BLACK)
        self.barTile.draw_tile()

        i = 0

        for x in range(0, self.bottles_names.__len__()):
            bottle = self.bottles_names[x]

            main_cord = Coordinate(0, 35 + (35 * x), 400, 30)
            cord = Coordinate(*main_cord.get_slice(50))
            if self.bottles[bottle]['ON'] != Register.BOTTLE_MOD[bottle]['ON']:
                pygame.draw.rect(self.lcd, Colors.RED, pygame.Rect(cord.size_full()))
            if self.bottles[bottle]['ON']:
                self.lcd.blit(self.switch_on_icon, cord.get_center(self.switch_on_icon.get_width(), self.switch_on_icon.get_height()))
            else:
                self.lcd.blit(self.switch_off_icon, cord.get_center(self.switch_off_icon.get_width(), self.switch_off_icon.get_height()))
            if self.selectedIndex == i:
                pygame.draw.rect(self.lcd, Colors.GRAY, cord.size_full(), 2)
            i += 1

            cord = Coordinate(*main_cord.get_slice(55))
            text_surface = Fonts.font_40.render(Register.BOTTLE_MOD[bottle]['NAME'],
                                                True, Colors.WHITE)
            self.lcd.blit(text_surface, cord.get_center(text_surface.get_width(), text_surface.get_height()))


            cord = Coordinate(*main_cord.get_slice(25))
            text_surface = Fonts.font_30.render("D", True, Colors.WHITE)
            self.lcd.blit(text_surface, cord.get_center(text_surface.get_width(), text_surface.get_height()))

            cord = Coordinate(*main_cord.get_slice(25))
            if self.bottles[bottle]['DOSE'] != Register.BOTTLE_MOD[bottle]['DOSE']:
                pygame.draw.rect(self.lcd, Colors.RED, pygame.Rect(cord.locate(0, 0), cord.size()))
            text_surface = Fonts.font_30.render(str(self.bottles[bottle]['DOSE']), True, Colors.WHITE)
            self.lcd.blit(text_surface, cord.get_center(text_surface.get_width(), text_surface.get_height()))


            cord = Coordinate(*main_cord.get_slice(20))
            self.lcd.blit(self.upIcon, cord.get_center(self.upIcon.get_width(), self.upIcon.get_height()+20))
            if self.selectedIndex == i:
                pygame.draw.rect(self.lcd, Colors.GRAY, pygame.Rect(cord.get_center(20, 18+26), (20, 18)), 2)
            i += 1
            self.lcd.blit(self.downIcon, cord.get_center(self.upIcon.get_width(), self.upIcon.get_height()-20))
            if self.selectedIndex == i:
                pygame.draw.rect(self.lcd, Colors.GRAY, pygame.Rect(cord.get_center(20, 18-26), (20, 18)), 2)
            i += 1

            cord = Coordinate(*main_cord.get_slice(35))
            text_surface = Fonts.font_20.render("m/s", True, Colors.WHITE)
            self.lcd.blit(text_surface, cord.get_center(text_surface.get_width(), text_surface.get_height()))

            cord = Coordinate(*main_cord.get_slice(30))
            if self.bottles[bottle]['SEC_PER_ML'] != Register.BOTTLE_MOD[bottle]['SEC_PER_ML']:
                pygame.draw.rect(self.lcd, Colors.RED, pygame.Rect(cord.locate(0, 0), cord.size()))
            text_surface = Fonts.font_30.render(str(self.bottles[bottle]['SEC_PER_ML']), True, Colors.WHITE)
            self.lcd.blit(text_surface, cord.get_center(text_surface.get_width(), text_surface.get_height()))

            cord = Coordinate(*main_cord.get_slice(20))
            self.lcd.blit(self.upIcon, cord.get_center(self.upIcon.get_width(), self.upIcon.get_height()+20))
            if self.selectedIndex == i:
                pygame.draw.rect(self.lcd, Colors.GRAY, pygame.Rect(cord.get_center(20, 18+26), (20, 18)), 2)
            i += 1
            self.lcd.blit(self.downIcon, cord.get_center(self.upIcon.get_width(), self.upIcon.get_height()-20))
            if self.selectedIndex == i:
                pygame.draw.rect(self.lcd, Colors.GRAY, pygame.Rect(cord.get_center(20, 18-26), (20, 18)), 2)
            i += 1


            cord = Coordinate(*main_cord.get_slice(25))
            text_surface = Fonts.font_30.render("H", True, Colors.WHITE)
            self.lcd.blit(text_surface, cord.get_center(text_surface.get_width(), text_surface.get_height()))

            cord = Coordinate(*main_cord.get_slice(25))
            if self.bottles[bottle]['HOUR'] != Register.BOTTLE_MOD[bottle]['HOUR']:
                pygame.draw.rect(self.lcd, Colors.RED, pygame.Rect(cord.locate(0, 0), cord.size()))
            text_surface = Fonts.font_30.render(str(self.bottles[bottle]['HOUR']), True, Colors.WHITE)
            self.lcd.blit(text_surface, cord.get_center(text_surface.get_width(), text_surface.get_height()))

            cord = Coordinate(*main_cord.get_slice(20))
            self.lcd.blit(self.upIcon, cord.get_center(self.upIcon.get_width(), self.upIcon.get_height()+20))
            if self.selectedIndex == i:
                pygame.draw.rect(self.lcd, Colors.GRAY, pygame.Rect(cord.get_center(20, 18+26), (20, 18)), 2)
            i += 1
            self.lcd.blit(self.downIcon, cord.get_center(self.upIcon.get_width(), self.upIcon.get_height()-20))
            if self.selectedIndex == i:
                pygame.draw.rect(self.lcd, Colors.GRAY, pygame.Rect(cord.get_center(20, 18-26), (20, 18)), 2)
            i += 1


            cord = Coordinate(*main_cord.get_slice(25))
            text_surface = Fonts.font_30.render("M", True, Colors.WHITE)
            self.lcd.blit(text_surface, cord.get_center(text_surface.get_width(), text_surface.get_height()))

            cord = Coordinate(*main_cord.get_slice(25))
            if self.bottles[bottle]['MIN'] != Register.BOTTLE_MOD[bottle]['MIN']:
                pygame.draw.rect(self.lcd, Colors.RED, pygame.Rect(cord.locate(0, 0), cord.size()))
            text_surface = Fonts.font_30.render(str(self.bottles[bottle]['MIN']), True, Colors.WHITE)
            self.lcd.blit(text_surface, cord.get_center(text_surface.get_width(), text_surface.get_height()))

            cord = Coordinate(*main_cord.get_slice(20))
            self.lcd.blit(self.upIcon, cord.get_center(self.upIcon.get_width(), self.upIcon.get_height()+20))
            if self.selectedIndex == i:
                pygame.draw.rect(self.lcd, Colors.GRAY, pygame.Rect(cord.get_center(20, 18+26), (20, 18)), 2)
            i += 1
            self.lcd.blit(self.downIcon, cord.get_center(self.upIcon.get_width(), self.upIcon.get_height()-20))
            if self.selectedIndex == i:
                pygame.draw.rect(self.lcd, Colors.GRAY, pygame.Rect(cord.get_center(20, 18-26), (20, 18)), 2)
            i += 1

        main_cord = Coordinate(0, 190, 400, 40)
        cord = Coordinate(*main_cord.get_slice(200))
        cord = Coordinate(*cord.get_center_surface(150, 40))
        pygame.draw.rect(self.lcd, Colors.BLUE, pygame.Rect(cord.size_full()))
        text_surface = Fonts.font_30.render("RESET", True, Colors.WHITE)
        self.lcd.blit(text_surface, cord.get_center(text_surface.get_width(), text_surface.get_height()))
        if self.selectedIndex == 36:
            pygame.draw.rect(self.lcd, Colors.GRAY, cord.size_full(), 2)

        cord = Coordinate(*main_cord.get_slice(200))
        cord = Coordinate(*cord.get_center_surface(150, 40))
        pygame.draw.rect(self.lcd, Colors.BLUE, pygame.Rect(cord.size_full()))
        text_surface = Fonts.font_30.render("ZAPISZ", True, Colors.WHITE)
        self.lcd.blit(text_surface, cord.get_center(text_surface.get_width(), text_surface.get_height()))
        if self.selectedIndex == 37:
            pygame.draw.rect(self.lcd, Colors.GRAY, cord.size_full(), 2)