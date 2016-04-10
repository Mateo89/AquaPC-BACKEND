from RPLCD import cleared

from Display import DisplayRegister
from register import Register
from Helpers import LircEvents

class MenuWindow:

    selecedIndex = 0
    tiles = []
    redraw = True

    def __init__(self):
        pass

    def __del__(self):
        self.tiles = None

    def event(self):
        if not Register.LIRC_EVENTS:
            return

        lirc_event = LircEvents.get_event()
        if lirc_event == LircEvents.KEY_BACK:
            DisplayRegister.set_mainWindow()

        if lirc_event == LircEvents.KEY_RIGHT:
            self.selecedIndex = (self.selecedIndex + 1) % 3
            self.redraw = True

        if lirc_event == LircEvents.KEY_LEFT:
            self.selecedIndex = (self.selecedIndex - 1) % 3
            self.redraw = True

        if lirc_event == LircEvents.KEY_OK:
            if self.selecedIndex == 0:
                DisplayRegister.set_lightWindow()
            if self.selecedIndex == 1:
                DisplayRegister.set_bottleWindow()
            if self.selecedIndex == 2:
                DisplayRegister.set_mainWindow()

    def redraw_text(self):
        self.redraw = True

    def draw(self):

        if not self.redraw:
            return

        self.redraw = False

        if self.selecedIndex == 0:
            with cleared(Register.LCD):
                Register.LCD.write_string("      MENU\n\r  PRZLACZNIKI")
        if self.selecedIndex == 1:
            with cleared(Register.LCD):
                Register.LCD.write_string("      MENU\n\r  USTAWIENIA")
        if self.selecedIndex == 2:
            with cleared(Register.LCD):
                Register.LCD.write_string("      MENU\n\r  WYJSCIE")




