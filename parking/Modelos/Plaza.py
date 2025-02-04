from Servicios import db
from sqlalchemy import Column, Integer, String, Float,Boolean


class Plaza(db.Base):
    __tablename__ = 'Plaza'
    id = Column(Integer, primary_key=True)
    __identificador = Column(String, nullable=True)
    __tipo = Column(String)
    __ocupado=Column(Boolean)
    __reservado=Column(Boolean)
    @property
    def ocupado(self):
        return self.__ocupado

    @ocupado.setter
    def ocupado(self, ocupado):
        self.__ocupado = ocupado

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo

    @property
    def identificador(self):
        return self.__identificador

    @identificador.setter
    def identificador(self, identificador):
        self.__identificador = identificador
    @property
    def reservado(self):
        return self.__reservado
    @reservado.setter
    def reservado(self,reservado):
        self.__reservado=reservado
    def __str__(self):
        return f"Identificador -> {self.identificador}, Ocupado -> {self.ocupado}, Tipo -> {self.tipo}, Coste Mínimo -> {self.coste_minimo}, Reservado -> {self.reservado}"
