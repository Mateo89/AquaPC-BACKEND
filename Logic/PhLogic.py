import datetime

from Helpers import PowerModHelper, TimesHelper
from register import Register
import Co2Logic


def ph_logic():

    if Register.PH_VALUE < (Register.PH_SETTINGS['value'] - Register.PH_SETTINGS['delta']):
        Co2Logic.turn_off_ph()  #koniec gazowania

    if Register.PH_VALUE > (Register.PH_SETTINGS['value'] + Register.PH_SETTINGS['delta']):
        Co2Logic.turn_on_ph()  #gazujemy dalej

