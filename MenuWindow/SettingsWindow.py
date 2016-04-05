from Display import DisplayRegister
from Display.BarTile import BarTile
from Helpers import Colors
from Helpers.Coordinate import Coordinate
from MenuWindow import MenuTile
from register import Register
from Helpers import LircEvents


class SettingsWindow():

    lcd = None

    barTile =None
    selectedIndex = 0
    tiles = []

    def __init__(self):
        self.lcd = Register.LCD
        self.barTile = BarTile(Coordinate(0, 0, 400, 25),"Ustawienia","settings25.png")

        self.tiles.append(MenuTile(Coordinate(15, 40, 180, 90),'light32.png',"Lampa 1"))
        self.tiles.append(MenuTile(Coordinate(205, 40, 180, 90),'pump32.png',"Dozownik"))
        self.tiles.append(MenuTile(Coordinate(15, 140, 180, 90),'light32.png',"Lampa 2"))
        self.tiles.append(MenuTile(Coordinate(205, 140, 180, 90),'heater32.png',"Grzalka"))

        self.tiles[self.selectedIndex].select()

    def event(self):
        if not Register.LIRC_EVENTS:
            return

        lirc_event = LircEvents.get_event()
        if lirc_event == LircEvents.KEY_BACK:
            self.tiles[self.selectedIndex].select()
            DisplayRegister.set_menuWindow()

        if lirc_event == LircEvents.KEY_RIGHT:
            self.tiles[self.selectedIndex].unselect()
            self.selectedIndex = (self.selectedIndex + 1) % 4
            self.tiles[self.selectedIndex].select()

        if lirc_event == LircEvents.KEY_LEFT:
            self.tiles[self.selectedIndex].unselect()
            self.selectedIndex = (self.selectedIndex - 1) % 4
            self.tiles[self.selectedIndex].select()

        if lirc_event == LircEvents.KEY_UP:
            self.tiles[self.selectedIndex].unselect()
            self.selectedIndex = (self.selectedIndex - 2) % 4
            self.tiles[self.selectedIndex].select()

        if lirc_event == LircEvents.KEY_DOWN:
            self.tiles[self.selectedIndex].unselect()
            self.selectedIndex = (self.selectedIndex + 2) % 4
            self.tiles[self.selectedIndex].select()

        if lirc_event == LircEvents.KEY_OK:
            if self.selectedIndex == 0:
                DisplayRegister.set_light1_settings_window()
            if self.selectedIndex == 1:
                DisplayRegister.set_bottle_settings_window()
            if self.selectedIndex == 2:
                DisplayRegister.set_light2_settings_window()
            if self.selectedIndex == 3:
                DisplayRegister .set_heater_settings_window()

    def draw(self):

        self.lcd.fill(Colors.BLACK)
        self.barTile.draw_tile()

        for tile in self.tiles:
            tile.draw()

