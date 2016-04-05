__author__ = 'mateu'
from register import Register
import Helpers
import time
import lirc
import threading
from Helpers import LircEvents


class LircThread(threading.Thread):

    lirc_socket = None

    def __init__(self):
        threading.Thread.__init__(self)
        self.lirc_socket = lirc.init("aquapc", blocking=False)

    def run(self):
        while True:

            codeIR = lirc.nextcode()
            if codeIR:
                event = codeIR[0]

                if event == LircEvents.KEY_POWER:
                    Register.EXIT_FLAG = True
                else:
                    Register.LIRC_EVENTS = event
                    #Helpers.log("dodanie lirc event : " + event)

            if Register.EXIT_FLAG:
                break
            time.sleep(0.05)

