from Apartamento import Apartamento

class ApartamentoFamiliar(Apartamento):
    def __init__(self, identificadorInmobiliario, área, dirección, númeroHabitaciones, númeroBaños, valorAdministración):
        super().__init__(identificadorInmobiliario, área, dirección, númeroHabitaciones, númeroBaños)
        self._valorAdministración =  valorAdministración
        self._valorArea = 2000000
        
    def mostrar_resultados(self):
        super().mostrar_resultados()
        print(f"Valor administración = ${self._valorAdministración}")
        print()
        