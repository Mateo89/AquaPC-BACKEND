from register import Register

DISPLAY_REGISTER = dict(
    mainWindow=None,
    menuWindow=None,
    lightWindow=None,
    settingsWindow=None,
    bottleWindow=None,
    switchWindow=None,
    light1SettingsWindow=None,
    light2SettingsWindow=None,
    bottleSettingsWindow=None,
    heaterSettingWindow=None
)


def set_mainWindow():
    if not DISPLAY_REGISTER['mainWindow']:
        from MainWindow import MainWindow
        DISPLAY_REGISTER['mainWindow'] = MainWindow()
    Register.CURRENT_SCREEN = DISPLAY_REGISTER['mainWindow']
    Register.CURRENT_SCREEN.redraw_text()


def set_menuWindow():
    if not DISPLAY_REGISTER['menuWindow']:
        from MenuWindow import MenuWindow
        DISPLAY_REGISTER['menuWindow'] = MenuWindow()
    Register.CURRENT_SCREEN = DISPLAY_REGISTER['menuWindow']
    Register.CURRENT_SCREEN.redraw_text()


def set_lightWindow():
    if not DISPLAY_REGISTER['lightWindow']:
        from MenuWindow import LightWindow
        DISPLAY_REGISTER['lightWindow'] = LightWindow()
    Register.CURRENT_SCREEN = DISPLAY_REGISTER['lightWindow']


def set_bottleWindow():
    if not DISPLAY_REGISTER['bottleWindow']:
        from MenuWindow import BottleWindow
        DISPLAY_REGISTER['bottleWindow'] = BottleWindow.BottleWindow()
    Register.CURRENT_SCREEN = DISPLAY_REGISTER['bottleWindow']


def set_switchWindow():
    if not DISPLAY_REGISTER['switchWindow']:
        from MenuWindow import SwitchWindow
        DISPLAY_REGISTER['switchWindow'] = SwitchWindow.SwitchWindow()
    Register.CURRENT_SCREEN = DISPLAY_REGISTER['switchWindow']
    Register.CURRENT_SCREEN.redraw_text()


def set_settingsWindow():
    if not DISPLAY_REGISTER['settingsWindow']:
        from MenuWindow import SettingsWindow
        DISPLAY_REGISTER['settingsWindow'] = SettingsWindow.SettingsWindow()
    Register.CURRENT_SCREEN = DISPLAY_REGISTER['settingsWindow']


def set_light1_settings_window():
    if not DISPLAY_REGISTER['light1SettingsWindow']:
        from MenuWindow import Light1Settings
        DISPLAY_REGISTER['light1SettingsWindow'] = Light1Settings.Light1SettingWindow()
    Register.CURRENT_SCREEN = DISPLAY_REGISTER['light1SettingsWindow']
    Register.CURRENT_SCREEN.redraw_text()


def set_light2_settings_window():
    if not DISPLAY_REGISTER['light2SettingsWindow']:
        from MenuWindow import Light2Settings
        DISPLAY_REGISTER['light2SettingsWindow'] = Light2Settings.Light2SettingWindow()
    Register.CURRENT_SCREEN = DISPLAY_REGISTER['light2SettingsWindow']
    Register.CURRENT_SCREEN.redraw_text()


def set_bottle_settings_window():
    if not DISPLAY_REGISTER['bottleSettingsWindow']:
        from MenuWindow import BottleSettings
        DISPLAY_REGISTER['bottleSettingsWindow'] = BottleSettings.BottleSettingWindow()
    Register.CURRENT_SCREEN = DISPLAY_REGISTER['bottleSettingsWindow']


def set_heater_settings_window():
    if not DISPLAY_REGISTER['heaterSettingWindow']:
        from MenuWindow import HeateSettings
        DISPLAY_REGISTER['heaterSettingWindow'] = HeateSettings.HeaterSettingWindow()
    Register.CURRENT_SCREEN = DISPLAY_REGISTER['heaterSettingWindow']

