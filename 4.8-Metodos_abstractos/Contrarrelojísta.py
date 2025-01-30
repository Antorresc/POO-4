from Ciclista import Ciclista

class Contrarrelojísta(Ciclista):
    
    def __init__(self, identificador, nombre, velocidad_máxima):
        super().__init__(identificador, nombre)
        self.velocidad_máxima = velocidad_máxima
    
    def get_velocidad_máxima(self):
        return self.velocidad_máxima

    def set_velocidad_máxima(self, velocidad_máxima):
        self.velocidad_máxima = velocidad_máxima

    def imprimir(self):
        super().imprimir()
        print(f"Velocidad máxima = {self.velocidad_máxima}")
        
    def imprimir_tipo(self):
        return "Es un Contrarrelojísta"