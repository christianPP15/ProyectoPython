from tkinter import *
from tkinter import messagebox

from Controller import ClienteSinAbonarController, PlazaController, CaducidadConsultaAbono, TicketController, \
    AbonadoController, CaducidadAbonoController, GestionAbonoController
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
                            height=4,
                            command=lambda:guardarVehiculoConAbono(root,frame_informacion_parking,textoInformacion,label_guardado_retirar_no_abono,label_guardado_retirar_abono,botonAdministracion))
    botonGuardarVehiculoAbono.pack(side=LEFT,fill="x",expand=1)
    botonRetirarVehiculoAbono=Button(label_guardado_retirar_abono,
                            text="Retirar vehículo abonado",
                            height=4,command=lambda:retirarVehiculoConAbono(root,frame_informacion_parking,textoInformacion,label_guardado_retirar_no_abono,label_guardado_retirar_abono,botonAdministracion))
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

def guardarVehiculoConAbono(root,frame_informacion_parking,textoInformacion,label_guardado_retirar_no_abono,label_guardado_retirar_abono,botonAdministracion):
    borrarMenuPrincipal(frame_informacion_parking,textoInformacion,label_guardado_retirar_no_abono,label_guardado_retirar_abono,botonAdministracion)
    AbonadoController.depositarAbonado(root)
def retirarVehiculoConAbono(root,frame_informacion_parking,textoInformacion,label_guardado_retirar_no_abono,label_guardado_retirar_abono,botonAdministracion):
    borrarMenuPrincipal(frame_informacion_parking,textoInformacion,label_guardado_retirar_no_abono,label_guardado_retirar_abono,botonAdministracion)
    AbonadoController.retirarVehiculoAbonado(root)
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
            administracion(root)
        else:
            messagebox.showinfo(message="Contraseña incorrecta", title="Contraseña")
            accesoAdministracionError(root)
    else:
        messagebox.showinfo(message="El campo de contraseña debe ser completado", title="Contraseña")
        accesoAdministracionError(root)

def volverInicioAdministracion(root,boton_inicio,frame_opcion_estado_facturacion,frame_opcion_consulta_abono,caducidadAbonoBoton):
    boton_inicio.destroy()
    frame_opcion_estado_facturacion.destroy()
    frame_opcion_consulta_abono.destroy()
    caducidadAbonoBoton.destroy()
    indice(root)
def eliminarMenuAdmin(boton_inicio,frame_opcion_estado_facturacion,frame_opcion_consulta_abono,caducidadAbonoBoton):
    boton_inicio.destroy()
    frame_opcion_estado_facturacion.destroy()
    frame_opcion_consulta_abono.destroy()
    caducidadAbonoBoton.destroy()
def redirigirEstadoParking(root,boton_inicio,frame_opcion_estado_facturacion,frame_opcion_consulta_abono,caducidadAbonoBoton):
    eliminarMenuAdmin(boton_inicio,frame_opcion_estado_facturacion,frame_opcion_consulta_abono,caducidadAbonoBoton)
    PlazaController.estadoParking(root)
def redirigirConsultaAbono(root,boton_inicio,frame_opcion_estado_facturacion,frame_opcion_consulta_abono,caducidadAbonoBoton):
    eliminarMenuAdmin(boton_inicio,frame_opcion_estado_facturacion,frame_opcion_consulta_abono,caducidadAbonoBoton)
    CaducidadConsultaAbono.consultaAbono(root)
def redirigirFacturacion(root,boton_inicio,frame_opcion_estado_facturacion,frame_opcion_consulta_abono,caducidadAbonoBoton):
    eliminarMenuAdmin(boton_inicio,frame_opcion_estado_facturacion,frame_opcion_consulta_abono,caducidadAbonoBoton)
    TicketController.facturacion_datos(root)
def redirigirCaducidad(root,boton_inicio,frame_opcion_estado_facturacion,frame_opcion_consulta_abono,caducidadAbonoBoton):
    eliminarMenuAdmin(boton_inicio,frame_opcion_estado_facturacion,frame_opcion_consulta_abono,caducidadAbonoBoton)
    CaducidadAbonoController.menuCaducidadAbono(root)
def rediridirMenuGestionAbono(root,boton_inicio,frame_opcion_estado_facturacion,frame_opcion_consulta_abono,caducidadAbonoBoton):
    eliminarMenuAdmin(boton_inicio,frame_opcion_estado_facturacion,frame_opcion_consulta_abono,caducidadAbonoBoton)
    GestionAbonoController.menuGestionAbono(root)
def administracion(root):
    #Información menú superior
    boton_inicio=Button(root,text="Volver al menú principal",
                             width=50,
                             height=4,
                             bd=3,
                             relief="groove",command=lambda:volverInicioAdministracion(root,boton_inicio,frame_opcion_estado_facturacion,frame_opcion_consulta_abono,caducidadAbonoBoton))
    boton_inicio.pack()
    #Información menú superior

    #Botonera frame_opcion_estado_facturacion
    frame_opcion_estado_facturacion=Frame(root,bd=1,relief="groove")
    frame_opcion_estado_facturacion.pack(fill="x",expand=1,anchor=N)
    estado=Button(frame_opcion_estado_facturacion,
                            text="Estado del parking",
                            height=4,command=lambda:redirigirEstadoParking(root,boton_inicio,frame_opcion_estado_facturacion,frame_opcion_consulta_abono,caducidadAbonoBoton))
    estado.pack(side=LEFT,fill="x",expand=1)
    facturacion=Button(frame_opcion_estado_facturacion,
                            text="Facturación",
                            height=4,command=lambda:redirigirFacturacion(root,boton_inicio,frame_opcion_estado_facturacion,frame_opcion_consulta_abono,caducidadAbonoBoton))
    facturacion.pack(side=RIGHT,fill="x",expand=1)
    #Botonera frame_opcion_estado_facturacion

    #Botonera frame_opcion_consulta_abono
    frame_opcion_consulta_abono=Frame(root,bd=1,relief="groove")
    frame_opcion_consulta_abono.pack(fill="x",expand=1,anchor=N)
    consultaAbonosBoton=Button(frame_opcion_consulta_abono,
                            text="Consulta de abonos",
                            height=4,command=lambda:redirigirConsultaAbono(root,boton_inicio,frame_opcion_estado_facturacion,frame_opcion_consulta_abono,caducidadAbonoBoton))
    consultaAbonosBoton.pack(side=LEFT,fill="x",expand=1)
    gestionAbonosBoton=Button(frame_opcion_consulta_abono,
                            text="Gestion abonos",
                            height=4,command=lambda:rediridirMenuGestionAbono(root,boton_inicio,frame_opcion_estado_facturacion,frame_opcion_consulta_abono,caducidadAbonoBoton))
    gestionAbonosBoton.pack(side=RIGHT,fill="x",expand=1)
    #Botonera frame_opcion_consulta_abono

    #Botonera caducidad
    caducidadAbonoBoton=Button(root,text="Caducidad abonos",width=400,height=4,bd=1,relief="groove",command=lambda:redirigirCaducidad(root,boton_inicio,frame_opcion_estado_facturacion,frame_opcion_consulta_abono,caducidadAbonoBoton))
    caducidadAbonoBoton.pack(side=BOTTOM)
