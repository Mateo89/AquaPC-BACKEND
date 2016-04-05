import settings
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
    settings.save_bottle()
