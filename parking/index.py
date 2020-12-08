from Servicios import PlazaServicio
from Servicios import TicketServicio
from Modelos import Ticket
from Modelos import Plaza
from Modelos import Abono
from Modelos import Vehiculos
from Modelos import Clientes
from Servicios import db
import datetime
import random
from Servicios import ClienteServicio
if __name__=='__main__':
    db.Base.metadata.drop_all(db.engine)
    db.Base.metadata.create_all(db.engine)
PlazaServicio.cargarDatosInicio()
t = datetime.timedelta(days=14, hours=4, seconds=1000)
fecha1=datetime.datetime.now()
fecha2=datetime.datetime.now()
fecha2=fecha2+t

PlazaServicio.mostrarDisponibilidad()

ClienteServicio.reservarPlaza()


#ClienteServicio.retirarVehiculo(parking,tickets)


ClienteServicio.reservarPlaza()

ClienteServicio.reservarPlaza()

ClienteServicio.reservarPlaza()
plazas=db.session.query(Plaza.Plaza).all()
for i in plazas:
    print(i)
