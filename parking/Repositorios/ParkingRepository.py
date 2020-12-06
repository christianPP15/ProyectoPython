from Modelos import Parking

def contadorPlazasLibres(listadoTipo):
    num=0
    for i in listadoTipo:
        if not i.ocupado:
            num+=1
    return num

def totalPlazas(parking):
    num=0
    num+=len(parking.turismos)
    num+=len(parking.movilidad)
    num+=len(parking.motos)
    return num

