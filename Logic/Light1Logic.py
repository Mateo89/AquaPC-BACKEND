import threading

import Helpers
from register import Register
from Helpers import PowerModHelper, TimesHelper, Light1ModHelper
import time


def light1_logic():

    if Register.POWERMOD_DATA[str(Register.I2C_POWERMOD_LIGHT1)]['override']:
        return

    if not Register.LAMPS_SETTINGS['1']['on']:
        set_percent(0)
        return

    if Register.CHANGE_WATER_MODE:
        if Register.LAMPS_SETTINGS['1']['water_change_on']:
            set_percent(Register.LAMPS_SETTINGS['1']['water_change_percent'])
    else:
        percent = TimesHelper.process_times_states(Register.LAMPS_SETTINGS['1']['times'])
        set_percent(int(percent))


def set_percent(percent):
    Register.LIGHT1_PERCENT = percent


def toggle_light():
    PowerModHelper.toggle_switch(Register.I2C_POWERMOD_LIGHT1)


def turn_on():
    PowerModHelper.set_switch(Register.I2C_POWERMOD_LIGHT1)


def turn_off():
    PowerModHelper.unset_switch(Register.I2C_POWERMOD_LIGHT1)


def process_percent(percent):

    lamp_percent = Register.LIGHT1_PERCENT

    if percent < lamp_percent:
        percent += 1
        Light1ModHelper.update_data(percent)

    if percent > lamp_percent:
        percent -= 1
        Light1ModHelper.update_data(percent)

    if percent == 0:
        turn_off()
    else:
        turn_on()

    return percent


class Light1Thread(threading.Thread):

    percent = 0

    def __init__(self):
        threading.Thread.__init__(self)
        self.percent = 0

    def process_heater(self):
        pass

    def run(self):
        while not Register.EXIT_FLAG:
            self.percent = process_percent(self.percent)
            time.sleep(1)

