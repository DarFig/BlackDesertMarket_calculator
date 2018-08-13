# -*- coding: utf-8 -*-
from BDOCalculator import app

from flask import render_template
from flask import redirect
from flask import url_for
from flask import request
from flask import make_response


from ..utils import *

from flask_wtf import FlaskForm
from wtforms import Form, StringField, IntegerField,validators
from wtforms.validators import *

class NuevoObjetoForm(Form):
    nombre = StringField('nombre')
    maximo = IntegerField('maximo')
    minimo = IntegerField('minimo')
    precio1 = IntegerField('precio1')
    precio2 = IntegerField('precio2')
    precio3 = IntegerField('precio3')
    precio4 = IntegerField('precio4')

@app.route('/<name>/<int:pk>/', methods=['GET'])
def objdetails(name, pk):
    objeto = get_object(pk)
    precio = get_precio(objeto.id_precio)
    recetas = get_recetas_por_Objeto(objeto.id)
    return render_template('_views/objeto.html', objeto=objeto, precio=precio, recetas=recetas)

@app.route('/newobject/', methods=['GET'])
def newobject():
    newobjForm = NuevoObjetoForm()
    precio = Precio()
    precio.maximo = 0
    precio.minimo = 0
    precio.precio1 = 0
    precio.precio2 = 0
    precio.precio3 = 0
    precio.precio4 = 0
    db.session.add(precio)
    db.session.commit()
    objeto = Objeto()
    objeto.nombre = "newobject"
    objeto.id_precio = precio.id
    db.session.add(objeto)
    db.session.commit()
    return render_template('_views/nuevoobjeto.html', objeto=objeto, precio=precio, newobjForm=newobjForm)


@app.route('/<int:pk>/edit/', methods=['GET', 'POST'])
def editobject(pk):
    if request.method == 'GET' :
        objeto = get_object(pk)
        precio = get_precio(objeto.id_precio)
        newobjForm = NuevoObjetoForm()
        return render_template('_views/nuevoobjeto.html', objeto=objeto, precio=precio, newobjForm=newobjForm)
    else :
        newobjForm = NuevoObjetoForm(request.form)
        objeto = get_object(pk)
        actualizar_precios(objeto.id_precio, newobjForm.data['maximo'], newobjForm.data['minimo'], newobjForm.data['precio1'],  newobjForm.data['precio2'], newobjForm.data['precio3'], newobjForm.data['precio4'])

        if objeto.nombre and objeto.nombre != newobjForm.data['nombre'] :
            actualizar_nombre_objeto(pk, newobjForm.data['nombre'])
        response = make_response(redirect(url_for('objdetails', name=objeto.nombre, pk=objeto.id)))
        return response

@app.route('/deleteObj/<int:pk>/', methods=['GET'])
def delobject(pk):
    response = make_response(redirect(url_for('index')))
    objeto = get_object(pk)
    precio = get_precio(objeto.id_precio)

    #borrar recetas donde esta el objeto
    ingredientes = get_ingredientes_por_objeto(objeto.id)
    for ingrediente in ingredientes :
        recetas = get_recetas_por_Ingrediente(ingrediente.id_receta)
        for receta in recetas :
            db.session.delete(receta)
            db.session.commit()
        #db.session.delete(ingrediente)#se borra en cascada
        #db.session.commit()


    #borrar recetas del objeto
    recetas = get_recetas_por_Objeto(objeto.id)
    for receta in recetas :
        ingredientes = get_ingredientes_por_receta(receta.id)
        for ingrediente in ingredientes :
            db.session.delete(ingrediente)
            db.session.commit()
        print(receta.id)
        db.session.delete(receta)
        db.session.commit()

    db.session.delete(precio)
    db.session.commit()

    #db.session.delete(objeto)#se elimina en cascada con su precio
    #db.session.commit()
    return response
