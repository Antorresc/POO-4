from Inmuebles import Inmueble

class InmuebleVivienda(Inmueble):
    def __init__(self, identificadorInmobiliario, área, dirección, númeroHabitaciones, númeroBaños):
        super().__init__(identificadorInmobiliario, área, dirección)
        
        self._númeroHabitaciones = númeroHabitaciones
        self._númeroBaños = númeroBaños
    
    def mostrar_resultados(self):
        super().mostrar_resultados()
        print(f"Número de habitaciones = {self._númeroHabitaciones}")
        print(f"Número de Baños = {self._númeroBaños}")