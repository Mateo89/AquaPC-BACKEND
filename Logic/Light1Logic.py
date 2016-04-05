from register import Register
from Helpers import PowerModHelper
import datetime


def light1_logic():

    if Register.LIGHT1_OVERDRIVE:
        return

    if not Register.CHANGE_WATER_MODE:
        time_now = datetime.datetime.now()
        time_off = time_now.replace(hour=Register.LIGHT1_OFF_HOUR, minute=Register.LIGHT1_OFF_MINUTE, second=0, microsecond=0)
        time_on = time_now.replace(hour=Register.LIGHT1_ON_HOUR, minute=Register.LIGHT1_ON_MINUTE, second=0, microsecond=0)

        if time_on <= time_now < time_off:
            turn_on_light()
        else:
            turn_off_light()
    else:
        if Register.LIGHT1_CHANGE_WATER_ON_FLAG:
            turn_on_light()


def turn_on_light():
    if not Register.I2C_POWERMOD_LIGHT1_FLAG:
        Register.LIGHT1_PERCENT = 100
        PowerModHelper.set_switch(Register.I2C_POWERMOD_LIGHT1)


def turn_off_light():
    if Register.I2C_POWERMOD_LIGHT1_FLAG:
        Register.LIGHT1_PERCENT = 0
        PowerModHelper.unset_switch(Register.I2C_POWERMOD_LIGHT1)


def block_light():
    Register.LIGHT1_OVERDRIVE = True


def unblock_light():
    Register.LIGHT1_OVERDRIVE = False


def toggle_light():
    PowerModHelper.toggle_switch(Register.I2C_POWERMOD_LIGHT1)


def up_percent(up):
    percent = Register.LIGHT1_PERCENT + up
    if percent > 100:
        percent = 100
    Register.LIGHT1_PERCENT = percent


def down_percent(down):
    percent = Register.LIGHT1_PERCENT - down
    if percent < 0:
        percent = 0
    Register.LIGHT1_PERCENT = percent

