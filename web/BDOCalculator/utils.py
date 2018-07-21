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

def get_receta(rec_id):
    recet = Receta.query.filter(Receta.id == rec_id).first()
    return recet

def get_recetas_por_Objeto(obj_id):
    recetas = Receta.query.filter(Receta.resultado == obj_id).all()
    return recetas

def get_ingredientes_por_receta(receta_id):
    ingredientes = Ingrediente.query.filter(Ingrediente.id_receta == receta_id).all()
    return ingredientes

def get_objetos_por_receta(receta_id):
    ingredientes = get_ingredientes_por_receta(receta_id)
    objetos = []
    for i in ingredientes:
        objetos.append(Objeto.query.join(Ingrediente).add_columns(Objeto.id, Objeto.nombre, Ingrediente.cantidad).filter(Objeto.id == i.id_objeto).first())
    return objetos

def get_cantidad_por_objeto_receta(objeto_id, receta_id):
    ingrediente = Ingrediente.query.filter(Ingrediente.id_receta == receta_id, Ingrediente.id_objeto == objeto_id).first()
    return ingrediente.cantidad

def get_objetosprecio():
    objetos = Objeto.query.join(Precio).add_columns(Objeto.id,Objeto.nombre, Precio.minimo, Precio.maximo, Precio.precio1, Precio.precio2, Precio.precio3, Precio.precio4).filter(Precio.id == Objeto.id_precio).all()
    return objetos

def actualizar_precios(precio_id, maximo, minimo, prec1, prec2, prec3, prec4):
    precio = get_precio(precio_id)
    db.session.delete(precio)
    precio.maximo = maximo
    precio.minimo = minimo
    precio.precio1 = prec1
    precio.precio2 = prec2
    precio.precio3 = prec3
    precio.precio4 = prec4
    db.session.add(precio)
    db.session.commit()

def actualizar_nombre_objeto(objeto_id, nombre):
    objeto = get_object(objeto_id)
    db.session.delete(objeto)
    objeto.nombre = nombre
    db.session.add(objeto)
    db.session.commit()
