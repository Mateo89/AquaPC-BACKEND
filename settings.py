import json

from configobj import ConfigObj
from register import Register
import os.path
import Helpers

def load_settings():

    #Register.LOGS_FLAG =  ConfigObj.as_bool(config,"LOGS_FLAG")

    with open('water.settings', 'r') as data_file:
        Register.WATER_SETTINGS = json.load(data_file)

    with open('lamp.settings', 'r') as data_file:
        Register.LAMPS_SETTINGS = json.load(data_file)

    with open('bottles.settings','r') as data_file:
        Register.BOTTLE_SETTINGS = json.load(data_file)

    with open('heater.settings', 'r') as data_file:
        Register.HEATER_SETTINGS = json.load(data_file)

    with open('co2.settings', 'r') as data_file:
        Register.CO2_SETTINGS = json.load(data_file)

    with open('o2.settings', 'r') as data_file:
        Register.O2_SETTINGS = json.load(data_file)

    with open('filter.settings', 'r') as data_file:
        Register.FILTER_SETTINGS = json.load(data_file)

    Helpers.log("Wczytano ustawienia")


def save_settings():

    save_water()
    save_lamp()
    save_bottle()
    save_heater()
    save_co2()
    save_o2()
    save_filter()


def save_water():
    with open('water.settings', 'w') as data_file:
        configString = json.dumps(Register.WATER_SETTINGS, default=lambda o: o.__dict__, sort_keys=True, indent=4,
                                  separators=(',', ': '))
        data_file.write(configString)
        data_file.close()
        Helpers.log("Zapisano ustawienia Wody")


def save_lamp():
    with open('lamp.settings', 'w') as data_file:
        configString = json.dumps(Register.LAMPS_SETTINGS, default=lambda o: o.__dict__, sort_keys=True, indent=4,
                                  separators=(',', ': '))
        data_file.write(configString)
        data_file.close()
        Helpers.log("Zapisano ustawienia Lamp")


def save_bottle():
    with open('bottles.settings', 'w') as data_file:
        configString = json.dumps(Register.BOTTLE_SETTINGS, default=lambda o: o.__dict__, sort_keys=True,indent=4, separators=(',', ': '))
        data_file.write(configString)
        data_file.close()
        Helpers.log("Zapisano ustawienia Dozownika")


def save_heater():
    with open('heater.settings', 'w') as data_file:
        configString = json.dumps(Register.HEATER_SETTINGS, default=lambda o: o.__dict__, sort_keys=True,indent=4, separators=(',', ': '))
        data_file.write(configString)
        data_file.close()
        Helpers.log("Zapisano ustawienia Grzalki")


def save_co2():
    with open('co2.settings', 'w') as data_file:
        configString = json.dumps(Register.CO2_SETTINGS, default=lambda o: o.__dict__, sort_keys=True, indent=4,
                                  separators=(',', ': '))
        data_file.write(configString)
        data_file.close()
        Helpers.log("Zapisano ustawienia CO2")


def save_o2():
    with open('o2.settings', 'w') as data_file:
        configString = json.dumps(Register.O2_SETTINGS, default=lambda o: o.__dict__, sort_keys=True, indent=4,
                                  separators=(',', ': '))
        data_file.write(configString)
        data_file.close()
        Helpers.log("Zapisano ustawienia O2")


def save_filter():
    with open('filter.settings', 'w') as data_file:
        configString = json.dumps(Register.FILTER_SETTINGS, default=lambda o: o.__dict__, sort_keys=True, indent=4,
                                  separators=(',', ': '))
        data_file.write(configString)
        data_file.close()
        Helpers.log("Zapisano ustawienia Filtrow")