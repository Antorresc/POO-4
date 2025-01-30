from InmuebleVivienda import InmuebleVivienda

class Casa(InmuebleVivienda):
    def __init__(self, identificadorInmobiliario, área, dirección, númeroHabitaciones, númeroBaños, númeroPisos):
        super().__init__(identificadorInmobiliario, área, dirección, númeroHabitaciones, númeroBaños)
        self.númeroPisos = númeroPisos
        
    def mostrar_resultados(self):
        super().mostrar_resultados()