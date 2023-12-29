import gpiozero, requests, json, socket
from datetime import datetime

### Load in config file
get_config = open("config.json")
config_file = json.load(get_config)
get_config.close()

### Node varibles
name = config["name"]
version = config["version"]
config_type = config["type"]
serverIP = config["serverIP"]
serverPort = config["serverPort"]

### Get IP
testIP = "8.8.8.8"
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect((testIP, 0))
# myip = source ip
myip = s.getsockname()[0]
s.close()

### Button varibles
button = gpiozero.Button(2)
button_status = 0
last_button_status = 0


node_status = {"name":name, 
             "type":config_type, 
             "version":version,
             "source ip":myip
             }

while True:
    button_status = 0
    if button.is_pressed:
        button_status = 1
        # get the current time
        now = datetime.now()
        # mm/dd/YY H:M:S
        now = now.strftime("%m/%d/%Y %H:%M:%S")
    
    if button_status == 1 and last_button_status == 0:
        node_status["event"] = {
            "datetime":now,
            "type":"button",
            "ID":"btn0",
            "event":"button_pressed"
        }

        status_url = "http://" + myip + ":5000/node/status"
        status = requests.get(status_url).json()

        node_status["status"] = status['status']

        r = requests.put(serverIP + ":" + serverPort + "/event", json=node_status)
        if int(r.status_code) == 200:
            print("OK")
        else:
            print(r.status_code)
        last_button_status = 1
    if button_status == 0 and last_button_status == 1:
        last_button_status = 0