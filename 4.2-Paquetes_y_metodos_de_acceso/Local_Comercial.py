from Local import Local

class LocalComercial(Local):
    def __init__(self, identificadorInmobiliario, área, dirección, tipoLocal, centroComercial):
        
        super().__init__(identificadorInmobiliario, área, dirección, tipoLocal)
        self._valorArea = 3000000
        self._centroComercial = centroComercial
        
    def mostrar_resultados(self):
        super().mostrar_resultados()
        print(f"Centro comercial = {self._centroComercial}")
        print()