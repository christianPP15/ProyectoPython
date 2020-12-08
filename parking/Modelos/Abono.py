import random
from Servicios import db
from sqlalchemy import Column, Integer, String, Float,Boolean,DateTime,ForeignKey
from sqlalchemy.orm import relationship
class Abono(db.Base):
    __tablename__ = 'Abono'
    id=Column(Integer,primary_key=True)
    __fechaInicial=Column(DateTime)
    __fechaFinal=Column(DateTime)
    __precio=Column(Float)
    __pin=Column(Integer)
    __meses=Column(Integer)
    __plaza_id=Column(Integer(), ForeignKey('Plaza.id'))
    __plaza=relationship('Plaza')
    @property
    def fechaInicial(self):
        return self.__fechaInicial
    @fechaInicial.setter
    def fechaInicial(self,fechaInicial):
        self.__fechaInicial=fechaInicial
    @property
    def fechaFinal(self):
        return self.__fechaFinal
    @fechaFinal.setter
    def fechaFinal(self,fechaFinal):
        self.__fechaFinal=fechaFinal
    @property
    def precio(self):
        return self.__precio
    @precio.setter
    def precio(self,precio):
        self.__precio=precio
    @property
    def pin(self):
        return self.__pin
    @pin.setter
    def pin(self,pin):
        self.__pin=pin
    @property
    def meses(self):
        return self.__meses
    @meses.setter
    def meses(self,meses):
        self.__meses=meses
    @property
    def plaza(self):
        return self.__plaza
    @plaza.setter
    def plaza(self,plaza):
        self.__plaza=plaza
    def __str__(self):
        return f"Fecha Inicial -> {self.fechaInicial},Fecha Final -> {self.fechaFinal}, Precio -> {self.precio}, Pin -> {self.pin}"



def __definir_pin__():
    return random.randint(111111,999999)



