from Servicios import db,PlazaServicio,ClienteServicio
from Modelos import Abono,Clientes,Vehiculos,Factura
from Repositorios import AbonoRepository
import datetime
import random
def AltaAbono(opcion,tipo,nombre,apellidos,dni,matricula,email,tarjeta):
    plazaReservada=PlazaServicio.darPlazaLibreTipo(tipo)
    PlazaServicio.reservarPlaza(plazaReservada)
    mes,precio,fechaFinal=switchMeses(opcion)
    abono=Abono.Abono(fechaInicial=datetime.datetime.now(),fechaFinal=fechaFinal,pin=random.randint(111111,999999),meses=mes,precio=precio,plaza=plazaReservada)
    vehiculoNuevo=Vehiculos.Vehiculos(matricula=matricula,tipo=tipo)
    cliente=Clientes.Cliente(nombre=nombre,apellidos=apellidos,vehiculo=vehiculoNuevo,abono=abono,dni=dni,email=email,tarjeta=tarjeta)
    factura=Factura.Factura(fechaCreacion=datetime.datetime.now(),cliente=cliente,coste=precio)
    db.session.add(factura)
    db.session.add(vehiculoNuevo)
    db.session.add(cliente)
    db.session.add(plazaReservada)
    db.session.add(abono)
    db.session.commit()
    return abono.pin
def switchMeses(opcion):
    actual=datetime.datetime.now()
    mes=None
    mesesSumar=0
    precio=None
    fechaFinal=None
    if opcion==1:
        mes=1
        precio=25
        if actual.month+1>12:
            fechaFinal=actual.replace(month=1,year=actual.year+1)
        else:
            fechaFinal=actual.replace(month=actual.month+1)
    elif opcion==2:
        mes=3
        precio=70
        if actual.month+3>12:
            mesesSumar=(actual.month+3)-12
            fechaFinal=actual.replace(month=mesesSumar,year=actual.year+1)
        else:
            fechaFinal=actual.replace(month=actual.month+3)
    elif opcion==3:
        mes=6
        precio=130
        if actual.month+6>12:
            mesesSumar=(actual.month+6)-12
            fechaFinal=actual.replace(month=mesesSumar,year=actual.year+1)
        else:
            fechaFinal=actual.replace(month=actual.month+6)
    elif opcion==4:
        mes=12
        precio=200
        fechaFinal=actual.replace(year=actual.year+1)
    else:
        print("Opción no valida")
    return mes, precio,fechaFinal


def borrarAbono(pin,identificador):
    abono,plaza=AbonoRepository.buscarAbonoPorIdentificadorYpin(pin,identificador.lower())
    if plaza:
        if abono:
            PlazaServicio.desReservarPlaza(plaza)
            PlazaServicio.liberarPlaza(plaza)
            db.session.add(plaza)
            db.session.delete(abono)
            db.session.commit()
            return "Se ha completado de forma satisfactoria"
        else:
            return "Error con la el pin de la plaza"
    else:
        return "Error con el identificador de la plaza"

def edicionCliente(dni_antiguo,matricula_antigua,nombre,apellidos,dni,matricula,email,tarjeta):
    cliente=ClienteServicio.buscarClientePorDniMatricula(dni_antiguo,matricula_antigua)
    if cliente!=None:
        cliente.vehiculo.matricula=matricula
        cliente.tarjeta=tarjeta
        cliente.nombre=nombre
        cliente.apellidos=apellidos
        cliente.email=email
        cliente.dni=dni
        db.session.add(cliente)
        db.session.commit()
        return True
    else:
        return False

def edicionAbono(dni,matricula,pin,opcion):
    cliente=ClienteServicio.buscarClientePorDniPinMatricula(dni,matricula,pin)
    if cliente!=None:
        abono=cliente.abono
        mes,precio,fechaFinal=switchMeses(opcion)
        abono.precio=precio
        abono.meses=mes
        abono.fechaFinal=fechaFinal
        db.session.add(abono)
        db.session.commit()
        return True
    else:
        return False

def caducidadAbonoMes(mes,anio):
    caducados=AbonoRepository.devolverCaducadosEnElMes(mes,anio)
    clientes=[]
    for i in caducados:
        clientes.append(ClienteServicio.buscarClientePorAbono(i))
    cadena=""
    cadena+="Caduca el abono de los siguientes clientes\n"
    cadena+="---------------------------------------------------\n"
    for i in clientes:
        cadena+="Nombre y apellidos "+i.nombre+ " "+i.apellidos+ " y con DNI "+i.dni+"\n"
    cadena+="---------------------------------------------------\n"
    return cadena

def caducidadAbonoProximos10Dias():
    caducados=AbonoRepository.caducidadAbonoProximosDias()
    clientes=[]
    for i in caducados:
        clientes.append(ClienteServicio.buscarClientePorAbono(i))
    cadena=""
    cadena+="Caduca el abono de los siguientes clientes\n"
    cadena+="---------------------------------------------------\n"
    for i in clientes:
        cadena+=("Nombre y apellidos "+i.nombre+ " "+i.apellidos+"\n")
    cadena+="---------------------------------------------------\n"
    return cadena

