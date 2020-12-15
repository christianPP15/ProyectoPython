from tkinter import *
from tkinter import messagebox

from Controller import IndiceController
from Servicios import AbonoServicio


def menuCaducidadAbono(root):
    botonMenuPrincipalAdmin=Button(root,text="Volver al menú principal",width=20,height=2,command=lambda:volverAlMenuPrincipalCaducidadAbono(root,botonMenuPrincipalAdmin,frame_caducidad_opciones))
    botonMenuPrincipalAdmin.pack(anchor=N,side=LEFT)
    frame_caducidad_opciones=Frame(root,bd=1,relief="groove")
    frame_caducidad_opciones.pack(fill="x",expand=1,anchor=CENTER)
    caducidad_mes=Button(frame_caducidad_opciones,
                            text="Caducidad en un mes concreto",
                            height=4,command=lambda:redirigirCaducidadMeses(root,botonMenuPrincipalAdmin,frame_caducidad_opciones))
    caducidad_mes.pack(side=LEFT,fill="x",expand=1)
    caducidad_dias=Button(frame_caducidad_opciones,
                            text="Caducidad proximos 10 días",
                            height=4,command=lambda:redirigirCaducidadDias(root,botonMenuPrincipalAdmin,frame_caducidad_opciones))
    caducidad_dias.pack(side=RIGHT,fill="x",expand=1)

def volverAlMenuPrincipalCaducidadAbono(root,botonMenuPrincipalAdmin,frame_caducidad_opciones):
    eliminarMenuCaducidadAbono(botonMenuPrincipalAdmin,frame_caducidad_opciones)
    IndiceController.administracion(root)
def eliminarMenuCaducidadAbono(botonMenuPrincipalAdmin,frame_caducidad_opciones):
    botonMenuPrincipalAdmin.destroy()
    frame_caducidad_opciones.destroy()
def redirigirCaducidadMeses(root,botonMenuPrincipalAdmin,frame_caducidad_opciones):
    eliminarMenuCaducidadAbono(botonMenuPrincipalAdmin,frame_caducidad_opciones)
    caducidadMeses(root)
def redirigirCaducidadDias(root,botonMenuPrincipalAdmin,frame_caducidad_opciones):
    eliminarMenuCaducidadAbono(botonMenuPrincipalAdmin,frame_caducidad_opciones)
    caducidadDias(root)
def caducidadMeses(root):
    botonMenuPrincipalAdmin=Button(root,text="Volver al menú administración",width=25,height=2,command=lambda:volverAlMenuPrincipalCaducidadAbonoMes(root,botonMenuPrincipalAdmin,frame_mes,frame_anio,botonEnviar))
    botonMenuPrincipalAdmin.pack(anchor=N,side=LEFT)
    frame_mes = Frame(root, bd=1, relief="groove", width=600)
    frame_mes.pack()
    mes_label = Label(frame_mes, text="Mes del año(1-12):", width=20)
    mes_label.config(padx=10, pady=10)
    mes_label.pack(side=LEFT, fill="x", expand=1)
    input_mes = Entry(frame_mes, width=50)
    input_mes.pack(side=RIGHT, fill="x", expand=1)
    frame_anio=Frame(root, bd=1, relief="groove", width=600)
    frame_anio.pack()
    anio_label=Label(frame_anio, text="Año(formato:yyyy 2020):", width=20)
    anio_label.config(padx=10, pady=10)
    anio_label.pack(side=LEFT, fill="x", expand=1)
    anio_input=Entry(frame_anio, width=50)
    anio_input.pack()
    botonEnviar = Button(root, text="Enviar información", width=50, height=5,command=lambda:redirigirProcesadoInfo(root,botonMenuPrincipalAdmin,frame_mes,frame_anio,botonEnviar,anio_input,input_mes))
    botonEnviar.pack(anchor=S, side=BOTTOM)
def volverAlMenuPrincipalCaducidadAbonoMes(root,botonMenuPrincipalAdmin,frame_mes,frame_anio,botonEnviar):
    botonMenuPrincipalAdmin.destroy()
    frame_mes.destroy()
    frame_anio.destroy()
    botonEnviar.destroy()
    IndiceController.administracion(root)
def redirigirProcesadoInfo(root,botonMenuPrincipalAdmin,frame_mes,frame_anio,botonEnviar,anio_input,input_mes):
    anio=anio_input.get()
    mes=input_mes.get()
    frame_mes.destroy()
    frame_anio.destroy()
    botonEnviar.destroy()
    botonMenuPrincipalAdmin.destroy()
    if anio!="" and mes!="":
        try:
            anio=int(anio)
            mes=int(mes)
            caducidadMesesCompletar(root,anio,mes)
        except ValueError:
            messagebox.showinfo(message="Error, se piden valores numericos, 1-12 para el mes y formato yyyy", title="Error con la información")
            menuCaducidadAbono(root)
    else:
        messagebox.showinfo(message="Error, todos los campos deben ir completos", title="Error con la información")
        caducidadMeses(root)
def caducidadMesesCompletar(root,anio,mes):
    caducados=Label(root, text=AbonoServicio.caducidadAbonoMes(mes, anio))
    caducados.pack()
    botonSalir=Button(root,text="Volver al inicio",command=lambda:volverAlAdministradorCaducidadDias(root,caducados,botonSalir))
    botonSalir.pack()
def caducidadDias(root):
    caducados=Label(root, text=AbonoServicio.caducidadAbonoProximos10Dias())
    caducados.pack()
    botonSalir=Button(root,text="Volver al inicio",command=lambda:volverAlAdministradorCaducidadDias(root,caducados,botonSalir))
    botonSalir.pack()

def volverAlAdministradorCaducidadDias(root,caducados,botonSalir):
    caducados.destroy()
    botonSalir.destroy()
    IndiceController.administracion(root)
