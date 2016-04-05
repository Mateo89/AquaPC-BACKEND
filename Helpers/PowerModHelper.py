__author__ = 'mateu'
from register import Register
from smbus import SMBus
import Helpers

def reset():
    i2c_bus = SMBus(1)
    i2c_bus.write_byte_data(Register.I2C_POWERMOD_ADRESS,0xff, 0x00)


def update_data():
    i2c_bus = SMBus(1)
    i2c_bus.write_byte_data(Register.I2C_POWERMOD_ADRESS,0xff, Register.I2C_POWERMOD_DATA)


def set_switch(switch):
    Register.I2C_POWERMOD_DATA |= 1 << switch
    update_data()
    update_flag(switch, True)


def unset_switch(switch):
    Register.I2C_POWERMOD_DATA &= ~(1 << switch)
    update_data()
    update_flag(switch, False)

def toggle_switch(switch):
    Register.I2C_POWERMOD_DATA ^= (1 << switch)
    flag = (Register.I2C_POWERMOD_DATA & (1 << switch)) >> switch
    update_data()
    update_flag(switch, flag)


def update_flag(switch, value):
    Helpers.log("Zmiana wartosci flagi: " + Register.POWERMOD_DATA[str(switch)]['name'] + " na " + str(value))
    Register.POWERMOD_DATA[str(switch)]['on'] = value


def override_switch(switch):
    Register.POWERMOD_DATA[str(switch)]['override'] = True


def remove_override_switch(switch):
    Register.POWERMOD_DATA[str(switch)]['override'] = False