import os
import pygame
from Display import DisplayRegister
from Display.BarTile import BarTile
from Helpers import Colors
from Helpers.Coordinate import Coordinate
from Helpers.Fonts import Fonts
from register import Register
from Helpers import LircEvents
from Helpers import PowerModHelper
from Logic import Light1Logic
from Logic import Light2Logic



class LightWindow():

    lcd = None

    barTile =None
    selecedIndex = 0
    onIcon = None
    offIcon = None

    def __init__(self):
        self.lcd = Register.LCD
        self.barTile = BarTile(Coordinate(0, 0, 400, 25),"Lampa","light25.png")
        self.onIcon = pygame.image.load(os.path.join('icons', "switchon75.png"))
        self.offIcon = pygame.image.load(os.path.join('icons', "switchoff75.png"))
        self.upIcon = pygame.image.load(os.path.join('icons', "up60.png"))
        self.downIcon = pygame.image.load(os.path.join('icons', "down60.png"))

    def event(self):
        if not Register.LIRC_EVENTS:
            return

        lirc_event = LircEvents.get_event()
        if lirc_event == LircEvents.KEY_BACK:
            DisplayRegister.set_menuWindow()

        if lirc_event == LircEvents.KEY_RIGHT:
            self.selecedIndex = (self.selecedIndex + 1 ) % 7
        if lirc_event == LircEvents.KEY_DOWN:
            if self.selecedIndex == 3 or self.selecedIndex == 5:
                self.selecedIndex = 6
            else:
                self.selecedIndex = (self.selecedIndex + 3 ) % 6
        if lirc_event == LircEvents.KEY_LEFT:
            self.selecedIndex = (self.selecedIndex - 1 ) % 7
        if lirc_event == LircEvents.KEY_UP:
            self.selecedIndex = (self.selecedIndex - 3 ) % 6

        if lirc_event == LircEvents.KEY_OK:
            if self.selecedIndex == 0:
                Light1Logic.block_light()
                Light1Logic.toggle_light()

            if self.selecedIndex == 1: # podniesienie procentow o 5%
                Light1Logic.block_light()
                Light1Logic.up_percent(5)

            if self.selecedIndex == 2:
                Light1Logic.block_light()
                Light1Logic.down_percent(5)

            if self.selecedIndex == 3:
                Light2Logic.block_light()
                Light2Logic.toggle_light()

            if self.selecedIndex == 6:
                Light1Logic.unblock_light()
                Light2Logic.unblock_light()

    def draw(self):

        self.lcd.fill(Colors.BLACK)
        self.barTile.draw_tile()

        #draw body
        #if Register.

        if Register.I2C_POWERMOD_LIGHT1_FLAG:
            self.lcd.blit(self.onIcon, (10, 35))
        else:
            self.lcd.blit(self.offIcon, (10, 35))

        if self.selecedIndex == 0:
            pygame.draw.rect(self.lcd, Colors.GRAY,  pygame.Rect((8,50),
                                                                 (79, 45)),2)

        text_surface = Fonts.font_50.render("LAMPA 1", True, Colors.WHITE)
        self.lcd.blit(text_surface, (90, 52))
        text_surface = Fonts.font_50.render(str(Register.LIGHT1_PERCENT)+"%", True, Colors.BLUE)
        self.lcd.blit(text_surface, (255, 52))

        self.lcd.blit(self.upIcon, (340,28))
        self.lcd.blit(self.downIcon, (340,57))

        if self.selecedIndex == 1:
            pygame.draw.rect(self.lcd, Colors.GRAY,  pygame.Rect((348,44),
                                                                 (44, 28)),2)
        if self.selecedIndex == 2:
            pygame.draw.rect(self.lcd, Colors.GRAY,  pygame.Rect((348,72),
                                                                 (44, 28)),2)

        if Register.I2C_POWERMOD_LIGHT2_FLAG:
            self.lcd.blit(self.onIcon, (10, 105))
        else:
            self.lcd.blit(self.offIcon, (10, 105))
        if self.selecedIndex == 3:
            pygame.draw.rect(self.lcd, Colors.GRAY,  pygame.Rect((8,120),
                                                                 (79, 45)),2)

        text_surface = Fonts.font_50.render("LAMPA 2", True, Colors.WHITE)
        self.lcd.blit(text_surface, (90, 122))
        text_surface = Fonts.font_50.render(str(Register.LIGHT2_PERCENT)+"%", True, Colors.WHITE)
        self.lcd.blit(text_surface, (255, 122))

        self.lcd.blit(self.upIcon, (340,96))
        self.lcd.blit(self.downIcon, (340,126))

        if self.selecedIndex == 4:
            pygame.draw.rect(self.lcd, Colors.GRAY,  pygame.Rect((348,112),
                                                                 (44, 28)),2)
        if self.selecedIndex == 5:
            pygame.draw.rect(self.lcd, Colors.GRAY,  pygame.Rect((348,141),
                                                                 (44, 28)),2)

        pygame.draw.rect(self.lcd, Colors.BLUE, pygame.Rect((100,180),(200,40)))
        text_surface = Fonts.font_40.render("AUTO", True, Colors.WHITE)
        self.lcd.blit(text_surface, (165, 185))

        if self.selecedIndex == 6:
            pygame.draw.rect(self.lcd, Colors.GRAY,  pygame.Rect((100,180),
                                                                 (200, 40)),2)









