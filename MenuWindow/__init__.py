from Display import DisplayRegister
from Display.BarTile import BarTile
from Helpers import Colors
from Helpers.Coordinate import Coordinate
from MainWindow import MainWindow
from MenuWindow.LightWindow import LightWindow
from register import Register
from Helpers import LircEvents
from MenuTile import MenuTile


class MenuWindow():

    barTile =None
    selecedIndex = 0
    tiles = []


    def __init__(self):
        self.lcd = Register.LCD
        self.barTile = BarTile(Coordinate(0, 0, 400, 25),"MENU","home25.png")

        self.tiles.append(MenuTile(Coordinate(15, 40, 180, 90),'light32.png',"Lampy"))
        self.tiles.append(MenuTile(Coordinate(205, 40, 180, 90),'pump32.png',"Dozownik"))
        self.tiles.append(MenuTile(Coordinate(15, 140, 180, 90),'switch32.png',"Wlacznik"))
        self.tiles.append(MenuTile(Coordinate(205, 140, 180, 90),'settings32.png',"Ustawienia"))

        self.tiles[self.selecedIndex].select()

    def __del__(self):
        self.tiles = None

    def event(self):
        if not Register.LIRC_EVENTS:
            return

        lirc_event = LircEvents.get_event()
        if lirc_event == LircEvents.KEY_BACK:
            self.tiles[self.selecedIndex].select()
            DisplayRegister.set_mainWindow()

        if lirc_event == LircEvents.KEY_RIGHT:
            self.tiles[self.selecedIndex].unselect()
            self.selecedIndex = (self.selecedIndex + 1) % 4
            self.tiles[self.selecedIndex].select()

        if lirc_event == LircEvents.KEY_LEFT:
            self.tiles[self.selecedIndex].unselect()
            self.selecedIndex = (self.selecedIndex - 1) % 4
            self.tiles[self.selecedIndex].select()

        if lirc_event == LircEvents.KEY_UP:
            self.tiles[self.selecedIndex].unselect()
            self.selecedIndex = (self.selecedIndex - 2) % 4
            self.tiles[self.selecedIndex].select()

        if lirc_event == LircEvents.KEY_DOWN:
            self.tiles[self.selecedIndex].unselect()
            self.selecedIndex = (self.selecedIndex + 2) % 4
            self.tiles[self.selecedIndex].select()

        if lirc_event == LircEvents.KEY_OK:
            if self.selecedIndex == 0:
                DisplayRegister.set_lightWindow()
            if self.selecedIndex == 1:
                DisplayRegister.set_bottleWindow()
            if self.selecedIndex == 2:
                DisplayRegister.set_switchWindow()
            if self.selecedIndex == 3:
                DisplayRegister.set_settingsWindow()

    def draw(self):

        self.lcd.fill(Colors.BLACK)
        self.barTile.draw_tile()

        for tile in self.tiles:
            tile.draw()
