from tkinter import *
from tkinter import messagebox

from Controller import IndiceController
from Servicios import ClienteServicio


def depositarAbonado(root):
    botonMenuPrincipal=Button(root,text="Volver al menú principal",width=20,height=2,command=lambda:volverMenuPrincipalGuardarVehiculoSinAbono(root,botonMenuPrincipal,frame_matricula,frame_dni,botonEnviar))
    botonMenuPrincipal.pack(anchor=N,side=LEFT)
    frame_matricula = Frame(root, bd=1, relief="groove", width=600)
    frame_matricula.pack()
    matricula_label = Label(frame_matricula, text="Matricula:",width=20)
    matricula_label.config(padx=10, pady=10)
    matricula_label.pack(side=LEFT, fill="x", expand=1)
    input_matricula = Entry(frame_matricula,width=50)
    input_matricula.pack(side=RIGHT, fill="x", expand=1)
    frame_dni=Frame(root, bd=1, relief="groove", width=600)
    frame_dni.pack()
    dni_label= Label(frame_dni, text="DNI:",width=20)
    dni_label.config(padx=10, pady=10)
    dni_label.pack(side=LEFT, fill="x", expand=1)
    input_dni=Entry(frame_dni,width=50)
    input_dni.pack(side=RIGHT, fill="x", expand=1)
    botonEnviar = Button(root, text="Enviar información", width=50, height=5,command=lambda:procesarInformacionGuardarVehiculoBono(root,botonMenuPrincipal,frame_matricula,frame_dni,botonEnviar,input_dni,input_matricula))
    botonEnviar.pack(anchor=S, side=BOTTOM)
def volverMenuPrincipalGuardarVehiculoSinAbono(root,botonMenuPrincipal,frame_matricula,frame_dni,botonEnviar):
    botonMenuPrincipal.destroy()
    frame_dni.destroy()
    frame_matricula.destroy()
    botonEnviar.destroy()
    IndiceController.indice(root)

def procesarInformacionGuardarVehiculoBono(root,botonMenuPrincipal,frame_matricula,frame_dni,botonEnviar,input_dni,input_matricula):
    dni=input_dni.get()
    matricula=input_matricula.get()
    botonMenuPrincipal.destroy()
    frame_matricula.destroy()
    frame_dni.destroy()
    botonEnviar.destroy()
    input_matricula.destroy()
    input_dni.destroy()
    if dni!="" and matricula!="":
        mensaje= ClienteServicio.depositarAbonados(matricula, dni)
        mensajeFinal=Label(root,text=mensaje)
        mensajeFinal.pack()
        volverMenuPrincipalBoton=Button(root,text="Volver al menú principal",command=lambda:volverAlMenuPrincipalTrasCompletar(root,mensajeFinal,volverMenuPrincipalBoton))
        volverMenuPrincipalBoton.pack()
    else:
        messagebox.showinfo(message="Error, todos los campos deben ir completos", title="Error con la información")
        depositarAbonado(root)

def volverAlMenuPrincipalTrasCompletar(root,mensajeFinal,volverMenuPrincipalBoton):
    mensajeFinal.destroy()
    volverMenuPrincipalBoton.destroy()
    IndiceController.indice(root)


def retirarVehiculoAbonado(root):
    botonMenuPrincipal=Button(root,text="Volver al menú principal",width=20,height=2,command=lambda:volverAlMenuPrincipalDesdeRetirar(root,botonMenuPrincipal,frame_matricula,frame_dni,botonEnviar,frame_iden))
    botonMenuPrincipal.pack(anchor=N,side=LEFT)
    frame_matricula = Frame(root, bd=1, relief="groove", width=600)
    frame_matricula.pack()
    matricula_label = Label(frame_matricula, text="Matricula:",width=20)
    matricula_label.config(padx=10, pady=10)
    matricula_label.pack(side=LEFT, fill="x", expand=1)
    input_matricula = Entry(frame_matricula,width=50)
    input_matricula.pack(side=RIGHT, fill="x", expand=1)
    frame_dni=Frame(root, bd=1, relief="groove", width=600)
    frame_dni.pack()
    dni_label= Label(frame_dni, text="DNI:",width=20)
    dni_label.config(padx=10, pady=10)
    dni_label.pack(side=LEFT, fill="x", expand=1)
    input_dni=Entry(frame_dni,width=50)
    input_dni.pack(side=RIGHT, fill="x", expand=1)
    frame_iden=Frame(root, bd=1, relief="groove", width=600)
    frame_iden.pack()
    identificador_label= Label(frame_iden, text="Pin:",width=20)
    identificador_label.config(padx=10, pady=10)
    identificador_label.pack(side=LEFT, fill="x", expand=1)
    input_pin=Entry(frame_iden,width=50)
    input_pin.pack(side=RIGHT, fill="x", expand=1)
    botonEnviar = Button(root, text="Enviar información", width=50, height=5,command=lambda:procesarInformacionRetirarVehiculoAbono(root,frame_iden,input_pin,botonMenuPrincipal,frame_matricula,frame_dni,botonEnviar,input_dni,input_matricula))
    botonEnviar.pack(anchor=S, side=BOTTOM)

def volverAlMenuPrincipalDesdeRetirar(root,botonMenuPrincipal,frame_matricula,frame_dni,botonEnviar,frame_iden):
    botonMenuPrincipal.destroy()
    frame_dni.destroy()
    frame_matricula.destroy()
    frame_iden.destroy()
    botonEnviar.destroy()
    IndiceController.indice(root)

def procesarInformacionRetirarVehiculoAbono(root,frame_iden,input_pin,botonMenuPrincipal,frame_matricula,frame_dni,botonEnviar,input_dni,input_matricula):
    dni=input_dni.get()
    matricula=input_matricula.get()
    pin=input_pin.get()
    frame_iden.destroy()
    frame_matricula.destroy()
    frame_dni.destroy()
    botonEnviar.destroy()
    botonMenuPrincipal.destroy()
    if dni!="" and matricula!="" and pin!="":
        mensaje= ClienteServicio.retirarAbono(matricula, dni, pin)
        mensajeFinal=Label(root,text=mensaje)
        mensajeFinal.pack()
        volverMenuPrincipalBoton=Button(root,text="Volver al menú principal",command=lambda:volverAlMenuPrincipalTrasCompletar(root,mensajeFinal,volverMenuPrincipalBoton))
        volverMenuPrincipalBoton.pack()
    else:
        messagebox.showinfo(message="Error, todos los campos deben ir completos", title="Error con la información")
        retirarVehiculoAbonado(root)
