__author__ = 'mateu'
import threading
import time


class WatchdogThread:

    def __init__(self):
        thread = threading.Thread(target=self.run, args=())
        thread.start()                                  # Start the execution

    def run(self):
        while True:
            f = open('/dev/watchdog','w')
            f.write('data')
            f.close()
            time.sleep(1)
