__author__ = 'mateu'

import datetime

class Register:

    # DISPLAY
    CURRENT_SCREEN = None
    LCD = None
    REMINDER_TEXT = None

    # GENERAL ZONE
    LOGS_FLAG = True
    LOGS_EVENTS = []
    EXIT_FLAG = False
    CHANGE_WATER_MODE = False

    # LOGIC ZONE
    LIRC_EVENTS = None

    WATER_SETTINGS = None

    WATER_TEMP = 25.0
    WATER_TEMP_UPDATE_DATE = 'Nigdy'

    AIR_TEMP = 25.0
    AIR_TEMP_UPDATE_DATE = 'Nigdy'

    PH_VALUE = 6.5
    PH_UPDATE_DATE = 'Nigdy'


    # 0 - night
    # 1 - sunrise/sunset
    # 2 - sunny
    LIGHT_MODE = 0

    # I2C BUS ZONE
    I2C_POWERMOD_ADRESS = 0x08
    I2C_POWERMOD_DATA = 0x00
    I2C_POWERMOD_LIGHT1 = 0
    I2C_POWERMOD_LIGHT2 = 1
    I2C_POWERMOD_FILTER1 = 2
    I2C_POWERMOD_FILTER2 = 3
    I2C_POWERMOD_O2 = 4
    I2C_POWERMOD_CO2 = 5
    I2C_POWERMOD_HEATER = 6
    I2C_POWERMOD_HEATER_LED = 7


    POWERMOD_DATA = {
        str(I2C_POWERMOD_LIGHT1): {"name": "Lampa 1", "on": False, "override": False, 'img': 'img/fan-128.png', "warning": False, "fanon": True, "fanoverride": False},
        str(I2C_POWERMOD_LIGHT2): {"name": "Lampa 2", "on": False, "override": False, 'img': 'img/fan-128.png'},
        str(I2C_POWERMOD_FILTER1): {"name": "Filtr 1", "on": False, "override": False, 'img': 'img/fan-128.png'},
        str(I2C_POWERMOD_FILTER2): {"name": "Filtr 2", "on": False, "override": False, 'img': 'img/fan-128.png'},
        str(I2C_POWERMOD_O2): {"name": "O2", "on": False, "override": False, 'img': 'img/o2v2128.png'},
        str(I2C_POWERMOD_CO2): {"name": "CO2", "on": False, "override": False, 'img': 'img/co2128.png'},
        str(I2C_POWERMOD_HEATER): {"name": "Grzalka", "on": False, "override": False, 'img': 'img/heater128.png'},
        str(I2C_POWERMOD_HEATER_LED): {"name": "Grzalka LED", "on": False, "override": False, 'img': 'img/heater128.png'}
    }

    OVERRIDE_TIME = 20

    POWERMOD_DATA_OVERRIDE = {
        str(I2C_POWERMOD_LIGHT1): {"override_time": datetime.datetime.now()},
        str(I2C_POWERMOD_LIGHT2): {"override_time": datetime.datetime.now()},
        str(I2C_POWERMOD_FILTER1): {"override_time": datetime.datetime.now()},
        str(I2C_POWERMOD_FILTER2): {"override_time": datetime.datetime.now()},
        str(I2C_POWERMOD_O2): {"override_time": datetime.datetime.now()},
        str(I2C_POWERMOD_CO2): {"override_time": datetime.datetime.now()},
        str(I2C_POWERMOD_HEATER): {"override_time": datetime.datetime.now()},
        str(I2C_POWERMOD_HEATER_LED): {"override_time": datetime.datetime.now()}
    }

    HEATER_SETTINGS = None

    LAMPS_SETTINGS = None

    LIGHT1_ADDRESS = 0x22
    LIGHT1_PERCENT = [0, 0, 0, 0]
    LIGHT1_TEMP = 23.0
    LIGHT1_TEMP_UPDATE_DATE = 'Nigdy'

    # LIGHT2 ZONE
    LIGHT2_ADDRESS = 0x20
    LIGHT2_PERCENT = [0, 0, 0, 0]

    # FEEDER ZONE
    FEEDER_RUNNING = False

    # BOTTLE ZONE

    BOTTLE_MANUAL_BOTTLE = None
    BOTTLE_MANUAL_DOSE = 0

    BOTTLE_DATA = 0x00
    BOTTLE_ADDRESS = 0x10

    BOTTLE_SETTINGS = None

    CO2_SETTINGS = None
    CO2_PH_FLAG = False
    O2_SETTINGS = None
    FILTER_SETTINGS = None
    PH_SETTINGS = None

    @staticmethod
    def initRegister():
        pass

    @staticmethod
    def get_switch_state(switch):
        if Register.POWERMOD_DATA[str(switch)]['on']:
            return "ON"
        else:
            return "OFF"




