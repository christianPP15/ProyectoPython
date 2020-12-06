from Modelos import Plaza
class Parking():
    def __init__(self):
        cadena=["Turismo", "Moto", "Movilidad reducida"]
        precio=[0.12,0.08,0.10];
        self.__turismos=[]
        self.__motos=[]
        self.__movilidad_reducida=[]
        for i in range(34):
            turismo=Plaza.Plaza(cadena[0],precio[0])
            self.__turismos.append(turismo)
        for i in range(8):
            moto=Plaza.Plaza(cadena[1],precio[1])
            self.__motos.append(moto)
        for i in range(8):
            movilidad=Plaza.Plaza(cadena[2],cadena[2])
            self.__movilidad_reducida.append(movilidad)

    @property
    def turismos(self):
        return self.__turismos
    @property
    def motos(self):
        return self.__motos
    @property
    def movilidad(self):
        return self.__movilidad_reducida

