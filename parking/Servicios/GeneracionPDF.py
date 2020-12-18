from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def crearPDF(ticket):
    w, h = A4
    c = canvas.Canvas("PDF/ticket"+ticket.vehiculo.matricula+".pdf", pagesize=A4)
    c.drawImage("img/icono.png",260,h-90,width=50, height=50)
    c.drawString(240,h-110, "Parking salesianos")
    c.drawString(230,h-125,"Calle Conde de Bustillo")
    text = c.beginText(30, h - 190)
    text.setFont("Times-Roman", 12)
    text.textLine("PIN asociado : "+str(ticket.pin))
    text.textLine(f"Fecha de entrada :{ticket.fechaEntrada.year}/{ticket.fechaEntrada.month}/{ticket.fechaEntrada.day} {ticket.fechaEntrada.hour}:{ticket.fechaEntrada.minute}:{ticket.fechaEntrada.second}")
    text.textLine("Plaza : "+ticket.plaza.identificador)
    text.textLine("Matricula :"+ticket.vehiculo.matricula)
    c.drawText(text)

    tarifas=c.beginText(30,h-260)
    tarifas.setFont("Times-Roman",9)
    tarifas.textLine(f"El coste por minuto es de {ticket.plaza.coste_minimo} € para convertirse en abonado hable con el administrador")
    c.drawText(tarifas)
    c.showPage()
    c.save()
