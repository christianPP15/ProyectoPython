from tkinter import *
from Controller import ClienteSinAbonarController
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
                            command=lambda:guardarVehiculoSinAbono(root,frame_informacion_parking,textoInformacion,label_guardado_retirar_no_abono,label_guardado_retirar_abono,botonAdministracion))
    botonGuardarVehiculo.pack(side=LEFT,fill="x",expand=1)
    botonRetirarVehiculo=Button(label_guardado_retirar_no_abono,
                            text="Retirar vehículo",
                            height=4,command=lambda:retirarVehiculoSinAbono(root,frame_informacion_parking,textoInformacion,label_guardado_retirar_no_abono,label_guardado_retirar_abono,botonAdministracion))
    botonRetirarVehiculo.pack(side=RIGHT,fill="x",expand=1)
    #Botonera label_guardado_retirar_no_abono

    #Botonera label_guardado_retirar_abono
    label_guardado_retirar_abono=Frame(root,bd=1,relief="groove")
    label_guardado_retirar_abono.pack(fill="x",expand=1,anchor=N)
    botonGuardarVehiculoAbono=Button(label_guardado_retirar_abono,
                            text="Guardar vehículo abonado",
                            height=4)
    botonGuardarVehiculoAbono.pack(side=LEFT,fill="x",expand=1)
    botonRetirarVehiculoAbono=Button(label_guardado_retirar_abono,
                            text="Retirar vehículo abonado",
                            height=4)
    botonRetirarVehiculoAbono.pack(side=RIGHT,fill="x",expand=1)
    #Botonera label_guardado_retirar_abono

    #Botonera admin
    botonAdministracion=Button(root,text="Zona administracion",width=400,height=4,bd=1,relief="groove")
    botonAdministracion.pack(side=BOTTOM)

def guardarVehiculoSinAbono(root,frame_informacion_parking,textoInformacion,label_guardado_retirar_no_abono,label_guardado_retirar_abono,botonAdministracion):
    frame_informacion_parking.destroy()
    textoInformacion.destroy()
    label_guardado_retirar_no_abono.destroy()
    label_guardado_retirar_abono.destroy()
    botonAdministracion.destroy()
    ClienteSinAbonarController.guardarVehiculo_obtenerInfo(root)


def retirarVehiculoSinAbono(root,frame_informacion_parking,textoInformacion,label_guardado_retirar_no_abono,label_guardado_retirar_abono,botonAdministracion):
    frame_informacion_parking.destroy()
    textoInformacion.destroy()
    label_guardado_retirar_no_abono.destroy()
    label_guardado_retirar_abono.destroy()
    botonAdministracion.destroy()
    ClienteSinAbonarController.retirarVehiculoObtenerInfo(root)
