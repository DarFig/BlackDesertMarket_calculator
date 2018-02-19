# -*- coding: utf-8 -*-

from models import *

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

def get_objetosprecio():
    objetos = Objeto.query.join(Precio).add_columns(Objeto.nombre, Precio.minimo, Precio.maximo, Precio.precio1, Precio.precio2, Precio.precio3, Precio.precio4).filter(Precio.id == Objeto.id_precio).all()
    return objetos
