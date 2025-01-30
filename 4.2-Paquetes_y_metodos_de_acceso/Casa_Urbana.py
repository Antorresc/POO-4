from Casa import Casa

class CasaUrbana(Casa):
    def __init__(self, identificadorInmobiliario, área, dirección, númeroHabitaciones, númeroBaños, númeroPisos):
        super().__init__(identificadorInmobiliario, área, dirección, númeroHabitaciones, númeroBaños, númeroPisos)
        
    def mostrar_resultados(self):
        super().mostrar_resultados()
        