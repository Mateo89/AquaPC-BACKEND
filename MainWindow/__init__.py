import settings
from Display.BarTile import BarTile
from Helpers import Colors
from Helpers.Coordinate import Coordinate
from MainWindow.AirTemp import AirTemp
from MainWindow.BottleTile import BottleTile
from MainWindow.Co2Switch import Co2Switch
from MainWindow.FanLedSwitch import FanLedSwitch
from MainWindow.FeederSwitch import FeedSwitch
from MainWindow.Filtr1Switch import Filtr1Switch
from MainWindow.Filtr2Switch import Filtr2Switch
from MainWindow.HeaterLedSwitch import HeaterLedSwitch
from MainWindow.HeaterSwitch import HeaterSwitch
from MainWindow.Lamp1Switch import Lamp1Switch
from MainWindow.Lamp2Switch import Lamp2Switch
from MainWindow.LedTemp import LedTemp
from MainWindow.LightModeTile import LigthModeTile
from MainWindow.O2Switch import O2Switch
from MainWindow.PhTile import PhTile
from MainWindow.ReminderTile import ReminderTile
from MainWindow.WaterTemp import WaterTemp
from register import Register
from Helpers import LircEvents

class MainWindow:
    lcd = None

    redraw_labels = True
    waterTemp = None
    airTemp = None
    barTile = None
    phTile = None
    ledTemp = None
    reminderTile = None

    lightModeTile = None

    bottle1tile = None
    bottle2tile = None
    bottle3tile = None
    bottle4tile = None
    bottle5tile = None
    bottle6tile = None
    bottle7tile = None
    bottle8tile = None


    # przelaczniki
    lamp1Switch = None
    lamp2Switch = None
    heaterLedSwitch = None
    fanLedSwitch = None
    filtr1Switch = None
    filtr2Switch = None
    o2Switch = None
    co2Switch = None
    feederSwitch = None
    heaterSwitch = None

    def __init__(self):
        self.lcd = Register.LCD
        self.lcd.fill(Colors.BLACK)

        self.barTile = BarTile(Coordinate(0, 0, 400, 25),"HOME","home25.png")

        self.waterTemp = WaterTemp(Coordinate(0, 30, 140, 40))
        self.airTemp = AirTemp(Coordinate(0, 75, 140, 40))
        self.ledTemp = LedTemp(Coordinate(0, 120, 140, 40))

        self.phTile = PhTile(Coordinate(0, 165, 140, 40))

        self.reminderTile = ReminderTile(Coordinate(0, 210, 400, 30))
        self.lightModeTile = LigthModeTile(Coordinate(142, 30, 70, 70))

        self.bottle1tile = BottleTile(Coordinate(373, 30, 20, 70), 'bottle1')
        self.bottle2tile = BottleTile(Coordinate(350, 30, 20, 70), 'bottle2')
        self.bottle3tile = BottleTile(Coordinate(327, 30, 20, 70), 'bottle3')
        self.bottle4tile = BottleTile(Coordinate(304, 30, 20, 70), 'bottle4')
        self.bottle5tile = BottleTile(Coordinate(281, 30, 20, 70), 'bottle5')
        self.bottle6tile = BottleTile(Coordinate(258, 30, 20, 70), 'bottle6')
        self.bottle7tile = BottleTile(Coordinate(235, 30, 20, 70), 'bottle7')
        self.bottle8tile = BottleTile(Coordinate(212, 30, 20, 70), 'bottle8')

        # przelaczniki

        # 1 linia
        self.lamp1Switch = Lamp1Switch(Coordinate(142, 103, 50, 50))
        self.heaterLedSwitch = HeaterLedSwitch(Coordinate(194, 103, 50, 50))
        self.filtr1Switch = Filtr1Switch(Coordinate(246, 103, 50, 50))
        self.o2Switch = O2Switch(Coordinate(298, 103, 50, 50))
        self.feederSwitch = FeedSwitch(Coordinate(350, 103, 50, 50))

        # 2 linia
        self.lamp2Switch = Lamp2Switch(Coordinate(142, 155, 50, 50))
        self.fanLedSwitch = FanLedSwitch(Coordinate(194, 155, 50, 50))
        self.filtr2Switch = Filtr2Switch(Coordinate(246, 155, 50, 50))
        self.co2Switch = Co2Switch(Coordinate(298, 155, 50, 50))
        self.heaterSwitch = HeaterSwitch(Coordinate(350, 155, 50, 50))

    def __del__(self):
        print 'usuniecie main window'
        self.lcd = None

    def event(self):
        if not Register.LIRC_EVENTS:
            return

        lirc_event = LircEvents.get_event()
        if lirc_event == LircEvents.KEY_0:
            settings.load_settings()

    def draw(self):
        self.lcd.fill(Colors.BLACK)
        self.barTile.draw_tile()
        self.waterTemp.draw_tile()
        self.phTile.draw_tile()
        self.airTemp.draw_tile()
        self.ledTemp.draw_tile()
        self.reminderTile.draw_tile()
        self.lightModeTile.draw()

        if Register.BOTTLE_MOD['bottle1']['ON']:
            self.bottle1tile.draw()

        if Register.BOTTLE_MOD['bottle2']['ON']:
            self.bottle2tile.draw()

        if Register.BOTTLE_MOD['bottle3']['ON']:
            self.bottle3tile.draw()

        if Register.BOTTLE_MOD['bottle4']['ON']:
            self.bottle4tile.draw()

        if Register.BOTTLE_MOD['bottle5']['ON']:
            self.bottle5tile.draw()

        if Register.BOTTLE_MOD['bottle6']['ON']:
            self.bottle6tile.draw()

        if Register.BOTTLE_MOD['bottle7']['ON']:
            self.bottle7tile.draw()

        if Register.BOTTLE_MOD['bottle8']['ON']:
            self.bottle8tile.draw()

        self.lamp1Switch.draw()
        self.lamp2Switch.draw()
        self.heaterLedSwitch.draw()
        self.fanLedSwitch.draw()
        self.filtr1Switch.draw()
        self.filtr2Switch.draw()
        self.o2Switch.draw()
        self.co2Switch.draw()
        self.feederSwitch.draw()
        self.heaterSwitch.draw()
