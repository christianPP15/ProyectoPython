from Servicios import db
from Modelos import Plaza
def ocuparPlaza(plaza):
    plaza.ocupado=True
    db.session.add(plaza)
    db.session.commit()
def liberarPlaza(plaza):
    plaza.ocupado=False
    db.session.add(plaza)
    db.session.commit()
def reservarPlaza(plaza):
    plaza.reservado=True
    db.session.add(plaza)
    db.session.commit()
def desReservarPlaza(plaza):
    plaza.reservado=False
    db.session.add(plaza)
    db.session.commit()
def contadorPlazasLibres(listadoTipo):
    num=0
    for i in listadoTipo:
        if not i.ocupado and not i.reservado:
            num+=1
    return num

def darPlazaLibreTipo(tipo):
    plazas_tipo=db.session.query(Plaza.Plaza).filter_by(_Plaza__tipo=tipo)
    for i in plazas_tipo:
        if not i.ocupado:
            return i
    return -1

def consultarTodasLasPlazas():
    plazas=db.session.query(Plaza.Plaza).all()
    return plazas

def pintarEstado(mapa):
    for k,v in mapa.items():
        print(k+" -> "+v)
