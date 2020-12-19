from Servicios import db
from sqlalchemy import Column, Integer, String, ForeignKey


class Vehiculos(db.Base):
    __tablename__='Vehiculos'
    id=Column(Integer,primary_key=True)
    __matricula=Column(String,nullable=False)
    type = Column(String(50))
    __mapper_args__ = {
        'polymorphic_on':type
    }
    @property
    def matricula(self):
        return self.__matricula
    @matricula.setter
    def matricula(self,matricula):
        self.__matricula=matricula
    def __str__(self):
        return f"Matricula -> {self.matricula}"

class Turismo(Vehiculos):
    __mapper_args__ = {
        'polymorphic_identity':'Turismo',
    }
    __tablename__ = 'Turismo'
    id = Column(None, ForeignKey('Vehiculos.id'), primary_key=True)





class Motocicleta(Vehiculos):
    __tablename__ = 'Motocicleta'
    id = Column(None, ForeignKey('Vehiculos.id'), primary_key=True)
    __mapper_args__ = {
        'polymorphic_identity':'Motocicleta',
    }

class MovilidadReducida(Vehiculos):
    __tablename__ = 'MovilidadReducida'
    id = Column(None, ForeignKey('Vehiculos.id'), primary_key=True)
    __mapper_args__ = {
        'polymorphic_identity':'MovilidadReducida',
    }
