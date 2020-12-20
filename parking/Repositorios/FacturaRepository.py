from Servicios import db
from Modelos import Factura


def devolverFacturas():
    return db.session.query(Factura.Factura).all()

def facturasAnio(anio):
    facturas=devolverFacturas()
    facturasAni=[]
    for i in facturas:
        if i.fechaCreacion.year==int(anio):
            facturasAni.append(i)
    return facturasAni
