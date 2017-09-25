import datetime

from Helpers import PowerModHelper, TimesHelper
from register import Register


def o2_logic():
    pass


def block_o2():
    PowerModHelper.override_switch(Register.I2C_POWERMOD_O2)


def unblock_o2():
    PowerModHelper.remove_override_switch(Register.I2C_POWERMOD_O2)


def turn_on():
    PowerModHelper.set_switch(Register.I2C_POWERMOD_O2)


def turn_off():
    PowerModHelper.unset_switch(Register.I2C_POWERMOD_O2)


def toggle_o2():
    PowerModHelper.toggle_switch(Register.I2C_POWERMOD_O2)