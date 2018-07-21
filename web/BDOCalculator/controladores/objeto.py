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
    return render_template('_views/nuevoobjeto.html', newobjForm=newobjForm)

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
