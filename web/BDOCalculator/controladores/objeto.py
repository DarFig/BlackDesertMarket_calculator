# -*- coding: utf-8 -*-
from BDOCalculator import app
from flask import render_template


from ..utils import *

@app.route('/<name>/<int:pk>/', methods=['GET'])
def objdetails(name, pk):
    objeto = get_object(pk)
    precio = get_precio(objeto.id_precio)
    recetas = get_recetas_por_Objeto(objeto.id)
    return render_template('_views/objeto.html', objeto=objeto, precio=precio, recetas=recetas)
