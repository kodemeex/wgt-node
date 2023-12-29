# WGT-Node

## Device Description
Raspberry Pi Zero 2 W

Operating System: 32 Bit default "Raspberry PI OS" minimal with no desktop

Folder structure

main applications /home/~name~/app/wgt-node

## Setup Activity:
- Confirmed RPI was updated
    - sudo app-get update
    - sudo apt-get upgrade
      
- Established Remote access
    - SSH - On by default from OS setting

## Setup git folder
    - from /home/~name~/app
    - git clone "http://github.com/kodemeex/wgt-node"

### Test git folder

    - from /home/~name~/app/wgt-node
    - git pull "https://github.com/kodemeex/wgt-node"

## Install PIP
    - in the terminal, type
    - sudo apt install python3-pip
    - after installed, reboot the pi.

## Install gpiozero
    - in the terminal, type
    - pip install gpiozero

## Install Flask
Make sure there was a virtual enviornment

    - from /home/~name~/app
    - in the terminal, type
    - pip install Flask
    - sudo apt install python3-venv  << to install virtual enviornment >>
    - python3 -m venv app << to create the virtual enviornment called app>>
    - . app/bin/activate  << to activate the virtual enviornment >>

## Test Flask
    - from /home/~name~/app
    - in the terminal, type
    - export FLASK_APP=node.py
    - flask run --host=0.0.0.0

    - go to a browser and type,
    - http://~ip address~:5000 << i.e. http://192.168.1.111:5000 or 10.0.0.1:5000 >>
    - the website response should be "Hello, this is a node!"
