from flask import Flask
from flask_cors import CORS
import threading
import time

import settings
from Helpers import PowerModHelper
from Logic import BottleLogic
from register import Register

from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/api/state/water')
def state_water_get():
    return jsonify({"warning": Register.WATER_SETTINGS['warning'], "temp": Register.WATER_TEMP})


@app.route('/api/state/air')
def state_air_get():
    return jsonify({'temp': Register.AIR_TEMP})


@app.route('/api/state/lamp')
def state_lamp_get():
    return jsonify({'warning': Register.POWERMOD_DATA[str(Register.I2C_POWERMOD_LIGHT1)]['warning'],
                    'temp': Register.LIGHT1_TEMP})


@app.route('/api/state/ph')
def state_ph_get():
    return jsonify({'warning': False, 'value': 6.5})


@app.route('/api/state/bottle')
def state_bottle_get():

    data = []
    for bottle in sorted(Register.BOTTLE_SETTINGS.viewkeys()):
        data.append({
            "name": Register.BOTTLE_SETTINGS[bottle]['name'],
            "percent": Register.BOTTLE_SETTINGS[bottle]['percent'],
            "alert": Register.BOTTLE_SETTINGS[bottle]['alert']
        })
    return jsonify({'data': data})


@app.route('/api/state/switches', methods=['GET'])
def state_switches_get():

    data = []
    for switch in sorted(Register.POWERMOD_DATA.viewkeys()):
        data.append({
            "id": int(switch),
            "name": Register.POWERMOD_DATA[switch]['name'],
            "override": Register.POWERMOD_DATA[switch]['override'],
            "on": Register.POWERMOD_DATA[switch]['on'],
            "img": Register.POWERMOD_DATA[switch]['img']
        })

    return jsonify({'data': data})


@app.route('/api/state/logs', methods=['GET'])
def state_log_get():
    data = Register.LOGS_EVENTS
    return jsonify({'data': data})


@app.route('/api/state/logs', methods=['DELETE'])
def state_log_delete():
    Register.LOGS_EVENTS = []
    return jsonify({'data': None})


@app.route('/api/settings/lamp/<int:index>/times', methods=['GET'])
def settings_lamptimes_get(index):
    iter = Register.LAMPS_SETTINGS[str(index)]['times']
    return jsonify({'data': sorted(iter, key=lambda x: x['day_of_week'])})


@app.route('/api/settings/lamp/<int:index>/times', methods=['PUT'])
def settings_lamptimes_put(index):
    ids = str(index)

    Register.LAMPS_SETTINGS[ids]['times'] = request.json
    print Register.LAMPS_SETTINGS[ids]
    settings.save_lamp()
    return settings_lamptimes_get(index)


@app.route('/api/settings/lamp/<int:index>/state', methods=['GET'])
def settings_lampstate_get(index):

    ids = str(index)

    data = {
        'on': Register.LAMPS_SETTINGS[ids]['on'],
        'water_change_on': Register.LAMPS_SETTINGS[ids]['water_change_on'],
        'use_heater_on': Register.LAMPS_SETTINGS[ids]['use_heater_on'],
        'use_heater_delta': Register.LAMPS_SETTINGS[ids]['use_heater_delta']
    }
    return jsonify({'data': data})


@app.route('/api/settings/lamp/<int:index>/state', methods=['PUT'])
def settings_lampstate_put(index):
    ids = str(index)
    Register.LAMPS_SETTINGS[ids]['use_heater_on'] = request.json['use_heater_on']
    Register.LAMPS_SETTINGS[ids]['on'] = request.json['on']
    Register.LAMPS_SETTINGS[ids]['use_heater_delta'] = request.json['use_heater_delta']
    Register.LAMPS_SETTINGS[ids]['water_change_on'] = request.json['water_change_on']
    settings.save_lamp()
    return settings_lampstate_get(index)


@app.route('/api/settings/water', methods=['GET'])
def settings_water_get():
    return jsonify({'temp': Register.WATER_SETTINGS['temp']})


@app.route('/api/settings/water', methods=['PUT'])
def settings_water_put():
    Register.WATER_SETTINGS['temp'] = request.json['temp']
    settings.save_water()
    return settings_water_get()


@app.route('/api/settings/heater', methods=['GET'])
def settings_heater_get():

    data = {
        'on': Register.HEATER_SETTINGS['on'],
        'water_change_off': Register.HEATER_SETTINGS['water_change_off'],
        'delta': Register.HEATER_SETTINGS['delta']
    }
    return jsonify({'data': data})


@app.route('/api/settings/heater', methods=['PUT'])
def settings_heater_put():
    Register.HEATER_SETTINGS['on'] = request.json['on']
    Register.HEATER_SETTINGS['water_change_off'] = request.json['water_change_off']
    Register.HEATER_SETTINGS['delta'] = request.json['delta']

    settings.save_heater()
    return settings_heater_get()


@app.route('/api/settings/pomp/<int:index>/times', methods=['GET'])
def settings_pomp_times_get(index):
    data = Register.BOTTLE_SETTINGS[str(index)]['times']
    return jsonify({'data': sorted(data, key=lambda x: x['day_of_week'])})


@app.route('/api/settings/pomp/<int:index>/times', methods=['PUT'])
def settings_pomp_times_put(index):

    Register.BOTTLE_SETTINGS[str(index)]['times'] = request.json
    settings.save_bottle()
    return settings_pomp_times_get(index)


@app.route('/api/settings/pomp/<int:index>/state', methods=['GET'])
def settings_pomp_state_get(index):

    ids = str(index)
    data = {
        'name': Register.BOTTLE_SETTINGS[ids]['name'],
        'on': Register.BOTTLE_SETTINGS[ids]['on'],
        'ml_per_sec': Register.BOTTLE_SETTINGS[ids]['ml_per_sec'],
        'ppm_per_ml': Register.BOTTLE_SETTINGS[ids]['ppm_per_ml'],
        'capacity': Register.BOTTLE_SETTINGS[ids]['capacity'],
        'state': Register.BOTTLE_SETTINGS[ids]['state'],
        'percent': Register.BOTTLE_SETTINGS[ids]['percent']
    }
    return jsonify({'data': data})


@app.route('/api/settings/pomp/<int:index>/state', methods=['PUT'])
def settings_pomp_state_put(index):
    ids = str(index)

    Register.BOTTLE_SETTINGS[ids]['name'] = request.json['name']
    Register.BOTTLE_SETTINGS[ids]['on'] = request.json['on']
    Register.BOTTLE_SETTINGS[ids]['ml_per_sec'] = float(request.json['ml_per_sec'])
    Register.BOTTLE_SETTINGS[ids]['ppm_per_ml'] = float(request.json['ppm_per_ml'])
    Register.BOTTLE_SETTINGS[ids]['capacity'] = int(request.json['capacity'])

    settings.save_bottle()
    return settings_pomp_state_get(index)


@app.route('/api/settings/pomp/<int:index>/dose', methods=['GET'])
def settings_pomp_dose_get(index):
    return jsonify({'dose': Register.BOTTLE_MANUAL_DOSE})


@app.route('/api/settings/filter/<int:index>/state', methods=['GET'])
def settings_filter_state(index):
    data = Register.FILTER_SETTINGS[str(index)]
    return jsonify({'data': data})


@app.route('/api/settings/filter/<int:index>/state', methods=['PUT'])
def settings_filter_state_put(index):
    Register.FILTER_SETTINGS[str(index)] = request.json
    settings.save_filter()
    return settings_filter_state(index)


@app.route('/api/settings/co2/times', methods=['GET'])
def settings_co2_times_get():
    data = Register.CO2_SETTINGS['times']
    return jsonify({'data': sorted(data, key=lambda x: x['day_of_week'])})


@app.route('/api/settings/co2/times', methods=['PUT'])
def settings_co2_times_put():
    Register.CO2_SETTINGS['times'] = request.json
    settings.save_co2()
    return settings_co2_times_get()


@app.route('/api/settings/co2/state', methods=['GET'])
def settings_co2_state_get():
    data = {
        'on': Register.CO2_SETTINGS['on'],
        'full_day': Register.CO2_SETTINGS['full_day'],
        'water_change_off': Register.CO2_SETTINGS['water_change_off']
    }
    return jsonify({'data': data})


@app.route('/api/settings/co2/state', methods=['PUT'])
def settings_co2_state_put():

    Register.CO2_SETTINGS['on'] = request.json['on']
    Register.CO2_SETTINGS['full_day'] = request.json['full_day']
    Register.CO2_SETTINGS['water_change_off'] = request.json['water_change_off']

    settings.save_co2()
    return settings_co2_state_get()


@app.route('/api/settings/o2/times', methods=['GET'])
def settings_o2_times_get():

    data = Register.O2_SETTINGS['times']
    return jsonify({'data': sorted(data, key=lambda x: x['day_of_week'])})


@app.route('/api/settings/o2/times', methods=['PUT'])
def settings_o2_times_put():
    Register.O2_SETTINGS['times'] = request.json
    settings.save_o2()
    return settings_o2_times_get()


@app.route('/api/settings/o2/state', methods=['GET'])
def settings_o2_state_get():
    data = {
        'on': Register.O2_SETTINGS['on'],
        'full_day': Register.O2_SETTINGS['full_day'],
        'water_change_off': Register.O2_SETTINGS['water_change_off']
    }
    return jsonify({'data': data})


@app.route('/api/settings/o2/state', methods=['PUT'])
def settings_o2_state_put():
    Register.O2_SETTINGS['on'] = request.json['on']
    Register.O2_SETTINGS['full_day'] = request.json['full_day']
    Register.O2_SETTINGS['water_change_off'] = request.json['water_change_off']
    return settings_o2_state_get()


########################################################
##
##              ACTIONS
##
########################################################
# wl/wyl przelacznika
@app.route('/api/actions/switches/<int:index>', methods=['PUT'])
def state_switches_put(index):

    #ids = str(index)
    PowerModHelper.toggle_switch(index)
    PowerModHelper.override_switch(index)
    return state_switches_get()


# zdejmowanie overrride dla przelacznikow
@app.route('/api/actions/switches', methods=['DELETE'])
def state_switches_delete():

    if request.json is None:
        for switch in Register.POWERMOD_DATA.viewkeys():
            PowerModHelper.remove_override_switch(switch)
    else:
        PowerModHelper.remove_override_switch(request.json)

    return state_switches_get()


@app.route('/api/actions/pomp/<int:index>/refill', methods=['PUT'])
def actions_pomp_refill_put(index):
    BottleLogic.refill_bottle(index)
    return settings_pomp_state_get(index)


@app.route('/api/actions/pomp/<int:index>/dose', methods=['PUT'])
def actions_pomp_dose_put(index):
    BottleLogic.dose_from_bottle(str(index), request.json)
    return settings_pomp_dose_get(index)


def run_server():
    app.run(debug=True, use_reloader=False)