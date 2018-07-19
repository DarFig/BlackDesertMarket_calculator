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



@app.route('/receta/<int:pk>/', methods=['GET'])
def recetadetails(pk, lista=[]):
    receta = get_receta(pk)
    objetos = get_objetos_por_receta(pk)

    return render_template('_views/receta.html', receta=receta, objetos=objetos, listaDlistaPrecioGanancia=lista)

@app.route('/receta/<int:pk>/', methods=['POST'])
def recetacompra(pk):
    objetos = get_objetos_por_receta(pk)
    precios_producto = get_precio(get_object(get_receta(pk).resultado).id_precio)
    formulario = request.form
    coste_max = 0
    coste_min = 0
    coste_1 = 0
    coste_2 = 0
    coste_3 = 0
    coste_4 = 0
    for key, value  in formulario.items():
        if value == "on" :
            precio = get_precio(key) #precios del ingrediente
            coste_max += precio.maximo * get_cantidad_por_objeto_receta(key, pk)
            coste_min += precio.minimo * get_cantidad_por_objeto_receta(key, pk)
            coste_1 += precio.precio1 * get_cantidad_por_objeto_receta(key, pk)
            coste_2 += precio.precio2 * get_cantidad_por_objeto_receta(key, pk)
            coste_3 += precio.precio3 * get_cantidad_por_objeto_receta(key, pk)
            coste_4 += precio.precio4 * get_cantidad_por_objeto_receta(key, pk)
    #toman lista de duplas precio : profit para todos los precios de venta
    listaDlistaPrecioGanancia = []
    listaDlistaPrecioGanancia.append(precio_profit(coste_max, precios_producto))
    listaDlistaPrecioGanancia.append(precio_profit(coste_min, precios_producto))
    listaDlistaPrecioGanancia.append(precio_profit(coste_1, precios_producto))
    listaDlistaPrecioGanancia.append(precio_profit(coste_2, precios_producto))
    listaDlistaPrecioGanancia.append(precio_profit(coste_3, precios_producto))
    listaDlistaPrecioGanancia.append(precio_profit(coste_4, precios_producto))



    #a partir de aqui no funciona, solo para la prueba
    receta = get_receta(pk)
    response = make_response(redirect(url_for('recetadetails', pk=pk, lista=listaDlistaPrecioGanancia)))
    return response
