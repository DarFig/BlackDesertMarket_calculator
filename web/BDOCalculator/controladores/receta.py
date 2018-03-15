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
    formulario = request.form
    print formulario
    for i in formulario:
        print i

    #a partir de aqui no funcional, solo para la prueba||||
    receta = get_receta(pk)
    response = make_response(redirect(url_for('recetadetails', pk=pk)))
    return response
