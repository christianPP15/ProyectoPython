from tkinter import *
from tkinter import messagebox

from Controller import IndiceController
from Servicios import AbonoServicio


def menuGestionAbono(root):
    boton_inicio = Button(root, text="Volver al menú principal",
                          width=50,
                          height=4,
                          bd=3,
                          relief="groove",
                          command=lambda: volverAdminDesdeMenu(root, boton_inicio, botoneraMenu, crearBoton,
                                                               EditarBoton, EliminarBoton))
    boton_inicio.pack()
    # Información menú superior

    # Botonera frame_opcion_estado_facturacion
    botoneraMenu = Frame(root, bd=1, relief="groove")
    botoneraMenu.pack(fill="x", expand=1, anchor=N)
    crearBoton = Button(botoneraMenu,
                        text="Crear Abono",
                        height=4,
                        command=lambda: crearAbonoFormulario(root, boton_inicio, botoneraMenu, crearBoton, EditarBoton,
                                                             EliminarBoton))
    crearBoton.pack(side=LEFT, fill="x", expand=1)
    EditarBoton = Button(botoneraMenu,
                         text="Editar Abono",
                         height=4, command=lambda: menuEditar(root, boton_inicio, botoneraMenu, crearBoton, EditarBoton,
                                                              EliminarBoton))
    EditarBoton.pack(side=RIGHT, fill="x", expand=1)
    EliminarBoton = Button(botoneraMenu,
                           text="Eliminar Abono",
                           height=4, width=30,
                           command=lambda: formularioBorrarAbono(root, boton_inicio, botoneraMenu, crearBoton,
                                                                 EditarBoton, EliminarBoton))
    EliminarBoton.pack(fill="x", expand=1)


def eliminarMenu(boton_inicio, botoneraMenu, crearBoton, EditarBoton, EliminarBoton):
    boton_inicio.destroy()
    botoneraMenu.destroy()
    crearBoton.destroy()
    EditarBoton.destroy()
    EliminarBoton.destroy()


def volverAdminDesdeMenu(root, boton_inicio, botoneraMenu, crearBoton, EditarBoton, EliminarBoton):
    eliminarMenu(boton_inicio, botoneraMenu, crearBoton, EditarBoton, EliminarBoton)
    IndiceController.administracion(root)

def volverMenuPrincipalDesdeCrearAbono(root,botonMenuPrincipal,botonEnviar,boton_inicio,frame_vehiculo,frame_opciones_meses):
    botonMenuPrincipal.destroy()
    botonEnviar.destroy()
    boton_inicio.destroy()
    frame_opciones_meses.destroy()
    frame_vehiculo.destroy()
    menuGestionAbono(root)
def crearAbonoFormulario(root, boton_inicio, botoneraMenu, crearBoton, EditarBoton, EliminarBoton):
    eliminarMenu(boton_inicio, botoneraMenu, crearBoton, EditarBoton, EliminarBoton)
    botonMenuPrincipal=Button(root,text="Volver al menú principal",width=20,height=2,command=lambda:volverMenuPrincipalDesdeCrearAbono(root,botonMenuPrincipal,botonEnviar,boton_inicio,frame_vehiculo,frame_opciones_meses))
    botonMenuPrincipal.pack(anchor=N,side=LEFT)
    tipo = IntVar()
    opcion = IntVar()
    frame_vehiculo = Frame(root, bd=1, relief="groove", width=200)
    frame_vehiculo.pack()
    checkbox_turismo = Radiobutton(frame_vehiculo, text="Turismo", variable=tipo, value=1).pack()
    checkbox_moto = Radiobutton(frame_vehiculo, text="Motocicleta", variable=tipo, value=2).pack()
    checkbox_movilidad = Radiobutton(frame_vehiculo, text="Movilidad reducida", variable=tipo, value=3).pack()
    frame_opciones_meses = Frame(root, bd=1, relief="groove", width=200)
    frame_opciones_meses.pack()
    checkbox_1mes = Radiobutton(frame_opciones_meses, text="mensual:25€", variable=opcion, value=1).pack()
    checkbox_3mes = Radiobutton(frame_opciones_meses, text="Trimestral:70€", variable=opcion, value=2).pack()
    checkbox_6mes = Radiobutton(frame_opciones_meses, text="Semestral:130€", variable=opcion, value=3).pack()
    checkbox_12mes = Radiobutton(frame_opciones_meses, text="Anual:200€", variable=opcion, value=4).pack()
    botonEnviar = Button(root, text="Enviar información", width=50, height=5,
                         command=lambda: creacionDeAbonoCompletar(root, frame_opciones_meses, tipo, opcion,
                                                                  frame_vehiculo, botonEnviar,botonMenuPrincipal))
    botonEnviar.pack(anchor=S, side=BOTTOM)


def creacionDeAbonoCompletar(root, frame_opciones_meses, tipo, opcion, frame_vehiculo, botonEnviar,botonMenuPrincipal):
    frame_opciones_meses.destroy()
    frame_vehiculo.destroy()
    botonEnviar.destroy()
    botonMenuPrincipal.destroy()
    try:
        if opcion.get() == 0:
            raise ValueError
        if tipo.get() == 1:
            tipo = "Turismo"
        elif tipo.get() == 2:
            tipo = "Moto"
        elif tipo.get() == 3:
            tipo = "Movilidad reducida"
        else:
            raise ValueError
        frame_nombre = Frame(root, bd=1, relief="groove", width=600)
        frame_nombre.pack()
        nombre_label = Label(frame_nombre, text="Nombre del cliente:", width=20)
        nombre_label.config(padx=10, pady=10)
        nombre_label.pack(side=LEFT, fill="x", expand=1)
        input_nombre = Entry(frame_nombre, width=50)
        input_nombre.pack(side=RIGHT, fill="x", expand=1)

        frame_apellidos = Frame(root, bd=1, relief="groove", width=600)
        frame_apellidos.pack()
        apellidos_label = Label(frame_apellidos, text="Apellidos del cliente:", width=20)
        apellidos_label.config(padx=10, pady=10)
        apellidos_label.pack(side=LEFT, fill="x", expand=1)
        input_apellidos = Entry(frame_apellidos, width=50)
        input_apellidos.pack(side=RIGHT, fill="x", expand=1)

        frame_dni = Frame(root, bd=1, relief="groove", width=600)
        frame_dni.pack()
        dni_label = Label(frame_dni, text="DNI del cliente:", width=20)
        dni_label.config(padx=10, pady=10)
        dni_label.pack(side=LEFT, fill="x", expand=1)
        input_dni = Entry(frame_dni, width=50)
        input_dni.pack(side=RIGHT, fill="x", expand=1)

        frame_matricula = Frame(root, bd=1, relief="groove", width=600)
        frame_matricula.pack()
        matricula_label = Label(frame_matricula, text="Matricula del vehículo del cliente:", width=30)
        matricula_label.config(padx=10, pady=10)
        matricula_label.pack(side=LEFT, fill="x", expand=1)
        input_matricula = Entry(frame_matricula, width=50)
        input_matricula.pack(side=RIGHT, fill="x", expand=1)

        frame_email = Frame(root, bd=1, relief="groove", width=600)
        frame_email.pack()
        email_label = Label(frame_email, text="Email del cliente:", width=20)
        email_label.config(padx=10, pady=10)
        email_label.pack(side=LEFT, fill="x", expand=1)
        input_email = Entry(frame_email, width=50)
        input_email.pack(side=RIGHT, fill="x", expand=1)

        frame_tarjeta = Frame(root, bd=1, relief="groove", width=600)
        frame_tarjeta.pack()
        tarjeta_label = Label(frame_tarjeta, text="Tarjeta del cliente:", width=20)
        tarjeta_label.config(padx=10, pady=10)
        tarjeta_label.pack(side=LEFT, fill="x", expand=1)
        input_tarjeta = Entry(frame_tarjeta, width=50)
        input_tarjeta.pack(side=RIGHT, fill="x", expand=1)

        botonEnviar = Button(root, text="Enviar información", width=50, height=5,
                             command=lambda: procesarInformacionAltaUsuario(root, frame_nombre, frame_apellidos
                                                                            , frame_matricula, frame_dni, frame_email,
                                                                            frame_tarjeta
                                                                            , input_nombre, input_apellidos,
                                                                            input_matricula, input_dni
                                                                            , input_email, input_tarjeta, opcion, tipo,
                                                                            botonEnviar))
        botonEnviar.pack(anchor=S, side=BOTTOM)
    except ValueError:
        mostrarMensaje(root, "Error, debes seleccionar una casilla de cada grupo")


def procesarInformacionAltaUsuario(root, frame_nombre, frame_apellidos, frame_matricula, frame_dni, frame_email,
                                   frame_tarjeta
                                   , input_nombre, input_apellidos, input_matricula, input_dni, input_email,
                                   input_tarjeta, opcion, tipo, botonEnviar):
    nombre = input_nombre.get()
    apellidos = input_apellidos.get()
    matricula = input_matricula.get()
    dni = input_dni.get()
    email = input_email.get()
    tarjeta = input_tarjeta.get()
    frame_nombre.destroy()
    frame_apellidos.destroy()
    frame_matricula.destroy()
    frame_dni.destroy()
    frame_email.destroy()
    frame_tarjeta.destroy()
    botonEnviar.destroy()
    if nombre != "" and apellidos != "" and matricula != "" and dni != "" and email != "" and tarjeta != "":
        pin = AbonoServicio.AltaAbono(opcion.get(), tipo, nombre, apellidos, dni, matricula, email, tarjeta)
        mostrarMensaje(root, f"Creacion de abono completado con exito, su pin es: {pin}")
    else:
        messagebox.showinfo(message="Error, todos los cambos deben completarse", title="Error con la información")
        menuGestionAbono(root)


def mostrarMensaje(root, mensaje):
    caducados = Label(root, text=mensaje)
    caducados.pack()
    botonSalir = Button(root, text="Volver al inicio", command=lambda: volverMenuGestion(root, caducados, botonSalir))
    botonSalir.pack()


def volverMenuGestion(root, caducados, botonSalir):
    caducados.destroy()
    botonSalir.destroy()
    menuGestionAbono(root)

def volverAlMenuPrincipalDesdeBorrado(root,botonMenuPrincipal,botonEnviar,boton_inicio,frame_pin,frame_identificador):
    boton_inicio.destroy()
    botonEnviar.destroy()
    botonMenuPrincipal.destroy()
    frame_pin.destroy()
    frame_identificador.destroy()
    menuGestionAbono(root)
def formularioBorrarAbono(root, boton_inicio, botoneraMenu, crearBoton, EditarBoton, EliminarBoton):
    eliminarMenu(boton_inicio, botoneraMenu, crearBoton, EditarBoton, EliminarBoton)
    botonMenuPrincipal=Button(root,text="Volver al menú principal",width=20,height=2,command=lambda:volverAlMenuPrincipalDesdeBorrado(root,botonMenuPrincipal,botonEnviar,boton_inicio,frame_pin,frame_identificador))
    botonMenuPrincipal.pack(anchor=N,side=LEFT)
    frame_pin = Frame(root, bd=1, relief="groove", width=600)
    frame_pin.pack()
    pin_label = Label(frame_pin, text="Pin del cliente:", width=20)
    pin_label.config(padx=10, pady=10)
    pin_label.pack(side=LEFT, fill="x", expand=1)
    input_pin = Entry(frame_pin, width=50)
    input_pin.pack(side=RIGHT, fill="x", expand=1)

    frame_identificador = Frame(root, bd=1, relief="groove", width=600)
    frame_identificador.pack()
    iden_label = Label(frame_identificador, text="Identificador de la plaza:", width=20)
    iden_label.config(padx=10, pady=10)
    iden_label.pack(side=LEFT, fill="x", expand=1)
    input_iden = Entry(frame_identificador, width=50)
    input_iden.pack(side=RIGHT, fill="x", expand=1)

    botonEnviar = Button(root, text="Enviar información", width=50, height=5,
                         command=lambda: eliminarAbonoCompletar(root, frame_pin, frame_identificador, input_pin,
                                                                input_iden, botonEnviar,botonMenuPrincipal))
    botonEnviar.pack(anchor=S, side=BOTTOM)


def eliminarAbonoCompletar(root, frame_pin, frame_identificador, input_pin, input_iden, botonEnviar,botonMenuPrincipal):
    pin = input_pin.get()
    identificador = input_iden.get()
    frame_identificador.destroy()
    frame_pin.destroy()
    botonEnviar.destroy()
    botonMenuPrincipal.destroy()
    if pin != "" and identificador != "":
        mensaje = AbonoServicio.borrarAbono(pin, identificador)
        mostrarMensaje(root, mensaje)
    else:
        messagebox.showinfo(message="Error, todos los cambos deben completarse", title="Error con la información")
        menuGestionAbono(root)


def eliminarMenuEditar(boton_inicio, frame_botonera_editar):
    boton_inicio.destroy()
    frame_botonera_editar.destroy()


def volverMenuAdmin(root, boton_inicio, frame_botonera_editar):
    eliminarMenuEditar(boton_inicio, frame_botonera_editar)
    menuGestionAbono(root)


def menuEditar(root, boton_inicio, botoneraMenu, crearBoton, EditarBoton, EliminarBoton):
    eliminarMenu(boton_inicio, botoneraMenu, crearBoton, EditarBoton, EliminarBoton)
    boton_inicio = Button(root, text="Volver al menú principal",
                          width=50,
                          height=4,
                          bd=3,
                          relief="groove", command=lambda: volverMenuAdmin(root, boton_inicio, frame_botonera_editar))
    boton_inicio.pack()
    frame_botonera_editar = Frame(root, bd=1, relief="groove")
    frame_botonera_editar.pack(fill="x", expand=1, anchor=N)
    editarUsuario = Button(frame_botonera_editar,
                           text="Editar información usuario",
                           height=4, command=lambda: editUsuario(root, boton_inicio, frame_botonera_editar))
    editarUsuario.pack(side=LEFT, fill="x", expand=1)
    editAbono = Button(frame_botonera_editar,
                       text="Editar abono",
                       height=4, command=lambda: editarAbono(root, boton_inicio, frame_botonera_editar))
    editAbono.pack(side=RIGHT, fill="x", expand=1)


def volverMenuGestionEdit(root, boton_inicio, frame_dni, frame_matricula, frame_opciones_meses, frame_pin, botonEnviar):
    boton_inicio.destroy()
    frame_dni.destroy()
    frame_matricula.destroy()
    frame_opciones_meses.destroy()
    frame_pin.destroy()
    botonEnviar.destroy()
    menuGestionAbono(root)


def editarAbono(root, boton_inicio, frame_botonera_editar):
    eliminarMenuEditar(boton_inicio, frame_botonera_editar)
    boton_inicio = Button(root, text="Volver al menú principal",
                          width=20,
                          height=4,
                          bd=3,
                          relief="groove",
                          command=lambda: volverMenuGestionEdit(root, boton_inicio, frame_dni, frame_matricula,
                                                                frame_opciones_meses, frame_pin, botonEnviar))
    boton_inicio.pack(side=LEFT, anchor=N)
    opcion = IntVar()
    frame_dni = Frame(root, bd=1, relief="groove", width=600)
    frame_dni.pack()
    dni_label = Label(frame_dni, text="DNI del cliente:", width=20)
    dni_label.config(padx=10, pady=10)
    dni_label.pack(side=LEFT, fill="x", expand=1)
    input_dni = Entry(frame_dni, width=50)
    input_dni.pack(side=RIGHT, fill="x", expand=1)

    frame_matricula = Frame(root, bd=1, relief="groove", width=600)
    frame_matricula.pack()
    matricula_label = Label(frame_matricula, text="Matricula del vehículo del cliente:", width=30)
    matricula_label.config(padx=10, pady=10)
    matricula_label.pack(side=LEFT, fill="x", expand=1)
    input_matricula = Entry(frame_matricula, width=50)
    input_matricula.pack(side=RIGHT, fill="x", expand=1)
    frame_pin = Frame(root, bd=1, relief="groove", width=600)
    frame_pin.pack()
    pin_label = Label(frame_pin, text="Pin del cliente:", width=30)
    pin_label.config(padx=10, pady=10)
    pin_label.pack(side=LEFT, fill="x", expand=1)
    input_pin = Entry(frame_pin, width=50)
    input_pin.pack(side=RIGHT, fill="x", expand=1)
    frame_opciones_meses = Frame(root, bd=1, relief="groove", width=200)
    frame_opciones_meses.pack()
    checkbox_1mes = Radiobutton(frame_opciones_meses, text="mensual:25€", variable=opcion, value=1).pack()
    checkbox_3mes = Radiobutton(frame_opciones_meses, text="Trimestral:70€", variable=opcion, value=2).pack()
    checkbox_6mes = Radiobutton(frame_opciones_meses, text="Semestral:130€", variable=opcion, value=3).pack()
    checkbox_12mes = Radiobutton(frame_opciones_meses, text="Anual:200€", variable=opcion, value=4).pack()
    botonEnviar = Button(root, text="Enviar información", width=50, height=5,
                         command=lambda: procesarCambioAbonoEditar(root, frame_matricula, frame_opciones_meses,
                                                                   frame_dni, frame_pin,
                                                                   opcion, input_matricula, input_dni, input_pin,
                                                                   botonEnviar, boton_inicio))
    botonEnviar.pack(anchor=S, side=BOTTOM)


def procesarCambioAbonoEditar(root, frame_matricula, frame_opciones_meses, frame_dni, frame_pin,
                              opcion, input_matricula, input_dni, input_pin, botonEnviar, boton_inicio):
    pin = input_pin.get()
    opcion = int(opcion.get())
    dni = input_dni.get()
    matricula = input_matricula.get()
    frame_matricula.destroy()
    frame_opciones_meses.destroy()
    frame_dni.destroy()
    frame_matricula.destroy()
    frame_pin.destroy()
    botonEnviar.destroy()
    boton_inicio.destroy()
    if pin.strip() != "" and dni.strip() != "" and matricula.strip() != "":
        try:
            if opcion != 0:
                resultado = AbonoServicio.edicionAbono(dni, matricula, pin, opcion)
                if resultado:
                    mostrarMensaje(root, "Edición completada con exito")
                else:
                    mostrarMensaje(root, "No encontramos ningún abono relacionado con los datos aportados")
            else:
                raise ValueError
        except ValueError:
            messagebox.showinfo(message="Error, debe seleccionar una tarifa", title="Error con la información")
            menuGestionAbono(root)
    else:
        messagebox.showinfo(message="Error, todos los cambos deben completarse", title="Error con la información")
        menuGestionAbono(root)

def volverMenuDesdeEliminar(root,botonMenuPrincipal,botonEnviar,boton_inicio,frame_dni_antiguo,frame_matricula_antiguo
                            ,frame_nombre,frame_apellidos,frame_dni,frame_matricula,frame_email,frame_tarjeta):
    botonMenuPrincipal.destroy()
    botonEnviar.destroy()
    boton_inicio.destroy()
    frame_matricula.destroy()
    frame_apellidos.destroy()
    frame_dni.destroy()
    frame_email.destroy()
    frame_nombre.destroy()
    frame_tarjeta.destroy()
    frame_dni_antiguo.destroy()
    frame_matricula_antiguo.destroy()
    menuGestionAbono(root)
def editUsuario(root, boton_inicio, frame_botonera_editar):
    eliminarMenuEditar(boton_inicio, frame_botonera_editar)
    boton_inicio.destroy()
    botonMenuPrincipal=Button(root,text="Volver al menú principal",width=20,height=2,command=lambda:volverMenuDesdeEliminar(root,botonMenuPrincipal,botonEnviar,boton_inicio,frame_dni_antiguo,frame_matricula_antiguo
                                                                                                                            ,frame_nombre,frame_apellidos,frame_dni,frame_matricula,frame_email,frame_tarjeta))
    botonMenuPrincipal.pack(anchor=N,side=LEFT)
    frame_dni_antiguo = Frame(root, bd=1, relief="groove", width=600)
    frame_dni_antiguo.pack()
    dni2_label = Label(frame_dni_antiguo, text="Introduce el antiguo dni del cliente:", width=50)
    dni2_label.config(padx=10, pady=10)
    dni2_label.pack(side=LEFT, fill="x", expand=1)
    input_dni2 = Entry(frame_dni_antiguo, width=50)
    input_dni2.pack(side=RIGHT, fill="x", expand=1)

    frame_matricula_antiguo = Frame(root, bd=1, relief="groove", width=600)
    frame_matricula_antiguo.pack()
    matricula2_label = Label(frame_matricula_antiguo, text="Introduce la matricula anterior:", width=20)
    matricula2_label.config(padx=10, pady=10)
    matricula2_label.pack(side=LEFT, fill="x", expand=1)
    input_matricula2 = Entry(frame_matricula_antiguo, width=50)
    input_matricula2.pack(side=RIGHT, fill="x", expand=1)

    frame_nombre = Frame(root, bd=1, relief="groove", width=600)
    frame_nombre.pack()
    nombre_label = Label(frame_nombre, text="Nombre del cliente:", width=20)
    nombre_label.config(padx=10, pady=10)
    nombre_label.pack(side=LEFT, fill="x", expand=1)
    input_nombre = Entry(frame_nombre, width=50)
    input_nombre.pack(side=RIGHT, fill="x", expand=1)

    frame_apellidos = Frame(root, bd=1, relief="groove", width=600)
    frame_apellidos.pack()
    apellidos_label = Label(frame_apellidos, text="Apellidos del cliente:", width=20)
    apellidos_label.config(padx=10, pady=10)
    apellidos_label.pack(side=LEFT, fill="x", expand=1)
    input_apellidos = Entry(frame_apellidos, width=50)
    input_apellidos.pack(side=RIGHT, fill="x", expand=1)

    frame_dni = Frame(root, bd=1, relief="groove", width=600)
    frame_dni.pack()
    dni_label = Label(frame_dni, text="Nuevo DNI del cliente:", width=20)
    dni_label.config(padx=10, pady=10)
    dni_label.pack(side=LEFT, fill="x", expand=1)
    input_dni = Entry(frame_dni, width=50)
    input_dni.pack(side=RIGHT, fill="x", expand=1)

    frame_matricula = Frame(root, bd=1, relief="groove", width=600)
    frame_matricula.pack()
    matricula_label = Label(frame_matricula, text="Nueva Matricula del vehículo del cliente:", width=30)
    matricula_label.config(padx=10, pady=10)
    matricula_label.pack(side=LEFT, fill="x", expand=1)
    input_matricula = Entry(frame_matricula, width=50)
    input_matricula.pack(side=RIGHT, fill="x", expand=1)

    frame_email = Frame(root, bd=1, relief="groove", width=600)
    frame_email.pack()
    email_label = Label(frame_email, text="Email del cliente:", width=20)
    email_label.config(padx=10, pady=10)
    email_label.pack(side=LEFT, fill="x", expand=1)
    input_email = Entry(frame_email, width=50)
    input_email.pack(side=RIGHT, fill="x", expand=1)

    frame_tarjeta = Frame(root, bd=1, relief="groove", width=600)
    frame_tarjeta.pack()
    tarjeta_label = Label(frame_tarjeta, text="Tarjeta del cliente:", width=20)
    tarjeta_label.config(padx=10, pady=10)
    tarjeta_label.pack(side=LEFT, fill="x", expand=1)
    input_tarjeta = Entry(frame_tarjeta, width=50)
    input_tarjeta.pack(side=RIGHT, fill="x", expand=1)

    botonEnviar = Button(root, text="Enviar información", width=50, height=5,
                         command=lambda: procesarInfoEditUsuario(root, frame_dni_antiguo, frame_dni,
                                                                 frame_matricula_antiguo, frame_matricula,
                                                                 frame_tarjeta, frame_nombre, frame_apellidos,
                                                                 frame_email,
                                                                 input_dni2, input_dni, input_matricula2,
                                                                 input_matricula,
                                                                 input_tarjeta, input_nombre, input_apellidos,
                                                                 input_email, botonEnviar,botonMenuPrincipal))
    botonEnviar.pack(anchor=S, side=BOTTOM)


def procesarInfoEditUsuario(root, frame_dni_antiguo, frame_dni, frame_matricula_antiguo, frame_matricula,
                            frame_tarjeta, frame_nombre, frame_apellidos, frame_email,
                            input_dni2, input_dni, input_matricula2, input_matricula,
                            input_tarjeta, input_nombre, input_apellidos, input_email, botonEnviar,botonMenuPrincipal):
    botonMenuPrincipal.destroy()
    dni_antiguo = input_dni2.get()
    matricula_antigua = input_matricula2.get()
    dni = input_dni.get()
    matricula = input_matricula.get()
    tarjeta = input_tarjeta.get()
    nombre = input_nombre.get()
    apellidos = input_apellidos.get()
    email = input_email.get()
    frame_dni_antiguo.destroy()
    frame_dni.destroy()
    frame_matricula_antiguo.destroy()
    frame_matricula.destroy()
    frame_tarjeta.destroy()
    frame_nombre.destroy()
    frame_apellidos.destroy()
    frame_email.destroy()
    botonEnviar.destroy()
    if dni_antiguo.strip() != "" and matricula_antigua.strip() != "" and dni.strip() != "" and matricula.strip() != "" and tarjeta.strip() != "" and nombre.strip() != "" and apellidos.strip() != "" and email.strip() != "":
        resultado = AbonoServicio.edicionCliente(dni_antiguo, matricula_antigua, nombre, apellidos, dni, matricula,
                                                 email, tarjeta)
        if resultado:
            mostrarMensaje(root, "La edición se ha completado con exito")
        else:
            mostrarMensaje(root,
                           f"No se ha encontrado un cliente con dni {dni_antiguo} y matricula de vehículo {matricula_antigua}")
    else:
        messagebox.showinfo(message="Error, todos los cambos deben completarse", title="Error con la información")
        menuGestionAbono(root)
