#!/bin/bash
cd /home/erika/app/zero2/
git pull https://github.com/erikashby/zero2
cd /home/erika/app/
. app/bin/activate
cd /home/erika/app/zero2/
export FLASK_APP=mainnode.py
flask run --host=0.0.0.0


