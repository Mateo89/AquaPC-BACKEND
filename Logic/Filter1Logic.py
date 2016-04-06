from Helpers import PowerModHelper
from register import Register


def filter1_logic():

    if Register.POWERMOD_DATA[str(Register.I2C_POWERMOD_FILTER1)]['override']:
        return

    if Register.CHANGE_WATER_MODE:
        PowerModHelper.unset_switch(Register.I2C_POWERMOD_FILTER1)
    else:
        PowerModHelper.set_switch(Register.I2C_POWERMOD_FILTER1)

def block_filter():
    Register.I2C_POWERMOD_FILTER1_OVERDRIVE = True


def unblock_filter():
    Register.I2C_POWERMOD_FILTER1_OVERDRIVE = False


def toggle_filter():
    PowerModHelper.toggle_switch(Register.I2C_POWERMOD_FILTER1)

