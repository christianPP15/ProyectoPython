from tkinter import *
from tkinter import messagebox

from Controller import IndiceController
from Servicios import FacturaServicio


def consultaAbono(root):
    botonMenuAdmin=Button(root,text="Volver al menú de administrador",width=25,height=2,command=lambda:volverAlMenuAdministrador(root,frame_contra,label_anio,input_anio,botonEnviar,botonMenuAdmin))
    botonMenuAdmin.pack(anchor=N,side=LEFT)
    frame_contra = Frame(root, bd=1, relief="groove", width=600)
    frame_contra.pack()
    label_anio = Label(frame_contra, text="Año a comprobar:", width=20)
    label_anio.config(padx=10, pady=10)
    label_anio.pack(side=LEFT, fill="x", expand=1)
    input_anio = Entry(frame_contra, width=50)
    input_anio.pack( fill="x", expand=1)
    botonEnviar = Button(root, text="Consultar datos", width=50, height=5,command=lambda:verificarAnio(root,frame_contra,label_anio,input_anio,botonEnviar,botonMenuAdmin))
    botonEnviar.pack(anchor=S, side=BOTTOM)

def eliminarFormularioConsulta(frame_contra,label_anio,input_anio,botonEnviar,botonMenuAdmin):
    frame_contra.destroy()
    label_anio.destroy()
    input_anio.destroy()
    botonEnviar.destroy()
    botonMenuAdmin.destroy()

def volverAlMenuAdministrador(root,frame_contra,label_anio,input_anio,botonEnviar,botonMenuAdmin):
    eliminarFormularioConsulta(frame_contra,label_anio,input_anio,botonEnviar,botonMenuAdmin)
    IndiceController.administracion(root)
def volverAlMenuAdministracionTrasConsultar(root,frame_informacion_consulta,textoInformacion,volverAdmin):
    frame_informacion_consulta.destroy()
    textoInformacion.destroy()
    volverAdmin.destroy()
    IndiceController.administracion(root)
def verificarAnio(root,frame_contra,label_anio,input_anio,botonEnviar,botonMenuAdmin):
    anio=input_anio.get()
    eliminarFormularioConsulta(frame_contra,label_anio,input_anio,botonEnviar,botonMenuAdmin)
    if anio!="":
        frame_informacion_consulta=Frame(root,
                             width=500,
                             height=100,
                             bd=3,
                             relief="groove")
        frame_informacion_consulta.pack()
        textoInformacion=Label(frame_informacion_consulta,foreground="black",text=FacturaServicio.calcularFacturasAnio(anio))
        textoInformacion.pack(anchor=N)
        volverAdmin = Button(root, text="Consultar datos", width=50, height=5,command=lambda:volverAlMenuAdministracionTrasConsultar(root,frame_informacion_consulta,textoInformacion,volverAdmin))
        volverAdmin.pack(anchor=N, side=TOP)
    else:
        messagebox.showinfo(message="Error, el campo año debe ir completo", title="Error con la información")
        consultaAbono(root)
