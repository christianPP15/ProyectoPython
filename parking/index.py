from Modelos import Parking
from Servicios import ParkingServicio
from Servicios import PlazaServicio
from Servicios import TicketServicio
from Modelos import  Ticket
from Modelos import Vehiculos
from Servicios import db
import datetime
from Servicios import ClienteServicio
def run():
    pass
if __name__=='__main__':
    db.Base.metadata.create_all(db.engine)
    run()
parking=Parking.Parking()
tickets=[]
ParkingServicio.mostrarDisponibilidad(parking)


#ClienteServicio.reservarPlaza(parking,tickets)


#ClienteServicio.retirarVehiculo(parking,tickets)
t = datetime.timedelta(days=14, hours=4, seconds=1000)
fecha1=datetime.datetime.now()
fecha2=datetime.datetime.now()
fecha2=fecha2+t



