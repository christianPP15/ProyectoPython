from Servicios import db
from sqlalchemy import Column, Integer, String


class Vehiculos(db.Base):
    __tablename__='Vehiculos'
    id=Column(Integer,primary_key=True)
    __matricula=Column(String,nullable=False)
    __tipo=Column(String,nullable=False)
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
