from sqlalchemy.orm import relationship
from Servicios import db
from sqlalchemy import Column, Integer, String, Float,Boolean


class Plaza(db.Base):
    __tablename__ = 'Plaza'
    id = Column(Integer, primary_key=True)
    __identificador = Column(String, nullable=True)
    __tipo = Column(String)
    __coste_minimo = Column(Float)
    __ocupado=Column(Boolean)
    @property
    def ocupado(self):
        return self.__ocupado

    @ocupado.setter
    def ocupado(self, ocupado):
        self.__ocupado = ocupado

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo

    @property
    def coste_minimo(self):
        return self.__coste_minimo

    @coste_minimo.setter
    def coste_minimo(self, coste_minimo):
        self.__coste_minimo = coste_minimo

    @property
    def identificador(self):
        return self.__identificador

    @identificador.setter
    def identificador(self, identificador):
        self.__identificador = identificador

    def __str__(self):
        return f"Identificador -> {self.identificador}, Ocupado -> {self.ocupado}, Tipo -> {self.tipo}, Coste Mínimo -> {self.coste_minimo}"
