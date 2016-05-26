from register import Register
import Helpers


def get_water_change_state():
    if Register.CHANGE_WATER_MODE:
        return " ON"
    else:
        return "OFF"


def toggle_water_change():
    if Register.CHANGE_WATER_MODE:
        Register.CHANGE_WATER_MODE = True
        Helpers.log("Wlaczenie trybu podmiany wody")
    else:
        Register.CHANGE_WATER_MODE = False
        Helpers.log("Wylaczenie trybu podmiany wody")
