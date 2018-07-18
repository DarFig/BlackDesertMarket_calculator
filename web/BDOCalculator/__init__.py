# -*- coding: utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__) #create the application instance

import sys

# revisión de la versión
if sys.version[0] == '2' :
    #2.7.x
    import io
    with io.open("configFile.txt", encoding="utf-8") as confFile:
        data_base_uri = confFile.readline()
        data_base_uri = data_base_uri.split()[1]
else:
    #3.x.x
    with open("configFile.txt", encoding="utf-8") as confFile:
        data_base_uri = confFile.readline()
        data_base_uri = data_base_uri.split()[1]


app.config['SQLALCHEMY_DATABASE_URI'] = data_base_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

import BDOCalculator.views
