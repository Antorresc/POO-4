from Local import Local

class Oficina(Local):
    def __init__(self, identificadorInmobiliario, área, dirección, tipoLocal, esGobierno):
        
        super().__init__(identificadorInmobiliario, área, dirección, tipoLocal)
        self._valorArea = 3500000
        self._esGobierno = esGobierno
        
    def mostrar_resultados(self):
        super().mostrar_resultados()
        # Atributo booleano que indica si la oficina es gubernamental
        print(f"Es oficina gubernamental = {self._esGobierno}") #True significa que SÍ y False que NO 
        print()
