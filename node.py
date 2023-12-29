### This is the main code for a node in the system

import json, math
from datetime import datetime
from gpiozero import LED as GPIO
from flask import Flask, request
app = Flask(__name__)

### Load in config file
get_config = open("config.json")
config_file = json.load(get_config)
get_config.close()


nodename = config["name"]

leds = [GPIO(12),GPIO(27),GPIO(22),GPIO(6),GPIO(25)]

light_status = [{'id':'led0', 'state':leds[0].value},
                {'id':'led1', 'state':leds[1].value},
                {'id':'led2', 'state':leds[2].value},
                {'id':'led3', 'state':leds[3].value},
                {'id':'led4', 'state':leds[4].value}]

status_led = GPIO(26)
status_led.on()

@app.route('/')
def status_home():
    status = get_status()
    return status

@app.route('/node/status')
def status_res():
    status = get_status()
    return status

@app.route('/node/light')
def change_light():
    id = request.args.get('id')
    action = request.args.get('action')
    if action == "on":
        light_on(id)
    elif action == "off":
        light_off(id)
    return get_status()

# Button pressed
# send to server


# Change lights status
def light_on(_id):
    findid = _id
    if not findid.isdigit():
        findid = find_id(_id)
    leds[int(findid)].on()

def light_off(_id):
    findid = _id
    if not findid.isdigit():
        findid = find_id(_id)
    leds[int(findid)].off()

def find_id(_id):
    count = 0
    for i in light_status:
        get_light_id = i.get('id')
        if get_light_id == _id:
            new_id = count
        count += 1
        print(new_id)
    return new_id

def update_light_status():
    light_status = [{'id':'led0', 'state':leds[0].value},
                {'id':'led1', 'state':leds[1].value},
                {'id':'led2', 'state':leds[2].value},
                {'id':'led3', 'state':leds[3].value},
                {'id':'led4', 'state':leds[4].value}]
    
    return light_status

# def status, ask the pi to return current status on the machine.
def get_status():
    # get the current time
    now = datetime.now()
    # mm/dd/YY H:M:S
    now = now.strftime("%m/%d/%Y %H:%M:%S")

    # build the json file status
    curr_status = {'nodeName':nodename,
              'status': {
                  'datetime' : now,
                  'lightstatus' : update_light_status()
              }
              }
    
    return curr_status
