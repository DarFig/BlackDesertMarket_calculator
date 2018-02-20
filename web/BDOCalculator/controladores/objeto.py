# -*- coding: utf-8 -*-
from BDOCalculator import app
from flask import render_template


from ..utils import *

@app.route('/<name>/<int:pk>/', methods=['GET'])
def objdetails(name, pk):
    objeto = get_object(pk)
    return render_template('_views/objeto.html', objeto=objeto)
