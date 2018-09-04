#!/bin/bash

sudo apt-get install python-mysqldb
sudo pip install virtualenv
sudo apt-get install python-virtualenv
virtualenv venv
. venv/bin/activate
pip install -r requirements.txt
