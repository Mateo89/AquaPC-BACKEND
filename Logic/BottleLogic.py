import threading
import time
import datetime
import Helpers
import settings
from Helpers import BottleModHelper, TimesHelper
from register import Register


def dose_from_bottle(bottle, dose):
    Register.BOTTLE_MANUAL_BOTTLE = bottle
    Register.BOTTLE_MANUAL_DOSE = dose


def up_dose(dose):
    Register.BOTTLE_MANUAL_DOSE += dose


def down_dose(dose):
    tmp = Register.BOTTLE_MANUAL_DOSE - dose
    if tmp < 0:
        tmp = 0
    Register.BOTTLE_MANUAL_DOSE = tmp


def set_bottle(bottle):
    Register.BOTTLE_MANUAL_BOTTLE = bottle


def refill_bottle(bottle):
    ids = str(bottle)
    Register.BOTTLE_SETTINGS[ids]['state'] = Register.BOTTLE_SETTINGS[ids]['capacity']
    Register.BOTTLE_SETTINGS[ids]['percent'] = 100
    Register.BOTTLE_SETTINGS[ids]['alert'] = False
    settings.save_bottle()


def get_weekly_dose(bottle):
    ids = str(bottle)
    weekly_dose = 0
    for pomp_time in Register.BOTTLE_SETTINGS[ids]['times']:
        if pomp_time['on']:
            weekly_dose += pomp_time['dose']
    return weekly_dose


def get_connected_pomp_weekly_dose(bottle):
    weekly_dose = get_weekly_dose(bottle)
    return  round(weekly_dose * Register.BOTTLE_SETTINGS[str(bottle)]['connect_ppm_per_ppm'],3)


def find_connected_poms(bottle):
    connected_pomps = []

    for connected in Register.BOTTLE_SETTINGS.viewkeys():
        if Register.BOTTLE_SETTINGS[connected]['connect_pomp'] == int(bottle):
            connected_pomps.append(int(connected))
    return connected_pomps


def get_connected_pomp_weekly_list(bottle):
    connected = find_connected_poms(bottle)
    list = []
    for pomp in connected:
        list.append(
            {
                "name": Register.BOTTLE_SETTINGS[str(pomp)]["name"],
                "weekly_ppm_dose": get_connected_pomp_weekly_dose(pomp)
            }
        )
    return list

class BottleThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while not Register.EXIT_FLAG:

            for bottle in Register.BOTTLE_SETTINGS.viewkeys():

                if Register.BOTTLE_SETTINGS[bottle]['on']:

                    if TimesHelper.process_times_point(Register.BOTTLE_SETTINGS[bottle]['times']):
                        if not Register.BOTTLE_SETTINGS[bottle]['dosed']:
                            self.dose_from_bottle(bottle)
                    else:
                        Register.BOTTLE_SETTINGS[bottle]['dosed'] = False

            # obsluga manualnego dozowania
            if Register.BOTTLE_MANUAL_BOTTLE:
                self.dose_from_bottle(Register.BOTTLE_MANUAL_BOTTLE, True)

            time.sleep(5)

    def dose_from_bottle(self, bottle, manual=False):
        dose = 0
        day_of_week = datetime.datetime.now().weekday()

        if manual:
            dose = Register.BOTTLE_MANUAL_DOSE
        else:
            dose = Register.BOTTLE_SETTINGS[bottle]['times'][day_of_week]['dose']

        if dose == 0:
            Helpers.log("Pomijanie pojemnika: " + Register.BOTTLE_SETTINGS[bottle]['name'] + " z powodu zerowej dawki")
            return
        ml = round(dose / Register.BOTTLE_SETTINGS[bottle]['ppm_per_ml'], 2)

        time_dose = ml * Register.BOTTLE_SETTINGS[bottle]['ml_per_sec']

        Helpers.log("Podawanie dawki " + str(dose) + "ppm (" + str(ml) + "ml) z pojemnika: " +
                    Register.BOTTLE_SETTINGS[bottle]['name'] +
                    " przez czas: " + str(time_dose) + "s")

        if Register.BOTTLE_SETTINGS[bottle]['connect_pomp'] != -1:
            connected_dose = dose * Register.BOTTLE_SETTINGS[bottle]['connect_ppm_per_ppm']
            Helpers.log("Zostanie rowniez podana dawka " + str(dose) + "ppm  " + Register.BOTTLE_SETTINGS['connect_pomp']['name'])

        #if manual:
        #    Register.BOTTLE_MANUAL_REMAINING_DOSE = dose

        number = int(bottle) - 1

        BottleModHelper.set_switch(number)
        time.sleep(time_dose)
        BottleModHelper.unset_switch(number)

        Helpers.log("Koniec dozowania z pojemnika: " + Register.BOTTLE_SETTINGS[bottle]['name'])
        Register.BOTTLE_SETTINGS[bottle]['dosed'] = True

        # zmiana stanu pojemnika i obliczenie aktualnego procentu

        state = Register.BOTTLE_SETTINGS[bottle]['state'] - ml
        capacity = Register.BOTTLE_SETTINGS[bottle]['capacity']

        Register.BOTTLE_SETTINGS[bottle]['state'] = state
        Register.BOTTLE_SETTINGS[bottle]['percent'] = int((float(state) / capacity) * 100)

        if Register.BOTTLE_SETTINGS[bottle]['percent'] <= Register.BOTTLE_SETTINGS[bottle]['alertpercent']:
            Register.BOTTLE_SETTINGS[bottle]['alert'] = True
        else:
            Register.BOTTLE_SETTINGS[bottle]['alert'] = False

        if manual:
            Register.BOTTLE_MANUAL_BOTTLE = None

        settings.save_bottle()
