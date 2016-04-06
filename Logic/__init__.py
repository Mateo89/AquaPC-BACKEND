__author__ = 'mateu'

from TempThread import TempThread
#from LircThread import LircThread
#import lirc
import threading
import time
import Helpers
from datetime import datetime
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

import math


class Logic(threading.Thread):

    i2c_bus = None

    tempThread = None
   #lircThread = None
    light1Thread = None
    light2Thread = None

    def __init__(self):
        threading.Thread.__init__(self)
        self.tempThread = TempThread()
        self.tempThread.start()

        time.sleep(0.5)
        #self.lircThread = LircThread()
        #self.lircThread.start()

        self.light1Thread = Light1Logic.Light1Thread()
        self.light1Thread.start()

        self.light2Thread = Light2Logic.Light2Thread()
        self.light2Thread.start()

        PowerModHelper.update_data()

    def run(self):

        while True:
            if Register.EXIT_FLAG:
                if not self.tempThread.isAlive():
                    if not self.lircThread.isAlive():
                        PowerModHelper.reset()
                        break
                continue

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
