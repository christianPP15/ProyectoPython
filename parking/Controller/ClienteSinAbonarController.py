from tkinter import *
from tkinter import messagebox
from Controller import IndiceController
from Servicios import ClienteServicio
from Servicios import PlazaServicio

def volverMenuPrincipalGuardarVehiculoSinAbono(root, frame_campos, frame_tipos, botonEnviar,botonMenuPrincipal):
    frame_tipos.pack_forget()
    frame_campos.pack_forget()
    botonEnviar.pack_forget()
    botonMenuPrincipal.pack_forget()
    IndiceController.indice(root)
def guardarVehiculo_obtenerInfo(root):
    botonMenuPrincipal=Button(root,text="Volver al menú principal",width=20,height=2,command=lambda:volverMenuPrincipalGuardarVehiculoSinAbono(root, frame_campos, frame_tipos, botonEnviar,botonMenuPrincipal))
    botonMenuPrincipal.pack(anchor=N,side=LEFT)
    var = IntVar()
    frame_campos = Frame(root, bd=1, relief="groove", width=100)
    frame_campos.pack()
    nombre_label = Label(frame_campos, text="Matricula:")
    nombre_label.config(padx=10, pady=10)
    nombre_label.pack(side=LEFT, fill="x", expand=1)
    input_nombre = Entry(frame_campos)
    input_nombre.pack(side=RIGHT, fill="x", expand=1)
    frame_tipos = Frame(root, bd=1, relief="groove", width=100)
    frame_tipos.pack()
    checkbox_turismo = Radiobutton(frame_tipos, text="Turismo", variable=var, value=1).pack()
    checkbox_moto = Radiobutton(frame_tipos, text="Motocicleta", variable=var, value=2).pack()
    checkbox_movilidad = Radiobutton(frame_tipos, text="Movilidad reducida", variable=var, value=3).pack()
    botonEnviar = Button(root, text="Enviar información", width=50, height=5,
                         command=lambda: guardarVehiculo_UsarInfo(root, frame_campos, frame_tipos, var, botonEnviar,
                                                                  input_nombre))
    botonEnviar.pack(anchor=S, side=BOTTOM)

def borrarBotonEInfo(boton, info, texto, root):
    boton.destroy()
    info.destroy()
    texto.destroy()
    IndiceController.indice(root)


def guardarVehiculo_UsarInfo(root, frame_campos, frame_tipos, opcion, boton, matricula):
    frame_tipos.pack_forget()
    frame_campos.pack_forget()
    boton.pack_forget()
    if opcion.get() != 0 and matricula.get() != "":
        informacion_ticket = Frame(root,
                                   width=500,
                                   height=100,
                                   bd=3,
                                   relief="groove")
        informacion_ticket.pack()
        textoInformacion = Label(informacion_ticket, foreground="black",
                                 text=ClienteServicio.depositarVehiculo(opcion.get(), matricula.get().upper()))
        textoInformacion.pack(anchor=N)
        volver_inicio = Button(root, text="Volver al inicio",
                               command=lambda: borrarBotonEInfo(volver_inicio, informacion_ticket, textoInformacion,
                                                                root))
        volver_inicio.pack()
    else:
        guardarVehiculo_obtenerInfo(root)
        messagebox.showinfo(message="Error, todos los campos deben ir completos", title="Error con la información")

def volverMenuPrincipalRetirarVehiculoSinAbono(root, frame_matricula, frame_pin, frame_identificador,botonEnviar, input_identificador, input_matricula,input_pin,botonMenuPrincipal):
    frame_matricula.destroy()
    frame_pin.destroy()
    frame_identificador.destroy()
    botonEnviar.destroy()
    input_pin.destroy()
    botonMenuPrincipal.destroy()
    input_matricula.destroy()
    input_identificador.destroy()
    IndiceController.indice(root)
def retirarVehiculoObtenerInfo(root):
    botonMenuPrincipal=Button(root,text="Volver al menú principal",width=20,height=2,command=lambda:volverMenuPrincipalRetirarVehiculoSinAbono(root, frame_matricula, frame_pin, frame_identificador,botonEnviar, input_identificador, input_matricula,input_pin,botonMenuPrincipal))
    botonMenuPrincipal.pack(anchor=N,side=LEFT)
    frame_matricula = Frame(root, bd=1, relief="groove", width=600)
    frame_matricula.pack()
    frame_pin = Frame(root, bd=1, relief="groove", width=600)
    frame_pin.pack()
    frame_identificador = Frame(root, bd=1, relief="groove", width=600)
    frame_identificador.pack()
    matricula_label = Label(frame_matricula, text="Matricula de su vehículo:", width=20)
    matricula_label.config(padx=10, pady=10)
    matricula_label.pack(side=LEFT, fill="x", expand=1)
    input_matricula = Entry(frame_matricula, width=50)
    input_matricula.pack(side=RIGHT, fill="x", expand=1)
    pin_label = Label(frame_pin, text="PIN:", width=20)
    pin_label.config(padx=10, pady=10)
    pin_label.pack(side=LEFT, fill="x", expand=1)
    input_pin = Entry(frame_pin, width=50)
    input_pin.pack(side=RIGHT, fill="x", expand=1)
    identificador_label = Label(frame_identificador, text="Identificador:", width=20)
    identificador_label.config(padx=10, pady=10)
    identificador_label.pack(side=LEFT, fill="x", expand=1)
    input_identificador = Entry(frame_identificador, width=50)
    input_identificador.pack(side=RIGHT, fill="x", expand=1)
    botonEnviar = Button(root, text="Enviar información", width=50, height=5,
                         command=lambda: procesarDatosRetirada(root, frame_matricula, frame_pin, frame_identificador,
                                                               botonEnviar, input_identificador, input_matricula,
                                                               input_pin,botonMenuPrincipal))
    botonEnviar.pack(anchor=S, side=BOTTOM)


def procesarDatosRetirada(root, frame_matricula, frame_pin, frame_identificador, botonEnviar, input_identificador,
                          input_matricula, input_pin,botonMenuPrincipal):
    identificador = input_identificador.get()
    matricula = input_matricula.get()
    pin = input_pin.get()
    frame_matricula.destroy()
    frame_pin.destroy()
    frame_identificador.destroy()
    botonEnviar.destroy()
    input_pin.destroy()
    input_matricula.destroy()
    input_identificador.destroy()
    botonMenuPrincipal.destroy()
    obtenerYprocesarInformacionRetirarVehiculoNoAbonado(root, identificador, matricula, pin)


def obtenerYprocesarInformacionRetirarVehiculoNoAbonado(root, identificador, matricula, pin):
    if matricula != "" and identificador != "" and pin != "":
        operacion=ClienteServicio.retirarVehiculo(matricula.upper(), pin, identificador.lower())
        if operacion:
            messagebox.showinfo(message="Retirada, completada con exito", title="Retirada")
            IndiceController.indice(root)
        else:
            messagebox.showinfo(message="Error, los campos no coinciden", title="Error con la información")
            retirarVehiculoObtenerInfo(root)
    else:
        messagebox.showinfo(message="Error, todos los campos deben ir completos", title="Error con la información")
        retirarVehiculoObtenerInfo(root)
