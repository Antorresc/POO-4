from Casa_Urbana import CasaUrbana

class CasaIndependiente(CasaUrbana):
    def __init__(self, identificadorInmobiliario, área, dirección, númeroHabitaciones, númeroBaños, númeroPisos):
        
        super().__init__(identificadorInmobiliario, área, dirección, númeroHabitaciones, númeroBaños, númeroPisos)
        self._valorArea = 3000000
        
    def mostrar_resultados(self):
        super().mostrar_resultados()
        print()