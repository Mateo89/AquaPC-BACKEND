import threading

import RPi.GPIO as GPIO

import Display
import Helpers
import settings
from register import Register

# import Display
import Logic
import RestThread
import time


def main():
    GPIO.cleanup()

    settings.load_settings()

    threads = [Logic.Logic(), Display.DisplayThread(), threading.Thread(target=RestThread.run_server)]
    # threads.append(WatchdogThread.WatchdogThread())
    # threads.append(ReminderThread.ReminderThread())

    for th in threads:
        th.start()
        time.sleep(0.5)

    while len(threads) > 0:
        try:
            temp_threads = []

            for t in threads:
                if t is not None and t.isAlive():
                    t.join(0.2)
                    temp_threads.append(t)

            threads = temp_threads

            time.sleep(0.1)
        except (KeyboardInterrupt, SystemExit):
            Register.EXIT_FLAG = True

    Helpers.log("ZAPISYWANIE KONFIGURACJI")
    settings.save_settings()
    Helpers.log("ZAMYKANIE APLIKACJI")


if __name__ == "__main__":
    main()
