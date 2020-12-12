from Repositorios import FacturaRepository
def calcularFacturasAnio(anio):
    facturas=FacturaRepository.facturasAnio(anio)
    precio=0
    for i in facturas:
        precio+=i.coste
    return f"El total de facturas del año {anio} es de {len(facturas)} por los cuales se ha ganado un total de {precio}€"
