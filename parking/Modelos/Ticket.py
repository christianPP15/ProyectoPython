import random
import datetime

from sqlalchemy.orm import relationship

from Servicios import db
from sqlalchemy import Column, Integer, String, Float,DateTime
class Ticket(db.Base):
    __tablename__='Ticket'
    id=Column(Integer,primary_key=True)
    fechaEntrada=Column(DateTime)
    fechaSalida=Column(DateTime)
    pin=Column(Integer)
    matricula=Column(String)
    coste=Column(Float)
    plaza=relationship(Integer,secondary='Plaza')
    def __init__(self,matricula,plaza):
        self.__fechaEntrada=datetime.datetime.now()
        self.__pin=random.randint(111111,999999)
        self.__fechaSalida=None
        self.__matricula=matricula
        self.__coste=0
        self.__plaza=plaza
    @property
    def fechaEntrada(self):
        return self.__fechaEntrada
    @fechaEntrada.setter
    def fechaEntrada(self,fechaEntrada):
        self.__fechaEntrada=fechaEntrada
    @property
    def pin(self):
        return self.__pin
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
    def __str__(self):
        return f"Fecha Inicial -> {self.fechaEntrada}, Fecha Salida -> {self.fechaSalida} , Matricula -> {self.matricula}, Coste -> {self.coste}, Plaza -> {self.plaza}, Pin -> {self.pin}"
