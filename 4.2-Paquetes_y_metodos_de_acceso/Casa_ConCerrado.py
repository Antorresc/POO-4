from Casa_Urbana import CasaUrbana

class CasaConjuntoCerrado(CasaUrbana):
    def __init__(self, identificadorInmobiliario, área, dirección, númeroHabitaciones, númeroBaños, númeroPisos, valorAdministración, tienepiscina=False, tienecamposdeportivos=False):
        
        super().__init__(identificadorInmobiliario, área, dirección, númeroHabitaciones, númeroBaños, númeroPisos)
        self._valorArea = 2500000
        self._valorAdministración = valorAdministración
        self._tienepiscina = tienepiscina
        self._tienecamposdeportivos = tienecamposdeportivos
    def mostrar_resultados(self):
        super().mostrar_resultados()
        print(f"¿Tiene piscina? = {self._tienepiscina}")
        print(f"¿Tiene campos deportivos? = {self._tienecamposdeportivos}")
        print()