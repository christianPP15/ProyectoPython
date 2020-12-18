from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def crearPDF(ticket):
    c = canvas.Canvas("PDF/ticket"+ticket.vehiculo.matricula+".pdf")
    c.setPageSize((300,300))
    c.drawImage("img/icono.png",125,240,width=50, height=50)
    c.setFont("Times-Roman", 15)
    c.drawString(110,220, "Parking salesianos")
    c.drawString(95,205,"Calle Conde de Bustillo")
    c.drawString(30,195,"---------------------------------------------------")
    text = c.beginText(50, 180)
    text.setFont("Times-Roman", 12)
    text.textLine("PIN asociado : "+str(ticket.pin))
    text.textLine(f"Fecha de entrada :{ticket.fechaEntrada.year}/{ticket.fechaEntrada.month}/{ticket.fechaEntrada.day} {ticket.fechaEntrada.hour}:{ticket.fechaEntrada.minute}:{ticket.fechaEntrada.second}")
    text.textLine("Plaza : "+ticket.plaza.identificador)
    text.textLine("Matricula :"+ticket.vehiculo.matricula)
    c.drawText(text)

    tarifas=c.beginText(110,120)
    tarifas.setFont("Times-Roman",9)
    tarifas.textLine(f"El coste por minuto es de {ticket.plaza.coste_minimo} €")
    c.drawText(tarifas)
    c.setFont("Times-Roman",15)
    c.drawString(30,110,"---------------------------------------------------")
    c.setFont("Times-Roman",12)
    c.drawString(50,100,"Gracias por contar con nuestros servicios")
    c.showPage()
    c.save()
