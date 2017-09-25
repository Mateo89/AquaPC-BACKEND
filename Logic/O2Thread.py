import threading
import time
import O2Logic
import datetime
from register import Register


class O2Thread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while True:

            if Register.POWERMOD_DATA[str(Register.I2C_POWERMOD_O2)]['override']:
                time_now = datetime.datetime.now()
                if time_now < Register.POWERMOD_DATA_OVERRIDE[str(Register.I2C_POWERMOD_O2)]['override_time']:
                    return
                else:
                    O2Logic.unblock_o2()

            if not Register.O2_SETTINGS['on']:
                O2Logic.turn_off()
                continue

            if Register.CHANGE_WATER_MODE:
                if Register.O2_SETTINGS['water_change_off']:
                    O2Logic.turn_off()
                    continue

            time.sleep(20)

            if Register.O2_SETTINGS['full_day']:
                O2Logic.turn_on()
            else:
                # wlaczamy na okdres 5 min
                O2Logic.turn_on()
                time.sleep(300)
                O2Logic.turn_off()
                time.sleep(300)
