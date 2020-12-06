class Cliente():
    def __init__(self, nombre, apellidos, vehiculo, abono):
        self.__nombre=nombre
        self.__apellidos=apellidos
        self.__vehiculo=vehiculo
        self.__abono=abono
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
