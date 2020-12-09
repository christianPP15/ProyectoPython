from Servicios import db,PlazaServicio,ClienteServicio
from Modelos import Abono,Clientes,Vehiculos,Factura
from Repositorios import AbonoRepository
import datetime
import random
def AltaAbono():
    meses={"1.Mensual":"25€","2.Trimestral":"70€","3.Semestral":"130€","4.Anual":"200€"}
    for k,v in meses.items():
        print(k+" -> "+v)
    opcion=int(input("Elige una opción(1-4)"))
    while opcion>4 or opcion<0:
        opcion=int(input("Elige una opción(1-4)"))
    print("Indica el tipo de plaza que desea")
    tipo=int(input("1.Turismo\t"
           "2.Motocicleta\t"
           "3.Movilidad reducida"))
    while tipo>3 or tipo<=0:
        tipo=int(input("1.Turismo\t"
           "2.Motocicleta\t"
           "3.Movilidad reducida"))
    if tipo==1:
        tipo="Turismo"
    elif tipo==2:
        tipo="Moto"
    else:
        tipo="Movilidad reducida"
    plazaReservada=PlazaServicio.darPlazaLibreTipo(tipo)
    PlazaServicio.reservarPlaza(plazaReservada)
    mes,precio,fechaFinal=switchMeses(opcion)
    abono=Abono.Abono(fechaInicial=datetime.datetime.now(),fechaFinal=fechaFinal,pin=random.randint(111111,999999),meses=mes,precio=precio,plaza=plazaReservada)
    nombre=input("Introduzca su nombre")
    apellidos=input("Introduzca sus apellidos")
    dni=input("Introduzca su dni")
    matricula=input("Introduzca la matricula de su vehículo")
    email=input("Introduzca su email")
    tarjeta=input("Introduzca su tarjeta de crédito")
    vehiculoNuevo=Vehiculos.Vehiculos(matricula=matricula,tipo=tipo)
    cliente=Clientes.Cliente(nombre=nombre,apellidos=apellidos,vehiculo=vehiculoNuevo,abono=abono,dni=dni,email=email,tarjeta=tarjeta)
    factura=Factura.Factura(fechaCreacion=datetime.datetime.now(),cliente=cliente,coste=precio)
    db.session.add(factura)
    db.session.add(vehiculoNuevo)
    db.session.add(cliente)
    db.session.add(plazaReservada)
    db.session.add(abono)
    db.session.commit()

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
    elif opcion==200:
        mes=12
        precio=200
        fechaFinal=actual.replace(year=actual.year+1)
    else:
        print("Opción no valida")
    return mes, precio,fechaFinal


def borrarAbono():
    pin=input("Introduce el pin asignada a la plaza")
    identificadorPlaza=input("Introduce el identificador de la plaza")
    abono,plaza=AbonoRepository.buscarAbonoPorIdentificadorYpin(pin,identificadorPlaza)
    if plaza:
        if abono:
            PlazaServicio.desReservarPlaza(plaza)
            PlazaServicio.liberarPlaza(plaza)
            db.session.add(plaza)
            db.session.delete(abono)
            db.session.commit()
            print("Se ha completado de forma satisfactoria")
        else:
            print("Error con la el pin de la plaza")
    else:
        print("Error con el identificador de la plaza")

def edicionCliente():
    nombre=input("Introduzca su nombre")
    apellidos=input("Introduzca sus apellidos")
    dni=input("Introduzca su dni")
    matricula=input("Introduzca la matricula de su vehículo")
    email=input("Introduzca su email")
    tarjeta=input("Introduzca su tarjeta de crédito")
    cliente=ClienteServicio.buscarClientePorDniMatricula(dni,matricula)
    cliente.vehiculo.matricula=matricula
    cliente.tarjeta=tarjeta
    cliente.nombre=nombre
    cliente.apellidos=apellidos
    cliente.email=email
    cliente.dni=dni
    db.session.add(cliente)
    db.session.commit()
    print("Edición llevada a cabo correctamente")

def edicionAbono():
    dni=input("Introduzca su dni")
    matricula=input("Introduzca la matricula de su vehículo")
    pin=input("Introduzca su pin")
    cliente=ClienteServicio.buscarClientePorDniPinMatricula(dni,matricula,pin)
    abono=cliente.abono
    meses={"1.Mensual":"25€","2.Trimestral":"70€","3.Semestral":"130€","4.Anual":"200€"}
    for k,v in meses.items():
        print(k+" -> "+v)
    opcion=int(input("Elige una opción(1-4)"))
    while opcion>4 or opcion<0:
        opcion=int(input("Elige una opción(1-4)"))
    mes,precio,fechaFinal=switchMeses(opcion)
    abono.precio=precio
    abono.meses=mes
    abono.fechaFinal=fechaFinal

def caducidadAbonoMes():
    mes=int(input("Mes a comprobar: "))
    anio=int(input("Año a comprobar: "))
    caducados=AbonoRepository.devolverCaducadosEnElMes(mes,anio)
    clientes=[]
    for i in caducados:
        clientes.append(ClienteServicio.buscarClientePorAbono(i))
    print("Caduca el abono de los siguientes clientes")
    print("---------------------------------------------------")
    for i in clientes:
        print("Nombre y apellidos "+i.nombre+ " "+i.apellidos+ " y con DNI "+i.dni)
    print("---------------------------------------------------")

def caducidadAbonoProximos10Dias():
    caducados=AbonoRepository.caducidadAbonoProximosDias()
    clientes=[]
    for i in caducados:
        clientes.append(ClienteServicio.buscarClientePorAbono(i))
    print("Caduca el abono de los siguientes clientes")
    print("---------------------------------------------------")
    for i in clientes:
        print("Nombre y apellidos "+i.nombre+ " "+i.apellidos)
    print("---------------------------------------------------")

