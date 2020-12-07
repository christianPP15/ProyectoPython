from Modelos import Plaza
from sqlalchemy.orm import relationship
from Servicios import db
from sqlalchemy import Column, Integer, String, Float,Boolean
class Parking():
    #__tablename__ = 'Parking'
    #id=Column(Integer,primary_key=True)
    #__turismos=relationship('Plaza',Column(ARRAY))
    #__motos=relationship('Plaza',Column(ARRAY))
    #__movilidad=relationship('Plaza',Column(ARRAY))
    def __init__(self):
        cadena=["Turismo", "Moto", "Movilidad reducida"]
        precio=[0.12,0.08,0.10];
        self.__turismos=[]
        self.__motos=[]
        self.__movilidad_reducida=[]
        for i in range(34):
            turismo=Plaza.Plaza(tipo=cadena[0],coste_minimo=precio[0],identificador='t'+str(i+1),ocupado=False)
            self.__turismos.append(turismo)
        for i in range(8):
            moto=Plaza.Plaza(tipo=cadena[1],coste_minimo=precio[1],identificador='m'+str(i+1),ocupado=False)
            self.__motos.append(moto)
        for i in range(8):
            movilidad=Plaza.Plaza(tipo=cadena[2],coste_minimo=cadena[2],identificador='r'+str(i+1),ocupado=False)
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
    def __str__(self):
        return f"Plazas de turismo -> {self.turismos}, Plazas motos -> {self.motos}, Plazas movilidad reducida -> {self.movilidad}"
