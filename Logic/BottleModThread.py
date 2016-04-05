import threading
import time
import datetime
import Helpers
from register import Register
from Helpers import BottleModHelper
import settings


class BottleModThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while True:

            time_now = datetime.datetime.now()
            time_now = time_now.replace(second=0, microsecond=0)

            for bottle in Register.BOTTLE_MOD.keys():

                if Register.BOTTLE_MOD[bottle]['ON']:

                    hour = Register.BOTTLE_MOD[bottle]['HOUR']
                    min2 = Register.BOTTLE_MOD[bottle]['MIN']

                    # utworzenie godziny i sprawdzenie czy uruchomic
                    time_on = time_now.replace(hour=hour, minute=min2, second=0, microsecond=0)

                    if time_now == time_on:
                        if not Register.BOTTLE_MOD[bottle]['DOSED']:
                            dose_from_bottle(bottle)
                    else:
                        Register.BOTTLE_MOD[bottle]['DOSED'] = False

            # obsluga manualnego dozowania
            if Register.BOTTLE_MANUAL_BOTTLE:
                dose_from_bottle(Register.BOTTLE_MANUAL_BOTTLE, True)

            if Register.EXIT_FLAG:
                break

            time.sleep(5)


def dose_from_bottle(bottle, manual=False):
    dose = 0
    if manual:
        dose = Register.BOTTLE_MANUAL_DOSE
    else:
        dose = Register.BOTTLE_MOD[bottle]['DOSE']

    if dose == 0:
        Helpers.log("Pomijanie pojemnika: " + Register.BOTTLE_MOD[bottle]['NAME'] + " z powodu zerowej dawki")
        return

    time_dose = dose * Register.BOTTLE_MOD[bottle]['SEC_PER_ML']
    Helpers.log("Podawanie dawki z pojemnika: " + Register.BOTTLE_MOD[bottle]['NAME'] +
                " przez czas: " + str(time_dose))

    if manual:
        Register.BOTTLE_MANUAL_REMAINING_DOSE = dose

    number = Register.BOTTLE_MOD[bottle]['NUM']
    BottleModHelper.set_switch(number)
    for x in range(dose):
        time.sleep(Register.BOTTLE_MOD[bottle]['SEC_PER_ML'])
        if manual:
            Register.BOTTLE_MANUAL_DOSE -= 1
    BottleModHelper.unset_switch(number)
    Helpers.log("Koniec dozowania z pojemnika: " + Register.BOTTLE_MOD[bottle]['NAME'])
    Register.BOTTLE_MOD[bottle]['DOSED'] = True

    # zmiana stanu pojemnika i obliczenie aktualnego procentu

    state = Register.BOTTLE_MOD[bottle]['STATE'] - dose
    capacity = Register.BOTTLE_MOD[bottle]['CAPACITY']

    Register.BOTTLE_MOD[bottle]['STATE'] = state
    Register.BOTTLE_MOD[bottle]['PERCENT'] = int((float(state) / capacity) * 100)

    if manual:
        Register.BOTTLE_MANUAL_BOTTLE = None

    settings.save_settings()
