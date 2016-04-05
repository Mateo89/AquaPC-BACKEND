from BottleTimes import *


class Bottle():
    on = False
    num = -1
    capacity = 500
    name = ""
    state = 0
    percent = 0
    dose = 0
    dosed = False
    sec_per_ml = 0

    times = []

    def __init__(self):
        self.times.append(BottleTimes(1,True,"10:20","20:20"))
