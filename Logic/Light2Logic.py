import threading

from register import Register
from Helpers import PowerModHelper, TimesHelper, Light2ModHelper
import time


def light2_logic():

    if Register.POWERMOD_DATA[str(Register.I2C_POWERMOD_LIGHT2)]['override']:
        return

    if Register.CHANGE_WATER_MODE:
        if Register.LAMPS_SETTINGS['1']['water_change_on']:
            set_percent(Register.LAMPS_SETTINGS['2']['water_change_percent'])
    else:
        percent = TimesHelper.process_times_states(Register.LAMPS_SETTINGS['2']['times'])
        set_percent(percent)


def set_percent(percent):
    Register.LIGHT1_PERCENT = percent


def toggle_light():
    PowerModHelper.toggle_switch(Register.I2C_POWERMOD_LIGHT2)


def turn_on():
    PowerModHelper.set_switch(Register.I2C_POWERMOD_LIGHT2)


def turn_off():
    PowerModHelper.unset_switch(Register.I2C_POWERMOD_LIGHT2)


# kontrolowanie poziomu swiatla
class Light2Thread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def process_percent(self, percent):
        if percent < Register.LIGHT2_PERCENT:
            percent += 1
            Light2ModHelper.update_data(percent)
        if percent > Register.LIGHT2_PERCENT:
            percent -= 1
            Light2ModHelper.update_data(percent)

        if percent == 0:
            turn_off()
        else:
            turn_on()

    def process_heater(self):
        pass

    def run(self):

        percent = 0

        while not Register.EXIT_FLAG:

            self.process_percent(percent)

            time.sleep(1)

