# -*- coding: utf-8 -*-

from model import *

def get_object_by_name(name):
    objt = Objeto.query.filter(Objeto.nombre == name).first()
    return objt

def get_object(obj_id):
    objt = Objeto.query.filter(Objeto.id == obj_id).first()
    return objt

def get_precio(precio_id):
    prec = Precio.query.filter(Precio.id == precio_id).first()
    return prec

def get_proceso_name(proc_id):
    proc = Proceso.query.filter(Proceso.id == proc_id).first()
    return proc

def get_recetas_por_Objeto(obj_id):
    recetas = Receta.query.filter(Receta.resultado == obj_id).all()
    return recetas

def get_ingredientes_por_receta(receta_id):
    ingredientes = Ingrediente.query.filter(Ingrediente.receta == receta_id).all()
    return ingredientes
