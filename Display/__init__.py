from Display import DisplayRegister
import pygame
import os
from MainWindow import MainWindow
from Helpers.Fonts import Fonts
import threading
from register import Register
from Helpers import LircEvents
import time


class Display(threading.Thread):

    current_screen = None
    lcd = None

    def __init__(self):
        threading.Thread.__init__(self)

        os.putenv('SDL_FBDEV', '/dev/fb0')
        pygame.init()
        Fonts.initFonts()

        pygame.mouse.set_visible(False)
        Register.LCD = pygame.display.set_mode((400, 240))
        self.lcd = Register.LCD
        pygame.display.update()

        DisplayRegister.set_mainWindow()

    def run(self):
        while not Register.EXIT_FLAG:
            #jakas logika odnosnie co ma byc wyswietlane

            if Register.LIRC_EVENTS and Register.LIRC_EVENTS == LircEvents.KEY_MENU:
                Register.LIRC_EVENTS = None
                DisplayRegister.set_menuWindow()

            Register.CURRENT_SCREEN.event()
            Register.CURRENT_SCREEN.draw()
            pygame.display.update()
            time.sleep(0.3)