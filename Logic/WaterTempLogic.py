import Helpers
from register import Register
from Helpers import PowerModHelper
import math


def water_temp_logic():

    if Register.POWERMOD_DATA[str(Register.I2C_POWERMOD_HEATER)]['override'] or Register.POWERMOD_DATA[str(Register.I2C_POWERMOD_HEATER_LED)]['override']:
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
    Register.POWERMOD_DATA[str(Register.I2C_POWERMOD_HEATER)]['override'] = True


def block_heater_led():
    Register.POWERMOD_DATA[str(Register.I2C_POWERMOD_HEATER_LED)]['override'] = True


def unblock_heater():
    Register.POWERMOD_DATA[str(Register.I2C_POWERMOD_HEATER)]['override'] = False


def unblock_heater_led():
    Register.POWERMOD_DATA[str(Register.I2C_POWERMOD_HEATER_LED)]['override'] = False


def toggle_heater():
    PowerModHelper.toggle_switch(Register.I2C_POWERMOD_HEATER)


def toggle_heater_led():
    PowerModHelper.toggle_switch(Register.I2C_POWERMOD_HEATER_LED)