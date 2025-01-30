from InmuebleVivienda import InmuebleVivienda

class Apartamento(InmuebleVivienda):
    def __init__(self, identificadorInmobiliario, área, dirección, númeroHabitaciones, númeroBaños):
        super().__init__(identificadorInmobiliario, área, dirección, númeroHabitaciones, númeroBaños)
        
    def mostrar_resultados(self):
        super().mostrar_resultados()