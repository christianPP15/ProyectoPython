from sqlalchemy.orm import relationship
from Servicios import db
from sqlalchemy import Column, Integer, String, Float,DateTime
class Plaza(db.Base):
    __tablename__='Plaza'
    id=Column(Integer,primary_key=True)
    identificador=Column(String,nullable=True)
    tipo=Column(String)
    costMin=Column(Float)
    def __init__(self,tipo,costMin,identificador):
        self.__identificador=identificador
        self.__ocupado=False
        self.__tipo=tipo
        self.__coste_minimo=costMin
    @property
    def ocupado(self):
        return self.__ocupado
    @ocupado.setter
    def ocupado(self,ocupado):
        self.__ocupado=ocupado
    @property
    def tipo(self):
        return self.__tipo
    @tipo.setter
    def tipo(self,tipo):
        self.__tipo=tipo
    @property
    def coste_minimo(self):
        return self.__coste_minimo
    @coste_minimo.setter
    def coste_minimo(self,coste_minimo):
        self.__coste_minimo=coste_minimo
    @property
    def identificador(self):
        return self.__identificador
    @identificador.setter
    def identificador(self,identificador):
        self.__identificador=identificador
    def __str__(self):
        return f"Identificador -> {self.identificador}, Ocupado -> {self.ocupado}, Tipo -> {self.tipo}, Coste Mínimo -> {self.coste_minimo}"
