from Repositorios import PlazaRepository
from Servicios import db
from Repositorios import PlazaRepository
from Modelos import Plaza
def ocuparPlaza(plaza):
    PlazaRepository.ocuparPlaza(plaza)
def liberarPlaza(plaza):
    PlazaRepository.liberarPlaza(plaza)

def mostrarDisponibilidad():
    turismos = db.session.query(Plaza.Plaza).filter_by(_Plaza__tipo='Turismo')
    motos = db.session.query(Plaza.Plaza).filter_by(_Plaza__tipo='Moto')
    movilidad=db.session.query(Plaza.Plaza).filter_by(_Plaza__tipo='Movilidad reducida')
    return f"Encontramos disponibles {PlazaRepository.contadorPlazasLibres(turismos)} plazas para turismo\n" \
           f"Encontramos disponibles {PlazaRepository.contadorPlazasLibres(motos)} plazas para motos\n" \
           f"Encontramos disponibles {PlazaRepository.contadorPlazasLibres(movilidad)} plazas para movilidad reducida"


def darPlazaLibreTipo(tipo):
    return PlazaRepository.darPlazaLibreTipo(tipo)

def cargarDatosInicio():
    cadena=["Turismo", "Moto", "Movilidad reducida"]
    precio=[0.12,0.08,0.10];
    for i in range(34):
        turismo=Plaza.Plaza(tipo=cadena[0],coste_minimo=precio[0],identificador='t'+str(i+1),ocupado=False,reservado=False)
        db.session.add(turismo)
    for i in range(8):
        moto=Plaza.Plaza(tipo=cadena[1],coste_minimo=precio[1],identificador='m'+str(i+1),ocupado=False,reservado=False)
        db.session.add(moto)
    for i in range(8):
        movilidad=Plaza.Plaza(tipo=cadena[2],coste_minimo=precio[2],identificador='r'+str(i+1),ocupado=False,reservado=False)
        db.session.add(movilidad)
        db.session.commit()

def reservarPlaza(plaza):
    PlazaRepository.reservarPlaza(plaza)
def desReservarPlaza(plaza):
    PlazaRepository.desReservarPlaza(plaza)

def estadoParking():
    diccionarioEstado={}
    plazas=PlazaRepository.consultarTodasLasPlazas()
    for i in plazas:
        if i.ocupado and i.reservado:
            diccionarioEstado[i.identificador]="Abono ocupado"
        elif i.reservado and not i.ocupado:
            diccionarioEstado[i.identificador]="Abono libre"
        elif not i.reservado and not i.ocupado:
            diccionarioEstado[i.identificador]="Plaza libre"
        elif not i.reservado and i.ocupado:
            diccionarioEstado[i.identificador]="Plaza ocupada"
    return diccionarioEstado
def pintarEstado(mapa):
    PlazaRepository.pintarEstado(mapa)
