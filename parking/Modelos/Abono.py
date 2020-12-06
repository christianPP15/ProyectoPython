import random
class Abono():
    def __init__(self,fechaInicial,fechaFinal,precio):
        self.__fechaInicial=fechaInicial
        self.__fechaFinal=fechaFinal
        self.__precio=precio
        self.__pin=__definir_pin__()

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
    def __str__(self):
        return f"Fecha Inicial -> {self.fechaInicial},Fecha Final -> {self.fechaFinal}, Precio -> {self.precio}, Pin -> {self.pin}"



def __definir_pin__():
    return random.randint(111111,999999)



