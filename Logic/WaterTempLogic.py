from register import Register
from Helpers import PowerModHelper
import math


def water_temp_logic():

    if not Register.POWERMOD_DATA[str(Register.I2C_POWERMOD_HEATER)]['override'] and \
            not Register.POWERMOD_DATA[str(Register.I2C_POWERMOD_HEATER_LED)]['override']:
        # sprawdzenie czy grzalki powinny dzialac
        if not Register.CHANGE_WATER_MODE:

            #sprwdzenie czy jest potrzebne wlaczenie ogrzewania
            if (Register.WATER_SETTINGS['temp'] - Register.WATER_TEMP) > Register.HEATER_SETTINGS['delta']:  # zgadzamy sie tylko na 0.5 stopnia roznicy

                # sprawdzenie czy swiatla sa wlaczne
                # jezeli tak - mozemy wlaczyc pompe

                if Register.LAMPS_SETTINGS["1"]['use_heater_on']:
                    if math.fabs(Register.LIGHT1_TEMP - Register.WATER_SETTINGS['temp']) > Register.LAMPS_SETTINGS["1"]['use_heater_delta']:
                        if not Register.POWERMOD_DATA[str(Register.I2C_POWERMOD_HEATER_LED)]['on']: # jezeli jest wylaczno
                            PowerModHelper.set_switch(Register.I2C_POWERMOD_HEATER_LED)
                            PowerModHelper.unset_switch(Register.I2C_POWERMOD_HEATER)
                    else: # musimy wlaczyc grzalke bo lampa jest za zimna
                        PowerModHelper.set_switch(Register.I2C_POWERMOD_HEATER)
                        PowerModHelper.unset_switch(Register.I2C_POWERMOD_HEATER_LED)

                else:  # jezeli nie jest to uzyjemy grzalki
                    if not Register.I2C_POWERMOD_HEATER_FLAG:
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
    if Register.POWERMOD_DATA[str(Register.I2C_POWERMOD_HEATER_LED)]['on']:
        PowerModHelper.unset_switch(Register.I2C_POWERMOD_HEATER)
    if Register.POWERMOD_DATA[str(Register.I2C_POWERMOD_HEATER)]['on']:
        PowerModHelper.unset_switch(Register.I2C_POWERMOD_HEATER_LED)


def block_heater():
    Register.I2C_POWERMOD_HEATER_OVERDRIVE = True


def block_heater_led():
    Register.I2C_POWERMOD_HEATER_LED_OVERDRIVE = True


def unblock_heater():
    Register.I2C_POWERMOD_HEATER_OVERDRIVE = False


def unblock_heater_led():
    Register.I2C_POWERMOD_HEATER_LED_OVERDRIVE = False


def toggle_heater():
    PowerModHelper.toggle_switch(Register.I2C_POWERMOD_HEATER)


def toggle_heater_led():
    PowerModHelper.toggle_switch(Register.I2C_POWERMOD_HEATER_LED)