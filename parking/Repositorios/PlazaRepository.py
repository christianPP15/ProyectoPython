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
def contadorPlazasLibres(listadoTipo):
    num=0
    for i in listadoTipo:
        if not i.ocupado:
            num+=1
    return num

def darPlazaLibreTipo(tipo):
    plazas_tipo=db.session.query(Plaza.Plaza).filter_by(_Plaza__tipo=tipo)
    for i in plazas_tipo:
        if not i.ocupado:
            return i
    return -1



