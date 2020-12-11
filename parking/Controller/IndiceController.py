from tkinter import *
from tkinter import messagebox

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
    botonAdministracion=Button(root,text="Zona administracion",width=400,height=4,bd=1,relief="groove",command=lambda:accesoAdministracion(root,frame_informacion_parking,textoInformacion,label_guardado_retirar_no_abono,label_guardado_retirar_abono,botonAdministracion))
    botonAdministracion.pack(side=BOTTOM)

def borrarMenuPrincipal(frame_informacion_parking,textoInformacion,label_guardado_retirar_no_abono,label_guardado_retirar_abono,botonAdministracion):
    frame_informacion_parking.destroy()
    textoInformacion.destroy()
    label_guardado_retirar_no_abono.destroy()
    label_guardado_retirar_abono.destroy()
    botonAdministracion.destroy()

def guardarVehiculoSinAbono(root,frame_informacion_parking,textoInformacion,label_guardado_retirar_no_abono,label_guardado_retirar_abono,botonAdministracion):
    borrarMenuPrincipal(frame_informacion_parking,textoInformacion,label_guardado_retirar_no_abono,label_guardado_retirar_abono,botonAdministracion)
    ClienteSinAbonarController.guardarVehiculo_obtenerInfo(root)


def retirarVehiculoSinAbono(root,frame_informacion_parking,textoInformacion,label_guardado_retirar_no_abono,label_guardado_retirar_abono,botonAdministracion):
    borrarMenuPrincipal(frame_informacion_parking,textoInformacion,label_guardado_retirar_no_abono,label_guardado_retirar_abono,botonAdministracion)
    ClienteSinAbonarController.retirarVehiculoObtenerInfo(root)

def accesoAdministracion(root,frame_informacion_parking,textoInformacion,label_guardado_retirar_no_abono,label_guardado_retirar_abono,botonAdministracion):
    borrarMenuPrincipal(frame_informacion_parking,textoInformacion,label_guardado_retirar_no_abono,label_guardado_retirar_abono,botonAdministracion)
    botonMenuPrincipal=Button(root,text="Volver al menú principal",width=20,height=2,command=lambda:volverAlMenuPrincipal(root,frame_contra,contra_label,input_contra,botonEnviar,botonMenuPrincipal))
    botonMenuPrincipal.pack(anchor=N,side=LEFT)
    frame_contra = Frame(root, bd=1, relief="groove", width=600)
    frame_contra.pack()
    contra_label = Label(frame_contra, text="Contraseña administrador:", width=20)
    contra_label.config(padx=10, pady=10)
    contra_label.pack(side=LEFT, fill="x", expand=1)
    input_contra = Entry(frame_contra, width=50)
    input_contra.pack( fill="x", expand=1)
    botonEnviar = Button(root, text="Verificar contraseña", width=50, height=5,command=lambda:verificarContraseña(root,frame_contra,contra_label,input_contra,botonEnviar,botonMenuPrincipal))
    botonEnviar.pack(anchor=S, side=BOTTOM)
def volverAlMenuPrincipal(root,frame_contra,contra_label,input_contra,botonEnviar,botonMenuPrincipal):
    frame_contra.destroy()
    input_contra.destroy()
    contra_label.destroy()
    botonEnviar.destroy()
    botonMenuPrincipal.destroy()
    indice(root)
def accesoAdministracionError(root):
    botonMenuPrincipal=Button(root,text="Volver al menú principal",width=20,height=2,command=lambda:volverAlMenuPrincipal(root,frame_contra,contra_label,input_contra,botonEnviar,botonMenuPrincipal))
    botonMenuPrincipal.pack(anchor=N,side=LEFT)
    frame_contra = Frame(root, bd=1, relief="groove", width=600)
    frame_contra.pack()
    contra_label = Label(frame_contra, text="Contraseña administrador:", width=20)
    contra_label.config(padx=10, pady=10)
    contra_label.pack(side=LEFT, fill="x", expand=1)
    input_contra = Entry(frame_contra, width=50)
    input_contra.pack( fill="x", expand=1)
    botonEnviar = Button(root, text="Verificar contraseña", width=50, height=5,command=lambda:verificarContraseña(root,frame_contra,contra_label,input_contra,botonEnviar,botonMenuPrincipal))
    botonEnviar.pack(anchor=S, side=BOTTOM)
def verificarContraseña(root,frame_contra,contra_label,input_contra,botonEnviar,botonMenuPrincipal):
    contra=input_contra.get()
    frame_contra.destroy()
    input_contra.destroy()
    contra_label.destroy()
    botonEnviar.destroy()
    botonMenuPrincipal.destroy()
    if contra!="":
        if contra=="1234":
            pass
        else:
            messagebox.showinfo(message="Contraseña incorrecta", title="Contraseña")
            accesoAdministracionError(root)
    else:
        messagebox.showinfo(message="El campo de contraseña debe ser completado", title="Contraseña")
        accesoAdministracionError(root)
