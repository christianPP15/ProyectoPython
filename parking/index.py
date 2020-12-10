from Servicios import PlazaServicio,AbonoServicio,TicketServicio,ClienteServicio,FacturaServicio
from Modelos import Ticket,Plaza,Abono,Vehiculos,Clientes
from Controller import IndiceController
from Servicios import db
from tkinter import *
import datetime
if __name__=='__main__':
    db.Base.metadata.drop_all(db.engine)
    db.Base.metadata.create_all(db.engine)
PlazaServicio.cargarDatosInicio()


root=Tk()
root.title("Gestión Parking")
root.iconbitmap("img/icono.ico")
root.resizable(True,True)
root.geometry("800x400")
#root.config(bg="grey")
# frame=Frame(root)
# frame.pack(side=LEFT,
#            anchor=N,
#            fill="x",
#            expand=1)#Existe fill y ocupa todo alto, y anchor S se situa debajo, expand=1
#Para usar fill x necesitamos usar expand 1/True si usamos y no
# frame.config(bg="blue"
#              ,width=200
#              ,height=100
#              ,relief="groove"
#              ,bd=5)#otra opcion es sunken
IndiceController.indice(root)



root.mainloop()
#agregar una w a la extesion .py-> .pyw para que se ejecute sin consola


