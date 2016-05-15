import datetime
import threading
import time

from Helpers import PowerModHelper, TimesHelper, Light2ModHelper
from register import Register


def light2_logic():

    if Register.POWERMOD_DATA[str(Register.I2C_POWERMOD_LIGHT2)]['override']:
        time_now = datetime.datetime.now()
        if time_now < Register.POWERMOD_DATA_OVERRIDE[str(Register.I2C_POWERMOD_LIGHT2)]['override_time']:
            return
        else:
            unblock()

    if not Register.LAMPS_SETTINGS['2']['on']:
        set_percent([0, 0, 0, 0])
        return

    if Register.CHANGE_WATER_MODE:
        if Register.LAMPS_SETTINGS['2']['water_change_on']:
            set_percent(Register.LAMPS_SETTINGS['2']['water_change_percent'])
    else:
        percent = TimesHelper.process_times_states(Register.LAMPS_SETTINGS['2']['times'])
        set_percent(percent)


def set_percent(percent):
    Register.LIGHT2_PERCENT = percent


def up_percent(up, channel):
    percent = Register.LIGHT2_PERCENT[channel] + up
    if percent > 100:
        percent = 100
    Register.LIGHT2_PERCENT[channel] = percent


def down_percent(down, channel):
    percent = Register.LIGHT2_PERCENT[channel] - down
    if percent < 0:
        percent = 0
    Register.LIGHT2_PERCENT[channel] = percent


def block():
    PowerModHelper.override_switch(Register.I2C_POWERMOD_LIGHT2)


def unblock():
    PowerModHelper.remove_override_switch(Register.I2C_POWERMOD_LIGHT2)


def toggle_light():
    PowerModHelper.toggle_switch(Register.I2C_POWERMOD_LIGHT2)


def turn_on():
    PowerModHelper.set_switch(Register.I2C_POWERMOD_LIGHT2)


def turn_off():
    PowerModHelper.unset_switch(Register.I2C_POWERMOD_LIGHT2)


# kontrolowanie poziomu swiatla
def process_percent(percent):

    lamp_percent = Register.LIGHT2_PERCENT

    for i in range(0, len(lamp_percent)):
        if percent[i] < lamp_percent[i]:
            percent[i] += 1
            Light2ModHelper.update_data(i, percent[i])

        if percent[i] > lamp_percent[i]:
            percent[i] -= 1
            Light2ModHelper.update_data(i, percent[i])

    if percent[0] == 0 and percent[1] == 0 and percent[2] == 0 and percent[3] == 0:
        turn_off()
    else:
        turn_on()

    return percent


class Light2Thread(threading.Thread):

    percent = [0, 0, 0, 0]

    def __init__(self):
        threading.Thread.__init__(self)

    def process_heater(self):
        pass

    def run(self):

        while not Register.EXIT_FLAG:
            self.percent = process_percent(self.percent)
            time.sleep(1)

