import datetime
import math

from Helpers import PowerModHelper
from register import Register


def water_temp_logic():

    if Register.POWERMOD_DATA[str(Register.I2C_POWERMOD_HEATER)]['override'] or Register.POWERMOD_DATA[str(Register.I2C_POWERMOD_HEATER_LED)]['override']:
        time_now = datetime.datetime.now()
        if (time_now < Register.POWERMOD_DATA_OVERRIDE[str(Register.I2C_POWERMOD_HEATER)]['override_time'] and
                    time_now < Register.POWERMOD_DATA_OVERRIDE[str(Register.I2C_POWERMOD_HEATER_LED)]['override_time']):
            return

    # sprawdzenie czy grzalki powinny dzialac
    if not Register.CHANGE_WATER_MODE:

        #sprwdzenie czy jest potrzebne wlaczenie ogrzewania

        delta = Register.WATER_SETTINGS['temp'] - Register.WATER_TEMP

        if float(delta) > float(Register.HEATER_SETTINGS['delta']):  # zgadzamy sie tylko na 0.5 stopnia roznicy
            # sprawdzenie czy swiatla sa wlaczne
            # jezeli tak - mozemy wlaczyc pompe

            if Register.LAMPS_SETTINGS["1"]['use_heater_on']:
                if math.fabs(Register.LIGHT1_TEMP - Register.WATER_SETTINGS['temp']) > Register.LAMPS_SETTINGS["1"]['use_heater_delta']:
                    PowerModHelper.set_switch(Register.I2C_POWERMOD_HEATER_LED)
                    PowerModHelper.unset_switch(Register.I2C_POWERMOD_HEATER)
                else: # musimy wlaczyc grzalke bo lampa jest za zimna
                    PowerModHelper.set_switch(Register.I2C_POWERMOD_HEATER)
                    PowerModHelper.unset_switch(Register.I2C_POWERMOD_HEATER_LED)

            else:  # jezeli nie jest to uzyjemy grzalki
                PowerModHelper.unset_switch(Register.I2C_POWERMOD_HEATER_LED)
                PowerModHelper.set_switch(Register.I2C_POWERMOD_HEATER)

        else:  # wylaczenie ogrzewania
            turn_off_heaters()
    else:
        if Register.POWERMOD_DATA[str(Register.I2C_POWERMOD_HEATER_LED)]['on']:
            PowerModHelper.unset_switch(Register.I2C_POWERMOD_HEATER_LED)
        if Register.POWERMOD_DATA[str(Register.I2C_POWERMOD_HEATER)]['on'] and \
            Register.HEATER_SETTINGS['water_change_off']:
            PowerModHelper.unset_switch(Register.I2C_POWERMOD_HEATER)


def turn_off_heaters():
    PowerModHelper.unset_switch(Register.I2C_POWERMOD_HEATER)
    PowerModHelper.unset_switch(Register.I2C_POWERMOD_HEATER_LED)


def block_heater():
    PowerModHelper.remove_override_switch(Register.I2C_POWERMOD_HEATER)


def block_heater_led():
    PowerModHelper.remove_override_switch(Register.I2C_POWERMOD_HEATER_LED)


def unblock_heater():
    PowerModHelper.remove_override_switch(Register.I2C_POWERMOD_HEATER)


def unblock_heater_led():
    PowerModHelper.remove_override_switch(Register.I2C_POWERMOD_HEATER_LED)


def toggle_heater():
    PowerModHelper.toggle_switch(Register.I2C_POWERMOD_HEATER)


def toggle_heater_led():
    PowerModHelper.toggle_switch(Register.I2C_POWERMOD_HEATER_LED)
