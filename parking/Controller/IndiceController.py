from tkinter import *
from Controller import ClienteController
from Servicios import PlazaServicio
def indice(root):
    #Información menú superior
    frame_informacion_parking=Frame(root,
                             width=500,
                             height=100,
                             bd=3,
                             relief="groove")
    frame_informacion_parking.pack()
    textoInformacion=Label(frame_informacion_parking,foreground="black",text=PlazaServicio.mostrarDisponibilidad())
    textoInformacion.pack(anchor=N)
    #Información menú superior

    #Botonera label_guardado_retirar_no_abono
    label_guardado_retirar_no_abono=Frame(root,bd=1,relief="groove")
    label_guardado_retirar_no_abono.pack(fill="x",expand=1,anchor=N)
    botonGuardarVehiculo=Button(label_guardado_retirar_no_abono,
                            text="Guardar vehículo",
                            height=4,
                            command=lambda:ClienteController.guardarVehiculo(root,label_guardado_retirar_no_abono,label_guardado_retirar_abono,textoInformacion,frame_informacion_parking))
    botonGuardarVehiculo.pack(side=LEFT,fill="x",expand=1)
    botonRetirarVehiculo=Button(label_guardado_retirar_no_abono,
                            text="Retirar vehículo",
                            height=4)
    botonRetirarVehiculo.pack(side=RIGHT,fill="x",expand=1)
    #Botonera label_guardado_retirar_no_abono

    #Botonera label_guardado_retirar_abono
    label_guardado_retirar_abono=Frame(root,bd=1,relief="groove")
    label_guardado_retirar_abono.pack(fill="x",expand=1,anchor=N)
    botonGuardarVehiculoAbono=Button(label_guardado_retirar_abono,
                            text="Guardar vehículo abonado",
                            height=4,
                            command=lambda:ClienteController.guardarVehiculo(root,botonGuardarVehiculo,botonRetirarVehiculo))
    botonGuardarVehiculoAbono.pack(side=LEFT,fill="x",expand=1)
    botonRetirarVehiculoAbono=Button(label_guardado_retirar_abono,
                            text="Retirar vehículo abonado",
                            height=4)
    botonRetirarVehiculoAbono.pack(side=RIGHT,fill="x",expand=1)
    #Botonera label_guardado_retirar_abono
