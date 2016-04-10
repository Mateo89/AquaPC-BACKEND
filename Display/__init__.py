from RPLCD import CharLCD

from Display import DisplayRegister
import threading
from register import Register
from Helpers import LircEvents
import time


class DisplayThread(threading.Thread):

    current_screen = None
    lcd = None

    def __init__(self):
        threading.Thread.__init__(self)
        Register.LCD = CharLCD()
        self.lcd = Register.LCD
        DisplayRegister.set_mainWindow()

    def run(self):
        while not Register.EXIT_FLAG:
            #jakas logika odnosnie co ma byc wyswietlane

            if Register.LIRC_EVENTS and Register.LIRC_EVENTS == LircEvents.KEY_MENU:
                Register.LIRC_EVENTS = None
                DisplayRegister.set_menuWindow()

            Register.CURRENT_SCREEN.event()
            Register.CURRENT_SCREEN.draw()
            time.sleep(0.3)
