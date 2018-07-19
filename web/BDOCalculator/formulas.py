# -*- coding: utf-8 -*-

def menos_impuesto_market(precio_venta):
    return precio_venta - precio_venta * 0.35

def menosImpuesto_masValue(precio_venta):
    precio = menos_impuesto_market(precio_venta)
    return precio + precio * 0.3

def precio_profit(coste_ingrediente, precios_producto):
    precioGanancia = []
    ganancia = menos_impuesto_market(precios_producto.maximo) - coste_ingrediente
    precioGanancia.append({'precioMax' : precios_producto.maximo, 'profit' : ganancia})

    ganancia = menos_impuesto_market(precios_producto.minimo) - coste_ingrediente
    precioGanancia.append({'precioMin' : precios_producto.minimo, 'profit' : ganancia})

    ganancia = menos_impuesto_market(precios_producto.precio1) - coste_ingrediente
    precioGanancia.append({'precio1' : precios_producto.precio1, 'profit' : ganancia})

    ganancia = menos_impuesto_market(precios_producto.precio2) - coste_ingrediente
    precioGanancia.append({'precio2' : precios_producto.precio2, 'profit' : ganancia})

    ganancia = menos_impuesto_market(precios_producto.precio3) - coste_ingrediente
    precioGanancia.append({'precio3' : precios_producto.precio3, 'profit' : ganancia})

    ganancia = menos_impuesto_market(precios_producto.precio4) - coste_ingrediente
    precioGanancia.append({'precio4' : precios_producto.precio4, 'profit' : ganancia})

    return precioGanancia

def precio_profit_value(coste_ingrediente, precios_producto):
    precioGanancia = []
    ganancia = menosImpuesto_masValue(precios_producto.maximo) - coste_ingrediente
    precioGanancia.append({'precioMax' : precios_producto.maximo, 'profit' : ganancia})

    ganancia = menosImpuesto_masValue(precios_producto.minimo) - coste_ingrediente
    precioGanancia.append({'precioMin' : precios_producto.minimo, 'profit' : ganancia})

    ganancia = menosImpuesto_masValue(precios_producto.precio1) - coste_ingrediente
    precioGanancia.append({'precio1' : precios_producto.precio1, 'profit' : ganancia})

    ganancia = menosImpuesto_masValue(precios_producto.precio2) - coste_ingrediente
    precioGanancia.append({'precio2' : precios_producto.precio2, 'profit' : ganancia})

    ganancia = menosImpuesto_masValue(precios_producto.precio3) - coste_ingrediente
    precioGanancia.append({'precio3' : precios_producto.precio3, 'profit' : ganancia})

    ganancia = menosImpuesto_masValue(precios_producto.precio4) - coste_ingrediente
    precioGanancia.append({'precio4' : precios_producto.precio4, 'profit' : ganancia})

    return precioGanancia
