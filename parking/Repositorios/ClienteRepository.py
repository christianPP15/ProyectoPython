from Servicios import db
from Modelos import Abono,Plaza,Clientes,Vehiculos
def pago(coste):
    print(f"El precio a pagar es de: {coste}")
    dinero=float(input("Introduce la cantidad a pagar: "))
    while dinero<coste:
        print("Error con su pago, intentelo de nuevo")
        dinero=float(input("Introduce la cantidad a pagar: "))
    print(f"Gracias por el pago, el cambio es de : {dinero-coste}")

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
