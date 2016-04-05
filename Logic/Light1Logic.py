import threading

from register import Register
from Helpers import PowerModHelper, TimesHelper, Light1ModHelper
from datetime import time


def light1_logic():

    if Register.POWERMOD_DATA[str(Register.I2C_POWERMOD_LIGHT1)]['override']:
        return

    if Register.CHANGE_WATER_MODE:
        if Register.LAMPS_SETTINGS['1']['water_change_on']:
            set_percent(Register.LAMPS_SETTINGS['1']['water_change_percent'])
    else:
        percent = TimesHelper.process_times_states(Register.LAMPS_SETTINGS['1']['times'])
        set_percent(percent)


def set_percent(percent):
    Register.LIGHT1_PERCENT = percent


def toggle_light():
    PowerModHelper.toggle_switch(Register.I2C_POWERMOD_LIGHT1)


def turn_on():
    PowerModHelper.set_switch(Register.I2C_POWERMOD_LIGHT1)


def turn_off():
    PowerModHelper.unset_switch(Register.I2C_POWERMOD_LIGHT1)


# kontrolowanie poziomu swiatla
class Light1Thread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):

        percent = 0

        while not Register.EXIT_FLAG:

            if percent < Register.LIGHT1_PERCENT:
                percent += 1
                Light1ModHelper.update_data(percent)
            if percent > Register.LIGHT1_PERCENT:
                percent -= 1
                Light1ModHelper.update_data(percent)

            if percent == 0:
                turn_off()
            else:
                turn_on()

            time.sleep(1)

