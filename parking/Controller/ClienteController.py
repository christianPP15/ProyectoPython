from tkinter import *
def ocultarPrincipal(boton1,boton2):
    boton1.pack_forget()
    boton2.pack_forget()

def guardarVehiculo(root,boton1,boton2):
    ocultarPrincipal(boton1,boton2)
    botonEnviar=Button(root,text="Enviar información",width=50,height=5)
    botonEnviar.pack()
