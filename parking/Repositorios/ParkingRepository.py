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

def darPlazaLibreTipo(parking,tipo):
    if tipo=="Turismo":
        for i in parking.turismos:
            if not i.ocupado:
                return i
    elif tipo=="Moto":
        for i in parking.motos:
            if not i.ocupado:
                return i
    else :
        for i in parking.movilidad:
            if not i.ocupado:
                return i
    return -1
