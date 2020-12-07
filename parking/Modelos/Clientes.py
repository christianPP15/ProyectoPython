from Servicios import db
from sqlalchemy import Column, Integer, String, Float,Boolean,DateTime,ForeignKey
from sqlalchemy.orm import relationship
class Cliente(db.Base):
    __tablename__='Cliente'
    id=Column(Integer,primary_key=True)
    __nombre=Column(String,nullable=True)
    __apellidos=Column(String)
    __vehiculo_id=Column(Integer(),ForeignKey('Vehiculos.id'))
    __vehiculo=relationship('Vehiculos')
    __abono_id=Column(Integer(),ForeignKey('Abono.id'))
    __abono=relationship('Abono')
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre=nombre
    @property
    def apellidos(self):
        return self.__apellidos
    @apellidos.setter
    def apellidos(self,apellidos):
        self.__apellidos=apellidos
    @property
    def vehiculo(self):
        return self.__vehiculo
    @vehiculo.setter
    def vehiculo(self,vehiculo):
        self.__vehiculo=vehiculo
    @property
    def abono(self):
        return self.__abono
    @abono.setter
    def abono(self,abono):
        self.__abono=abono
    def __str__(self):
        return f"Nombre -> {self.nombre}, Apellidos -> {self.apellidos}, Vehiculo -> {self.vehiculo}, Abono -> {self.abono}"
