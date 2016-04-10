from RPLCD import cleared

import settings
from register import Register
from Helpers import LircEvents

class MainWindow:
    lcd = None
    iter = 0
    i = 0

    def __init__(self):
       self.lcd = Register.LCD

    def __del__(self):
        pass

    def event(self):
        if not Register.LIRC_EVENTS:
            return

        lirc_event = LircEvents.get_event()
        if lirc_event == LircEvents.KEY_0:
            settings.load_settings()

        if lirc_event == LircEvents.KEY_LEFT:
            self.i = self.i - 1 % 18



    def redraw_text(self):
        self.i = 0
        self.iter = 0

    def draw(self):

        if 0 <= self.iter < 20:
            if self.i == 0:
                with cleared(self.lcd):
                    self.lcd.write_string("   TEMP WODY\r\n     " + str(Register.WATER_TEMP))
                    self.lcd.home()
                    self.i += 1

        if 20 <= self.iter < 40:
            if self.i == 1:
                with cleared(self.lcd):
                    self.lcd.write_string("   TEMP LAMPY\r\n     " + str(Register.LIGHT1_TEMP))
                    self.lcd.home()
                    self.i += 1

        if 40 <= self.iter < 60:
            if self.i == 2:
                with cleared(self.lcd):
                    self.lcd.write_string(" TEMP OTOCZENIA\r\n     " + str(Register.AIR_TEMP))
                    self.lcd.home()
                    self.i += 1

        if 60 <= self.iter < 80:
            if self.i == 3:
                with cleared(self.lcd):
                    self.lcd.write_string("    pH WODY\r\n     6.5pH")
                    self.lcd.home()
                    self.i += 1

        #STAN BUTELEK

        if 80 <= self.iter < 100:
            if self.i == 4:
                with cleared(self.lcd):
                    self.lcd.write_string("STAN " +Register.BOTTLE_SETTINGS['1']['name'] + "\r\n     " + str(Register.BOTTLE_SETTINGS['1']['percent']) + '%')
                    self.lcd.home()
                    self.i += 1

        if 100 <= self.iter < 120:
            if self.i == 5:
                with cleared(self.lcd):
                    self.lcd.write_string("STAN " + Register.BOTTLE_SETTINGS['2']['name'] + "\r\n     " + str(
                        Register.BOTTLE_SETTINGS['2']['percent']) + '%')
                    self.lcd.home()
                    self.i += 1  # ostatni przypisuje na zero

        if 120 <= self.iter < 140:
            if self.i == 6:
                with cleared(self.lcd):
                    self.lcd.write_string("STAN " + Register.BOTTLE_SETTINGS['3']['name'] + "\r\n     " + str(
                        Register.BOTTLE_SETTINGS['3']['percent']) + '%')
                    self.lcd.home()
                    self.i += 1  # ostatni przypisuje na zero
        if 140 <= self.iter < 160:
            if self.i == 7:
                with cleared(self.lcd):
                    self.lcd.write_string("STAN " + Register.BOTTLE_SETTINGS['4']['name'] + "\r\n     " + str(
                        Register.BOTTLE_SETTINGS['4']['percent']) + '%')
                    self.lcd.home()
                    self.i += 1  # ostatni przypisuje na zero

        if 160 <= self.iter < 180:
            if self.i == 8:
                with cleared(self.lcd):
                    self.lcd.write_string("STAN " + Register.BOTTLE_SETTINGS['5']['name'] + "\r\n     " + str(
                        Register.BOTTLE_SETTINGS['5']['percent']) + '%')
                    self.lcd.home()
                    self.i += 1  # ostatni przypisuje na zero

        if 180 <= self.iter < 200:
            if self.i == 9:
                with cleared(self.lcd):
                    self.lcd.write_string("STAN " + Register.BOTTLE_SETTINGS['6']['name'] + "\r\n     " + str(
                        Register.BOTTLE_SETTINGS['6']['percent']) + '%')
                    self.lcd.home()
                    self.i += 1  # ostatni przypisuje na zero


        # STAN WLACZNIKOW

        if 200 <= self.iter < 220:
            if self.i == 10:
                with cleared(self.lcd):
                    self.lcd.write_string("STAN " + Register.POWERMOD_DATA[str(Register.I2C_POWERMOD_LIGHT1)]['name'] +
                                    "\r\n     " + str(Register.POWERMOD_DATA[str(Register.I2C_POWERMOD_LIGHT1)]['on']))
                    self.lcd.home()
                    self.i += 1  # ostatni przypisuje na zero

        if 220 <= self.iter < 240:
            if self.i == 11:
                with cleared(self.lcd):
                    self.lcd.write_string("STAN " + Register.POWERMOD_DATA[str(Register.I2C_POWERMOD_LIGHT2)]['name'] +
                                    "\r\n     " + str(Register.POWERMOD_DATA[str(Register.I2C_POWERMOD_LIGHT2)]['on']))
                    self.lcd.home()
                    self.i += 1  # ostatni przypisuje na zero

        if 240 <= self.iter < 260:
            if self.i == 12:
                with cleared(self.lcd):
                    self.lcd.write_string("STAN " + Register.POWERMOD_DATA[str(Register.I2C_POWERMOD_FILTER1)]['name'] +
                                    "\r\n     " + str(Register.POWERMOD_DATA[str(Register.I2C_POWERMOD_FILTER1)]['on']))
                    self.lcd.home()
                    self.i += 1  # ostatni przypisuje na zero

        if 260 <= self.iter < 280:
            if self.i == 13:
                with cleared(self.lcd):
                    self.lcd.write_string("STAN " + Register.POWERMOD_DATA[str(Register.I2C_POWERMOD_FILTER2)]['name'] +
                                    "\r\n     " + str(Register.POWERMOD_DATA[str(Register.I2C_POWERMOD_FILTER2)]['on']))
                    self.lcd.home()
                    self.i += 1  # ostatni przypisuje na zero

        if 280 <= self.iter < 300:
            if self.i == 14:
                with cleared(self.lcd):
                    self.lcd.write_string("STAN " + Register.POWERMOD_DATA[str(Register.I2C_POWERMOD_O2)]['name'] +
                                    "\r\n     " + str(Register.POWERMOD_DATA[str(Register.I2C_POWERMOD_O2)]['on']))
                    self.lcd.home()
                    self.i += 1  # ostatni przypisuje na zero

        if 300 <= self.iter < 320:
            if self.i == 15:
                with cleared(self.lcd):
                    self.lcd.write_string("STAN " + Register.POWERMOD_DATA[str(Register.I2C_POWERMOD_CO2)]['name'] +
                                    "\r\n     " + str(Register.POWERMOD_DATA[str(Register.I2C_POWERMOD_CO2)]['on']))
                    self.lcd.home()
                    self.i += 1  # ostatni przypisuje na zero

        if 340 <= self.iter < 360:
            if self.i == 16:
                with cleared(self.lcd):
                    self.lcd.write_string("STAN " + Register.POWERMOD_DATA[str(Register.I2C_POWERMOD_HEATER)]['name'] +
                                    "\r\n     " + str(Register.POWERMOD_DATA[str(Register.I2C_POWERMOD_HEATER)]['on']))
                    self.lcd.home()
                    self.i += 1  # ostatni przypisuje na zero

        if 360 <= self.iter < 380:
            if self.i == 17:
                with cleared(self.lcd):
                    self.lcd.write_string("STAN " + Register.POWERMOD_DATA[str(Register.I2C_POWERMOD_HEATER_LED)]['name'] +
                                          "\r\n     " + str(Register.POWERMOD_DATA[str(Register.I2C_POWERMOD_HEATER_LED)]['on']))
                    self.lcd.home()
                    self.i = 0  # ostatni przypisuje na zero

        self.iter += 1
        self.iter %= 380



