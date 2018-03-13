# -*- coding: utf-8 -*-
from BDOCalculator import app

from flask import render_template
from flask import request

from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, validators
from wtforms.validators import *

from ..utils import *


class LoCompramosForm(Form):
    comprar = BooleanField('comprar')

@app.route('/receta/<int:pk>/', methods=['GET'])
def recetadetails(pk):
    formulario = LoCompramosForm()
    receta = get_receta(pk)
    objetos = get_objetos_por_receta(pk)
    return render_template('_views/receta.html', receta=receta, objetos=objetos, loCompramosForm=formulario)

@app.route('/receta/<int:pk>/', methods=['POST'])
def recetacompra(pk):
    formulario = LoCompramosForm(request.form)

    #a partir de aqui no funcional, solo para la prueba||||
    receta = get_receta(pk)
    objetos = get_objetos_por_receta(pk)
    return render_template('_views/receta.html', receta=receta, objetos=objetos, loCompramosForm=formulario)
