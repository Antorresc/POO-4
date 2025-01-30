from Casa import Casa

class CasaRural(Casa):
    def __init__(self, identificadorInmobiliario, área, dirección, númeroHabitaciones, númeroBaños, númeroPisos, distanciaCabera, altitud):
        
        super().__init__(identificadorInmobiliario, área, dirección, númeroHabitaciones, númeroBaños, númeroPisos)
        self._distanciaCabera = distanciaCabera
        self._altitud = altitud
        self._valorArea = 1500000
        
    def mostrar_resultados(self):
        super().mostrar_resultados()
        print(f"Distancia la cabecera municipal = {self._distanciaCabera} km")
        print(f"Altitud sobre el nivel del mar = {self._altitud} metros")
        print()
    
        
        
        
    
