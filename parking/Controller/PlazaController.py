from tkinter import *
from Servicios import PlazaServicio
from Controller import IndiceController


def estadoParking(root):
    cadena1,cadena2= PlazaServicio.pintarEstado(PlazaServicio.estadoParking())
    frame_informacion_parking=Frame(root,
                             bd=3,
                             relief="groove")
    frame_informacion_parking.pack(side=LEFT)
    textoInformacion=Label(frame_informacion_parking,foreground="black",text=cadena1)
    textoInformacion.pack(anchor=N)
    frame_informacion_parking2=Frame(root,
                             bd=3,
                             relief="groove")
    frame_informacion_parking2.pack(side=RIGHT)
    textoInformacion2=Label(frame_informacion_parking2,foreground="black",text=cadena2)
    textoInformacion2.pack(anchor=N)
    boton_volver_admin=Button(root,text="Volver al menú de administrador",width=25,height=2,command=lambda:volverAdmin(root,frame_informacion_parking,frame_informacion_parking2,boton_volver_admin))
    boton_volver_admin.pack(anchor=N,side=TOP)

def volverAdmin(root,frame_informacion_parking,frame_informacion_parking2,boton_volver_admin):
    frame_informacion_parking2.destroy()
    frame_informacion_parking.destroy()
    boton_volver_admin.destroy()
    IndiceController.administracion(root)
