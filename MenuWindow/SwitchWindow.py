from RPLCD import cleared

from Display import DisplayRegister
from Helpers import LircEvents, PowerModHelper
from Logic import Co2Logic
from Logic import Filter1Logic
from Logic import Filter2Logic
from Logic import O2Logic
from Logic import WaterTempLogic
from register import Register


class SwitchWindow:

    lcd = None

    selected_index = 0
    redraw = True

    def __init__(self):
        self.lcd = Register.LCD

    def redraw_text(self):
        self.redraw = True

    def event(self):
        if not Register.LIRC_EVENTS:
            return

        lirc_event = LircEvents.get_event()
        if lirc_event == LircEvents.KEY_BACK:
            DisplayRegister.set_menuWindow()

        if lirc_event == LircEvents.KEY_RIGHT:
            self.selected_index = (self.selected_index + 1) % 8
            self.redraw = True

        if lirc_event == LircEvents.KEY_LEFT:
            self.selected_index = (self.selected_index - 1) % 8
            self.redraw = True

        if lirc_event == LircEvents.KEY_OK:
            if self.selected_index == 0:
                Filter1Logic.block_filter()
                Filter1Logic.toggle_filter()
                self.redraw = True

            if self.selected_index == 1:
                Filter2Logic.block_filter()
                Filter2Logic.toggle_filter()
                self.redraw = True

            if self.selected_index == 2:
                O2Logic.block_o2()
                O2Logic.toggle_o2()
                self.redraw = True

            if self.selected_index == 3:
                Co2Logic.block_co2()
                Co2Logic.toggle_co2()
                self.redraw = True

            if self.selected_index == 4:
                WaterTempLogic.block_heater()
                WaterTempLogic.toggle_heater()
                self.redraw = True

            if self.selected_index == 5:
                WaterTempLogic.block_heater_led()
                WaterTempLogic.toggle_heater_led()
                self.redraw = True

            if self.selected_index == 6:
                for switch in Register.POWERMOD_DATA.viewkeys():
                    PowerModHelper.remove_override_switch(switch)

            if self.selected_index == 7:
                DisplayRegister.set_menuWindow()

    def get_override(self, switch):
        if Register.POWERMOD_DATA[str(switch)]['override']:
            return "!"
        else:
            return ""

    def draw(self):
        if not self.redraw:
            return

        self.redraw = False

        if self.selected_index == 0:
            with cleared(Register.LCD):
                Register.LCD.write_string("  PRZELACZNIKI\n\rFILTR 1     " +
                                          Register.get_switch_state(Register.I2C_POWERMOD_FILTER1) +
                                          self.get_override(Register.I2C_POWERMOD_FILTER1))
        if self.selected_index == 1:
            with cleared(Register.LCD):
                Register.LCD.write_string("  PRZELACZNIKI\n\rFILTR 2     " +
                                          Register.get_switch_state(Register.I2C_POWERMOD_FILTER2) +
                                          self.get_override(Register.I2C_POWERMOD_FILTER2))
        if self.selected_index == 2:
            with cleared(Register.LCD):
                Register.LCD.write_string("  PRZELACZNIKI\n\rO2          " +
                                          Register.get_switch_state(Register.I2C_POWERMOD_O2) +
                                          self.get_override(Register.I2C_POWERMOD_O2))
        if self.selected_index == 3:
            with cleared(Register.LCD):
                Register.LCD.write_string("  PRZELACZNIKI\n\rCO2         " +
                                          Register.get_switch_state(Register.I2C_POWERMOD_CO2) +
                                          self.get_override(Register.I2C_POWERMOD_CO2))
        if self.selected_index == 4:
            with cleared(Register.LCD):
                Register.LCD.write_string("  PRZELACZNIKI\n\rGRZALKA     " +
                                          Register.get_switch_state(Register.I2C_POWERMOD_HEATER) +
                                          self.get_override(Register.I2C_POWERMOD_HEATER))
        if self.selected_index == 5:
            with cleared(Register.LCD):
                Register.LCD.write_string("  PRZELACZNIKI\n\rGRZALKA LED " +
                                          Register.get_switch_state(Register.I2C_POWERMOD_HEATER_LED) +
                                          self.get_override(Register.I2C_POWERMOD_HEATER_LED))
        if self.selected_index == 6:
            with cleared(Register.LCD):
                Register.LCD.write_string("  PRZELACZNIKI\n\r  RESET BLOKAD ")
        if self.selected_index == 7:
            with cleared(Register.LCD):
                Register.LCD.write_string("  PRZELACZNIKI\n\r    WYJSCIE")




