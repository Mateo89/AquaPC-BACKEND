from Helpers import PowerModHelper
from register import Register


def filter1_logic():

    if Register.I2C_POWERMOD_FILTER1_OVERDRIVE:
        return

    if Register.CHANGE_WATER_MODE:
        if Register.I2C_POWERMOD_FILTER1_FLAG:
            PowerModHelper.unset_switch(Register.I2C_POWERMOD_FILTER1)
    else:
        if not Register.I2C_POWERMOD_FILTER1_FLAG:
            PowerModHelper.set_switch(Register.I2C_POWERMOD_FILTER1)

def block_filter():
    Register.I2C_POWERMOD_FILTER1_OVERDRIVE = True


def unblock_filter():
    Register.I2C_POWERMOD_FILTER1_OVERDRIVE = False


def toggle_filter():
    PowerModHelper.toggle_switch(Register.I2C_POWERMOD_FILTER1)

