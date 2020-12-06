class Plaza():
    def __init__(self,tipo,costMin):
        self.__ocupado=False
        self.__tipo=tipo
        self.__coste_minimo=costMin
    @property
    def ocupado(self):
        return self.__ocupado
    @ocupado.setter
    def ocupado(self,ocupado):
        self.__ocupado=ocupado
    @property
    def tipo(self):
        return self.__tipo
    @tipo.setter
    def tipo(self,tipo):
        self.__tipo=tipo
    @property
    def coste_minimo(self):
        return self.__coste_minimo
    @coste_minimo.setter
    def coste_minimo(self,coste_minimo):
        self.__coste_minimo=coste_minimo
