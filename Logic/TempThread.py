__author__ = 'mateu'
from register import Register
import time
import threading
from subprocess import Popen, PIPE


class TempThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while True:
            process = Popen(["/root/DS18B20-read", "16", "6"], stdout=PIPE)
            (output, err) = process.communicate()
            process.wait()

            lines = output.split('\n')
            try:
                float(lines[0])
                float(lines[1])
            except ValueError:
                continue

            Register.WATER_TEMP = float(lines[0])
            Register.AIR_TEMP = float(lines[1])

            for x in range(0, 30):
                time.sleep(1)
                if Register.EXIT_FLAG:
                    return
