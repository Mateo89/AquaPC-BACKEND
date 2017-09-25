import datetime

from Helpers import PowerModHelper, TimesHelper
from register import Register


def co2_logic():
    if Register.POWERMOD_DATA[str(Register.I2C_POWERMOD_CO2)]['override']:
        time_now = datetime.datetime.now()
        if time_now < Register.POWERMOD_DATA_OVERRIDE[str(Register.I2C_POWERMOD_CO2)]['override_time']:
            return
        else:
            unblock_co2()

    if not Register.CO2_SETTINGS['on']:
        turn_off()
        return

    if Register.CHANGE_WATER_MODE:
        if Register.CO2_SETTINGS['water_change_off']:
            turn_off()
            return

    if Register.CO2_SETTINGS['bind_with_filter']:
        if not Register.POWERMOD_DATA[str(Register.I2C_POWERMOD_FILTER1)]['on']:
            turn_off()
            return

    # sprawdzenie czy dzialac ma 24h
    if Register.CO2_SETTINGS['full_day']:
        turn_on()
        return

    if Register.CO2_PH_FLAG:
        turn_on()
    else:
        turn_off()


def block_co2():
    PowerModHelper.override_switch(Register.I2C_POWERMOD_CO2)


def unblock_co2():
    PowerModHelper.remove_override_switch(Register.I2C_POWERMOD_CO2)


def turn_on():
    #ustawienie czasu start
    PowerModHelper.set_switch(Register.I2C_POWERMOD_CO2)


def turn_off():
    #ustawienie czasu stop
    PowerModHelper.unset_switch(Register.I2C_POWERMOD_CO2)


def toggle_co2():
    PowerModHelper.toggle_switch(Register.I2C_POWERMOD_CO2)


def save_co2_use():
    pass


def turn_on_ph():
    Register.CO2_PH_FLAG = True


def turn_off_ph():
    Register.CO2_PH_FLAG = False
