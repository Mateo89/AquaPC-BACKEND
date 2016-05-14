import datetime
import threading
import time

from Helpers import PowerModHelper, TimesHelper, Light1ModHelper
from register import Register


def light1_logic():
    # logika dokonania pomiaru temp
    # Register.LIGHT1_TEMP = Light1ModHelper.get_temp()

    if Register.LIGHT1_TEMP > 50:
        Light1ModHelper.set_fun_speed(2)
    else:
        Light1ModHelper.set_fun_speed(0)


    if Register.POWERMOD_DATA[str(Register.I2C_POWERMOD_LIGHT1)]['override']:
        time_now = datetime.datetime.now()
        if time_now < Register.POWERMOD_DATA_OVERRIDE[str(Register.I2C_POWERMOD_LIGHT1)]['override_time']:
            return
        else:
            unblock()

    if not Register.LAMPS_SETTINGS['1']['on']:
        set_percent([0, 0, 0, 0])
        return

    if Register.CHANGE_WATER_MODE:
        if Register.LAMPS_SETTINGS['1']['water_change_on']:
            set_percent(Register.LAMPS_SETTINGS['1']['water_change_percent'])
    else:
        percent = TimesHelper.process_times_states(Register.LAMPS_SETTINGS['1']['times'])
        set_percent(percent)


def set_percent(percent):
    Register.LIGHT1_PERCENT = percent


def up_percent(up, channel):
    percent = Register.LIGHT1_PERCENT[channel] + up
    if percent > 100:
        percent = 100
    Register.LIGHT1_PERCENT[channel] = percent


def down_percent(down, channel):
    percent = Register.LIGHT1_PERCENT[channel] - down
    if percent < 0:
        percent = 0
    Register.LIGHT1_PERCENT[channel] = percent


def block():
    Register.POWERMOD_DATA[str(Register.I2C_POWERMOD_LIGHT1)]['override'] = True
    Register.POWERMOD_DATA_OVERRIDE[str(Register.I2C_POWERMOD_LIGHT1)]['override_time'] = datetime.datetime.now() \
                                                                                          + datetime.timedelta(
        minutes=Register.OVERRIDE_TIME)


def unblock():
    Register.POWERMOD_DATA[str(Register.I2C_POWERMOD_LIGHT1)]['override'] = False
    Register.POWERMOD_DATA_OVERRIDE[str(Register.I2C_POWERMOD_LIGHT1)]['override_time'] = datetime.datetime.now()


def toggle_light():
    PowerModHelper.toggle_switch(Register.I2C_POWERMOD_LIGHT1)


def turn_on():
    PowerModHelper.set_switch(Register.I2C_POWERMOD_LIGHT1)


def turn_off():
    PowerModHelper.unset_switch(Register.I2C_POWERMOD_LIGHT1)


def process_percent(percent):

    lamp_percent = Register.LIGHT1_PERCENT

    for i in range(0, len(lamp_percent)):
        if percent[i] < lamp_percent[i]:
            percent[i] += 1
            Light1ModHelper.update_data(i, percent[i])

        if percent[i] > lamp_percent[i]:
            percent[i] -= 1
            Light1ModHelper.update_data(i, percent[i])

    if percent[0] == 0 and percent[1] == 0 and percent[2] == 0 and percent[3] == 0:
        turn_off()
    else:
        turn_on()

    return percent


class Light1Thread(threading.Thread):

    percent = [0, 0, 0, 0]

    def __init__(self):
        threading.Thread.__init__(self)

    def process_heater(self):
        pass

    def run(self):
        while not Register.EXIT_FLAG:
            self.percent = process_percent(self.percent)
            time.sleep(1)

