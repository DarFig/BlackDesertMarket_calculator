# -*- coding: utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__) #create the application instance


app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://bdocalculator:bdocalculator@localhost/bdocalculator"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

import BDOCalculator.views
