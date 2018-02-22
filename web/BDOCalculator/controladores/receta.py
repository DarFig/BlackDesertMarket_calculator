# -*- coding: utf-8 -*-
from BDOCalculator import app

from flask import render_template


from ..utils import *


@app.route('/<int:pk>/', methods=['GET'])
def recetadetails(pk):
    receta = get_receta(pk)
    ingredientes = get_ingredientes_por_receta(pk)
    return render_template('_views/receta.html', receta=receta, ingredientes=ingredientes)
