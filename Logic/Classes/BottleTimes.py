
class BottleTimes():
    name = ""
    on = True
    fromTime = "10:30"
    toTime = "18:30"
    day_of_week = 0

    def __init__(self,day_of_week,on,fromTime,toTime):
        self.day_of_week = day_of_week
        self.on = on
        self.fromTime = fromTime
        self.toTime = toTime
