from Servicios import PlazaServicio,AbonoServicio,TicketServicio,ClienteServicio,FacturaServicio
from Modelos import Ticket,Plaza,Abono,Vehiculos,Clientes
from Controller import IndiceController
from Servicios import db
from tkinter import *
import datetime


#db.Base.metadata.drop_all(db.engine)
db.Base.metadata.create_all(db.engine)
#PlazaServicio.cargarDatosInicio()


root=Tk()
root.title("Gestión Parking")
root.iconbitmap("img/icono.ico")
root.resizable(True,True)
root.geometry("800x400")

IndiceController.indice(root)

root.mainloop()



