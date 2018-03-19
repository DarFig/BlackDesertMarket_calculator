# -*- coding: utf-8 -*-
from BDOCalculator import app

from flask import render_template
from flask import request
from flask import make_response
from flask import redirect
from flask import url_for

from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, validators
from wtforms.validators import *

from ..utils import *
from ..formulas import is_profit

#class LoCompramosForm(Form):
#    comprar = BooleanField('comprar')

@app.route('/receta/<int:pk>/', methods=['GET'])
def recetadetails(pk):
    receta = get_receta(pk)
    objetos = get_objetos_por_receta(pk)
    #formulario = {}
    #for i in objetos:
        #formulario[i.id] = LoCompramosForm()
        #print formulario[i.id]
    return render_template('_views/receta.html', receta=receta, objetos=objetos)

@app.route('/receta/<int:pk>/', methods=['POST'])
def recetacompra(pk):
    objetos = get_objetos_por_receta(pk)
    precios_producto = get_precio(get_object(get_receta(pk).resultado))
    formulario = request.form
    coste_max = 0
    coste_min = 0
    coste_1 = 0
    coste_2 = 0
    coste_3 = 0
    coste_4 = 0
    for i in formulario:
        precio = get_precio(i) #precios del objetos
        coste_max += precio.maximo
        coste_min += precio.minimo
        coste_1 += precio.precio1
        coste_2 += precio.precio2
        coste_3 += precio.precio3
        coste_4 += precio.precio4
    #toman el valor de si es profit
    coste_max = is_profit(coste_max, precios_producto)
    coste_min =  is_profit(coste_min, precios_producto)
    coste_1 =  is_profit(coste_1, precios_producto)
    coste_2 =  is_profit(coste_2, precios_producto)
    coste_3 =  is_profit(coste_3, precios_producto)
    coste_4 =  is_profit(coste_4, precios_producto)

    #a partir de aqui no funcional, solo para la prueba|||
    #hay que devolver los que son profit
    receta = get_receta(pk)
    response = make_response(redirect(url_for('recetadetails', pk=pk)))
    return response
