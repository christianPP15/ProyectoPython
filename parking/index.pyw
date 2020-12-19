from Controller import IndiceController
from Servicios import db, PlazaServicio, GeneracionPDF
from tkinter import *
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
db.Base.metadata.drop_all(db.engine)
db.Base.metadata.create_all(db.engine)
PlazaServicio.cargarDatosInicio(50)

root = Tk()
root.title("Gestión Parking")
root.iconbitmap("img/icono.ico")
root.resizable(True, True)
root.geometry("800x400")

IndiceController.indice(root)

root.mainloop()
