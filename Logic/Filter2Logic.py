from Helpers import PowerModHelper
from register import Register


def filter2_logic():

    if Register.I2C_POWERMOD_FILTER2_OVERDRIVE:
        return

    if Register.CHANGE_WATER_MODE:
        if Register.I2C_POWERMOD_FILTER2_FLAG:
            PowerModHelper.unset_switch(Register.I2C_POWERMOD_FILTER2)
    else:
        if not Register.I2C_POWERMOD_FILTER2_FLAG:
            PowerModHelper.set_switch(Register.I2C_POWERMOD_FILTER2)

def block_filter():
    Register.I2C_POWERMOD_FILTER2_OVERDRIVE = True


def unblock_filter():
    Register.I2C_POWERMOD_FILTER2_OVERDRIVE = False


def toggle_filter():
    PowerModHelper.toggle_switch(Register.I2C_POWERMOD_FILTER2)