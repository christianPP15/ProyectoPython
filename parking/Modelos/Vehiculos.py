from Servicios import db
from sqlalchemy import Column, Integer, String, Float
class Vehiculos(db.Base):
    __tablename__='Vehículos'
    id=Column(Integer,primary_key=True)
    matricula=Column(String,nullable=False)
    tipo=Column(String,nullable=False)
    def __init__(self,matricula,tipo):
        self.__matricula=matricula
        self.__tipo=tipo
    @property
    def matricula(self):
        return self.__matricula
    @matricula.setter
    def matricula(self,matricula):
        self.__matricula=matricula
    @property
    def tipo(self):
        return self.__tipo
    @tipo.setter
    def tipo(self,tipo):
        self.__tipo=tipo
    def __str__(self):
        return f"Matricula -> {self.matricula}, Tipo -> {self.tipo}"
