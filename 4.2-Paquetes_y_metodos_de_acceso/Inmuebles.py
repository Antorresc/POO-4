class Inmueble:
    def __init__(self, identificadorInmobiliario, área, dirección):
        
        self._identificadorInmobiliario = identificadorInmobiliario
        self._área = área
        self._dirección = dirección
        self._precioVenta = 0.0
        
    def calcular_precioVenta(self, valorArea):
        self._precioVenta = self._área * valorArea
        return self._precioVenta
    
    def mostrar_resultados(self):
        print(f"Identificador inmobiliario = {self._identificadorInmobiliario}")
        print(f"Área = {self._área}")
        print(f"Dirección = {self._dirección}")
        print(f"Precio de venta = ${self._precioVenta}")