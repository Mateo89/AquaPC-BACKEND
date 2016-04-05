from register import Register

def light_mode_logic():

    percent = 0

    if Register.I2C_POWERMOD_LIGHT1_FLAG and  (Register.LIGHT1_PERCENT > percent):
        percent = Register.LIGHT1_PERCENT

    if Register.I2C_POWERMOD_LIGHT2_FLAG and (Register.LIGHT2_PERCENT > percent):
        percent = Register.LIGHT2_PERCENT

    if 20 <= percent <= 40:
        Register.LIGHT_MODE = 1

    if percent < 20:
        Register.LIGHT_MODE = 0

    if percent > 40:
        Register.LIGHT_MODE = 2