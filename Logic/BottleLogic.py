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

        time_dose = dose * Register.BOTTLE_SETTINGS[bottle]['ml_per_sec']
        Helpers.log("Podawanie dawki " + str(dose) + "ml z pojemnika: " + Register.BOTTLE_SETTINGS[bottle]['name'] +
                    " przez czas: " + str(time_dose))

        #if manual:
        #    Register.BOTTLE_MANUAL_REMAINING_DOSE = dose

        number = int(bottle) - 1
        BottleModHelper.set_switch(number)
        for x in range(dose):
            time.sleep(Register.BOTTLE_SETTINGS[bottle]['ml_per_sec'])
            if manual:
                Register.BOTTLE_MANUAL_DOSE -= 1
        BottleModHelper.unset_switch(number)
        Helpers.log("Koniec dozowania z pojemnika: " + Register.BOTTLE_SETTINGS[bottle]['name'])
        Register.BOTTLE_SETTINGS[bottle]['dosed'] = True

        # zmiana stanu pojemnika i obliczenie aktualnego procentu

        state = Register.BOTTLE_SETTINGS[bottle]['state'] - dose
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
