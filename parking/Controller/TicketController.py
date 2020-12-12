from tkinter import *
from tkinter import ttk
import time
from Controller import IndiceController
from tkcalendar import Calendar, DateEntry
from Servicios import TicketServicio
def crearCalendario1(root,mensaje,botonCalendario1):
    botonCalendario1.destroy()
    mensaje.destroy()
    top = Toplevel(root)
    cal = Calendar(top,
                   font="Arial 14", selectmode='day',
                   cursor="hand1", year=2020, month=12, day=12)
    cal.pack(fill="both", expand=True)
    ttk.Button(top, text="ok", command=lambda:procesarFecha1(root,cal,top)).pack()
def facturacion_datos(root):
    mensaje=Label(root,text="Vamos a seleccionar dos fechas para consultar los datos")
    mensaje.pack()
    botonCalendario1 = Button(root, text="Elegir primera fecha", width=50, height=5,command=lambda:crearCalendario1(root,mensaje,botonCalendario1))
    botonCalendario1.pack(anchor=N, side=TOP)
def crearCalendario2(root,mensaje,botonCalendario2,fecha1):
    botonCalendario2.destroy()
    mensaje.destroy()
    top = Toplevel(root)
    cal = Calendar(top,
                   font="Arial 14", selectmode='day',
                   cursor="hand1", year=2020, month=12, day=12)
    cal.pack(fill="both", expand=True)
    ttk.Button(top, text="ok", command=lambda:procesarFecha2(root,cal,top,fecha1)).pack()
def procesarFecha2(root,cal,top,fecha1):
    fecha2=cal.selection_get()
    cal.destroy()
    top.destroy()
    info=TicketServicio.facturacion(fecha1.year,fecha1.month,fecha1.day,fecha2.year,fecha2.month,fecha2.day)
    mensaje=Label(root,text=info)
    mensaje.pack()
    volver_inicio = Button(root, text="Volver al inicio",
                               command=lambda: borrarDatosVolverAdmin(root,mensaje,volver_inicio))
    volver_inicio.pack()
def procesarFecha1(root,cal,top):
    fecha1=cal.selection_get()
    cal.destroy()
    top.destroy()
    mensaje=Label(root,text="Vamos a seleccionar la segunda fecha")
    mensaje.pack()
    botonCalendario2 = Button(root, text="Elegir segunda fecha", width=50, height=5,command=lambda:crearCalendario2(root,mensaje,botonCalendario2,fecha1))
    botonCalendario2.pack(anchor=N, side=TOP)

def borrarDatosVolverAdmin(root,mensaje,volver_inicio):
    mensaje.destroy()
    volver_inicio.destroy()
    IndiceController.administracion(root)
