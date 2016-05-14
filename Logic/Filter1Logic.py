import datetime

from Helpers import PowerModHelper
from register import Register


def filter1_logic():

    if Register.POWERMOD_DATA[str(Register.I2C_POWERMOD_FILTER1)]['override']:
        time_now = datetime.datetime.now()
        if (time_now < Register.POWERMOD_DATA_OVERRIDE[str(Register.I2C_POWERMOD_FILTER1)]['override_time']):
            return

    if Register.CHANGE_WATER_MODE:
        PowerModHelper.unset_switch(Register.I2C_POWERMOD_FILTER1)
    else:
        PowerModHelper.set_switch(Register.I2C_POWERMOD_FILTER1)


def block_filter():
    PowerModHelper.override_switch(Register.I2C_POWERMOD_FILTER1)


def unblock_filter():
    PowerModHelper.remove_override_switch(Register.I2C_POWERMOD_FILTER1)


def toggle_filter():
    PowerModHelper.toggle_switch(Register.I2C_POWERMOD_FILTER1)
