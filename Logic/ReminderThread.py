from register import Register
import time
import threading


class ReminderThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while True:
            f = open('/opt/aquapc/reminder.txt', 'r')
            Register.REMINDER_TEXT = f.readlines()
            f.close()
            time.sleep(600)
            if Register.EXIT_FLAG:
                return
