# -*- coding: utf-8 -*-
from BDOCalculator import app
from flask import render_template

from flask import request
from functools import wraps
from flask import redirect
from flask import url_for

@app.route('/')
def index():
    return render_template('_views/index.html')
