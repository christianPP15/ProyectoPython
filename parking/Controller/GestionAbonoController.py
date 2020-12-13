from tkinter import *
from tkinter import messagebox

from Controller import IndiceController
from Servicios import AbonoServicio


def menuGestionAbono(root):
    boton_inicio=Button(root,text="Volver al menú principal",
                             width=50,
                             height=4,
                             bd=3,
                             relief="groove",command=lambda:volverAdminDesdeMenu(root,boton_inicio,botoneraMenu,crearBoton,EditarBoton,EliminarBoton))
    boton_inicio.pack()
    #Información menú superior

    #Botonera frame_opcion_estado_facturacion
    botoneraMenu=Frame(root,bd=1,relief="groove")
    botoneraMenu.pack(fill="x",expand=1,anchor=N)
    crearBoton=Button(botoneraMenu,
                            text="Crear Abono",
                            height=4,command=lambda:crearAbonoFormulario(root,boton_inicio,botoneraMenu,crearBoton,EditarBoton,EliminarBoton))
    crearBoton.pack(side=LEFT,fill="x",expand=1)
    EditarBoton=Button(botoneraMenu,
                            text="Editar Abono",
                            height=4)
    EditarBoton.pack(side=RIGHT,fill="x",expand=1)
    EliminarBoton=Button(botoneraMenu,
                            text="Eliminar Abono",
                            height=4,width=30,command=lambda:formularioBorrarAbono(root,boton_inicio,botoneraMenu,crearBoton,EditarBoton,EliminarBoton))
    EliminarBoton.pack(fill="x",expand=1)
def eliminarMenu(boton_inicio,botoneraMenu,crearBoton,EditarBoton,EliminarBoton):
    boton_inicio.destroy()
    botoneraMenu.destroy()
    crearBoton.destroy()
    EditarBoton.destroy()
    EliminarBoton.destroy()
def volverAdminDesdeMenu(root,boton_inicio,botoneraMenu,crearBoton,EditarBoton,EliminarBoton):
    eliminarMenu(boton_inicio,botoneraMenu,crearBoton,EditarBoton,EliminarBoton)
    IndiceController.administracion(root)

def crearAbonoFormulario(root,boton_inicio,botoneraMenu,crearBoton,EditarBoton,EliminarBoton):
    eliminarMenu(boton_inicio,botoneraMenu,crearBoton,EditarBoton,EliminarBoton)
    tipo = IntVar()
    opcion=IntVar()
    frame_vehiculo = Frame(root, bd=1, relief="groove", width=200)
    frame_vehiculo.pack()
    checkbox_turismo = Radiobutton(frame_vehiculo, text="Turismo", variable=tipo, value=1).pack()
    checkbox_moto = Radiobutton(frame_vehiculo, text="Motocicleta", variable=tipo, value=2).pack()
    checkbox_movilidad = Radiobutton(frame_vehiculo, text="Movilidad reducida", variable=tipo, value=3).pack()
    frame_opciones_meses=Frame(root,bd=1,relief="groove",width=200)
    frame_opciones_meses.pack()
    checkbox_1mes=Radiobutton(frame_opciones_meses,text="mensual:25€",variable=opcion,value=1).pack()
    checkbox_3mes=Radiobutton(frame_opciones_meses,text="Trimestral:70€",variable=opcion,value=2).pack()
    checkbox_6mes=Radiobutton(frame_opciones_meses,text="Semestral:130€",variable=opcion,value=3).pack()
    checkbox_12mes=Radiobutton(frame_opciones_meses,text="Anual:200€",variable=opcion,value=4).pack()
    botonEnviar = Button(root, text="Enviar información", width=50, height=5,
                         command=lambda:creacionDeAbonoCompletar(root,frame_opciones_meses,tipo,opcion,frame_vehiculo,botonEnviar))
    botonEnviar.pack(anchor=S, side=BOTTOM)

def creacionDeAbonoCompletar(root,frame_opciones_meses,tipo,opcion,frame_vehiculo,botonEnviar):
    frame_opciones_meses.destroy()
    frame_vehiculo.destroy()
    botonEnviar.destroy()
    try:
        if opcion.get()==0:
            raise ValueError
        if tipo.get()==1:
            tipo="Turismo"
        elif tipo.get()==2:
            tipo="Moto"
        elif tipo.get()==3:
            tipo="Movilidad reducida"
        else:
            raise ValueError
        frame_nombre = Frame(root, bd=1, relief="groove", width=600)
        frame_nombre.pack()
        nombre_label = Label(frame_nombre, text="Nombre del cliente:", width=20)
        nombre_label.config(padx=10, pady=10)
        nombre_label.pack(side=LEFT, fill="x", expand=1)
        input_nombre = Entry(frame_nombre, width=50)
        input_nombre.pack(side=RIGHT, fill="x", expand=1)

        frame_apellidos= Frame(root, bd=1, relief="groove", width=600)
        frame_apellidos.pack()
        apellidos_label = Label(frame_apellidos, text="Apellidos del cliente:", width=20)
        apellidos_label.config(padx=10, pady=10)
        apellidos_label.pack(side=LEFT, fill="x", expand=1)
        input_apellidos = Entry(frame_apellidos, width=50)
        input_apellidos.pack(side=RIGHT, fill="x", expand=1)

        frame_dni= Frame(root, bd=1, relief="groove", width=600)
        frame_dni.pack()
        dni_label = Label(frame_dni, text="DNI del cliente:", width=20)
        dni_label.config(padx=10, pady=10)
        dni_label.pack(side=LEFT, fill="x", expand=1)
        input_dni = Entry(frame_dni, width=50)
        input_dni.pack(side=RIGHT, fill="x", expand=1)

        frame_matricula= Frame(root, bd=1, relief="groove", width=600)
        frame_matricula.pack()
        matricula_label = Label(frame_matricula, text="Matricula del vehículo del cliente:", width=30)
        matricula_label.config(padx=10, pady=10)
        matricula_label.pack(side=LEFT, fill="x", expand=1)
        input_matricula = Entry(frame_matricula, width=50)
        input_matricula.pack(side=RIGHT, fill="x", expand=1)

        frame_email= Frame(root, bd=1, relief="groove", width=600)
        frame_email.pack()
        email_label = Label(frame_email, text="Email del cliente:", width=20)
        email_label.config(padx=10, pady=10)
        email_label.pack(side=LEFT, fill="x", expand=1)
        input_email = Entry(frame_email, width=50)
        input_email.pack(side=RIGHT, fill="x", expand=1)

        frame_tarjeta= Frame(root, bd=1, relief="groove", width=600)
        frame_tarjeta.pack()
        tarjeta_label = Label(frame_tarjeta, text="Tarjeta del cliente:", width=20)
        tarjeta_label.config(padx=10, pady=10)
        tarjeta_label.pack(side=LEFT, fill="x", expand=1)
        input_tarjeta = Entry(frame_tarjeta, width=50)
        input_tarjeta.pack(side=RIGHT, fill="x", expand=1)

        botonEnviar = Button(root, text="Enviar información", width=50, height=5,
                         command=lambda:procesarInformacionAltaUsuario(root,frame_nombre,frame_apellidos
                                                                       ,frame_matricula,frame_dni,frame_email,frame_tarjeta
                                                                       ,input_nombre,input_apellidos,input_matricula,input_dni
                                                                       ,input_email,input_tarjeta,opcion,tipo,botonEnviar))
        botonEnviar.pack(anchor=S, side=BOTTOM)
    except ValueError:
        mostrarMensaje(root,"Error, debes seleccionar una casilla de cada grupo")
def procesarInformacionAltaUsuario(root,frame_nombre,frame_apellidos,frame_matricula,frame_dni,frame_email,frame_tarjeta
                                   ,input_nombre,input_apellidos,input_matricula,input_dni,input_email,input_tarjeta,opcion,tipo,botonEnviar):
    nombre=input_nombre.get()
    apellidos=input_apellidos.get()
    matricula=input_matricula.get()
    dni=input_dni.get()
    email=input_email.get()
    tarjeta=input_tarjeta.get()
    frame_nombre.destroy()
    frame_apellidos.destroy()
    frame_matricula.destroy()
    frame_dni.destroy()
    frame_email.destroy()
    frame_tarjeta.destroy()
    botonEnviar.destroy()
    if nombre!="" and apellidos!="" and matricula!="" and dni!="" and email!="" and tarjeta!="":
        pin=AbonoServicio.AltaAbono(opcion,tipo,nombre,apellidos,dni,matricula,email,tarjeta)
        mostrarMensaje(root,f"Creacion de abono completado con exito, su pin es: {pin}")
    else:
        messagebox.showinfo(message="Error, todos los cambos deben completarse", title="Error con la información")
        menuGestionAbono(root)
def mostrarMensaje(root,mensaje):
    caducados=Label(root,text=mensaje)
    caducados.pack()
    botonSalir=Button(root,text="Volver al inicio",command=lambda:volverMenuGestion(root,caducados,botonSalir))
    botonSalir.pack()
def volverMenuGestion(root,caducados,botonSalir):
    caducados.destroy()
    botonSalir.destroy()
    menuGestionAbono(root)

def formularioBorrarAbono(root,boton_inicio,botoneraMenu,crearBoton,EditarBoton,EliminarBoton):
    eliminarMenu(boton_inicio,botoneraMenu,crearBoton,EditarBoton,EliminarBoton)
    frame_pin= Frame(root, bd=1, relief="groove", width=600)
    frame_pin.pack()
    pin_label = Label(frame_pin, text="Pin del cliente:", width=20)
    pin_label.config(padx=10, pady=10)
    pin_label.pack(side=LEFT, fill="x", expand=1)
    input_pin = Entry(frame_pin, width=50)
    input_pin.pack(side=RIGHT, fill="x", expand=1)

    frame_identificador= Frame(root, bd=1, relief="groove", width=600)
    frame_identificador.pack()
    iden_label = Label(frame_identificador, text="Identificador de la plaza:", width=20)
    iden_label.config(padx=10, pady=10)
    iden_label.pack(side=LEFT, fill="x", expand=1)
    input_iden = Entry(frame_identificador, width=50)
    input_iden.pack(side=RIGHT, fill="x", expand=1)

    botonEnviar = Button(root, text="Enviar información", width=50, height=5,
                         command=lambda:eliminarAbonoCompletar(root,frame_pin,frame_identificador,input_pin,input_iden,botonEnviar))
    botonEnviar.pack(anchor=S, side=BOTTOM)

def eliminarAbonoCompletar(root,frame_pin,frame_identificador,input_pin,input_iden,botonEnviar):
    pin=input_pin.get()
    identificador=input_iden.get()
    frame_identificador.destroy()
    frame_pin.destroy()
    botonEnviar.destroy()
    if pin!="" and identificador!="":
        mensaje=AbonoServicio.borrarAbono(pin,identificador)
        mostrarMensaje(root,mensaje)
    else:
        messagebox.showinfo(message="Error, todos los cambos deben completarse", title="Error con la información")
        menuGestionAbono(root)
