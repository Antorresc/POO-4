from Apartamento import Apartamento

class Apartaestudio(Apartamento):
    def __init__(self, identificadorInmobiliario, área, dirección, númeroHabitaciones=1, númeroBaños=1):
        super().__init__(identificadorInmobiliario, área, dirección, númeroHabitaciones, númeroBaños)
        self._valorArea = 1500000
        
    def mostrar_resultados(self):
        super().mostrar_resultados()
        print()