from Servicios import db,PlazaServicio
from Modelos import Abono,Plaza
def buscarAbonoPorIdentificadorYpin(pin,identificador):
    abono=db.session.query(Abono.Abono).join(Plaza.Plaza).filter(
        Abono.Abono._Abono__pin==pin
    ).filter(
        Plaza.Plaza._Plaza__identificador==identificador
    ).first()
    plaza=db.session.query(Plaza.Plaza).filter(
        Plaza.Plaza._Plaza__identificador==identificador
    ).first()
    return abono,plaza


