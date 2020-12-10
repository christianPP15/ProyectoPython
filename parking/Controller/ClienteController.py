from tkinter import *
from tkinter import messagebox
from Controller import IndiceController
from Servicios import ClienteServicio
from Servicios import PlazaServicio
def ocultarPrincipal(frame1,frame2,menuSuperiorTexto,frame_informacion_parking):
    frame1.destroy()
    frame2.destroy()
    menuSuperiorTexto.destroy()
    frame_informacion_parking.destroy()

def guardarVehiculo(root,frame1,frame2,menuSuperiorTexto,frame_informacion_parking):
    var=IntVar()
    ocultarPrincipal(frame1,frame2,menuSuperiorTexto,frame_informacion_parking)
    frame_campos=Frame(root,bd=1,relief="groove",width=600)
    frame_campos.pack()
    nombre_label= Label(frame_campos, text="Matricula:")
    nombre_label.config(padx=10, pady=10)
    nombre_label.pack(side=LEFT,fill="x",expand=1)
    input_nombre=Entry(frame_campos)
    input_nombre.pack(side=RIGHT,fill="x",expand=1)
    frame_tipos=Frame(root,bd=1,relief="groove",width=600)
    frame_tipos.pack()
    checkbox_turismo=Radiobutton(frame_tipos,text="Turismo",variable=var,value=1).pack()
    checkbox_moto=Radiobutton(frame_tipos,text="Motocicleta",variable=var,value=2).pack()
    checkbox_movilidad=Radiobutton(frame_tipos,text="Movilidad reducida",variable=var,value=3).pack()
    botonEnviar=Button(root,text="Enviar información",width=50,height=5,command=lambda:obtenerDatos(root,frame1,frame2,frame_campos,frame_tipos,var,botonEnviar,input_nombre))
    botonEnviar.pack(anchor=S,side=BOTTOM)

def borrarBotonEInfo(boton,info,texto,root):
    boton.destroy()
    info.destroy()
    texto.destroy()
    IndiceController.indice(root)
def obtenerDatos(root,frame1,frame2,frame_campos,frame_tipos,opcion,boton,matricula):
    frame_tipos.pack_forget()
    frame_campos.pack_forget()
    boton.pack_forget()
    if opcion.get()!=0 and matricula.get()!="":
        informacion_ticket=Frame(root,
                         width=500,
                         height=100,
                         bd=3,
                         relief="groove")
        informacion_ticket.pack()
        textoInformacion=Label(informacion_ticket,foreground="black",text=ClienteServicio.depositarVehiculo(opcion.get(),matricula.get()))
        textoInformacion.pack(anchor=N)
        volver_inicio=Button(root,text="Volver al inicio",command=lambda:borrarBotonEInfo(volver_inicio,informacion_ticket,textoInformacion,root))
        volver_inicio.pack()
    else:
        guardarVehiculo(root,frame1,frame2)
        messagebox.showinfo(message="Error, todos los campos deben ir completos", title="Error con la información")



