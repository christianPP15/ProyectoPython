import random
from Servicios import db
from sqlalchemy import Column, Integer, String, Float,Boolean,DateTime
class Abono(db.Base):
    __tablename__ = 'Abono'
    id=Column(Integer,primary_key=True)
    __fechaInicial=Column(DateTime)
    __fechaFinal=Column(DateTime)
    __precio=Column(Float)
    __pin=Column(Integer)
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
    def __str__(self):
        return f"Fecha Inicial -> {self.fechaInicial},Fecha Final -> {self.fechaFinal}, Precio -> {self.precio}, Pin -> {self.pin}"



def __definir_pin__():
    return random.randint(111111,999999)



