__author__ = 'mateu'
from register import Register
import time
import threading
from subprocess import Popen, PIPE

class WaterTempThread:

    def __init__(self):
        thread = threading.Thread(target=self.run, args=())
        thread.start()                                  # Start the execution

    def run(self):
        while True:
            process = Popen(["/root/DS18B20V2", "16"], stdout=PIPE)
            (output, err) = process.communicate()
            process.wait()

            temp = float(output)
            Register.water_temp = temp
            time.sleep(1)
