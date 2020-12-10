from Servicios import PlazaServicio,AbonoServicio,TicketServicio,ClienteServicio,FacturaServicio
from Modelos import Ticket,Plaza,Abono,Vehiculos,Clientes
from Controller import ClienteController
from Servicios import db
from tkinter import *
import datetime
if __name__=='__main__':
    #db.Base.metadata.drop_all(db.engine)
    db.Base.metadata.create_all(db.engine)
#PlazaServicio.cargarDatosInicio()


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
frame_informacion_parking=Frame(root,
                         width=500,
                         height=100,
                         bd=3,
                         relief="groove")
frame_informacion_parking.pack()
textoInformacion=Label(frame_informacion_parking,foreground="black",text=PlazaServicio.mostrarDisponibilidad())
textoInformacion.pack()

botonGuardarVehiculo=Button(root,
                        text="Guardar vehículo",
                        command=lambda:ClienteController.guardarVehiculo(root,botonGuardarVehiculo,botonRetirarVehiculo),
                        width=50,
                        height=5)
botonGuardarVehiculo.pack()
botonRetirarVehiculo=Button(root,
                        text="Retirar vehículo",
                        width=50,
                        height=5)
botonRetirarVehiculo.pack()
root.mainloop()
#agregar una w a la extesion .py-> .pyw para que se ejecute sin consola


