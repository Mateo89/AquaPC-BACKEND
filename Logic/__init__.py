from Logic.LircThread import LircThread

__author__ = 'mateu'

from TempThread import TempThread
from LircThread import LircThread
import threading
import time
from register import Register
from Helpers import PowerModHelper

from Logic import Light1Logic
from Logic import Light2Logic
from Logic import WaterTempLogic
from Logic import Co2Logic
from Logic import O2Logic
from Logic import Filter1Logic
from Logic import Filter2Logic
from Logic import LightModeLogic
from Logic import BottleLogic


class Logic(threading.Thread):

    i2c_bus = None

    threads = []

    def __init__(self):
        threading.Thread.__init__(self)

        self.threads.append(TempThread())
        self.threads.append(LircThread())

        self.threads.append(Light1Logic.Light1Thread())
        self.threads.append(Light2Logic.Light2Thread())
        self.threads.append(BottleLogic.BottleThread())

        PowerModHelper.update_data()

    def run(self):

        for th in self.threads:
            th.start()
            time.sleep(0.5)

        while True:
            if Register.EXIT_FLAG:
                temp_threads = []

                for t in self.threads:
                    if t is not None and t.isAlive():
                        t.join(0.1)
                        temp_threads.append(t)

                threads = temp_threads

            # glowna czesc

            Light1Logic.light1_logic()
            Light2Logic.light2_logic()
            WaterTempLogic.water_temp_logic()

            Co2Logic.co2_logic()
            O2Logic.o2_logic()
            Filter1Logic.filter1_logic()
            Filter2Logic.filter2_logic()

            LightModeLogic.light_mode_logic()
            time.sleep(0.2)
