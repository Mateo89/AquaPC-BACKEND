from Logic import Light2Logic
from RPLCD import cleared

from Display import DisplayRegister
from Helpers import LircEvents
from register import Register


class Light2SettingWindow:

    lcd = None
    selected_index = 0
    redraw = True

    def __init__(self):
        self.lcd = Register.LCD

    def event(self):
        if not Register.LIRC_EVENTS:
            return

        lirc_event = LircEvents.get_event()
        if lirc_event == LircEvents.KEY_BACK:
            DisplayRegister.set_menuWindow()

        if lirc_event == LircEvents.KEY_RIGHT:
            self.selected_index = (self.selected_index + 1) % 6
            self.redraw = True

        if lirc_event == LircEvents.KEY_LEFT:
            self.selected_index = (self.selected_index - 1) % 6
            self.redraw = True

        if lirc_event == LircEvents.KEY_UP:
            if self.selected_index == 0:
                Light2Logic.block()
                Light2Logic.up_percent(5, 0)
                self.redraw = True
            if self.selected_index == 1:
                Light2Logic.block()
                Light2Logic.up_percent(5, 1)
                self.redraw = True
            if self.selected_index == 2:
                Light2Logic.block()
                Light2Logic.up_percent(5, 2)
                self.redraw = True
            if self.selected_index == 3:
                Light2Logic.block()
                Light2Logic.up_percent(5, 3)
                self.redraw = True

        if lirc_event == LircEvents.KEY_DOWN:
            if self.selected_index == 0:
                Light2Logic.block()
                Light2Logic.down_percent(5, 0)
                self.redraw = True
            if self.selected_index == 1:
                Light2Logic.block()
                Light2Logic.down_percent(5, 1)
                self.redraw = True
            if self.selected_index == 2:
                Light2Logic.block()
                Light2Logic.down_percent(5, 2)
                self.redraw = True
            if self.selected_index == 3:
                Light2Logic.block()
                Light2Logic.down_percent(5, 3)
                self.redraw = True

        if lirc_event == LircEvents.KEY_OK:
            if self.selected_index == 4:
                Light2Logic.unblock()

            if self.selected_index == 5:
                DisplayRegister.set_menuWindow()

    def redraw_text(self):
        self.redraw = True

    def get_override(self):
        if Register.POWERMOD_DATA[str(Register.I2C_POWERMOD_LIGHT2)]['override']:
            return "!"
        else:
            return ""

    def draw(self):

        if not self.redraw:
            return

        self.redraw = False

        if self.selected_index == 0:
            with cleared(Register.LCD):
                Register.LCD.write_string("    LAMPA 2\n\rPROCENT CH1 " +
                                          str(Register.LIGHT2_PERCENT[0]) + "%" +
                                          self.get_override())
        if self.selected_index == 1:
            with cleared(Register.LCD):
                Register.LCD.write_string("    LAMPA 2\n\rPROCENT CH2 " +
                                          str(Register.LIGHT2_PERCENT[1]) + "%" +
                                          self.get_override())
        if self.selected_index == 2:
            with cleared(Register.LCD):
                Register.LCD.write_string("    LAMPA 2\n\rPROCENT CH3 " +
                                          str(Register.LIGHT2_PERCENT[2]) + "%" +
                                          self.get_override())
        if self.selected_index == 3:
            with cleared(Register.LCD):
                Register.LCD.write_string("    LAMPA 2\n\rPROCENT CH4 " +
                                          str(Register.LIGHT2_PERCENT[3]) + "%" +
                                          self.get_override())
        if self.selected_index == 4:
            with cleared(Register.LCD):
                Register.LCD.write_string("    LAMPA 2\n\r  RESET BLOKAD ")
        if self.selected_index == 5:
            with cleared(Register.LCD):
                Register.LCD.write_string("    LAMPA 2\n\r    WYJSCIE")


