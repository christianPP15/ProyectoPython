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
    __matricula=Column(String(7))
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
    def matricula(self):
        return self.__matricula
    @matricula.setter
    def matricula(self,matricula):
        self.__matricula=matricula
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
        return f"Fecha Inicial -> {self.fechaEntrada}, Fecha Salida -> {self.fechaSalida} , Matricula -> {self.matricula}, Coste -> {self.coste}, Plaza -> {self.plaza}, Pin -> {self.pin}"
