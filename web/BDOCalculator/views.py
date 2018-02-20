# -*- coding: utf-8 -*-
from BDOCalculator import app
from flask import render_template

from utils import *
from flask import request
from functools import wraps
from flask import redirect
from flask import url_for



from controladores.objeto import *

@app.route('/')
@app.route('/', methods=['GET'])
def index():
    lista = get_objetosprecio()
    return render_template('_views/index.html', objetos=lista)
