from time import sleep

from register import Register
from smbus import SMBus

anti_log = [
    0, 0, 1, 1, 1, 1, 2, 2, 2, 3,
    3, 3, 4, 4, 4, 5, 5, 6, 6, 7,
    8, 8, 9, 10, 10, 11, 12, 13, 14, 15,
    16, 17, 18, 19, 20, 22, 23, 24, 26, 27,
    29, 30, 32, 34, 35, 37, 39, 41, 43, 45,
    47, 49, 51, 54, 56, 58, 61, 64, 66, 69,
    72, 75, 78, 81, 84, 87, 90, 93, 97, 100,
    104, 108, 111, 115, 119, 123, 127, 131, 136, 140,
    145, 149, 154, 159, 163, 168, 173, 179, 184, 189,
    195, 200, 206, 212, 217, 223, 230, 236, 242, 248,
    255
]


def reset():
    def reset():
        i2c_bus = SMBus(1)
        i2c_bus.write_byte_data(Register.LIGHT2_ADDRESS, 0, 0)
        i2c_bus.write_byte_data(Register.LIGHT2_ADDRESS, 1, 0)
        i2c_bus.write_byte_data(Register.LIGHT2_ADDRESS, 2, 0)
        i2c_bus.write_byte_data(Register.LIGHT2_ADDRESS, 3, 0)
        i2c_bus.write_byte_data(Register.LIGHT2_ADDRESS, 4, 255)


def get_temp():
    # zlecenie konwersji
    i2c_bus = SMBus(1)
    i2c_bus.write_byte_data(Register.LIGHT2_ADDRESS, 10, 1)
    sleep(1)
    cel = i2c_bus.read_word_data(0x20, 5)
    cel = cel >> 8
    return cel


def set_fun_speed(level):
    i2c_bus = SMBus(1)

    if level == 0:
        i2c_bus.write_byte_data(Register.LIGHT2_ADDRESS, 4, 255)
    if level == 1:
        i2c_bus.write_byte_data(Register.LIGHT2_ADDRESS, 4, 125)
    if level == 2:
        i2c_bus.write_byte_data(Register.LIGHT2_ADDRESS, 4, 0)


def update_data(chanel, percent):
    i2c_bus = SMBus(1)
    i2c_bus.write_byte_data(Register.LIGHT2_ADDRESS, chanel, anti_log[percent])
