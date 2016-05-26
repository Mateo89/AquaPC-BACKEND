from RPLCD import cleared

from Display import DisplayRegister
from register import Register
from Helpers import LircEvents
from Logic import WaterChangeLogic

class MenuWindow:

    selected_index = 0
    redraw = True

    def __init__(self):
        pass

    def event(self):
        if not Register.LIRC_EVENTS:
            return

        lirc_event = LircEvents.get_event()
        if lirc_event == LircEvents.KEY_BACK:
            DisplayRegister.set_mainWindow()

        if lirc_event == LircEvents.KEY_RIGHT:
            self.selected_index = (self.selected_index + 1) % 5
            self.redraw = True

        if lirc_event == LircEvents.KEY_LEFT:
            self.selected_index = (self.selected_index - 1) % 5
            self.redraw = True

        if lirc_event == LircEvents.KEY_OK:
            if self.selected_index == 0:
                DisplayRegister.set_switchWindow()
            if self.selected_index == 1:
                DisplayRegister.set_light1_settings_window()
            if self.selected_index == 2:
                DisplayRegister.set_light2_settings_window()
            if self.selected_index == 3:
                WaterChangeLogic.toggle_water_change()
                self.redraw_text()
            if self.selected_index == 4:
                DisplayRegister.set_mainWindow()

    def redraw_text(self):
        self.redraw = True

    def draw(self):

        if not self.redraw:
            return

        self.redraw = False

        if self.selected_index == 0:
            with cleared(Register.LCD):
                Register.LCD.write_string("      MENU\n\r  PRZELACZNIKI")
        if self.selected_index == 1:
            with cleared(Register.LCD):
                Register.LCD.write_string("      MENU\n\r    LAMPA 1")
        if self.selected_index == 2:
            with cleared(Register.LCD):
                Register.LCD.write_string("      MENU\n\r    LAMPA 2")
        if self.selected_index == 3:
            with cleared(Register.LCD):
                Register.LCD.write_string("      MENU\n\rPODM. WODY  " + WaterChangeLogic.get_water_change_state())
        if self.selected_index == 4:
            with cleared(Register.LCD):
                Register.LCD.write_string("      MENU\n\r    WYJSCIE")




