from register import Register
from smbus import SMBus


def reset():
    i2c_bus = SMBus(1)
    i2c_bus.write_byte_data(Register.BOTTLE_ADDRESS, 0xff, 0x00)


def update_data():
    i2c_bus = SMBus(1)
    i2c_bus.write_byte_data(Register.BOTTLE_ADDRESS, 0xff, Register.BOTTLE_DATA)


def set_switch(switch):
    Register.BOTTLE_DATA |= 1 << switch
    update_data()


def unset_switch(switch):
    Register.BOTTLE_DATA &= ~(1 << switch)
    update_data()
