from register import Register

__author__ = 'mateu'

KEY_POWER = "power"
KEY_DOWN = "down"
KEY_UP = "up"
KEY_RIGHT = "right"
KEY_LEFT = "left"
KEY_OK = "ok"
KEY_MENU = "menu"
KEY_BACK = "back"
KEY_0 = "0"
KEY_1 = "1"
KEY_2 = "2"
KEY_3 = "3"
KEY_4 = "4"
KEY_5 = "5"
KEY_6 = "6"
KEY_7 = "7"
KEY_8 = "8"
KEY_9 = "9"


def get_event():
    lirc_event = Register.LIRC_EVENTS
    Register.LIRC_EVENTS = None
    return lirc_event