from Servicios import PlazaServicio,AbonoServicio,TicketServicio,ClienteServicio
from Modelos import Ticket,Plaza,Abono,Vehiculos,Clientes
from Servicios import db
import datetime
if __name__=='__main__':
    #db.Base.metadata.drop_all(db.engine)
    db.Base.metadata.create_all(db.engine)
#PlazaServicio.cargarDatosInicio()
t = datetime.timedelta(days=14, hours=4, seconds=1000)
fecha1=datetime.datetime.now()
fecha2=datetime.datetime.now()
fecha2=fecha2+t
salirVal=False
salirValAdmin=False
case=15000
def switch(case):
    if case==1:
       ClienteServicio.reservarPlaza()
    elif case==2:
        ClienteServicio.retirarVehiculo()
    elif case==5:
        while case>=1:
            case=int(input("\n\nMenú Administración introduce una opción"
                           "\n1.Estado del parking"
                           "\n2.Facturación"
                           "\n3.Consulta abonados"
                           "\n4.Administración abonados"
                           "\n5.Caducidad abonos"
                           "\n0.Salir"))
            switchAdmin(case)
    elif case==0:
        print("Saliendo...")
    else:
        case=9000
        print("Error, opción no valida")

def switchAdmin(case):
    if case==1:
        PlazaServicio.pintarEstado(PlazaServicio.estadoParking())
    elif case==2:
        pass
    elif case==3:
        while case >=1:
            case=int(input("\n\nOpciones abonados"
                           "\n1.Alta abonados"
                           "\n2.Edición abonados"
                           "\n3.Borrar abonados"
                           "\n0.Salir"))
            switchAbonos(case)
    elif case==4:
        pass
    elif case==5:
        pass
    elif case==0:
        print("Volviendo al menú principal...")
    else:
        case=9000
        print("Error opción no valida")
def switchAbonos(case):
    if case==1:
        AbonoServicio.AltaAbono()
    elif case==2:
        pass
    elif case==3:
        AbonoServicio.borrarAbono()
    elif case==4:
        abonos=db.session.query(Abono.Abono).all()
        for i in abonos:
            print(i)
    elif case==0:
        print("Volviendo al menú de administración")
    else:
        case=9000
        print("Error, opción no valida")
while case>=1:
    PlazaServicio.mostrarDisponibilidad()
    case=int(input("\n\nIntroduce la opción"
               "\n1.Guardar Vehículo"
               "\n2.Retirar Vehículo"
                   "\n5.Administración"
                   "\n0.Salir"))
    switch(case)


print("Gracias por contar con nosotros")

