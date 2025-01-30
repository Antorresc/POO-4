from Inmuebles import Inmueble
from enum import Enum

class Tipo(Enum):
    INTERNO = 1
    CALLE = 2
    
class Local(Inmueble):
    def __init__(self, identificadorInmobiliario, área, dirección, tipoLocal: Tipo):
        
        super().__init__(identificadorInmobiliario, área, dirección)
        self._tipoLocal = tipoLocal
        
    def mostrar_resultados(self):
        super().mostrar_resultados()
        print(f"Tipo de local = {self._tipoLocal}")