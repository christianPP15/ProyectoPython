import random
import datetime

from sqlalchemy.orm import relationship

from Servicios import db
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey


class Ticket(db.Base):
    __tablename__='Ticket'
    id=Column(Integer(),primary_key=True)
    __fechaEntrada=Column(DateTime(), default=datetime.datetime.now())
    __fechaSalida=Column(DateTime())
    __pin=Column(Integer())
    __vehiculo_id=Column(Integer(), ForeignKey('Vehiculos.id'))
    __vehiculo=relationship('Vehiculos')
    __coste=Column(Float())
    __plaza_id=Column(Integer(), ForeignKey('Plaza.id'))
    __plaza=relationship('Plaza')
    @property
    def fechaEntrada(self):
        return self.__fechaEntrada
    @fechaEntrada.setter
    def fechaEntrada(self,fechaEntrada):
        self.__fechaEntrada=fechaEntrada
    @property
    def pin(self):
        return self.__pin
    @pin.setter
    def pin(self,pin):
        self.__pin=pin
    @property
    def fechaSalida(self):
        return self.__fechaSalida
    @fechaSalida.setter
    def fechaSalida(self,fechaSalida):
        self.__fechaSalida=fechaSalida
    @property
    def vehiculo(self):
        return self.__vehiculo
    @vehiculo.setter
    def vehiculo(self,vehiculo):
        self.__vehiculo=vehiculo
    @property
    def coste(self):
        return self.__coste
    @coste.setter
    def coste(self,coste):
        self.__coste=coste
    @property
    def plaza(self):
        return self.__plaza
    @plaza.setter
    def plaza(self,plaza):
        self.__plaza=plaza
    def __str__(self):
        return f"Fecha Inicial -> {self.fechaEntrada}, Fecha Salida -> {self.fechaSalida} , Vehículo -> {self.vehiculo}, Coste -> {self.coste}, Plaza -> {self.plaza}, Pin -> {self.pin}"
