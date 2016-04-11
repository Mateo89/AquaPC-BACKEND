import threading

from register import Register
from Helpers import PowerModHelper, TimesHelper, Light2ModHelper
import time


def light2_logic():

    if Register.POWERMOD_DATA[str(Register.I2C_POWERMOD_LIGHT2)]['override']:
        return

    if not Register.LAMPS_SETTINGS['2']['on']:
        set_percent(0)
        return

    if Register.CHANGE_WATER_MODE:
        if Register.LAMPS_SETTINGS['2']['water_change_on']:
            set_percent(Register.LAMPS_SETTINGS['2']['water_change_percent'])
    else:
        percent = TimesHelper.process_times_states(Register.LAMPS_SETTINGS['2']['times'])
        set_percent(percent)


def set_percent(percent):
    Register.LIGHT2_PERCENT = percent


def up_percent(up):
    percent = Register.LIGHT2_PERCENT + up
    if percent > 100:
        percent = 100
    Register.LIGHT2_PERCENT = percent


def down_percent(down):
    percent = Register.LIGHT2_PERCENT - down
    if percent < 0:
        percent = 0
    Register.LIGHT2_PERCENT = percent


def block():
    Register.POWERMOD_DATA[str(Register.I2C_POWERMOD_LIGHT2)]['override'] = True


def unblock():
    Register.POWERMOD_DATA[str(Register.I2C_POWERMOD_LIGHT2)]['override'] = False


def toggle_light():
    PowerModHelper.toggle_switch(Register.I2C_POWERMOD_LIGHT2)


def turn_on():
    PowerModHelper.set_switch(Register.I2C_POWERMOD_LIGHT2)


def turn_off():
    PowerModHelper.unset_switch(Register.I2C_POWERMOD_LIGHT2)


# kontrolowanie poziomu swiatla
def process_percent(percent):

    lamp_percent = Register.LIGHT2_PERCENT

    if percent < lamp_percent:
        percent += 1
        Light2ModHelper.update_data(percent)

    if percent > lamp_percent:
        percent -= 1
        Light2ModHelper.update_data(percent)

    if percent == 0:
        turn_off()
    else:
        turn_on()

    return percent


class Light2Thread(threading.Thread):

    percent = 0

    def __init__(self):
        threading.Thread.__init__(self)

    def process_heater(self):
        pass

    def run(self):

        while not Register.EXIT_FLAG:
            self.percent = process_percent(self.percent)
            time.sleep(1)

