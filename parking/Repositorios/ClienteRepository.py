from Servicios import db
from Modelos import Abono,Plaza,Clientes,Vehiculos


def listaClientes():
    return db.session.query(Clientes.Cliente).all()
def buscarClientePorAbono(abono):
    clientes=listaClientes()
    for i in clientes:
        if i.abono==abono:
            return i

def buscarClientePorDniMatricula(dni,matricula):
    return db.session.query(Clientes.Cliente).join(Vehiculos.Vehiculos).filter(
    Clientes.Cliente._Cliente__dni==dni
).filter(
    Vehiculos.Vehiculos._Vehiculos__matricula==matricula
).first()

def buscarClientePorDniPinMatricula(dni,matricula,pin):
    return db.session.query(Clientes.Cliente).join(Vehiculos.Vehiculos).join(Abono.Abono).filter(
    Clientes.Cliente._Cliente__dni==dni
).filter(
    Vehiculos.Vehiculos._Vehiculos__matricula==matricula
).filter(
        Abono.Abono._Abono__pin==pin
    ).first()
