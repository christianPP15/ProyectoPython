from Modelos import Parking
from Repositorios import ParkingRepository
def mostrarDisponibilidad(parking):
    turismos=parking.turismos
    motos=parking.motos
    movilidad=parking.movilidad
    print(f'Existen un total de {ParkingRepository.totalPlazas(parking)}')
    print(f"Encontramos disponibles {ParkingRepository.contadorPlazasLibres(turismos)} plazas para turismo")
    print(f"Encontramos disponibles {ParkingRepository.contadorPlazasLibres(motos)} plazas para motos")
    print(f"Encontramos disponibles {ParkingRepository.contadorPlazasLibres(movilidad)} plazas para movilidad reducida")
