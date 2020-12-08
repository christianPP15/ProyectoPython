from Servicios import db
from sqlalchemy import Column, Integer, String, Float,Boolean,DateTime,ForeignKey
from sqlalchemy.orm import relationship
class Factura(db.Base):
    __tablename__='Factura'
    id=Column(Integer,primary_key=True)
    __fechaCreacion=Column(DateTime)
    __cliente_id=Column(Integer(),ForeignKey('Cliente.id'))
    __cliente=relationship('Cliente')
    __coste=Column(Float)

    @property
    def fechaCreacion(self):
        return self.__fechaCreacion
    @fechaCreacion.setter
    def fechaCreacion(self,fechaCreacion):
        self.__fechaCreacion=fechaCreacion
    @property
    def cliente(self):
        return self.__cliente
    @cliente.setter
    def cliente(self,cliente):
        self.__cliente=cliente
    @property
    def coste(self):
        return self.__coste
    @coste.setter
    def coste(self,coste):
        self.__coste=coste
    def __str__(self):
        return f"Fecha Creacion -> {self.__fechaCreacion}, Cliente -> {self.__cliente}, Coste -> {self.__coste}"
