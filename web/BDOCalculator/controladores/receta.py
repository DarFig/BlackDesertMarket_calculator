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
from ..formulas import precio_profit
from ..formulas import precio_profit_value


@app.route('/receta/<int:pk>/', methods=['GET'])
def recetadetails(pk):
    receta = get_receta(pk)
    objetos = get_objetos_por_receta(pk)
    lista = []
    return render_template('_views/receta.html', receta=receta, objetos=objetos, listaDlistaPrecioGanancia=lista)

@app.route('/receta/<int:pk>/', methods=['POST'])
def recetacompra(pk):
    receta = get_receta(pk)
    objetos = get_objetos_por_receta(pk)
    precios_producto = get_precio(get_object(get_receta(pk).resultado).id_precio)
    formulario = request.form
    coste_max = 0
    coste_min = 0
    for key, value  in formulario.items():
        if value == "on" :
            costes = get_precio(key) #precios del ingrediente
            coste_max += costes.maximo * get_cantidad_por_objeto_receta(key, pk)
            coste_min += costes.minimo * get_cantidad_por_objeto_receta(key, pk)
    #toman lista de duplas precio : profit para todos los precios de venta
    listaDlistaPrecioGanancia = []
    listaDlistaPrecioGanancia.append(precio_profit(coste_max, precios_producto))
    listaDlistaPrecioGanancia.append(precio_profit(coste_min, precios_producto))

    #con precio_profit_value
    listaDlistaPrecioGanancia.append(precio_profit_value(coste_max, precios_producto))
    listaDlistaPrecioGanancia.append(precio_profit_value(coste_min, precios_producto))

    return render_template('_views/receta.html', receta=receta, objetos=objetos, listaDlistaPrecioGanancia=listaDlistaPrecioGanancia)
