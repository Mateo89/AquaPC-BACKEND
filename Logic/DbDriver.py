import sqlite3
import threading
from Queue import *
import datetime

db_queue = Queue()

database_name = 'aquapc.db'


def save_water_temp(temp):
    conn = sqlite3.connect(database_name)
    c = conn.cursor()
    c.execute("INSERT INTO water_temps VALUES ( datetime('now','localtime'),"+str(temp)+" )")
    conn.commit()
    conn.close()


def save_light1_temp(temp):
    conn = sqlite3.connect(database_name)
    c = conn.cursor()
    c.execute("INSERT INTO light1_temps VALUES ( datetime('now','localtime'),"+str(temp)+")")
    conn.commit()
    conn.close()


def save_co2_use(date_start, date_stop, value):
    conn = sqlite3.connect(database_name)
    c = conn.cursor()
    c.execute("INSERT INTO co2_use VALUES ( ?, ?, ? )", date_start, date_stop, value)
    conn.commit()
    conn.close()


def save_o2_use(date_start, date_stop, value):
    conn = sqlite3.connect(database_name)
    c = conn.cursor()
    c.execute("INSERT INTO o2_use VALUES ( ?, ?, ? )", date_start, date_stop, value)
    conn.commit()
    conn.close()


def save_heater_use(date_start, date_stop, value):
    conn = sqlite3.connect(database_name)
    c = conn.cursor()
    c.execute("INSERT INTO heater_use VALUES ( ?, ?, ? )", date_start, date_stop, value)
    conn.commit()
    conn.close()


def save_ph_values(value):
    conn = sqlite3.connect(database_name)
    c = conn.cursor()
    c.execute("INSERT INTO ph_values VALUES ( datetime('now','localtime') ,"+str(value)+")")
    conn.commit()
    conn.close()


class DbThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while True:
            f = db_queue.get()
            f()
