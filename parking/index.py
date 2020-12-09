from Servicios import PlazaServicio,AbonoServicio,TicketServicio,ClienteServicio,FacturaServicio
from Modelos import Ticket,Plaza,Abono,Vehiculos,Clientes
from Servicios import db
import datetime
if __name__=='__main__':
    #db.Base.metadata.drop_all(db.engine)
    db.Base.metadata.create_all(db.engine)
#PlazaServicio.cargarDatosInicio()

salirVal=False
salirValAdmin=False
case=15000

def switch(case):
    if case==1:
       ClienteServicio.reservarPlaza()
    elif case==2:
        ClienteServicio.retirarVehiculo()
    elif case==3:
        ClienteServicio.depositarAbonados()
    elif case==4:
        ClienteServicio.retirarAbono()
    elif case==5:
        while case!=0:
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
        TicketServicio.facturacion()
    elif case==3:
        FacturaServicio.calcularFacturasAnio()
    elif case==4:
        while case !=0:
            case=int(input("\n\nOpciones abonados"
                           "\n1.Alta abonados"
                           "\n2.Edición abonados"
                           "\n3.Borrar abonados"
                           "\n0.Salir"))
            switchAbonos(case)
    elif case==5:
        while case !=0:
            case=int(input("\n\nOpciones caducidad"
                           "\n1.Caducidad abono en un mes"
                           "\n2.Caducidad en los proximos 10 días"
                           "\n0.Salir"))
            switchCaducidad(case)

    elif case==0:
        print("Volviendo al menú principal...")
    else:
        case=9000
        print("Error opción no valida")
def switchCaducidad(case):
    if case==1:
        AbonoServicio.caducidadAbonoMes()
    elif case==2:
        AbonoServicio.caducidadAbonoProximos10Dias()
    elif case==0:
        print("Saliendo al menu de administración")
    else:
        print("Opción no valida")
def switchAbonos(case):
    if case==1:
        AbonoServicio.AltaAbono()
    elif case==2:
        while case !=0:
            case=int(input("\n\nOpciones edición"
                           "\n1.Edición usuario"
                           "\n2.Extender abono"
                           "\n0.Salir"))
            switchEdicion(case)
    elif case==3:
        AbonoServicio.borrarAbono()
    elif case==0:
        print("Volviendo al menú de administración")
    else:
        case=9000
        print("Error, opción no valida")
def switchEdicion(case):
    if case==1:
        AbonoServicio.edicionCliente()
    elif case==2:
        AbonoServicio.edicionAbono()
    elif case==0:
        print("Volviendo al menú de abonos")
    else:
        print("Error, opción no valida")
while case>=1:
    PlazaServicio.mostrarDisponibilidad()
    case=int(input("\n\nIntroduce la opción"
               "\n1.Guardar Vehículo"
               "\n2.Retirar Vehículo"
                   "\n3.Guardar Vehículo Abonado"
                   "\n4.Retirar Vehículo Abonado"
                   "\n5.Administración"
                   "\n0.Salir"))
    switch(case)


print("Gracias por contar con nosotros")

