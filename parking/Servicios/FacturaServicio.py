from Repositorios import FacturaRepository
def calcularFacturasAnio():
    anio=int(input("¿De que año desea consultar la facturación? "))
    facturas=FacturaRepository.facturasAnio(anio)
    precio=0
    for i in facturas:
        precio+=i.coste
    print(f"El total de facturas del año {anio} es de {len(facturas)} por los cuales se ha ganado un total de {precio}")
