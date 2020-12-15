from Servicios import db
from Modelos import Abono, Plaza
import datetime


def buscarAbonoPorIdentificadorYpin(pin, identificador):
    abono = db.session.query(Abono.Abono).join(Plaza.Plaza).filter(
        Abono.Abono._Abono__pin == pin
    ).filter(
        Plaza.Plaza._Plaza__identificador == identificador
    ).first()
    plaza = db.session.query(Plaza.Plaza).filter(
        Plaza.Plaza._Plaza__identificador == identificador
    ).first()
    return abono, plaza


def devolverAbonos():
    return db.session.query(Abono.Abono).all()


def devolverCaducadosEnElMes(mes, anio):
    abonos = devolverAbonos()
    caducados = []
    for abono in abonos:
        fecha = abono.fechaFinal
        if fecha.year == anio and fecha.month == mes:
            caducados.append(abono)
    return caducados


def caducidadAbonoProximosDias():
    abonos = devolverAbonos()
    actual = datetime.datetime.now()
    t = datetime.timedelta(days=10)
    aux = actual + t
    caducados = []
    for abono in abonos:
        fecha = abono.fechaFinal
        if actual.year <= fecha.year <= aux.year and actual.month <= fecha.month <= aux.month and actual.day <= fecha.day <= aux.day:
            caducados.append(abono)
    return caducados
