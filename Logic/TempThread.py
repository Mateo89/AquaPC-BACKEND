__author__ = 'mateu'
import threading
import time
import DbDriver
from subprocess import Popen, PIPE
import datetime

from register import Register


class TempThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):

        counter = 0
        water_temp_sum = 0
        water_temp_count = 0
        water_temp = 0

        light1_temp_sum = 0
        light1_temp_count = 0
        light1_temp = 0

        while True:
            process = Popen(["/root/read-temp.sh"], stdout=PIPE)
            (output, err) = process.communicate()
            process.wait()

            lines = output.split('\n')
            try:
                float(lines[0])
                float(lines[1])
            except ValueError:
                continue

            water_temp = float(lines[0])/1000
            light1_temp = float(lines[1])/1000

            Register.WATER_TEMP = water_temp
            Register.LIGHT1_TEMP = light1_temp

            Register.WATER_TEMP_UPDATE_DATE = str(datetime.datetime.now().replace(microsecond=0))
            Register.LIGHT1_TEMP_UPDATE_DATE = str(datetime.datetime.now().replace(microsecond=0))


            water_temp_sum += water_temp
            water_temp_count += 1
            light1_temp_sum += light1_temp
            light1_temp_count += 1

            counter += 1

            counter += 1
            if counter == 10:

            # wyliczenie sredniej z 5 min i przeslanie do bazy
                water_5min_avg = water_temp_sum / water_temp_count
                light1_5min_avg = light1_temp_sum / light1_temp_count

                DbDriver.db_queue.put(lambda: DbDriver.save_water_temp(water_5min_avg))
                DbDriver.db_queue.put(lambda: DbDriver.save_light1_temp(light1_5min_avg))

                counter = 0
                water_temp_sum = 0
                water_temp_count = 0
                water_temp = 0
                light1_temp_sum = 0
                light1_temp_count = 0
                light1_temp = 0

            for x in range(0, 30):
                time.sleep(1)
                if Register.EXIT_FLAG:
                    return


