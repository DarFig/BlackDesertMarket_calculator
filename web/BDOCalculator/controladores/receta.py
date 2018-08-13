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

from wtforms import Form, StringField, IntegerField,validators

class NuevaRecetaForm(Form):
    ingrediente1 = StringField('ingrediente1')
    ingrediente2 = StringField('ingrediente2')
    ingrediente3 = StringField('ingrediente3')
    ingrediente4 = StringField('ingrediente4')
    cantidad1 = IntegerField('cantidad1')
    cantidad2 = IntegerField('cantidad2')
    cantidad3 = IntegerField('cantidad3')
    cantidad4 = IntegerField('cantidad4')
    proceso = StringField('proceso')
    nota = StringField('nota')

@app.route('/receta/<int:pk>/', methods=['GET'])
def recetadetails(pk):
    receta = get_receta(pk)
    objetos = []
    if receta :
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

@app.route('/newrecipe/<int:resultID>/', methods=['GET','POST'])
def newrecipe(resultID):
    if request.method == 'GET' :
        newrectForm = NuevaRecetaForm()
        objetos = get_objetos()
        procesos = get_procesos()
        return render_template('_views/nuevareceta.html', objetos=objetos, procesos=procesos, newrectForm=newrectForm, resultID=resultID)
    else:
        newrectForm = NuevaRecetaForm(request.form)
        proceso = get_proceso_por_nombre(newrectForm.data['proceso'])
        receta = Receta()
        receta.nota = newrectForm.data['nota']
        receta.resultado = resultID
        receta.proceso = proceso.id
        db.session.add(receta)
        db.session.commit()

        if newrectForm.data['ingrediente1'] != '------' :
            ingrediente1 = Ingrediente()
            ingrediente1.id_receta = receta.id
            ingrediente1.id_objeto = get_object_by_name(newrectForm.data['ingrediente1']).id
            ingrediente1.cantidad = newrectForm.data['cantidad1']
            db.session.add(ingrediente1)
            db.session.commit()
        if newrectForm.data['ingrediente2'] != '------' :
            ingrediente2 = Ingrediente()
            ingrediente2.id_receta = receta.id
            ingrediente2.id_objeto = get_object_by_name(newrectForm.data['ingrediente2']).id
            ingrediente2.cantidad = newrectForm.data['cantidad2']
            db.session.add(ingrediente2)
            db.session.commit()
        if newrectForm.data['ingrediente3'] != '------' :
            ingrediente3 = Ingrediente()
            ingrediente3.id_receta = receta.id
            ingrediente3.id_objeto = get_object_by_name(newrectForm.data['ingrediente3']).id
            ingrediente3.cantidad = newrectForm.data['cantidad3']
            db.session.add(ingrediente3)
            db.session.commit()
        if newrectForm.data['ingrediente4'] != '------' :
            ingrediente4 = Ingrediente()
            ingrediente4.id_receta = receta.id
            ingrediente4.id_objeto = get_object_by_name(newrectForm.data['ingrediente4']).id
            ingrediente4.cantidad = newrectForm.data['cantidad4']
            db.session.add(ingrediente4)
            db.session.commit()
        response = make_response(redirect(url_for('recetadetails', pk=receta.id)))
        return response

@app.route('/deleteReceta/<int:recetaID>/<int:resultID>/', methods=['GET'])
def delRecipe(recetaID, resultID):
    objeto = get_object(resultID)
    response = make_response(redirect(url_for('objdetails', name=objeto.nombre, pk=objeto.id)))

    receta = get_receta(recetaID)

    ingredientes = get_ingredientes_por_receta(receta.id)
    for ingrediente in ingredientes :
        db.session.delete(ingrediente)
        db.session.commit()
        
    db.session.delete(receta)
    db.session.commit()

    return response
