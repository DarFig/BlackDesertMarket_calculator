# -*- coding: utf-8 -*-

from BDOCalculator import db

db.Model.metadata.reflect(db.engine)

class Ingrediente(db.Model):
    __table__ = db.Model.metadata.tables['ingrediente']

class Objeto(db.Model):
    __table__ = db.Model.metadata.tables['objeto']

class Precio(db.Model):
    __table__ = db.Model.metadata.tables['precio']

class Proceso(db.Model):
    __table__ = db.Model.metadata.tables['proceso']

class Receta(db.Model):
    __table__ = db.Model.metadata.tables['receta']
